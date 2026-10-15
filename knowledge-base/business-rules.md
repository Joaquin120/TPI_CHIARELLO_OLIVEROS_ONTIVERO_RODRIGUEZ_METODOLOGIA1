# Reglas del Dominio Odontológico

## Entidades Principales
- **Profesional:** Odontólogo matriculado.
- **Sillón / Box:** Recurso físico (equipamiento).
- **Paciente:** Persona que recibe la atención.
- **Turno:** Reserva temporal en un intervalo $[T_{inicio}, T_{fin})$.

## Regla Central de Negocio: El Doble Candado
Para registrar o modificar un turno en un horario determinado:
1. **Validación de Profesional:** No puede existir otro turno activo (no cancelado) asignado al mismo `profesional_id` en el rango horaria que se solape con $[T_{inicio}, T_{fin})$.
2. **Validación de Sillón:** No puede existir otro turno activo (no cancelado) asignado al mismo `sillon_id` en el rango horaria que se solape con $[T_{inicio}, T_{fin})$.

## Ciclo de Vida del Turno
Los estados válidos y sus transiciones son:
- `PENDIENTE` -> `CONFIRMADO` | `CANCELADO`
- `CONFIRMADO` -> `COMPLETADO` | `CANCELADO`
- `CANCELADO` (libera de forma inmediata tanto al profesional como al sillón).
- `COMPLETADO`