# File: .agent/skills/reviewer/SKILL.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la skill conceptual del rol Reviewer dentro del ciclo SDD.
# Rol: Skill documental y no activa (no ejecutable) del arnés.
# ──────────────────────────────────────────────────────────────────────

# Skill documental: Reviewer

## Descripción
Contrato operativo conceptual que define las responsabilidades, entradas, salidas y flujo de trabajo para el auditor y revisor independiente de especificaciones y código candidato en el flujo Spec-Driven Development (SDD).

---

## 1. Propósito de la skill
Esta skill establece las pautas metodológicas y operativas del rol **Reviewer** para la inspección independiente, verificación de cumplimiento técnico y control de calidad de las características desarrolladas. Su objetivo principal es asegurar de forma objetiva que el entregable candidato cumple con la especificación de diseño aprobada, no introduce regresiones, mantiene la limpieza del codebase y no altera zonas críticas sin autorización.

## 2. Estado actual
* **Estado actual:** Documental / No activa / No ejecutable.
* **Límite operativo:** Este documento define directrices de procesos para la fase de Producto Mínimo Viable (MVP). No contiene scripts, hooks automatizados ni configuraciones activas. Antigravity o cualquier otro agente de IA debe considerarla exclusivamente como una especificación de solo lectura y abstenerse de ejecutar automatizaciones de revisión basadas en ella.

## 3. Documentos de referencia obligatoria
El Reviewer debe contrastar sus auditorías y subordinarse a las siguientes fuentes de verdad del repositorio:
- [docs/constitucion_del_proyecto.md](../../../docs/constitucion_del_proyecto.md) (Regla de entregable candidato y revisión cruzada).
- [docs/02_metodologia_desarrollo_software_sdd_harness.md](../../../docs/02_metodologia_desarrollo_software_sdd_harness.md) (QA y validación).
- [.agent/workflows/sdd_feature_workflow.md](../../workflows/sdd_feature_workflow.md) (Workflow de la feature).
- [.agent/skills/spec_author/SKILL.md](../spec_author/SKILL.md) (Criterios de calidad de especificación).
- [.agent/skills/implementer/SKILL.md](../implementer/SKILL.md) (Salidas y límites del implementador).

## 4. Entradas esperadas futuras
Para iniciar conceptualmente la fase de revisión, el Reviewer debe recopilar los siguientes artefactos:
- **Especificación completa aprobada:** `requirements.md`, `clarifications.md`, `design.md`, `tasks.md` y `validation.md` de la carpeta `specs/<feature_id>/`.
- **Reporte de implementación:** Resumen de cambios redactado por el `implementer`.
- **Diff de Git:** Diferencia de Git detallada de los archivos candidatos modificados.
- **Evidencias de validación:** Logs de ejecución, capturas de pantalla, reportes de tests o checklists de pruebas locales.

## 5. Salidas esperadas futuras
La auditoría del Reviewer dará como resultado la preparación de las siguientes salidas conceptuales:
- **Reporte de revisión:** Evaluación global del entregable candidato y recomendación de avance.
- **Lista de hallazgos:** Detalle estructurado de defectos, inconsistencias o deuda técnica detectada.
- **Clasificación por severidad:** Catalogación de hallazgos en categorías (Bloqueante, Mayor, Menor).
- **Verificación de spec y evidencias:** Auditoría de cumplimiento punto por punto frente a requerimientos y validaciones.
- **Recomendación de estado:** Propuesta para transitar a `review_pending`, `done`, `blocked` o `re_plan_required`.
- **Actualización documental:** Propuesta de registro en `specs/<feature_id>/review.md`.
- **Solicitud de aprobación humana:** Elevación formal al aprobador humano cuando corresponda.

## 6. Límites del rol
El Reviewer opera bajo límites estrictos para salvaguardar la independencia de la auditoría:
- **No reemplaza al humano:** Las revisiones del Reviewer se consideran "entregables candidatos" y de ningún modo sustituyen la aprobación humana explícita cuando el cambio afecta zonas críticas.
- **No codificación:** El Reviewer **no escribe código, no aplica correcciones directas sobre los archivos y no modifica archivos de producto** del repositorio. Si detecta un fallo, debe reportarlo para que el implementador lo corrija.
- **Independencia obligatoria:** El Reviewer no puede revisar ni aprobar su propio trabajo, ni el trabajo de un rol (como el implementador o autor de especificaciones) que haya sido ejecutado por la misma entidad agéntica en la misma feature.
- **Revisión contra la spec:** La auditoría se realiza confrontando los cambios candidatos contra los archivos aprobados en `specs/`, **nunca contra la memoria del chat o supuestos informales**.

## 7. Flujo de trabajo recomendado
El Reviewer sigue de forma secuencial los siguientes pasos operativos:
1. **Recepción:** Identificar que la feature ha transitado al estado `review_pending` o `qa_pending` en el workflow.
2. **Carga y Lectura:** Cargar y analizar toda la documentación de la spec y el diff de Git candidato.
3. **Auditoría de Requerimientos y Diseño:** Comparar los cambios en el código frente a `requirements.md` y `design.md`.
4. **Comprobación de Planificación:** Verificar en el diff que el avance sigue estrictamente lo pautado en `tasks.md` sin desvíos no autorizados.
5. **Inspección de Evidencias:** Auditar minuciosamente las evidencias de ejecución locales recopiladas.
6. **Revisión del Código:** Evaluar la limpieza del diff (remoción de trazas de depuración, imports obsoletos y cumplimiento de estilo).
7. **Emisión de Dictamen:** Documentar los hallazgos en el reporte y proponer la actualización de `review.md`.
8. **Elevación:** Solicitar la aprobación explícita del desarrollador humano cuando el dictamen recomiende avanzar hacia cierre o consolidación.

## 8. Criterios mínimos de revisión
La auditoría del Reviewer debe inspeccionar obligatoriamente los siguientes puntos clave:
- **Cumplimiento funcional:** Que el código satisfaga los criterios de aceptación obligatorios definidos en `requirements.md`, sin fallos pendientes de resolución.
- **Alineación de arquitectura:** Que las modificaciones sigan estrictamente el diseño aprobado en `design.md` y no alteren componentes fuera del alcance definido.
- **Limpieza del diff:** Ausencia de código muerto, archivos temporales, prints de desarrollo o comentarios obsoletos.
- **Validación robusta:** Que las pruebas obligatorias definidas en `validation.md` hayan sido ejecutadas y no reporten fallos pendientes.
- **Control de zonas críticas:** Verificar que la implementación no haya modificado de forma no autorizada la arquitectura limpia, modelos de datos, dependencias externas, seguridad, permisos, costes financieros, pasarelas de pago o entornos de producción.

## 9. Revisión de evidencia
El Reviewer no debe dar por buenas las afirmaciones del implementador. Debe:
- Comprobar que los logs y reportes de pruebas corresponden a la versión actual de la rama.
- Validar que los casos de prueba obligatorios definidos en `validation.md` no reporten fallos pendientes de resolución.
- Asegurar que la evidencia es reproducible por un tercero si fuera necesario.

## 10. Casos de bloqueo
El Reviewer detendrá la auditoría y marcará la feature como `blocked` si:
- El diff de Git candidato altera archivos que no estaban previstos ni autorizados en `design.md`.
- No se suministran las evidencias de prueba requeridas o estas presentan inconsistencias lógicas.
- Se detectan cambios no autorizados en zonas críticas del sistema (seguridad, base de datos o costes).

## 11. Relación con `sdd_feature_workflow.md`
El Reviewer interviene en las etapas de transición final de la característica:
- Opera durante los estados `qa_pending` y `review_pending`.
- Recomienda la transición al estado `done` si la revisión es exitosa y se cuenta con aprobación humana.
- Recomienda la transición al estado `re_plan_required` si se identifican fallos en las pruebas o desviaciones del diseño original.

## 12. Relación con `spec_author`
- El Reviewer utiliza las especificaciones preparadas por el Spec Author como la única base normativa para contrastar la implementación. Si detecta vacíos lógicos en la spec durante la revisión, debe reportar la inconsistencia.

## 13. Relación con `implementer`
- El Reviewer actúa como un auditor independiente y crítico del código candidato generado por el Implementer. No interactúa directamente con el implementador en el código, sino a través de los reportes de revisión formalizados.

## 14. Límites del MVP actual
- **Sin automatización de gates:** Durante el MVP actual del arnés, esta skill no autoriza la ejecución de revisiones automáticas, integración continua o gates de calidad activos sobre el código real del proyecto. Su uso se restringe a la simulación y diseño de procesos de revisión documental.

## 15. Nota de compatibilidad futura
Cuando esta skill pase de estado documental a estado activo, deberá revisarse y adaptarse al formato vigente de Agent Skills del motor correspondiente. Esa adaptación podrá incluir front matter o metadata mínima como `name` y `description`, revisión de la ruta esperada por cada herramienta y validación de compatibilidad con Codex, Antigravity u otros runtimes agénticos autorizados.

Mientras el proyecto permanezca en fase documental / MVP estructural, esta skill no debe interpretarse como recurso activo, ejecutable ni invocable automáticamente.
