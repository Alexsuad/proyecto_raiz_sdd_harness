# File: progress/feature_list.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar la lista oficial inicial de características (features) y capacidades previstas del arnés.
# Rol: Inventario operativo documental de seguimiento del avance del MVP.
# ──────────────────────────────────────────────────────────────────────

# Feature List inicial — Proyecto raíz SDD + Harness

**Versión:** v0.1  
**Estado:** Aprobado dentro del cierre de Fase 0 documental  
**Tipo:** Inventario operativo documental  
**Ubicación:** `progress/feature_list.md`

---

## 1. Propósito
Este documento funciona como el inventario oficial de características y capacidades previstas del proyecto raíz `proyecto_raiz_sdd_harness`. Su objetivo es organizar de forma secuencial y estructurada el avance de los entregables durante el MVP actual y estructurar las fases futuras, impidiendo la activación de implementaciones técnicas prematuras fuera del orden LEAN establecido.

---

## 2. Reglas de uso
* **No equivale a Spec:** Este inventario de capacidades no sustituye en ningún caso a las especificaciones funcionales y de diseño detalladas en la carpeta `specs/`.
* **No autoriza implementación:** La presencia de una característica en esta lista no faculta a los agentes a iniciar su codificación.
* **No crea scripts ni gates:** La definición documental de capacidades técnicas futuras no permite la creación física de scripts ejecutables en `scripts/` o gates en `.agent/`.
* **Evidencia física real:** El cambio de estado de una característica debe estar sustentado por una evidencia física real (commits, diffs, archivos creados en el repositorio), no por intenciones declaradas en el chat.

---

## 3. Estados permitidos de una feature
Cada capacidad técnica o documental debe clasificarse en uno de los siguientes estados:
* **completado:** El artefacto documental o técnico ha sido creado, auditado y commiteado en la rama principal.
* **pendiente:** Característica prioritaria e inmediata dentro de la fase actual a la espera de ser creada.
* **en revisión:** Artefacto candidato en fase de lectura y auditoría por parte de la revisión humana o cruzada.
* **revisada documentalmente:** Artefacto documental que ya tiene revisión registrada, pero aún queda pendiente una decisión humana final antes de marcarlo como completado o cerrar la fase relacionada.
* **completado documentalmente:** Artefacto documental creado, revisado, validado y cerrado en sentido documental, sin implicar implementación técnica ni activación de runtime.
* **bloqueado:** Característica cuyo desarrollo está suspendido debido a dependencias de fases previas no aprobadas.
* **futuro/inactivo:** Capacidad prevista para fases posteriores inactivas; no operable en este momento.
* **post-MVP:** Característica técnica de largo plazo excluida de la versión v0.1.
* **descartado:** Capacidad eliminada del alcance por obsolescencia o sobreingeniería.

---

## 4. Tabla inicial de features/capacidades

| ID | Nombre | Descripción breve | Estado | Evidencia / archivo asociado | Próximo paso | Observaciones |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **F-001** | Plan de implementación v0.1 | Hoja de ruta v0.1 priorizando el orden LEAN de consolidación documental. | **completado** | [plan_implementacion_v0_1...md](./plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md) | Seguimiento del avance | Auditado y consolidado. |
| **F-002** | Procedimiento de inicio | Guía paso a paso de arranque de proyectos derivados con controles. | **completado** | [procedimiento_inicio...md](../docs/procedimiento_inicio_proyecto_sdd_harness.md) | Mantener actualizado | Ajustado con las directrices agénticas aprobadas. |
| **F-003** | Origen del proyecto raíz | Registro documental del intake inicial, justificación y alcance negativo. | **completado** | [fase_00_origen...md](./fase_00_origen_del_proyecto_raiz.md) | Mantener como referencia | Consolidado sin autoaprobaciones. |
| **F-004** | Visión y alcance | Definición de objetivos e hitos finales del MVP estructural. | **completado** | [vision_y_alcance...md](../docs/vision_y_alcance_del_proyecto_raiz.md) | Mantener como referencia | Define los criterios de salida del MVP. |
| **F-005** | Auditoría arquitectónica | Inventario de la coherencia documental y operativa del repositorio. | **completado** | [auditoria_arquitectonica...md](./auditoria_arquitectonica_interna_2026-06-07.md) | Seguimiento de control | Matizado en estado candidato. |
| **F-006** | Política de zonas | Reglas de delimitación de carpetas físicas y estados de artefactos. | **completado** | [politica_zonas...md](../docs/politica_zonas_repositorio.md) | Mantener como referencia | Prohíbe limpiezas destructivas ad-hoc. |
| **F-007** | README raíz | Puerta de entrada y mapa de navegación del repositorio raíz. | **completado** | [README.md](../README.md) | Mantener actualizado | Orienta a humanos y agentes agénticos. |
| **F-008** | Feature list inicial | Inventario de capacidades y estados del arnés. | **completado** | [feature_list.md](./feature_list.md) | Mantener actualizado | Este documento. |
| **F-009** | Auditoría final de Fase 0 | Reporte de cierre y validación final de entregables documentales. | **completado** | [auditoria_final_cierre_fase_0_2026-06-07.md](./auditoria_final_cierre_fase_0_2026-06-07.md) (commit 0f2ae3e) | Mantener como registro de Fase 0 | Criterio de salida obligatorio de Fase 0. |
| **F-010** | Primera spec piloto — completado documentalmente mediante F-013 | Spec piloto documental de Fase 1. F-010 funciona como hito/contenedor de la primera spec piloto; F-013 es la spec piloto específica creada y cerrada documentalmente. | **completado documentalmente** | [specs/f_013_gate_manual_futuro/](../specs/f_013_gate_manual_futuro/) | Seguimiento del avance | Hito de Fase 1 satisfecho documentalmente a través de F-013. |
| **F-011** | Plantillas de specs | Estándar formalizado de plantillas markdown para la carpeta `specs/`. | **futuro/inactivo** | - | Crear borradores en docs/ | Planificado para fases futuras. |
| **F-012** | Inventario de validaciones | Definición de reglas estáticas a auditar automáticamente. | **futuro/inactivo** | - | Registro conceptual | Enlace previsto con scripts locales. |
| **F-013** | Gate manual futuro | Definición de flujos de aprobación y firmas humanas en texto. | **completado documentalmente** | [specs/f_013_gate_manual_futuro/](../specs/f_013_gate_manual_futuro/) | Fase 1 cerrada / pendiente autorización humana para Fase 2 | Cierre documental en Microfase 1.8. No hay implementación técnica (gate inactivo, Fase 2 bloqueada). Base pre-cierre: commit e46870d. |
| **F-014** | Gate automatizado futuro | Criterios de integración y smoke tests de validación. | **futuro/inactivo** | - | Enlace a scripts/ | Pendiente de suite de testeo. |
| **F-015** | Scripts deterministas | Inicialización técnica y herramientas de control (`gate_0_preflight.py`). | **futuro/inactivo** | - | Esperar autorización de fase técnica | Inactivo en la Fase 0. |
| **F-016** | Tests automatizados | Suite de pruebas unitarias locales utilizando `pytest` en `tests/`. | **futuro/inactivo** | - | Esperar autorización de fase técnica | Inactivo en la Fase 0. |
| **F-017** | Activación de skills | Transición operativa de skills documentales a activas en background. | **futuro/inactivo** | - | Definir metadatos | Bloqueado en esta etapa. |
| **F-018** | Revisión de adaptadores | Ajuste futuro a los archivos pragmáticos de la raíz. | **futuro/inactivo** | [AGENTS.md](../AGENTS.md) / [GEMINI.md](../GEMINI.md) | Auditoría técnica futura | Requiere el inicio técnico. |
| **F-019** | Revisión de `.agent/` | Integración operativa y metadatos de configuración en rules/workflows. | **futuro/inactivo** | - | Vincular al entorno de desarrollo | Bloqueado en esta etapa. |
| **F-020** | Apertura controlada de Fase 2 | Definición de condiciones mínimas para preparar entorno técnico verificable sin desarrollo funcional. | **en revisión** | - | Definir límites y condiciones mínimas | F-020 en curso. La Microfase 2.2 validó físicamente el aislamiento del entorno virtual mínimo (.venv) sin código funcional ni pytest/uv. |

---

## 5. Bloqueos explícitos
Tras la apertura controlada de la Fase 1, y hasta nueva autorización humana explícita, se mantienen **estrictamente bloqueados y sin autorización para ser ejecutados** los siguientes componentes:
* Codificación o creación de especificaciones reales de características en `specs/`.
* Programación de scripts ejecutables en `scripts/` (incluyendo `gate_0_preflight.py`).
* Configuración de gates automatizados o inicialización de suites de test locales con `pytest`.
* Activación técnica de habilidades agénticas, workflows ejecutables o prompts automáticos en la carpeta `.agent/`.
* Modificación física (creación de archivos candidato de software o alteración de código existente) en el repositorio.

---

## 6. Relación con el plan de implementación
Este documento forma parte de los entregables cerrados de la Fase 0 documental y sirve como inventario base para evaluar futuras fases sin habilitarlas automáticamente. Provee la estructura necesaria para preparar de forma ordenada la futura transición hacia la Fase 1 (Spec Piloto), pero no habilita de manera autónoma el inicio de desarrollos técnicos o automatizaciones en el repositorio.

---

## 7. Criterios de aceptación
* [ ] Se listan de forma exhaustiva los entregables documentales ya completados, vinculados con sus archivos correspondientes en Git.
* [ ] Se realiza una división clara entre las tareas pendientes de la fase actual y las capacidades futuras inactivas.
* [ ] No se otorga ninguna autorización de codificación técnica.
* [ ] No se crean plantillas de specs ni automatizaciones en background.
* [ ] Se mantiene explícita la restricción de bloqueo sobre el runtime y el entorno de pruebas.
* [ ] Se establece el cierre documental de la Fase 0 a la ejecución de una auditoría final.

---

## 8. Estado del documento
* **Estado:** Aprobado dentro del cierre de Fase 0 documental
