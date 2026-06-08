# File: specs/f_013_gate_manual_futuro/tasks.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar las tareas atómicas y control del avance documental de la spec F-013.
# Rol: Spec de tareas de la feature F-013 en estado candidato.
# ──────────────────────────────────────────────────────────────────────

# Plan de trabajo y tareas — F-013: Gate manual futuro

**Versión:** v0.1-candidato  
**Estado:** Candidato (Fase 1 - Spec Piloto Documental)  
**Tipo:** Plan de Trabajo Documental (SDD)  
**Ubicación:** `specs/f_013_gate_manual_futuro/tasks.md`

---

## 1. Propósito de las tareas

Este documento funciona como la lista de control de tareas necesarias para finalizar la especificación de la feature **Gate manual futuro (F-013)**. Al seguir un enfoque estrictamente LEAN, no contiene tareas de programación, ejecución técnica, ni configuración de sistemas.

---

## 2. Checklist de tareas atómicas (Documentales)

> [!NOTE]
> Las tareas permanecen pendientes hasta que la spec sea revisada y aprobada por el desarrollador humano, aunque los documentos candidatos ya existan físicamente.

- [ ] **Tarea Documental 1: Definición de Requerimientos**
  * Redactar y consolidar el alcance, justificación, roles y bloqueos explícitos en `requirements.md`.
- [ ] **Tarea Documental 2: Definición de Diseño Conceptual**
  * Elaborar el flujo conceptual de estados y estructurar la plantilla estándar del bloque de firma en `design.md`.
- [ ] **Tarea Documental 3: Planificación de Tareas**
  * Definir esta lista de control atómica y el criterio de finalización de la spec en `tasks.md`.
- [ ] **Tarea Documental 4: Plan de Validación Manual**
  * Detallar las pruebas manuales de casos de transición y la trazabilidad documental en `validation.md`.
- [ ] **Tarea Documental 5: Estructura de Revisión y Dictamen**
  * Crear la plantilla de control del Equipo Auditor Procedimental y el bloque de decisión humana en `review.md`.

---

## 3. Restricciones de tareas (Negativo)

* **NO** crear tareas para escribir código Python, C, Javascript u otros lenguajes.
* **NO** crear tareas para crear archivos script en `scripts/` (e.g. `gate_0_preflight.py`).
* **NO** crear tareas para inicializar el entorno virtual con `uv`, configurar test de pytest o ejecutar comandos de instalación de librerías.
* **NO** crear tareas de automatización de Git o integración con la carpeta `.agent/`.

---

## 4. Criterio de aceptación para considerar completada la Spec Piloto

La especificación piloto documental de F-013 se considerará oficialmente finalizada y lista para su commit cuando se cumplan las siguientes condiciones:
1. Existan los 5 archivos Markdown correctos de la especificación en la carpeta `specs/f_013_gate_manual_futuro/`.
2. Todos los archivos declaren explícitamente que son de carácter candidato y documental.
3. Se excluya toda referencia a scripts, código, pytest, uv, automatizaciones y skills activas.
4. Se utilicen enlaces de rutas relativas válidas del repositorio para todas las referencias cruzadas.
5. El desarrollador humano realice la revisión física, estampe su firma con el dictamen de `APROBADO` en `review.md` y se proceda a consolidar mediante commit en Git.
