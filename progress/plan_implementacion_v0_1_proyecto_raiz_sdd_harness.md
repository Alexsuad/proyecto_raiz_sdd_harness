# File: progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Checklist vivo del proyecto.
# Rol: Norte operativo breve para controlar qué está hecho, qué sigue y qué está bloqueado.
# ──────────────────────────────────────────────────────────────────────

# Plan vivo v0.1

## Estado general

| Fase | Estado | Nota |
| :--- | :--- | :--- |
| Fase 0 | ✅ REALIZADO | Base documental inicial cerrada. |
| Fase 1 | ✅ REALIZADO | Feature piloto documental cerrada. |
| Fase 2 | ✅ REALIZADO | Entorno técnico mínimo cerrado. |
| Fase 3 | ✅ REALIZADO | Gate mínimo local publicado. |
| Saneamiento documental | ✅ REALIZADO | Reordenado y alineado `progress/` como sistema vivo de control. |
| Fase 4 | ✅ REALIZADO | Fase 4 base documental cerrada y auditada (sin implementación agéntica). |
| Fase 5 | 🔓 ABIERTA | Fase 5 — Readiness de implementación controlada. Apertura documental únicamente; sin activación técnica todavía. |
| Capacidades candidatas futuras | 🧊 FUTURO | improve_plan, ponytail_review, capa agéntica futura (pendientes de diseño específico posterior). |

## Checklist vivo

| Estado | Área | Detalle |
| :--- | :--- | :--- |
| ✅ REALIZADO | Base documental | Fases 0, 1, 2 y 3 cerradas. |
| ✅ REALIZADO | Gate mínimo | `scripts/gate_0_preflight.py` activo como único gate mínimo local autorizado. |
| ✅ REALIZADO | Saneamiento | Reducir y alinear `current`, `history` y `feature_list`. |
| ✅ REALIZADO | Saneamiento documental | Actualizado `docs/gate_0_preflight_definicion.md` para reflejar `scripts/gate_0_preflight.py` como único gate mínimo local autorizado. |
| ✅ REALIZADO | Fase 4 | Fase 4 base documental cerrada y auditada. No hay implementación agéntica. |
| ✅ REALIZADO | Fase 4 - Diseño | Diseñado el contrato conceptual de misiones agénticas en `docs/contrato_misiones_agenticas.md`. |
| ✅ REALIZADO | Fase 4 - Roles | Diseñado el mapa conceptual de roles agénticos en `docs/mapa_roles_agenticos.md`. |
| ✅ REALIZADO | Fase 4 - Workflow | Diseñado el workflow conceptual de misiones agénticas en `docs/workflow_misiones_agenticas.md`. |
| 🔓 ABIERTA | Fase 5 - Readiness | Apertura documental de Fase 5 (2026-06-21) sobre `a8c5835`. La Fase 5 es de readiness, no de implementación. La primera tarea será diseñar el plan de activación controlada. No activa runtime, `.agent/`, skills, workflows, scripts, tests, pytest ni uv. |
| ⛔ BLOQUEADO | Runtime técnico | Habilitación de runtime técnico (existen recursos documentales en `.agent/`, pero no hay recursos agénticos activos ni runtime habilitado). |
| 🧊 FUTURO | Capas candidatas | Diseño de `improve_plan`, `ponytail_review` y `capa_agentica_futura` (pendientes de diseño específico posterior). |

## Bloqueos vigentes

- `uv` bloqueado.
- `pytest` bloqueado.
- No hay skills activas, agentes activos, workflows activos ni CLI activa (los archivos de `.agent/` son únicamente documentales/conceptuales).
- `scripts/` parcialmente activo solo por `scripts/gate_0_preflight.py`; todo script adicional o gate técnico nuevo sigue bloqueado.
- Workflows e implementaciones activas bloqueados.
- CLI bloqueada.
- Fase 4 de implementación no abierta (solo abierta para diseño y especificación documental).

## Próxima acción

Fase 5 abierta documentalmente como readiness de implementación controlada. La primera tarea de Fase 5 será diseñar el plan de activación controlada.

Toda activación técnica futura (runtime agéntico, `.agent/` como runtime, skills activas, workflows activos, scripts nuevos, tests, `uv`, `pytest`) requerirá misión separada con archivos permitidos explícitos, archivos prohibidos explícitos, criterios de validación, Gate 0 y aprobación humana explícita. La apertura de Fase 5 no activa por sí misma ninguno de esos elementos.
