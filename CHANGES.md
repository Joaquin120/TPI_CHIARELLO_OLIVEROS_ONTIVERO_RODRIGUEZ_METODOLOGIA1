# Historical Changes & Roadmap

All notable changes to the SaaS Odontológico project will be documented in this file.

## [Unreleased] - MVP Release Target

### Added
- **Core Domain Entities:** Modelado de `Profesional`, `Sillon`, `Paciente` y `Turno`.
- **Overlap Validation Engine:** Algoritmo de validación bidireccional que previene reservas duplicadas para el mismo profesional o el mismo sillón odontológico en intervalos $[T_{inicio}, T_{fin})$.
- **Turno Lifecycle Management:** Transiciones de estados para turnos (`PENDIENTE`, `CONFIRMADO`, `CANCELADO`, `COMPLETADO`).
- **Automated Test Suite:** Pruebas unitarias e integrales que aseguran el cumplimiento del "doble candado" sin excepciones.

### Completed
- **`2026-10-15-crear-turno-sin-solapamientos`** — ✔️ Archivado. Specs sincronizados en `openspec/specs/crear-turno/spec.md` (2 requirements ADDED) y cambio movido a `openspec/changes/archive/2026-10-15-crear-turno-sin-solapamientos/`. Suite verde: 8 tests pasados, 100% cobertura.

## [0.1.0] - Discovery & Foundation Phase
- Complete Discovery report with 15 analyzed competitors.
- Manual verification of 5 real market sources.
- Domain knowledge base initialization (`knowledge-base/`).