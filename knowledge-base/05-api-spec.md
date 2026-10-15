# 05. Especificación de Endpoints REST API

## Turnos
- `GET /api/v1/turnos` -> Lista turnos (filtrables por `profesional_id`, `sillon_id`, `fecha`).
- `POST /api/v1/turnos` -> Crea un nuevo turno (ejecuta validación de solapamiento).
- `PATCH /api/v1/turnos/{id}/estado` -> Cambia el estado del turno (`CONFIRMADO`, `CANCELADO`, `COMPLETADO`).

## Recursos
- `GET /api/v1/profesionales` -> Lista de profesionales.
- `GET /api/v1/sillones` -> Lista de sillones/boxes disponibles.