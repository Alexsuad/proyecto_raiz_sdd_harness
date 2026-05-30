# File: docs/00_mapa_y_gobernanza_documental.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la gobernanza, organización, mantenimiento y auditoría de la documentación del proyecto raíz.
# Rol: Documento rector de gobernanza y mapa documental inicial del sistema.
# ──────────────────────────────────────────────────────────────────────

# 00 — Mapa y gobernanza documental

## 1. Propósito del documento
Este documento define cómo se organiza, mantiene y audita la documentación del proyecto raíz. Establece los estándares de calidad, las directrices contra la redundancia y los lineamientos de diseño para que toda la información técnica sea coherente y fácil de entender por desarrolladores y agentes de inteligencia artificial.

## 2. Principio de fuente de verdad
"Cada información debe tener una sola sede principal. Otros documentos pueden referenciarla, resumirla o aplicarla, pero no duplicarla completa."

Esto previene inconsistencias cuando las especificaciones o metodologías cambian y asegura que tanto humanos como agentes consulten datos siempre actualizados en su ubicación de origen.

## 3. Alcance del proyecto raíz
Este proyecto raíz no busca producir una aplicación final, sino crear una base metodológica, documental y agéntica reutilizable para futuros proyectos reales de desarrollo de software. Es el "arnés" o base metodológica que define cómo interactúan Codex, Antigravity, el ciclo SDD (Spec-Driven Development) y las validaciones automáticas.

## 4. Tipos de documentos del sistema
Los documentos que integran el sistema se clasifican en:
- **Documentos metodológicos**: Guías estructuradas que dictan cómo proceder en actividades de desarrollo y control.
- **Documentos operativos para agentes**: Instrucciones simplificadas y directrices en la raíz (ej. reglas e instrucciones de contexto) que indican a los asistentes de IA cómo actuar.
- **Constitución del proyecto**: El acuerdo inicial sobre las metas, alcance, límites y estándares de calidad del proyecto.
- **Preflight estructural**: checklist documental manual para verificar la coherencia del repositorio antes de avanzar.
- **Specs por feature**: Carpetas de especificaciones completas para características individuales de software.
- **Skills**: Contratos operativos reutilizables que extienden las habilidades de los agentes.
- **Workflows**: Flujos de pasos secuenciales para guiar la interacción humano-agente o multi-agente.
- **Scripts**: sede futura de scripts deterministas y gates automatizados.
- **Tests**: sede futura de pruebas del arnés.
- **ADR (Architecture Decision Records)**: Registro cronológico de decisiones arquitectónicas y técnicas críticas.
- **Anexos**: Repositorios de datos, logs, configuraciones o transcripciones largas para evitar inflar documentos maestros.
- **Progress e history**: seguimiento operativo, estado actual e historial de hitos del arnés.

## 5. Jerarquía documental inicial
La estructura de jerarquía y prioridad documental del proyecto raíz se define de la siguiente manera:
1. [00_mapa_y_gobernanza_documental.md](./00_mapa_y_gobernanza_documental.md)
2. [constitucion_del_proyecto.md](./constitucion_del_proyecto.md)
3. [01_metodologia_base_comun.md](./01_metodologia_base_comun.md)
4. [02_metodologia_desarrollo_software_sdd_harness.md](./02_metodologia_desarrollo_software_sdd_harness.md)
5. [preflight_estructural.md](./preflight_estructural.md)
6. `AGENTS.md` / `GEMINI.md`
7. `.agent/rules/`, `.agent/workflows/` y `.agent/skills/` como sedes documentales futuras no activas
8. `specs/`
9. `progress/`
10. `scripts/` y `tests/`
11. `anexos/`

Nota de subordinación operativa: `AGENTS.md`, `GEMINI.md` y la carpeta `.agent/` actúan como adaptadores y canalizadores de contexto para los agentes. No son documentos maestros y no pueden contradecir, reemplazar ni ignorar las normas definidas en `docs/00_mapa_y_gobernanza_documental.md`, `docs/constitucion_del_proyecto.md`, `docs/01_metodologia_base_comun.md` ni `docs/02_metodologia_desarrollo_software_sdd_harness.md`.

## 6. Qué vive en cada documento o carpeta

| Documento o carpeta | Función principal | Qué debe contener | Qué no debe contener |
| :--- | :--- | :--- | :--- |
| `docs/00_mapa_y_gobernanza_documental.md` | Rectoría y mapas | Propósito, jerarquías, reglas de nomenclatura, checklist de auditoría documental y mapa general. | Código fuente, reglas metodológicas detalladas de desarrollo o prompts. |
| `docs/01_metodologia_base_comun.md` | Metodología común | Estándares transversales, lineamientos de comunicación, uso de herramientas generales y filosofía de trabajo. | Código de software, especificaciones de features específicas. |
| `docs/02_metodologia_desarrollo_software_sdd_harness.md` | Guía de SDD y desarrollo | Flujo SDD detallado, guías de arquitectura limpia, tooling estándar, QA y procesos de compilación. | Reglas documentales generales, acuerdos comerciales del proyecto. |
| `docs/03_metodologia_proyectos_documentales_agenticos.md` | [POST-MVP - PLACEHOLDER] Ruta documental/agéntica futura | Referencia mínima de que existirá una metodología futura para proyectos documentales, creativos o analíticos. | Desarrollo completo de la metodología documental/agéntica durante el MVP actual, lógica de negocio o base de datos del proyecto. |
| `docs/constitucion_del_proyecto.md` | Definición de límites y objetivos | Alcance del proyecto, roles, hitos, tecnologías principales permitidas y límites de presupuesto/tiempo. | Guías paso a paso de codificación, scripts de automatización. |
| `docs/preflight_estructural.md` | Checklist documental de preflight. | Revisión manual de estructura base, estado agéntico, no duplicación, criterio LEAN, bloqueos y resultado esperado. | Scripts ejecutables, automatización, gates activos o metodología extensa. |
| `AGENTS.md` | Instrucciones operativas de agentes | Instrucciones específicas de arranque, comportamiento y restricciones inmediatas para agentes de IA de desarrollo. | Metodologías de desarrollo extensas, código de aplicación. |
| `GEMINI.md` | Adaptador operativo para Gemini | Contexto mínimo, restricciones operativas y referencias hacia la constitución, el mapa documental y los documentos operativos autorizados. | Reglas de estilo de código general, arquitectura del software. |
| `.agent/skills/` | Sede documental futura de skills. | README de sede, futura estructura de skills y criterios mínimos para `SKILL.md` cuando se autorice su creación. | Skills activas, código de productos derivados, metodología completa o credenciales. |
| `.agent/workflows/` | Sede documental futura de workflows. | README de sede, estructura futura de workflows, regla de descripción máxima de 250 caracteres y criterios de diseño. | Workflows activos, scripts ejecutables, specs de features o reportes de progreso. |
| `.agent/rules/` | Sede documental futura de rules locales. | README de sede y criterios para futuras reglas breves, claras y accionables. | Rules activas, metodología completa, prompts extensos, credenciales o configuraciones sensibles. |
| `specs/` | Especificaciones de features | Carpetas individuales por característica con sus requerimientos, diseños, tareas e historial de cambios. | Metodología del proyecto general, utilidades compartidas de código. |
| `progress/` | Seguimiento operativo del arnés. | `README.md`, `current.md`, `history.md`, estado actual, hitos relevantes, bloqueos futuros y cierres con evidencia. | Specs aprobadas, metodología completa, código o decisiones arquitectónicas que deban vivir en ADR. |
| `scripts/` | Sede futura de scripts y gates deterministas. | README de sede, scripts de validación, gates automatizados y utilidades deterministas cuando sean autorizados. | Código core de productos derivados, credenciales, tokens, prompts extensos o specs. |
| `tests/` | Sede futura de pruebas del arnés. | README de sede, tests de gates, tests de estructura, smoke tests, pruebas de integración y validaciones del arnés cuando existan. | Specs, reportes de progreso, credenciales, tokens o código de productos derivados. |
| `docs/adr/` | Decisiones de arquitectura | Registros históricos numerados de decisiones de diseño, justificaciones técnicas y alternativas descartadas. | Documentos de requerimientos iniciales de usuario. |
| `anexos/` | Soporte de datos e investigación | Transcripciones, dumps de datos de prueba, especificaciones de terceros o logs extensos de auditoría. | Código fuente ejecutable, reglas metodológicas globales. |

## 7. Reglas contra duplicación
Una regla o definición no debe copiarse completa en múltiples documentos. Si una regla vive en la constitución o metodología principal:
- `AGENTS.md` y `GEMINI.md` deben hacer una referencia mediante enlaces relativos hacia ella, en lugar de duplicarla.
- Si es necesario resumirla para fines operativos de los agentes, se colocará un extracto mínimo y se apuntará explícitamente a la sede principal para evitar que la regla quede desactualizada.

## 8. Reglas para AGENTS.md y GEMINI.md
`AGENTS.md` y `GEMINI.md` no son documentos maestros de conocimiento ni metodológicos.
- Son adaptadores operativos pragmáticos diseñados para orientar al agente al iniciar sesión o en su ejecución.
- Deben ser breves, directos, orientados a la acción y referenciar la constitución y este mapa documental para detalles normativos profundos.

## 9. Reglas para skills y workflows
Una skill o workflow no es un prompt suelto o una instrucción informal.
- Cada skill debe entenderse y estructurarse como un contrato operativo reutilizable.
- Debe incluir: propósito claro, entradas esperadas (esquema), límites de operación, pasos exactos de procesamiento, criterios de validación y la evidencia resultante esperada.

Durante la fase documental/MVP estructural, `.agent/skills/`, `.agent/workflows/` y `.agent/rules/` son sedes documentales futuras. Ningún archivo dentro de esas carpetas debe interpretarse como recurso activo hasta que exista autorización explícita, revisión y evidencia.

## 10. Reglas para specs por feature
Cada funcionalidad relevante (feature) del sistema se gestionará dentro de su propio subdirectorio en `specs/<feature_id>/`. Este debe estructurarse obligatoriamente con los siguientes archivos:
- `requirements.md`: Definición funcional del requisito, casos de uso y criterios de aceptación.
- `clarifications.md`: Registro de dudas resueltas por el humano y aclaraciones técnicas.
- `design.md`: Arquitectura, diagramas de secuencia, flujos de datos e interfaz.
- `tasks.md`: Lista de tareas granularizadas para la implementación.
- `validation.md`: Pruebas a realizar y criterios automáticos/manuales de aceptación.
- `review.md`: Registro de feedback y revisiones post-implementación.

## 11. Reglas para anexos
Los anexos se utilizarán exclusivamente para contenido extenso, dumps de datos de prueba, registros detallados de logs o información de soporte de terceros. Esto mantiene los documentos conceptuales y metodológicos limpios, ligeros y enfocados. Todo anexo debe estar correctamente referenciado desde al menos un documento principal.

## 12. Reglas para ADR (Architecture Decision Records)
Cualquier decisión técnica o arquitectónica relevante que afecte el flujo del programa, la selección de herramientas clave o la estructura de datos:
- Debe documentarse como un archivo ADR individual dentro de la carpeta `docs/adr/`.
- Debe seguir la estructura estándar: Título, Contexto, Decisión, Consecuencias y Estado (Propuesto/Aceptado/Reemplazado).
- No debe quedar diluida en comentarios de código ni en la memoria del historial del chat.

## 13. Nomenclatura documental
Para asegurar el orden y la coherencia en el repositorio, se aplican las siguientes directrices:
- **Números iniciales**: Los documentos clave del directorio `docs/` deben ir numerados cronológica o jerárquicamente (ej. `00_mapa_y_gobernanza_documental.md`, `01_metodologia_base_comun.md`).
- **snake_case**: Todos los nombres de archivos y carpetas del sistema documental deben estar escritos en minúsculas y separados por guiones bajos (ej. `constitucion_del_proyecto.md`).
- **Nombres descriptivos**: Evitar el uso de nombres genéricos, temporales o ambiguos como `documento_final.md`, `notas.md`, `version_nueva.md` o `temp.md`.
- **Excepciones por interoperabilidad**: Se exceptúan de la regla `snake_case` las carpetas y archivos nativos exigidos por herramientas, IDEs o agentes de IA, como `.agent/`, `AGENTS.md`, `GEMINI.md`, `SKILL.md`, `README.md` u otros nombres requeridos por compatibilidad. Estas excepciones deben usarse solo cuando respondan a una convención real de la herramienta.

## 14. Auditoría documental mínima
Antes de dar por cerrado un ciclo de cambios en la documentación, se debe verificar este checklist:
- [ ] No hay duplicación innecesaria de contenido.
- [ ] Cada regla o estándar del proyecto tiene una única sede principal identificada.
- [ ] Los documentos operativos de los agentes (`AGENTS.md`, `GEMINI.md`) no contradicen ni reemplazan las metodologías de `docs/`.
- [ ] Las especificaciones técnicas (`specs/`) están alineadas y no contradicen la constitución del proyecto.
- [ ] Los archivos de anexo están vinculados y referenciados desde un documento maestro.
- [ ] Los cambios importantes a nivel documental quedan registrados en el control de cambios de cada archivo.
- [ ] No se agregaron carpetas o archivos documentales fuera de la estructura autorizada por este mapa.
- [ ] `docs/preflight_estructural.md` fue revisado antes de crear nuevas piezas estructurales.
- [ ] `progress/current.md` refleja el estado operativo actual del arnés.
- [ ] `progress/history.md` registra los hitos relevantes sin convertirse en bitácora excesiva.
- [ ] `.agent/` sigue documentado como sede futura y no como sistema activo, salvo autorización explícita.

## 15. Estado del documento
- **Estado**: Borrador consolidado inicial.
- **Uso**: Documento rector para iniciar la separación documental del proyecto raíz.
- **Pendiente**: Validar nuevamente tras la primera feature piloto o cuando se cree el primer recurso activo real del arnés.
