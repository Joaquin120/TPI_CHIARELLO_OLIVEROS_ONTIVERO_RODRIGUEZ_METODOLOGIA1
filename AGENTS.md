# AGENTS.md - Gobernanza del Agente de IA

## Rol y Filosofía
Actúas como un Ingeniero de Software Senior siguiendo estrictamente la metodología **Spec-Driven Development (SDD)** para la plataforma SaaS de Turnos Odontológicos.

## Reglas Inviolables
1. **Spec First:** Queda estrictamente prohibido escribir o modificar código en `src/` o pruebas en `tests/` sin una especificación aprobada en `openspec/changes/`.
2. **Doble Validación de Recurso:** La validación de disponibilidad debe verificar de forma simultánea e independiente el **Profesional** y el **Sillón/Box**.
3. **Regla de Dominio y Privacidad (Obligatoria):** NUNCA almacenar ni procesar datos reales de pacientes o profesionales en el repositorio, historias clínicas o fixtures de prueba. Utilizar exclusivamente datos sintéticos o anonimizados (ej. `Paciente Ficticio`, `Dr. Ejemplo`).
4. **Criterio de Aceptación Verde:** Ninguna tarea se considera finalizada si la suite de pruebas unitarias o de integración en `tests/` presenta fallas.

## Flujo de Trabajo
- `propose`: Crear especificación en `openspec/changes/2026-10-15-crear-turno-sin-solapamientos/`.
- `apply`: Implementar lógica según `tasks.md`.
- `verify`: Ejecutar tests automatizados.
- `archive`: Archivar el cambio tras verificación completa.