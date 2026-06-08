# File: specs/f_013_gate_manual_futuro/validation.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el plan de validación documental y pruebas manuales del Gate.
# Rol: Spec de validación de la feature F-013 en estado candidato.
# ──────────────────────────────────────────────────────────────────────

# Plan de validación manual — F-013: Gate manual futuro

**Versión:** v0.1-candidato  
**Estado:** Completado documentalmente (Fase 1 - Spec Piloto Documental)  
**Tipo:** Plan de Validación Documental  
**Ubicación:** `specs/f_013_gate_manual_futuro/validation.md`

---

## 1. Propósito de la validación

Este documento establece el plan de validación manual para confirmar la coherencia, claridad y cumplimiento procedimental de la feature **Gate manual futuro (F-013)**. Dado el alcance estrictamente documental del proyecto en esta etapa, toda validación descrita aquí es procedimental y se ejecuta mediante inspección visual y firmas de texto, sin interacción con código ejecutable.

---

## 2. Checklist de validación de claridad y estructura

> [!NOTE]
> Nota de pre-cierre: La validación registrada es exclusivamente documental/procedimental. No constituye ejecución de tests automatizados, no habilita pytest, no habilita uv, no crea scripts, no crea gates ejecutables y no modifica .agent/.

El Equipo Auditor o el Revisor Humano deben verificar las siguientes condiciones:
* [x] **C-013-01: Claridad de Roles:** ¿Se identifica claramente quién realiza la revisión y quién la firma en `review.md`?
* [x] **C-013-02: Bloque de Firma Completo:** ¿El bloque de firma contiene todos los campos necesarios descritos en `design.md`?
* [x] **C-013-03: No-Autoaprobación:** ¿Se prohíbe explícitamente que el agente de IA autorice o firme su propia documentación?
* [x] **C-013-04: Rutas Relativas:** ¿Todas las referencias cruzadas de archivos dentro de la carpeta `specs/f_013_gate_manual_futuro/` y del resto del repositorio usan rutas relativas del tipo `./archivo.md` en lugar de rutas absolutas?

---

## 3. Verificación de no-automatización y aislamiento técnico

* [x] **VA-013-01:** Confirmar que no se ha creado ningún script `.py`, `.sh`, `.bat` ni ningún otro binario ejecutable en el repositorio.
* [x] **VA-013-02:** Confirmar que no se han modificado ni agregado archivos en `.agent/` ni skills de ejecución automática.
* [x] **VA-013-03:** Confirmar que las suites de pruebas automáticas con `pytest`, el entorno virtual y la herramienta de gestión `uv` no han sido activadas ni llamadas en el proceso.

---

## 4. Validación de trazabilidad Input/Output

* [x] **VT-013-01:** Confirmar que todos los requisitos funcionales de `requirements.md` tienen un correspondiente diseño conceptual en `design.md`.
* [x] **VT-013-02:** Confirmar que las tareas en `tasks.md` cubren la redacción y revisión de todos los documentos candidatos.
* [x] **VT-013-03:** Confirmar que las evidencias listadas en `review.md` enlazan de forma correcta a la versión exacta que se audita.

---

## 5. Casos de validación procedimental (Simulación manual)

### Caso 1: Flujo de Aprobación
* **Acción:** El revisor completa los metadatos de firma en `review.md` con el dictamen `APROBADO`.
* **Resultado Esperado:** El estado del gate cambia a `aprobado`, lo que permite planificar la apertura de la siguiente fase en la hoja de ruta general.

### Caso 2: Flujo de Bloqueo
* **Acción:** El revisor detecta omisiones graves de calidad (ej. falta de firmas o rutas absolutas) y estampa el dictamen `BLOQUEADO` en `review.md`.
* **Resultado Esperado:** El estado cambia a `bloqueado`, el agente detiene su avance e inicia inmediatamente las correcciones indicadas en las observaciones.

### Caso 3: Flujo de Aclaración
* **Acción:** El revisor requiere más detalle sobre un requisito y estampa el dictamen `REQUIERE_ACLARACION` con una pregunta.
* **Resultado Esperado:** El agente responde en el chat o en un anexo documental y vuelve a solicitar la revisión sin avanzar a otras fases del proyecto.

### Caso 4: Flujo de Replanificación
* **Acción:** El revisor observa que el diseño excede el alcance del MVP y firma con `REQUIERE_REPLANIFICACION`.
* **Resultado Esperado:** El agente detiene las tareas de especificación, ajusta la planificación y vuelve a someter la propuesta a revisión.

---

## 6. Evidencia física de validación

La única evidencia física válida para esta feature piloto consiste en:
1. El archivo `review.md` completado con la firma de texto y el dictamen final.
2. El registro del commit en el repositorio Git que contenga este cambio documental sin ningún archivo ejecutable o script en su diff.
