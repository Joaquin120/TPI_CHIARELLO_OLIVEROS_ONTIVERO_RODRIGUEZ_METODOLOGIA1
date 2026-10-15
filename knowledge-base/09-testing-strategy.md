# 09. Estrategia de Testing

## Pruebas Unitarias Prioritarias
1. **Validación de Solapamiento de Profesional:** Intentar crear dos turnos en el mismo rango de tiempo para el mismo profesional -> Debe fallar.
2. **Validación de Solapamiento de Sillón:** Intentar crear dos turnos en el mismo rango de tiempo para dos profesionales distintos pero en el **mismo sillón** -> Debe fallar.
3. **Liberación por Cancelación:** Cancelar un turno previo y verificar que el profesional y el sillón quedan libres para agendar en ese mismo horario.