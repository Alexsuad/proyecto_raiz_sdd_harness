# File: GEMINI.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Servir como adaptador operativo mínimo para Gemini y Antigravity.
# Rol: Contexto breve de trabajo para agentes Gemini dentro del repositorio.
# ──────────────────────────────────────────────────────────────────────

# GEMINI.md — Adaptador operativo para Gemini y Antigravity

## 1. Propósito

Este archivo entrega contexto operativo mínimo para Gemini, Antigravity y herramientas compatibles que trabajen dentro del repositorio `proyecto_raiz_sdd_harness`.

No reemplaza la documentación oficial del proyecto. Su función es orientar al agente para que trabaje respetando la constitución, el mapa documental y el adaptador operativo general `AGENTS.md`.

## 2. Fuente de verdad

Antes de modificar cualquier archivo, el agente debe considerar como fuentes principales:

- `docs/00_mapa_y_gobernanza_documental.md`
- `docs/constitucion_del_proyecto.md`
- `docs/01_metodologia_base_comun.md`
- `docs/02_metodologia_desarrollo_software_sdd_harness.md`
- `AGENTS.md`

Este archivo no debe duplicar esas reglas. Solo debe referenciarlas y aplicarlas de forma operativa.

## 3. Reglas operativas para Antigravity

Cuando Antigravity o Gemini trabajen en este repositorio deben cumplir estas reglas:

- Trabajar solo sobre los archivos autorizados por la tarea.
- No crear archivos, carpetas, skills, workflows, specs, scripts ni gates sin autorización explícita.
- No modificar documentos base dentro de `docs/` salvo instrucción directa.
- No inventar rutas, comandos, estados, decisiones ni dependencias.
- No usar respuestas de chat como fuente oficial de verdad.
- No autoaprobar cambios relevantes.
- Detenerse y reportar si existe ambigüedad, riesgo o conflicto documental.
- **Política de Commits:** No realizar commits ni pushes por microfase local. Consolidar cambios en un único commit/push por fase o bloque real tras aprobación humana.
- **Revisión de Documentación al Cierre:** Al finalizar cada fase, auditar y actualizar `README.md`, `AGENTS.md`, `GEMINI.md`, `progress/` y documentos de soporte correspondientes.

El proyecto se encuentra en etapa de MVP. La Fase 3 de verificación automatizada ya fue implementada y publicada.
- **Verificación Determinista Mínima:** Utilizar siempre el script `scripts/gate_0_preflight.py` para validar la estructura del repositorio localmente mediante `.venv/bin/python scripts/gate_0_preflight.py`.
- **Límites de herramientas:** No se debe activar `pytest`, `uv`, GitHub Actions ni inicializar la automatización de `.agent/` de fondo sin autorización explícita.
- Mientras no existan plantillas mínimas de `specs/` y skills de fondo habilitadas, Antigravity no debe actuar como implementador sobre código de proyectos derivados.
- El uso actual permitido es planificación, documentación, edición controlada, ejecución del preflight local en mantenimiento, y simulaciones.

## 5. Cierre obligatorio

Al terminar una tarea, el agente debe entregar un reporte con:

- archivos creados o modificados;
- resumen de cambios;
- validaciones realizadas;
- riesgos o dudas detectadas;
- confirmación de archivos no tocados;
- estado final: `completado` o `bloqueado`.

## 6. Futuras actualizaciones

Cuando existan `.agent/skills/`, `.agent/workflows/`, `specs/`, `scripts/`, `tests/` o `progress/`, este archivo deberá actualizarse solo para referenciarlos.

No debe convertirse en una copia de la constitución, de `AGENTS.md` ni de la metodología completa.
