"""Servicio de dominio para el agendamiento de turnos odontológicos."""

from src.domain.exceptions import (
    SolapamientoProfesionalError,
    SolapamientoSillonError,
)
from src.domain.models import Profesional, Sillon, Turno


def _horas_a_minutos(hora: str) -> int:
    """Convierte una hora 'HH:MM' a minutos desde medianoche."""
    horas, minutos = hora.split(":")
    return int(horas) * 60 + int(minutos)


def _hay_solapamiento(
    inicio_a: int, fin_a: int, inicio_b: int, fin_b: int
) -> bool:
    """Intervalos semiabiertos [inicio, fin): solapan iff a_inicio < b_fin and a_fin > b_inicio.

    Si fin_a == inicio_b (contiguo) NO hay solapamiento.
    """
    return inicio_a < fin_b and fin_a > inicio_b


class ServicioTurnos:
    """Registra turnos validando solapamientos por profesional y por sillón de forma independiente."""

    def __init__(self) -> None:
        self._turnos: list[Turno] = []

    def agendar_turno(
        self,
        paciente: str,
        fecha: str,
        hora_inicio: str,
        hora_fin: str,
        profesional: Profesional,
        sillon: Sillon,
    ) -> Turno:
        """Crea y registra un turno si no hay solapamiento de profesional ni de sillón."""
        inicio = _horas_a_minutos(hora_inicio)
        fin = _horas_a_minutos(hora_fin)

        for turno_existente in self._turnos:
            if turno_existente.fecha != fecha:
                continue
            existente_inicio = _horas_a_minutos(turno_existente.hora_inicio)
            existente_fin = _horas_a_minutos(turno_existente.hora_fin)
            if not _hay_solapamiento(inicio, fin, existente_inicio, existente_fin):
                continue
            # Doble validación de recurso: profesional y sillón, de forma independiente.
            if turno_existente.profesional == profesional:
                raise SolapamientoProfesionalError(
                    f"El profesional {profesional.nombre} ya tiene un turno "
                    f"el {fecha} de {turno_existente.hora_inicio} a {turno_existente.hora_fin}"
                )
            if turno_existente.sillon == sillon:
                raise SolapamientoSillonError(
                    f"El sillón {sillon.nombre} ya está ocupado "
                    f"el {fecha} de {turno_existente.hora_inicio} a {turno_existente.hora_fin}"
                )

        turno = Turno(
            profesional=profesional,
            sillon=sillon,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            paciente=paciente,
        )
        self._turnos.append(turno)
        return turno

    def turnos_registrados(self) -> list[Turno]:
        """Devuelve una copia de la lista de turnos registrados."""
        return list(self._turnos)
