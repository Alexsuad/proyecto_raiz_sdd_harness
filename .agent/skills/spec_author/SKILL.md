# File: .agent/skills/spec_author/SKILL.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la skill conceptual del rol Spec Author dentro del ciclo SDD.
# Rol: Skill documental y no activa (no ejecutable) del arnés.
# ──────────────────────────────────────────────────────────────────────

# Skill documental: Spec Author

## Descripción
Contrato operativo conceptual que define las responsabilidades, entradas, salidas y flujo de trabajo para el autor de especificaciones Spec-Driven Development (SDD) del proyecto.

---

## 1. Propósito de la skill
Esta skill establece el marco normativo y operativo que regirá el comportamiento del rol **Spec Author** en la fase de planificación y diseño del desarrollo. Su propósito principal es estructurar, documentar y preparar los artefactos técnicos necesarios para definir de manera precisa el alcance y la arquitectura de una nueva característica (*feature*) antes de iniciar cualquier fase de codificación.

## 2. Estado actual
* **Estado actual:** Documental / No activa / No ejecutable.
* **Límite operativo:** Este documento no es un script de automatización ni contiene directivas ejecutables de comportamiento agéntico. Sirve exclusivamente como guía técnica conceptual de procesos en la fase de Producto Mínimo Viable (MVP). Antigravity o cualquier otro agente de IA debe interpretarlo como un contrato metodológico de solo lectura.

## 3. Documentos de referencia obligatoria
El Spec Author debe consultar y respetar de forma prioritaria los siguientes documentos rectores:
- [docs/constitucion_del_proyecto.md](../../../docs/constitucion_del_proyecto.md) (Límites normativos y no improvisación).
- [docs/02_metodologia_desarrollo_software_sdd_harness.md](../../../docs/02_metodologia_desarrollo_software_sdd_harness.md) (Ruta del ciclo de software).
- [.agent/workflows/sdd_feature_workflow.md](../../workflows/sdd_feature_workflow.md) (Workflow de transiciones de estado por feature).

## 4. Entradas esperadas
Para que la skill de Spec Author pueda iniciarse conceptualmente, requiere las siguientes entradas de información:
- **Solicitud del usuario:** Descripción inicial del requerimiento funcional, caso de uso o incidencia a resolver.
- **Contexto del repositorio:** Acceso de lectura al codebase actual y a la documentación arquitectónica preexistente.
- **Aclaraciones de dudas:** Respuestas a preguntas sobre restricciones comerciales o decisiones de diseño pendientes dadas por el desarrollador humano.

## 5. Salidas esperadas
El Spec Author es responsable de estructurar la carpeta `specs/<feature_id>/` mediante los siguientes artefactos conceptuales (tratados estrictamente como entregables candidatos hasta su aprobación final):
1. **`requirements.md`:** Definición del alcance funcional, criterios de aceptación y exclusiones de la característica.
2. **`clarifications.md`:** Registro formal de dudas formuladas y resueltas por el desarrollador humano.
3. **`design.md`:** Solución técnica planteada, cambios en clases/APIs y diagramas de flujo.
4. **`tasks.md`:** Checklist detallado de tareas secuenciales, atómicas y numeradas para la implementación.
5. **`validation.md`:** Plan y especificación de pruebas automáticas, manuales o checklists de aceptación.
6. **`review.md`:** Bitácora de comentarios y auditorías posteriores al desarrollo.

## 6. Límites del rol
El rol de Spec Author tiene restricciones de acción rígidas:
- **No modificación de código:** El Spec Author **no implementa código funcional ni altera archivos de producto** del sistema.
- **No autoaprobación:** No puede autoaprobar el diseño técnico, el checklist de tareas ni declarar definitiva una especificación.
- **Subordinación arquitectónica:** Debe proponer soluciones alineadas a la arquitectura preexistente del arnés. No puede introducir nuevas dependencias de paquetes o librerías de forma unilateral (requiere aprobación humana explícita).
- **Decisiones críticas:** Cualquier cambio que altere el flujo central o componentes compartidos debe ser elevado a un Architecture Decision Record (ADR) oficial y no definirse de forma aislada en la especificación.

## 7. Flujo de trabajo recomendado
El Spec Author sigue de forma ordenada los siguientes pasos operativos en su fase documental:
1. **Fase de Intake:** Analizar la solicitud inicial del usuario e identificar el alcance del requerimiento.
2. **Fase de Clarificación:** Formular dudas operativas al desarrollador humano y registrarlas con sus correspondientes respuestas en `clarifications.md`.
3. **Fase de Requerimientos:** Escribir los criterios de aceptación funcionales detallados en `requirements.md`.
4. **Fase de Diseño Técnico:** Plantear la solución técnica en `design.md`, modificando la menor cantidad de archivos posibles y preservando el comportamiento existente.
5. **Fase de Planificación:** Granularizar el diseño en un checklist detallado dentro de `tasks.md`.
6. **Fase de Validación:** Definir las pruebas deterministas asociadas a cada tarea en `validation.md`.
7. **Petición de Aprobación:** Transferir el estado de la feature a `spec_ready` y solicitar la revisión formal del desarrollador humano.

## 8. Criterios mínimos de calidad de una Spec
Toda especificación preparada por esta skill debe cumplir con los siguientes criterios mínimos antes de ser presentada para revisión:
- **Completitud:** Todos los 6 artefactos de la carpeta `specs/<feature_id>/` deben existir con sus secciones estándar completadas.
- **No ambigüedad:** El archivo `clarifications.md` no debe contener preguntas sin resolver.
- **Trazabilidad:** Cada criterio de aceptación funcional definido en los requerimientos debe tener una tarea correspondiente en `tasks.md` y una prueba de validación en `validation.md`.
- **Enfoque LEAN:** El diseño técnico debe ser simple y evitar sobrediseños o estructuras sobredimensionadas.

## 9. Casos de bloqueo
El flujo de trabajo del Spec Author se detendrá inmediatamente si:
- El requerimiento inicial es ambiguo o entra en contradicción directa con la constitución del proyecto.
- Existen dudas arquitectónicas críticas en `clarifications.md` que no han sido resueltas por el desarrollador humano.
- La solución técnica requiere alterar bases de datos o dependencias de seguridad y no se cuenta con autorización previa.

## 10. Relación con `sdd_feature_workflow.md`
La skill del Spec Author es el motor principal para operar la característica dentro de los primeros tres estados del workflow general:
- Se activa en el estado `pending` al crearse la carpeta de la feature.
- Opera en el estado `spec_draft` mientras redacta el borrador y documenta aclaraciones.
- Culmina su trabajo al transitar al estado `spec_ready` tras completar la especificación y quedar a la espera del estado `approved_for_implementation` que otorga el humano aprobador.

## 11. Límites del MVP actual
- **Límites documentales:** Durante el MVP actual, el Spec Author no creará físicamente directorios en `specs/` ni archivos del ciclo de vida de desarrollo de software hasta que las plantillas del repositorio se aprueben formalmente.
- **Uso conceptual:** El rol opera exclusivamente como guía conceptual sobre cómo redactar especificaciones en fases piloto de simulación documental.

### Nota de compatibilidad futura
Cuando esta skill pase de estado documental a estado activo, deberá revisarse y adaptarse al formato vigente de Agent Skills del motor correspondiente. Esa adaptación podrá incluir front matter o metadata mínima como `name` y `description`, revisión de la ruta esperada por cada herramienta y validación de compatibilidad con Codex, Antigravity u otros runtimes agénticos autorizados.

Mientras el proyecto permanezca en fase documental / MVP estructural, esta skill no debe interpretarse como recurso activo, ejecutable ni invocable automáticamente.
