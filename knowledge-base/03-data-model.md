# 03. Modelo de Datos

## Entidad: Profesional
- `id` (UUID / Integer)
- `nombre` (String)
- `apellido` (String)
- `matricula` (String)
- `especialidad` (String)

## Entidad: Sillon
- `id` (UUID / Integer)
- `nombre` (String, ej: "Sillón 1 - Cirugía")
- `equipamiento` (String)
- `activo` (Boolean)

## Entidad: Paciente
- `id` (UUID / Integer)
- `dni` (String)
- `nombre` (String)
- `telefono` (String)

## Entidad: Turno
- `id` (UUID / Integer)
- `paciente_id` (FK -> Paciente)
- `profesional_id` (FK -> Profesional)
- `sillon_id` (FK -> Sillon)
- `fecha_hora_inicio` (DateTime)
- `fecha_hora_fin` (DateTime)
- `estado` (Enum: PENDIENTE, CONFIRMADO, CANCELADO, COMPLETADO)