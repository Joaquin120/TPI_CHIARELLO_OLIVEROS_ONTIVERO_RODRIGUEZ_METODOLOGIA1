# Informe de Discovery: Sistema SaaS de Gestión de Turnos Odontológicos

**Autor / Líder de Discovery:** Santi  
**Auditoría de Fuentes:** Cristian  
**Proyecto:** Trabajo Práctico de Integración - Metodología I  
**Etapa:** 2 - Discovery Obligatorio  

---

## A. Contexto y Objetivos del Producto

### 1. Problema de Negocio
En la gestión operativa de consultorios y clínicas odontológicas en Argentina, la coordinación de citas presenta una restricción ausente en la medicina ambulatoria general: **el doble recurso crítico simultáneo**.
En un consultorio médico tradicional, el factor limitante es únicamente la agenda horaria del profesional. En odontología, toda intervención requiere la concurrencia obligatoria de dos recursos:
- La presencia del **profesional odontólogo** (con su respectiva especialidad).
- La disponibilidad física del **sillón/box odontológico** (infraestructura compuesta por sillón ergonómico, unidad dental con turbinas, succión, compresor y eventualmente instrumental radiológico o lámparas de fotocurado).

Actualmente, muchas clínicas administran la agenda mediante planillas de cálculo, agendas en papel o software médico genérico. Esto genera los siguientes problemas operativos:
- **Colisión de sillones:** Dos profesionales agendados en el mismo horario dentro de consultorios que poseen menor cantidad de sillones que de profesionales en servicio.
- **Tasa de ausentismo (no-show) elevada:** Pacientes que olvidan su turno debido a la falta de recordatorios en canales de comunicación directos y de alta tasa de apertura (WhatsApp).
- **Falta de trazabilidad en cancelaciones:** Dificultad para liberar y reasignar de inmediato recursos físicos ante cancelaciones imprevistas.

### 2. Objetivos del Producto
Desarrollar un software como servicio (SaaS) multi-tenant, web-first y adaptado a la operatoria odontológica argentina, enfocado en:
1. Eliminar los conflictos de solapamiento mediante un motor de validación bidireccional (profesional y sillón/box).
2. Reducir la fricción de uso diario para recepcionistas y profesionales con una vista de agenda clara y filtrable.
3. Servir de base desacoplada y escalable para futuras integraciones de mensajería automatizada y ficha clínica/odontograma.

---

## B. Matriz Comparativa de Competidores (15 Soluciones)

*Nota metodológica: Cualquier celda o característica que no cuente con evidencia pública y verificable en la documentación o sitio oficial del proveedor se declara estrictamente como "No evidenciado".*

| # | Competidor | Tipo / Despliegue | Gestión de Sillón / Box | Recordatorios (WhatsApp / SMS) | Ficha Odontológica / Odontograma | Precios Públicos (Argentina) |
|---|---|---|---|---|---|---|
| 1 | **Clinic Cloud** | Web / Cloud | No evidenciado | SMS y Email | Ficha e historia clínica básica | No evidenciado (cotización en EUR) |
| 2 | **DasiClinic** | On-premise / Híbrido | Asignación por sala | SMS | Odontograma integrado | No evidenciado |
| 3 | **DentalTech** | Web / Cloud | Asignación de gabinete | Email / SMS | Odontograma 2D | No evidenciado |
| 4 | **DentiDesk** | Web / Cloud | Multi-box configurable | WhatsApp y Email | Odontograma digital interactivo | Sí (Planes mensuales en USD/CLP) |
| 5 | **Doctoralia** | Web / Cloud | No evidenciado (solo por doctor) | WhatsApp y SMS | No evidenciado | No evidenciado (requiere llamada demo) |
| 6 | **NaturalSoft** | On-premise / Cloud | Gestión por salas | SMS y Email | Ficha clínica completa | No evidenciado |
| 7 | **Nubimed** | Web / Cloud | Gestión por gabinetes | SMS y Email | Odontograma vectorial | Sí (Planes en EUR por profesional) |
| 8 | **Odontosys** | Desktop / Local | No evidenciado | No evidenciado | Odontograma tradicional | No evidenciado |
| 9 | **Dentalink** | Web / Cloud | Sí (Asignación por sillón/box) | WhatsApp automático y Email | Odontograma visual y presupuestos | Sí (Planes en USD adaptados a LATAM) |
| 10 | **XDental** | On-premise / Web | Asignación básica de box | SMS | Odontograma y periodontograma | No evidenciado |
| 11 | **Wiri Salud** | Web / Cloud | No evidenciado | WhatsApp y Email | No evidenciado | Sí (Esquema mixto en ARS) |
| 12 | **Medesk** | Web / Cloud | Asignación por sala/box | WhatsApp y SMS | Ficha clínica general | Sí (Planes desde 30 USD/mes) |
| 13 | **DentalSoft** | Híbrido / Local | No evidenciado | Email | Odontograma básico | No evidenciado |
| 14 | **SaludTools** | Web / Cloud | No evidenciado | WhatsApp y SMS | Historia clínica general | Sí (Planes en moneda extranjera) |
| 15 | **OmniDoc** | Web / Cloud | No evidenciado | WhatsApp | Ficha médica general | No evidenciado |

---

## C. Hallazgos Clave y Brecha de Oportunidad

1. **La deficiencia del modelo de recurso único:**
   La gran mayoría de los sistemas ambulatorios (Doctoralia, SaludTools, OmniDoc) modelan la reserva bajo el esquema tradicional `(Paciente, Profesional, Horario)`. En odontología este modelo es insuficiente: en clínicas con rotación de especialistas o con más odontólogos que sillones disponibles, se generan colisiones físicas directas. Únicamente las plataformas verticalizadas de gama alta contemplan la entidad gabinete/sillón de forma independiente.

2. **La fricción cambiaria y de onboarding:**
   Las plataformas que contemplan gestión de boxes operan con tarifas en moneda extranjera (USD/EUR) o exigen procesos comerciales con llamadas de venta consultiva. Hay una brecha clara para un SaaS ágil, con contratación transparente y adaptado a consultorios pequeños y medianos de Argentina.

3. **Canales de comunicación tradicionales en desuso:**
   Los proveedores tradicionales apoyan sus notificaciones en correo electrónico o SMS, herramientas con tasas de lectura bajas en comparación con la mensajería instantánea directa (WhatsApp).

---

## D. Definición del MVP (Minimum Viable Product)

En función de los hallazgos del Discovery, el alcance nuclear para el primer ciclo de desarrollo se define en torno a:

### 1. Entidades del Dominio
- **Profesional:** Odontólogo/a matriculado/a responsable de la atención.
- **Sillón / Box:** Recurso físico donde se realiza la práctica.
- **Paciente:** Persona receptora del servicio odontológico.
- **Turno:** Registro temporal que vincula de forma unívoca a un Paciente, un Profesional y un Sillón/Box en un rango horario $[T_{inicio}, T_{fin})$.

### 2. Regla Central de Negocio (Validación Bidireccional)
Al solicitar la creación o modificación de un turno en el intervalo $[T_{inicio}, T_{fin})$:
- El **Profesional** no debe registrar ningún otro turno activo (no cancelado) que solape con dicho intervalo.
- El **Sillón/Box** no debe registrar ningún otro turno activo (no cancelado) que solape con dicho intervalo.

### 3. Ciclo de Vida del Turno
Estados válidos:
- `PENDIENTE`: Turno reservado en espera de ratificación.
- `CONFIRMADO`: Turno verificado con el paciente.
- `CANCELADO`: Turno dado de baja; libera de forma inmediata tanto al profesional como al sillón.
- `COMPLETADO`: Atención finalizada con éxito.

---

<!-- SECCIÓN RESERVADA PARA AUDITORÍA DE CRISTIAN -->
## Verificación de Fuentes (Auditoría Manual)
*(Esta sección será completada por Cristian con la auditoría de 5 fuentes reales).*