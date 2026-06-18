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
| Saneamiento documental actual | 🟡 EN DESARROLLO | Reordenar `progress/` como sistema vivo de control. |
| Fase 4 | ⬜ PENDIENTE | Diseño de la capa agéntica del arnés. No abierta. Requiere definición y aprobación humana antes de cualquier implementación. |
| Capacidades candidatas futuras | 🧊 FUTURO | `improve_plan`, `ponytail_review`, capa agéntica futura. |

## Checklist vivo

| Estado | Área | Detalle |
| :--- | :--- | :--- |
| ✅ REALIZADO | Base documental | Fases 0, 1, 2 y 3 cerradas. |
| ✅ REALIZADO | Gate mínimo | `scripts/gate_0_preflight.py` activo como único gate mínimo local autorizado. |
| 🟡 EN DESARROLLO | Saneamiento | Reducir y alinear `current`, `history` y `feature_list`. |
| ✅ REALIZADO | Saneamiento documental | Actualizado `docs/gate_0_preflight_definicion.md` para reflejar `scripts/gate_0_preflight.py` como único gate mínimo local autorizado. |
| ⬜ PENDIENTE | Fase 4 | Definir cómo se convertirán procedimientos repetibles y documentación larga en piezas agénticas controladas: skills, agentes, subagentes, auditores, workflows, CLI, gates, scripts y checklists. |
| ⛔ BLOQUEADO | Runtime técnico | `uv`, `pytest`, workflows y `.agent/` activo. |
| 🧊 FUTURO | Capas candidatas | `improve_plan`, `ponytail_review`, capa agéntica completa. |

## Bloqueos vigentes

- `uv` bloqueado.
- `pytest` bloqueado.
- `.agent/` no activo.
- `scripts/` parcialmente activo solo por `scripts/gate_0_preflight.py`; todo script adicional sigue bloqueado.
- Workflows bloqueados.
- CLI bloqueada.
- Fase 4 no abierta.

## Próxima acción

Cerrar saneamiento documental de `progress/`.
