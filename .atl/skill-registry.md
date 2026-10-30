# Skill Registry

**Delegator use only.** Any agent that launches sub-agents reads this registry to resolve compact rules, then injects them directly into sub-agent prompts. Sub-agents do NOT read this registry or individual SKILL.md files.

See `_shared/skill-resolver.md` for the full resolution protocol.

**Project**: turnos-odontologia (SaaS de turnos odontológicos — Python 3.11+/FastAPI/SQLite, Spec-Driven Development, TDD estricto)

## User Skills

| Trigger | Skill | Path |
|---------|-------|------|
| FastAPI APIs, Pydantic models, dependencies (`Annotated`/`Depends`), streaming/SSE, serving frontend apps | `fastapi` | `/home/joaquin/.agents/skills/fastapi/SKILL.md` |
| Writing Python tests, pytest suites/fixtures/mocking, TDD, integration/async/DB tests | `python-testing-patterns` | `/home/joaquin/.agents/skills/python-testing-patterns/SKILL.md` |
| Architecture layers, dependency rule, ports & adapters, "where does this logic go", SOLID, module boundaries | `clean-architecture` | `/home/joaquin/.agents/skills/clean-architecture/SKILL.md` |
| Domain modeling, bounded context, aggregate root, ubiquitous language, domain events, context mapping | `domain-driven-design` | `/home/joaquin/.agents/skills/domain-driven-design/SKILL.md` |
| SQLAlchemy ORM models, Alembic migrations, schema changes, indexes/constraints, query optimization | `sqlalchemy-alembic-expert-best-practices-code-review` | `/home/joaquin/.agents/skills/sqlalchemy-alembic-expert-best-practices-code-review/SKILL.md` |
| Discovery/fase de investigación previa a la KB: checklist de mercado, competidores, reglas de negocio | `discovery-research` | `/home/joaquin/.agents/skills/discovery-research/SKILL.md` |
| Scrapear una URL de competidor (problema, features, pricing, posicionamiento) con WebFetch/WebSearch | `web-scraper` | `/home/joaquin/.agents/skills/web-scraper/SKILL.md` |

## Compact Rules

Pre-digested rules per skill. Delegators copy matching blocks into sub-agent prompts as `## Project Standards (auto-resolved)`.

**Always prepend this project-level block to every sub-agent prompt (inviolable, from AGENTS.md):**

```markdown
## Project Standards (auto-resolved)
- Spec First: prohibido escribir/modificar código en `src/` o tests en `tests/` sin spec aprobada en `openspec/changes/`.
- Doble validación de recurso: verificar de forma simultánea e independiente Profesional Y Sillón/Box al validar disponibilidad.
- Privacidad: NUNCA datos reales de pacientes/profesionales en repo, historias clínicas ni fixtures — solo datos sintéticos (`Paciente Ficticio`, `Dr. Ejemplo`).
- Criterio verde: ninguna tarea termina con la suite de `tests/` en rojo (`pytest` debe pasar).
- Comandos: `pytest` · `pytest --cov=src` · `openspec validate` · Python 3.11+, type hints, PEP 8.
- Excepciones de dominio explícitas: `SolapamientoProfesionalError`, `SolapamientoSillonError`.
```

### fastapi
- Usar siempre estilo `Annotated` para parámetros y dependencias: `Annotated[int, Path(...)]`, `Dep = Annotated[T, Depends(f)]` (alias de tipo reutilizable por dependencia).
- Nunca usar `...` como default de parámetros requeridos ni campos de modelos Pydantic; tampoco `RootModel` (usar anotaciones con `Field`).
- Declarar `prefix`, `tags` y `dependencies` compartidas en el `APIRouter`, no en `include_router()`.
- Preferir tipo de retorno (`-> Item`) para validar/filtrar/serializar; `response_model` solo cuando el esquema público difiere del valor retornado.
- No usar `ORJSONResponse`/`UJSONResponse` (deprecados); la serialización la hace Pydantic.
- `async` solo si el interior es 100% no bloqueante; ante la duda usar `def` (threadpool). Nunca código bloqueante dentro de `async`.
- Un solo HTTP operation por función (un handler `POST` y otro `GET` separados).
- SSE: `response_class=EventSourceResponse` + `yield` (objeto o `ServerSentEvent`); datos estáticos con `app.frontend("/", directory="dist")` en vez de montar `StaticFiles`.
- Nuevas libs preferidas: uv/Ruff/ty, Asyncer, SQLModel, HTTPX (no Requests).

### python-testing-patterns
- Estructura AAA (Arrange/Act/Assert); tests independientes, sin estado compartido, cada uno limpia tras de sí.
- Naming `test_<unit>_<scenario>_<expected_outcome>` (ej. `test_crear_turno_con_sillon_ocupado_lanza_solapamiento_error`).
- Organizar `tests/` en `conftest.py` + carpetas (unit/integration); fixtures compartidas en conftest, no setup global.
- Mock con `Mock.side_effect=[...]` para secuencias (reintentos), `unittest.mock` para dependencias externas; `freezegun.freeze_time` para fechas/horas.
- Marcar con `@pytest.mark.*` (integration, slow) y `skip/xfail` con `reason=` explícito.
- Coverage: `pytest --cov=src --cov-report=term-missing`; exigir cobertura significativa, no solo el número.
- TDD estricto en este proyecto: red → green → refactor; nunca mergear con suite roja (regla de AGENTS.md).

### clean-architecture
- Regla de dependencia: los imports apuntan hacia adentro (Controllers → Use Cases → Entities); el inner nunca importa el outer.
- Reglas de negocio viven en Entities/Use Cases; controllers solo traducen HTTP y delegan — nada de lógica en endpoints ni en modelos ORM.
- DTOs simples cruzan fronteras (`CreateTurnoRequest`), nunca objetos de framework ni entidades ORM.
- Interfaces (puertos) definidas por la capa interna, implementadas fuera: repositorios como `TurnoRepository` (interfaz) + `SqliteTurnoRepository` (adapter).
- Framework y base de datos son detalles: confinarlos al círculo exterior (composition root/`main` ensambla todo).
- Un Use Case por operación de aplicación (`CrearTurno`, `CancelarTurno`), no un orquestador gigante.
- Aplicar SOLID (SRP/OCP/LSP/ISP/DIP), grafo de componentes sin ciclos (romper con DIP).
- Anti-patrones a detectar en review: ORM filtrándose en el dominio, reglas en controllers, dependencias circulares, modelo anémico.

### domain-driven-design
- Modelo = código: nombres en lenguaje ubicuo (`Turno`, `Profesional`, `Sillon`, `agendar()`, no `DataManager`/`Handler`/`Utils`).
- Preferir Value Objects inmutables sobre Entities; Entity solo cuando hay identidad persistente.
- Agregados pequeños, una raíz que valida invariantes (el Turno es raíz de su consistencia); referenciar otros agregados por ID.
- Invariantes dentro de la raíz del agregado, no en servicios: la validación de solapamiento es responsabilidad del dominio del Turno.
- Eventos de dominio en pasado (`TurnoAgendado`, `TurnoCancelado`) para desacoppar; solo hechos que al dominio le importan.
- Interfaces de Repository en la capa de dominio (hablan el lenguaje ubicuo), implementación en infraestructura.
- Anti-Corruption Layer en toda integración externa; un bounded context ≠ microservice (empezar por módulos).
- Clasificar subdominios: la agenda/turnos es Core Domain — ahí va el modelado profundo.

### sqlalchemy-alembic-expert-best-practices-code-review
- Índices en migraciones: `postgresql_concurrently=True` dentro de bloque autocommit (nunca locks de tabla).
- Unique constraints: pasar por índice concurrente + constraint en pasos separados.
- FKs nuevos: agregar con `NOT VALID` primero y validar después; igual para CHECK constraints.
- Cambios de tipo de columna: enfoque multi-paso para evitar bloqueos largos.
- Índices no únicos: máximo 3 columnas; evitar índices redundantes cubiertos por compuestos.
- Verificar que todo patrón de query frecuente tenga índice (`verify-query-patterns-are-indexed`).
- Detalle por regla en `rules/*.md` dentro del directorio de la skill.
- Nota: muchas reglas asumen PostgreSQL; en este proyecto (SQLite) adaptar — solo aplicar lo que el motor soporta.

### discovery-research
- Corre antes de la KB: Q&A del checklist completo (problema, usuarios, competidores, funcionalidades, reglas de negocio, integraciones, restricciones, riesgos, preguntas abiertas).
- Si hay URLs de competidores, invocar `web-scraper` como sub-skill; NO construir la KB (eso es `kb-creator`) ni scrapear URLs sueltas sin el checklist.

### web-scraper
- Output en notas markdown con esquema fijo: problema que resuelve, usuarios objetivo, features, pricing, posicionamiento.
- Usar solo WebFetch/WebSearch (sin API keys ni costos); no crawling masivo ni sitios con JS pesado/anti-bot.

## Project Skills (SDD workflow — no compact rules; read SKILL.md at invocation)

| Trigger | Skill | Path |
|---------|-------|------|
| `openspec apply` / implementar tasks | `openspec-apply-change` | `{project}/.opencode/skills/openspec-apply-change/SKILL.md` |
| `openspec archive` | `openspec-archive-change` | `{project}/.opencode/skills/openspec-archive-change/SKILL.md` |
| `openspec explore` | `openspec-explore` | `{project}/.opencode/skills/openspec-explore/SKILL.md` |
| `openspec propose` | `openspec-propose` | `{project}/.opencode/skills/openspec-propose/SKILL.md` |
| `openspec sync` | `openspec-sync-specs` | `{project}/.opencode/skills/openspec-sync-specs/SKILL.md` |
| `openspec update change` | `openspec-update-change` | `{project}/.opencode/skills/openspec-update-change/SKILL.md` |

Duplicates in `{project}/.gemini/skills/` are the same skills — use the `.opencode` path above.

## Project Conventions

| File | Path | Notes |
|------|------|-------|
| AGENTS.md | `{project}/AGENTS.md` | Index — reglas duras e inviolables (ver bloque de Project Standards arriba); referencia rutas: `openspec/changes/`, `src/`, `tests/`; flujo `propose → apply → verify → archive`. |
| CLAUDE.md | `{project}/CLAUDE.md` | Comandos de entorno (`pytest`, `pytest --cov=src`, `openspec validate`) y estándares de código (Python 3.11+, type hints, PEP 8, excepciones de dominio). |
| openspec/ | `{project}/openspec/` | Specs canónicas (`specs/`), cambios (`changes/`, `changes/archive/`), `config.yaml`. Fuente de verdad para Spec-Driven Development. |
| knowledge-base/ | `{project}/knowledge-base/` | KB canónica (10 archivos: `vision.md`, `description.md`, `features.md`, `business-rules.md`, `data-models.md`, `architecture.md`, `flows.md`, `actors.md`, `decisions.md`, `open-questions.md`). Leer el archivo relevante antes de implementar. |
| CHANGES.md | `{project}/CHANGES.md` | Roadmap operativo de changes con dependencias y alcance por cambio. |

Read the convention files listed above for project-specific patterns and rules. All referenced paths have been extracted — no need to read index files to discover more.
