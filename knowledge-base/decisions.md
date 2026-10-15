# Decisiones Arquitectónicas y Tecnológicas

## Stack y Persistencia
- Lenguaje: Python 3.11+ / Node.js.
- Persistencia: SQLite para desarrollo y testing integral.
- Configuración: Variables de entorno (.env) por tenant.

## Estrategia de Pruebas
- Pruebas unitarias obligatorias sobre las reglas de negocio del doble candado.
- Cobertura del 100% en casos de solapamiento temporal $[T_{inicio}, T_{fin})$.
