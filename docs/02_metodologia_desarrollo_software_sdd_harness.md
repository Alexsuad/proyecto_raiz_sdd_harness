# File: docs/02_metodologia_desarrollo_software_sdd_harness.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la metodología específica de desarrollo de software con SDD y arnés agéntico.
# Rol: Documento de especificación metodológica de software subordinado a los principios comunes.
# ──────────────────────────────────────────────────────────────────────

# 02 — Metodología de desarrollo de software con SDD y harness agéntico

## 1. Propósito del documento
Este documento define la ruta específica para proyectos de desarrollo de software utilizando Spec-Driven Development (SDD), validación técnica determinista, revisión cruzada y soporte mediante arnés agéntico. Sirve como guía técnica inicial para los futuros proyectos derivados, asegurando la reproducibilidad, la calidad y el control en cada cambio del código.

## 2. Relación con los documentos anteriores
Este documento:
- Se subordina jerárquicamente a [docs/00_mapa_y_gobernanza_documental.md](./00_mapa_y_gobernanza_documental.md).
- Aplica directamente los principios fundamentales descritos en [docs/01_metodologia_base_comun.md](./01_metodologia_base_comun.md).
- Desarrolla únicamente la ruta específica para software, código y validación técnica.
- No abarca la ruta metodológica documental y agéntica, la cual está planificada como una fase futura post-MVP.

## 3. Alcance de la ruta software
Esta metodología es la ruta de referencia obligatoria para todo proyecto derivado del arnés cuyo entregable principal sea software ejecutable, integrable o mantenible. Su profundidad de aplicación debe ajustarse al tamaño, riesgo e impacto del cambio, manteniendo siempre trazabilidad, validación y cierre con evidencia. Aplica especialmente a:
- Desarrollo de Backend (servicios y servidores).
- Interfaces de usuario frontend.
- Desarrollo y diseño de APIs.
- Herramientas de línea de comandos (CLI).
- Scripts de automatización en Python u otros lenguajes.
- Paneles y dashboards de visualización de datos.
- Integraciones de sistemas de terceros.
- Aplicaciones o conectores con bases de datos.
- Herramientas internas y utilidades de soporte técnico.

## 4. Principio rector de la ruta software
En proyectos de software no basta con que la inteligencia artificial o el agente escriban y entreguen código. Todo cambio en el codebase debe nacer de una necesidad documentada, convertirse en una especificación clara, pasar por un diseño técnico validado y tareas granularizadas, implementarse como código candidato, verificarse mediante pruebas deterministas, pasar revisión cruzada y consolidarse mediante un cierre con evidencia verificable.

## 5. Flujo general de trabajo
El ciclo de vida de un cambio o característica de software sigue la siguiente secuencia conceptual:

Necesidad o solicitud
↓
Fase 00 mínima (evaluación de la idea)
↓
Visión y alcance (definición del límite)
↓
Requisitos y reglas de negocio
↓
Arquitectura y decisiones técnicas
↓
Spec operativa por feature
↓
Implementación candidata
↓
Validación técnica y QA (testing automático/manual)
↓
Revisión cruzada (humana o multi-agente)
↓
Cierre con evidencia (merge, diff y commits)

## 5.1. Profundidad proporcional del flujo SDD

No todos los cambios requieren el mismo nivel de formalidad documental. Para mantener el enfoque LEAN, la profundidad del flujo SDD debe ajustarse al riesgo, impacto y tamaño del cambio.

| Tipo de cambio | Profundidad recomendada | Evidencia mínima esperada |
| :--- | :--- | :--- |
| Cambio mínimo o corrección menor | Checklist simple | Diff revisado y validación básica |
| Cambio pequeño de bajo riesgo | Mini-spec | Objetivo, alcance, archivos afectados y prueba básica |
| Feature nueva | SDD completo por feature | `requirements.md`, `clarifications.md`, `design.md`, `tasks.md`, `validation.md` y `review.md` |
| Cambio arquitectónico | SDD completo + ADR | Spec completa, ADR y revisión humana |
| Seguridad, datos, permisos, costes o producción | SDD completo + gate bloqueante | Validación automática, validación manual documentada y aprobación humana |
| Skill, workflow o gate del arnés | SDD completo + revisión cruzada | Spec, prueba controlada y evidencia de comportamiento esperado |

La decisión de usar un flujo reducido debe quedar justificada. Un flujo reducido no elimina la obligación de validar ni de dejar evidencia.

El orquestador, agente o herramienta de IA puede proponer una reducción de profundidad del flujo SDD cuando el cambio sea claramente pequeño, de bajo riesgo y con impacto limitado. Sin embargo, no debe aplicar automáticamente esa reducción si existe duda razonable sobre impacto, riesgo o alcance. Para cambios mínimos de bajo riesgo podrá avanzar con flujo reducido solo si cumple criterios objetivos, deja evidencia y pasa revisión o checklist. Si el cambio afecta arquitectura, datos, seguridad, permisos, costes, producción, integraciones o comportamiento funcional existente, requiere autorización humana explícita.

## 6. Fase 00 mínima en proyectos de software
Antes de planificar cualquier esfuerzo de desarrollo de software, debe existir una evaluación preliminar básica que considere:
- Una necesidad inicial del negocio o del usuario.
- Un solicitante o impulsor del cambio bien identificado.
- Un problema, dolor, riesgo u oportunidad real a resolver.
- El resultado mínimo esperado que defina el éxito de la intervención.
- Una decisión formal para avanzar, solicitar más detalles o descartar la iniciativa.

*Nota: Esta fase permanecerá en su versión más simple e introductoria durante el desarrollo del MVP actual del arnés.*

## 7. Spec operativa por feature
Toda característica relevante (feature) del sistema se gestionará dentro de su propio subdirectorio en `specs/<feature_id>/` (carpeta que será creada en fases posteriores del proyecto). Los archivos previstos dentro de esta estructura y sus funciones principales son:
- **`requirements.md`**: Define los casos de uso, restricciones de usuario y criterios de aceptación funcionales.
- **`clarifications.md`**: Registra las dudas resueltas por el humano y los supuestos de negocio.
- **`design.md`**: Detalla la arquitectura de la solución, clases, APIs a modificar y flujos de datos.
- **`tasks.md`**: Lista granular de subtareas numeradas y atómicas necesarias para implementar el diseño.
- **`validation.md`**: Describe las pruebas y el plan de verificación de los criterios de aceptación.
- **`review.md`**: Documenta el resultado de las revisiones, auditorías de calidad y feedback del humano.

## 8. Clarificación antes del diseño
Si existen dudas, huecos normativos, zonas grises o ambigüedades en los requerimientos, la IA no debe asumir comportamientos ni inventar soluciones por su cuenta. Se deben recopilar y registrar formalmente estas preguntas o supuestos pendientes en el archivo `clarifications.md` (que será creado en fases posteriores) y alinearse con el desarrollador humano antes de redactar el diseño técnico o escribir código.

## 9. Diseño antes de implementación
El diseño de la feature, documentado en `design.md` (que será creado en fases posteriores), debe plantear la solución técnica detallada antes de programar. El diseño debe estructurarse de tal manera que resuelva el requerimiento alterando el menor número de archivos posible, respetando la arquitectura preexistente del sistema y absteniéndose de introducir nuevas dependencias de librerías a menos que estén previamente autorizadas.

## 10. Tasks pequeñas y verificables
El archivo `tasks.md` (que será creado en fases posteriores) debe traducir el diseño en un checklist detallado de tareas pequeñas, ordenadas de forma secuencial y lógica. Cada tarea individual debe ser atómica y contar con una forma directa de verificar su correcta ejecución mediante una prueba técnica simple.

## 11. Implementación candidata
El código generado de manera preliminar por la IA o los agentes se clasifica como código candidato. Este código debe:
- Preservar la funcionalidad existente del sistema.
- Evitar regresiones de software mediante pruebas retrospectivas.
- Mantenerse limpio, legible y adherido al estándar del proyecto.
- No incluir código muerto, comentarios obsoletos, prints de depuración ni duplicidades.

No podrá consolidarse como código definitivo en el codebase principal hasta que apruebe la validación técnica determinista, pase la revisión cruzada obligatoria y cuente con evidencia de cierre.

## 12. Validación, QA y pruebas
El testing en el arnés no es una actividad opcional al final del desarrollo; se gestiona como una fase formal y rigurosa. Los niveles de prueba conceptualizados son:
- **Tests unitarios:** Validación de funciones o clases aisladas.
- **Tests de integración:** Verificación del comportamiento conjunto de varios módulos.
- **Tests end-to-end (E2E):** Pruebas de flujos completos de usuario si el sistema cuenta con interfaz.
- **Smoke test:** Pruebas rápidas para asegurar la estabilidad básica post-despliegue o post-compilación.
- **Pruebas manuales críticas:** Escenarios exploratorios realizados por humanos.
- **Revisión con checklist:** Control sistemático de calidad de código y diseño.

*Importante: Cualquier funcionalidad relacionada con transacciones financieras, manejo de datos personales/sensibles, gestión de permisos, entornos de producción o integraciones críticas requiere obligatoriamente una validación manual documentada que complemente a los tests automatizados.*

## 13. Estados de una feature
Para el control y seguimiento técnico, cada feature transitará por los siguientes estados:
- **`pending`**: Feature identificada pero sin trabajo iniciado.
- **`spec_draft`**: Redacción inicial de requerimientos y aclaraciones.
- **`spec_ready`**: Requerimientos listos y aclarados.
- **`approved_for_implementation`**: Diseño aprobado por el humano, listo para programar.
- **`in_progress`**: Implementación de código candidato en curso.
- **`implementation_done`**: Código candidato completado y listo para pruebas.
- **`qa_pending`**: Pendiente de ejecución de validaciones automáticas y manuales.
- **`review_pending`**: Pruebas pasadas; pendiente de auditoría y revisión humana final.
- **`done`**: Modificaciones consolidadas y aprobadas en el codebase principal.
- **`blocked`**: Trabajo detenido debido a impedimentos o dependencias externas.
- **`re_plan_required`**: Gate de validación fallido; requiere replanificar el diseño o tareas.

*Nota: Estos estados se reflejarán más adelante en los archivos del directorio de seguimiento `progress/` (que será creado en fases posteriores).*

## 14. Roles mínimos del arnés
Los roles mínimos concebidos en el flujo del arnés son:
- **Orquestador (Leader):** Coordina los pasos del flujo, delega tareas y controla las transiciones de estado de la feature.
- **Spec Author:** Redacta y clarifica los requerimientos, supuestos y criterios de aceptación de la característica. Puede proponer un diseño técnico inicial, pero las decisiones técnicas relevantes deben revisarse antes de autorizar la implementación.
- **Implementer:** Se encarga de escribir el código candidato y los scripts de prueba que implementan la especificación.
- **Reviewer:** Realiza auditorías de código, valida los criterios de calidad e identifica errores o deuda técnica.
- **Humano Aprobador:** Desarrollador humano con la última palabra para validar transiciones críticas, resolver dudas en aclaraciones y firmar el cierre de la feature.

*Nota: Estos roles se estructurarán operativamente mediante agentes de IA dedicados, configuraciones de prompts o tareas del programador humano según el entorno disponible.*

Los agentes pueden realizar autoauditoría como primera revisión interna de su propio trabajo, pero esa autoauditoría no equivale a aprobación definitiva. En cambios relevantes, la validación debe realizarla un rol distinto, como un reviewer, un qa_reviewer, un gate automatizado, un checklist independiente o el humano aprobador.

## 15. Harness para Codex y Antigravity
El arnés (harness) no debe confundirse con el modelo de lenguaje en sí. Es la infraestructura de reglas, documentos, flujos de trabajo, habilidades agénticas, checkpoints de avance y bitácoras que enmarcan la operación de Codex y Antigravity en el workspace.
- `AGENTS.md` actúa como adaptador operativo mínimo para Codex y agentes compatibles.
- `GEMINI.md` actúa como adaptador operativo mínimo para Gemini y Antigravity.
- `.agent/rules/`, `.agent/workflows/` y `.agent/skills/` existen como sedes documentales conceptuales no activas, aunque ya contienen recursos documentales no ejecutables.
- Estos adaptadores y sedes deben vincularse a la constitución y gobernanza del proyecto mediante referencias cruzadas en lugar de duplicar sus lineamientos.

## 16. Gates de la ruta software
Los gates son puntos de control y calidad que regulan el avance entre fases. Se clasifican de forma general en:
- **Gates documentales:** Revisión y completitud de especificaciones escritas.
- **Gates técnicos:** Herramientas automáticas (ej. linters, analizadores de tipos, compiladores).
- **Gates manuales:** Revisión humana y firma visual.
- **Gates automatizados:** Cobertura de pruebas unitarias o de integración.

Se proyectan los siguientes gates conceptuales para la ruta de desarrollo (cuyos scripts de validación automática serán programados en fases posteriores):
- **`gate_0_preflight`**: Comprobación inicial de limpieza del área de trabajo, variables de entorno y dependencias.
- **`gate_spec_ready`**: Verificación documental de que la especificación y aclaraciones de la feature están completas y aprobadas.
- **`gate_pre_implementation`**: Validación de que el diseño y el checklist de tareas cuentan con aprobación humana para iniciar codificación.
- **`gate_review`**: Verificación de que el código candidato pasa los tests, no rompe la arquitectura y está listo para la revisión final de código.

## 17. Regla de replanificación
Si una característica de software falla en superar un gate crítico, un test de regresión, una validación de negocio o una validación técnica compleja, está prohibido realizar parches rápidos o modificaciones ad-hoc a ciegas. El agente debe detener el proceso de codificación, registrar la evidencia detallada de la falla en `validation.md` o `review.md`, revisar la especificación y el diseño técnico, ajustar el plan en `tasks.md` cuando corresponda, y reiniciar el ciclo de validación de manera ordenada. Solo se usará `clarifications.md` si la falla revela una ambigüedad, duda o supuesto no resuelto en los requisitos.

## 18. Límites del MVP actual
Este documento establece la estructura lógica de desarrollo de software, pero no crea ni habilita de forma operativa los siguientes elementos, los cuales quedan pendientes para fases posteriores:

- Plantillas documentales formalizadas para los archivos de la carpeta `specs/`.
- Skills activas (`.agent/skills/`).
- Workflows activos (`.agent/workflows/`).
- Rules activas (`.agent/rules/`).
- Scripts ejecutables de validación técnica o gates automatizados.
- Tests reales del arnés.
- Implementaciones de código productivo o suite de pruebas unitarias reales.

`AGENTS.md`, `GEMINI.md` y `progress/` ya existen como adaptadores y sedes documentales mínimas dentro de la fase documental / MVP estructural. Su existencia no autoriza implementación sobre código real ni activación de automatización.

Mientras no existan plantillas mínimas de specs, recursos agénticos activos autorizados y gates mínimos auditados, ningún agente implementador debe activarse sobre código real de un proyecto derivado. Hasta entonces, el arnés solo puede usarse para planificación, documentación, simulación controlada o pruebas piloto sin impacto productivo.

## 19. Estado del documento
- **Estado:** aprobado para fase documental / MVP estructural.
- **Uso:** metodología inicial vigente para orientar la ruta de desarrollo de software con SDD durante la fase documental actual.
- **Pendiente:** revalidar y ajustar tras la primera especificación de feature piloto del arnés o cuando se cree el primer recurso activo real.
