# File: .agent/skills/implementer/SKILL.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la skill conceptual del rol Implementer dentro del ciclo SDD.
# Rol: Skill documental y no activa (no ejecutable) del arnés.
# ──────────────────────────────────────────────────────────────────────

# Skill documental: Implementer

## Descripción
Contrato operativo conceptual que define las responsabilidades, entradas, salidas y flujo de trabajo para el programador de código candidato bajo el ciclo Spec-Driven Development (SDD).

---

## 1. Propósito de la skill
Esta skill establece el marco metodológico y operativo que regirá el comportamiento del rol **Implementer** en la fase de codificación y desarrollo de software. Su objetivo principal es asegurar que la implementación del código candidato se realice de forma ordenada, adhiriéndose estrictamente al diseño técnico, preservando la estabilidad del sistema mediante validaciones y colaborando de forma segura con el resto de roles del repositorio.

## 2. Estado actual
* **Estado actual:** Documental / No activa / No ejecutable.
* **Límite operativo:** Este documento es una especificación conceptual para la fase de Producto Mínimo Viable (MVP). No contiene lógica de ejecución, scripts de automatización ni configuraciones activas. Antigravity o cualquier otro agente de IA debe interpretarlo exclusivamente como material informativo y de solo lectura.

## 3. Documentos de referencia obligatoria
El Implementer debe consultar y respetar de forma prioritaria las siguientes fuentes de verdad del repositorio:
- [docs/constitucion_del_proyecto.md](../../../docs/constitucion_del_proyecto.md) (Código candidato, no improvisación y revisión cruzada).
- [docs/02_metodologia_desarrollo_software_sdd_harness.md](../../../docs/02_metodologia_desarrollo_software_sdd_harness.md) (Ruta del ciclo de software y pruebas).
- [.agent/workflows/sdd_feature_workflow.md](../../workflows/sdd_feature_workflow.md) (Workflow de transiciones de estado por feature).
- [.agent/skills/spec_author/SKILL.md](../spec_author/SKILL.md) (Skill del rol autor de especificaciones).

## 4. Entradas esperadas futuras
Para que el Implementer inicie conceptualmente su labor de codificación, debe contar de manera obligatoria con los siguientes artefactos:
- **`specs/<feature_id>/requirements.md`:** Criterios de aceptación funcionales claros.
- **`specs/<feature_id>/clarifications.md`:** Dudas resueltas y supuestos validados.
- **`specs/<feature_id>/design.md`:** Diseño técnico aprobado y archivos a modificar identificados.
- **`specs/<feature_id>/tasks.md`:** Checklist detallado de tareas granularizadas y numeradas.
- **`specs/<feature_id>/validation.md`:** Plan y criterios de pruebas locales definidos.
- **Aprobación humana explícita:** Confirmación documentada del aprobador humano para pasar al estado de implementación (`approved_for_implementation`).

## 5. Salidas esperadas futuras
La labor del Implementer dará como resultado la preparación de las siguientes salidas candidatas:
- **Código candidato:** Modificaciones localizadas en los archivos fuente explícitamente autorizados en `design.md`.
- **Reporte de implementación:** Resumen de las modificaciones aplicadas, lógica agregada y archivos intervenidos.
- **Evidencias de validación:** Logs, salidas de terminal o reportes de ejecución que acrediten el paso de las pruebas locales de `validation.md`.
- **Propuesta de actualización de pruebas:** Modificaciones sugeridas en `validation.md` si durante el desarrollo se identificó una brecha en los casos de prueba.
- **Trazabilidad de incidencias:** Lista de riesgos, dudas de última hora o bloqueos técnicos detectados.
- **Petición de revisión:** Solicitud formal de inspección dirigida al `reviewer` o al desarrollador humano.

## 6. Límites del rol
El Implementer opera bajo restricciones críticas que garantizan la gobernanza y estabilidad técnica:
- **No inicio sin spec aprobada:** El Implementer **no puede iniciar trabajo en el código** si la feature no se encuentra en el estado `approved_for_implementation`.
- **No autoaprobación:** El Implementer no puede autoaprobar su código candidato ni declararlo como definitivo para su fusión en la rama principal.
- **Prohibido saltarse controles:** El Implementer no puede saltarse gates de calidad, validaciones deterministas automáticas ni el paso por la revisión cruzada independiente.
- **Aislamiento del diseño:** El Implementer debe ceñirse al diseño técnico documentado en `design.md`. Si el desarrollo revela la necesidad de modificar un archivo no mapeado en el diseño original, debe pausar la tarea y solicitar un ajuste de la spec.
- **Zonas críticas y escalamiento:** Si el código candidato involucra cambios en la arquitectura del sistema, adición de nuevas dependencias externas, permisos de acceso, seguridad, persistencia de datos reales, costes financieros o entornos de producción, el Implementer debe detenerse, documentar el caso como un bloqueo y elevarlo a aprobación humana o a la redacción de un ADR.

## 7. Flujo de trabajo recomendado
El Implementer sigue conceptualmente la siguiente secuencia operativa:
1. **Recepción:** Verificar que la feature está en el estado `approved_for_implementation` y asimilar el diseño y tareas de la spec.
2. **Desarrollo por Pasos:** Implementar los cambios en el código candidato de forma iterativa, abordando las tareas numeradas de `tasks.md` en orden lógico y mediante cambios pequeños, limpios y reversibles.
3. **Control Local:** A medida que completa cada tarea, verificar el comportamiento local del código usando smoke tests o comprobaciones manuales rápidas.
4. **Verificación de QA:** Ejecutar la suite de pruebas del plan definido en `validation.md` y proponer mejoras al archivo si es necesario.
5. **Limpieza del Código:** Realizar una revisión y limpieza de su propio código para asegurar que no se introducen regresiones, código muerto, imports obsoletos ni trazas de depuración de desarrollo persistentes.
6. **Solicitud de Cierre:** Redactar el reporte de implementación con su correspondiente diff de Git y cambiar el estado de la feature a `implementation_done` / `qa_pending` para la revisión cruzada.

## 8. Criterios mínimos de calidad de implementación candidata
El código candidato debe cumplir rigurosamente el siguiente estándar de calidad:
- **Alineación con la Spec:** Comportarse funcionalmente de forma idéntica a lo especificado en los requerimientos.
- **No Regresión:** No romper código existente ni introducir vulnerabilidades.
- **Limpieza Absoluta:** Código legible, estructurado y exento de trazas de desarrollo, prints o comentarios temporales obsoletos.
- **Evidencia reproducible:** Los resultados de las pruebas deben poder replicarse en el entorno de validación del revisor de forma idéntica.

## 9. Casos de bloqueo
El flujo de trabajo del Implementer se detiene y la feature pasa al estado `blocked` si:
- Se identifica que la implementación de la spec requiere introducir librerías de terceros que no han sido autorizadas.
- Se detecta una inconsistencia lógica insalvable entre el diseño técnico (`design.md`) y el requerimiento de negocio (`requirements.md`).
- El entorno local de desarrollo presenta fallos técnicos críticos (errores de compilación, fallas del linter o dependencias de red caídas).

## 10. Relación con `sdd_feature_workflow.md`
El Implementer es el actor principal de las transiciones operativas centrales del workflow:
- Interviene conceptualmente al transitar al estado `in_progress` cuando comienza la programación candidata de la característica.
- Finaliza su rol directo al cambiar el estado a `implementation_done` tras completar el checklist y solicitar la validación.
- Participa en la resolución de fallos bajo el estado `re_plan_required` aplicando las correcciones ordenadas según la replanificación acordada.

## 11. Relación con `spec_author`
- **Dependencia de diseño:** El Implementer consume de forma directa el trabajo del Spec Author.
- **Retroalimentación:** Si el Implementer identifica una ambigüedad, vacío técnico o error en la lógica de las tareas durante la codificación, debe bloquear el flujo y solicitar al Spec Author la aclaración del caso, registrando la resolución en `clarifications.md` antes de reanudar el desarrollo.

## 12. Límites del MVP actual
- **Restricción absoluta de código real:** Mientras el proyecto permanezca en la fase documental / MVP estructural y los scripts de validación técnica automatizados o las plantillas de specs no estén consolidados, **esta skill no otorga autorización técnica ni operativa para modificar código real de proyectos derivados**.
- **Propósito didáctico y de diseño:** El rol de Implementer en esta etapa sirve únicamente para modelar el flujo de transiciones lógicas del arnés y simular el ciclo de desarrollo en escenarios de pruebas conceptuales controlados.

## 13. Nota de compatibilidad futura
Cuando esta skill pase de estado documental a estado activo, deberá revisarse y adaptarse al formato vigente de Agent Skills del motor correspondiente. Esa adaptación podrá incluir front matter o metadata mínima como `name` y `description`, revisión de la ruta esperada por cada herramienta y validación de compatibilidad con Codex, Antigravity u otros runtimes agénticos autorizados.

Mientras el proyecto permanezca en fase documental / MVP estructural, esta skill no debe interpretarse como recurso activo, ejecutable ni invocable automáticamente.
