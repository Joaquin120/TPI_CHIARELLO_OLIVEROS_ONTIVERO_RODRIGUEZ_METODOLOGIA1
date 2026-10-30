"""Excepciones de dominio explícitas para la gestión de turnos."""


class SolapamientoProfesionalError(Exception):
    """El profesional ya tiene un turno asignado que colisiona en horario."""

    def __init__(self, mensaje: str = "El profesional ya tiene un turno en ese horario") -> None:
        super().__init__(mensaje)


class SolapamientoSillonError(Exception):
    """El sillón/box ya está ocupado en ese rango horario."""

    def __init__(self, mensaje: str = "El sillón ya está ocupado en ese horario") -> None:
        super().__init__(mensaje)
