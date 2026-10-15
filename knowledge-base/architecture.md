# Arquitectura del Sistema

## Patrón de Diseño
El sistema sigue una arquitectura en capas (Layered Architecture / Monolito Modular) preparada para un entorno SaaS web-first:

1. **Capa de Presentación / API:** Controladores RESTful que reciben peticiones HTTP y serializan JSON.
2. **Capa de Servicios de Dominio:** Contiene las reglas del negocio (validación del doble candado).
3. **Capa de Persistencia / Repositorios:** Abstracción para el acceso a datos.

## Modelo Multi-Tenant
- Cada clínica/consultorio opera como un **Tenant** aislado.
- Todas las consultas a la base de datos deben incluir implícita o explícitamente la clave de aislamiento `tenant_id`.