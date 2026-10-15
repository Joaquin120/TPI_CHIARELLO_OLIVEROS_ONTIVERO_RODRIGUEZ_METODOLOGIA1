# Preguntas Abiertas

## Puntos no evidenciados en competidores
1. **Mantenimiento y bloqueo de sillón:** ¿Cómo reacciona la agenda si un sillón sufre un desperfecto físico imprevisto?
2. **Atención por sobreturno / Urgencias:** Tolerancia de sobreposición temporal en casos de urgencia odontológica fuera de la agenda planificada.
3. **Integración nativa con facturación (AFIP):** La mayoría de los competidores locales no evidencian conexión directa por API para emisión automática de comprobantes.

## Resoluciones para el MVP
- Para el MVP, el mantenimiento de un sillón se gestiona marcando un turno de tipo bloqueo o inactivando el recurso `Sillon`.
- Se prioriza estrictamente la validación del solapamiento sin excepciones de sobreturno para garantizar la coherencia física en el MVP.