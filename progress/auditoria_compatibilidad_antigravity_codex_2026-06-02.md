# File: progress/auditoria_compatibilidad_antigravity_codex_2026-06-02.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Evaluar la compatibilidad del arnés actual con los formatos esperados por Antigravity y Codex.
# Rol: Documento informativo de auditoría, sin autoridad normativa.
# ──────────────────────────────────────────────────────────────────────

# Auditoría de Compatibilidad: Antigravity & Codex (2026-06-02)

## 1. Propósito de la Auditoría
Esta auditoría tiene como propósito analizar la compatibilidad estructural y terminológica del repositorio raíz `proyecto_raiz_sdd_harness` (el arnés) con respecto a los estándares y formatos operativos esperados o documentados para Codex y Antigravity. El fin es identificar desviaciones sintácticas, de nomenclatura de directorios y de metadatos, estableciendo recomendaciones de contención para evitar automatizaciones accidentales o prematuras.

---

## 2. Alcance
El alcance de esta revisión se limita estrictamente a la estructura de archivos documentales conceptuales existentes en el workspace, con énfasis en el directorio `.agent/` (rules, workflows, skills), los adaptadores raíz (`AGENTS.md`, `GEMINI.md`), la gobernanza documental en `docs/` y el tracking en `progress/`. 

---

## 3. Fuentes Consultadas
Para la realización de esta auditoría se consultaron y contrastaron las siguientes especificaciones técnicas y documentación de referencia:

### Fuentes Internas
- `docs/constitucion_del_proyecto.md`
- `docs/00_mapa_y_gobernanza_documental.md`
- `docs/02_metodologia_desarrollo_software_sdd_harness.md`
- `docs/preflight_estructural.md`
- `docs/gate_0_preflight_definicion.md`
- `progress/current.md`
- `progress/history.md`
- `progress/snapshot_estado_2026-06-02.md`
- Adaptadores `AGENTS.md` y `GEMINI.md`
- Recursos conceptuales en `.agent/rules/`, `.agent/workflows/` y `.agent/skills/`

### Fuentes Externas (Documentación Oficial de Runtimes)
- **Codex Reference Guides:** `https://developers.openai.com/codex/guides/agents-md`
- **Codex Skills Specification:** `https://developers.openai.com/codex/skills`
- **Antigravity Engine Guides (Skills):** `https://antigravity.google/docs/skills`
- **Antigravity Engine Guides (Rules):** `https://antigravity.google/docs/rules`
- **Antigravity Engine Guides (Workflows):** `https://antigravity.google/docs/workflows`

---

## 4. Estado Actual del Arnés
El repositorio completo se encuentra congelado en **Fase Documental / MVP Estructural**. Todos los componentes funcionales, scripts de validación, herramientas de gates, archivos de automatización y adaptadores de agentes operan en estado de plantillas conceptuales, no activas y no ejecutables. No existe código fuente de software real ni integraciones activas en el workspace.

---

## 5. Tabla de Compatibilidad por Componente

| Componente | Estado Actual | Compatibilidad con Antigravity | Compatibilidad con Codex | Riesgo | Acción Recomendada |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AGENTS.md` | Adaptador operativo general. | Parcial (informativo de contexto). | Alta (estructura estándar). | Bajo. No duplica la constitución pero requiere mantener enlaces actualizados. | Mantener como adaptador minimalista sin lógica de negocio. |
| `GEMINI.md` | Adaptador operativo para Antigravity. | Media/Alta como adaptador contextual, pendiente de verificación práctica en el workspace. | Media (desvío a especificación Codex). | Bajo. Requiere subordinación constante. | Mantener subordinado a la constitución del proyecto. |
| `.agent/rules/` | Sede documental conceptual. | Media/Alta futura: compatible como sede conceptual, pendiente de adaptación al formato activo del runtime. | Media (Codex no utiliza reglas por defecto). | Medio. Confusión de reglas ejecutables vs conceptuales. | Mantener sin front matter ni glob triggers. |
| `.agent/rules/00_reglas_locales_mvp_documental.md` | Regla documental, no activa. | Incompatible (no tiene triggers, metadata, globs o `alwaysApply`). | Incompatible (Codex no consume este formato de regla local). | Medio. Una herramienta externa podría intentar parsear el contenido. | No incorporar front matter ni activar comportamientos. |
| `.agent/workflows/` | Sede documental conceptual. | Alta (futura ubicación de workflows Antigravity). | Baja (Codex utiliza flujos secuenciales propios). | Medio. Duplicación metodológica. | Mantener como guías conceptuales en formato Markdown plano. |
| `.agent/workflows/sdd_feature_workflow.md` | Workflow conceptual, no activo. | Incompatible (no posee YAML metadata ni steps estructurados ejecutables). | No compatible como workflow activo de Codex; requeriría adaptación futura al mecanismo operativo que se decida para Codex. | Medio. Automatización involuntaria de transiciones. | Mantener en formato de texto plano sin directivas ejecutables. |
| `.agent/skills/` | Sede documental conceptual. | Alta (futura ubicación de habilidades Antigravity). | Baja (Codex puede preferir o buscar la carpeta `.agents/skills/`). | Alto. Divergencia en la ruta de descubrimiento de habilidades. | Evaluar futura matriz de compatibilidad antes de activar. |
| `.agent/skills/spec_author/SKILL.md` | Skill conceptual, no activa. | Incompatible (no tiene metadata `name`/`description`, ni inputs/outputs). | Incompatible (no tiene front matter de descubrimiento Codex). | Medio. Incompatibilidad de sintaxis de llamadas. | No añadir metadatos activos ni front matter. |
| `.agent/skills/implementer/SKILL.md` | Skill conceptual, no activa. | Incompatible (sin metadatos ni validadores deterministas). | Incompatible (sin front matter Codex). | Medio. Que un agente intente suplantar la skill de ejecución. | Preservar como plantilla informativa inerte. |
| `.agent/skills/reviewer/SKILL.md` | Skill conceptual, no activa. | Incompatible (sin metadatos ni validadores deterministas). | Incompatible (sin front matter Codex). | Medio. Autoaprobación accidental de entregables. | Preservar como contrato puramente documental de revisión. |
| `progress/current.md` | Log de progreso activo. | Compatible (solo lectura). | Compatible (solo lectura). | Bajo. Requiere actualización manual constante. | Mantener actualizado sin delegar a automatizaciones. |
| `progress/history.md` | Historial de hitos activo. | Compatible (solo lectura). | Compatible (solo lectura). | Bajo. Inflado excesivo de logs. | Registrar únicamente hitos de cierre verificados con hashes de Git. |
| `progress/snapshot_estado_2026-06-02.md` | Snapshot operativo. | Compatible (solo lectura). | Compatible (solo lectura). | Bajo. Pérdida de foco si se le asigna autoridad. | Mantener como recurso auxiliar sin autoridad normativa. |

---

## 6. Hallazgos
1. **Sintaxis Inerte y Ausencia de Metadatos:** Los recursos de habilidades (`spec_author`, `implementer` y `reviewer`) y la regla local de MVP carecen intencionalmente de front matter, identificadores únicos (`name`/`description`), parámetros tipados de entrada/salida y disparadores (`glob`, `alwaysApply` o triggers de ejecución). Por lo tanto, **no son recursos activos de Codex ni de Antigravity**.
2. **Divergencia en Nomenclatura del Repositorio:** El arnés utiliza actualmente el directorio `.agent/` en singular. No obstante, la especificación de Codex puede requerir o preferir el directorio `.agents/` (en plural) para el descubrimiento y escaneo automático de habilidades en el repositorio.
3. **Ausencia de Runtimes y Gates:** No existen los directorios `.agent/gates/` ni herramientas de orquestación técnica, manteniendo el desacoplamiento total del plano de ejecución.

---

## 7. Riesgos
- **Activación Prematura:** Si un desarrollador o agente traslada recursos a rutas activas, incorpora metadata requerida o configura reglas/skills como recursos activos del runtime, podrían quedar disponibles para descubrimiento o invocación de forma prematura.
- **Incompatibilidad Terminológica Futura:** Que la decisión de usar `.agent/` (Antigravity) o `.agents/` (Codex) quede indeterminada, forzando a reestructurar todo el árbol de archivos.
- **Riesgo de Duplicación Normativa:** Intentar traducir reglas metodológicas de `docs/` directamente al front matter de las rules de Antigravity sin usar referencias cruzadas, violando el principio de fuente única de verdad.

---

## 8. Decisiones que NO deben tomarse todavía
Durante la actual fase de MVP documental, queda estrictamente prohibido realizar cualquiera de las siguientes acciones:
- **No se debe crear el directorio `.agent/gates/`** ni automatizar validaciones deterministas.
- **No se debe crear el directorio `.agents/`** (plural) sin una previa decisión explícita de arquitectura.
- **No se debe agregar front matter, YAML metadata, ni parámetros activos** a las habilidades (`SKILL.md`) ni a las reglas locales.
- **No se debe activar ningún recurso agéntico** (rules, workflows o skills) en los motores de Codex o Antigravity en el workspace.

---

## 9. Recomendaciones Futuras
1. **Matriz de Equivalencia y Adaptación:** Diseñar una matriz que defina la equivalencia y mapeo entre las sedes documentales de Antigravity (`.agent/`) y el runtime de descubrimiento de Codex (`.agents/`).
2. **Decisión Arquitectónica Formal:** Evaluar si se mantiene `.agent/` como la sede conceptual y de gobernanza propia de este proyecto, utilizando `.agents/` exclusivamente como un adaptador de compilación o enlace simbólico cuando se prepare la integración con Codex.
3. **Criterios de Transición Documental a Activo:** Definir mediante un Architecture Decision Record (ADR) los criterios específicos que debe cumplir una skill documental para que se le autorice la adición de front matter y parámetros funcionales.
4. **Validación de Activación:** Diseñar planes de pruebas manuales y simulaciones (dry-runs) que se ejecuten obligatoriamente antes de activar formalmente cualquier regla o habilidad en el runtime.
5. **Preservar el Aislamiento Lean:** Garantizar que la documentación de las habilidades y workflows resida en formato Markdown estándar de lectura humana, separando nítidamente el diseño conceptual de la implementación instrumental del código.

---

## 10. Conclusión
El arnés se encuentra en un estado documental consistente y seguro. Las sedes de `.agent/` están debidamente aisladas de los motores de ejecución gracias a la ausencia intencional de metadatos de configuración. La principal recomendación es mantener este esquema inerte hasta que se defina la integración de Codex y Antigravity a través de decisiones formales de arquitectura.

---

## 11. Nota de No Autoridad Normativa
Este documento es un informe de auditoría informativa realizado al cierre de la sesión y no posee autoridad normativa. Las reglas, prohibiciones y guías rectores del proyecto raíz se encuentran exclusivamente en `docs/constitucion_del_proyecto.md` y `docs/00_mapa_y_gobernanza_documental.md`.
