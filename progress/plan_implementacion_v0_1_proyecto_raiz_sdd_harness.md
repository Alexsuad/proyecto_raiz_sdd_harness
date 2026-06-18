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
| Fase 4 | 🟡 EN DESARROLLO | Fase 4 — Diseño de la capa agéntica del arnés (solo diseño documental, implementación bloqueada). |
| Capacidades candidatas futuras | 🟡 EN DESARROLLO | `improve_plan`, `ponytail_review`, capa agéntica futura (en fase de diseño documental). |

## Checklist vivo

| Estado | Área | Detalle |
| :--- | :--- | :--- |
| ✅ REALIZADO | Base documental | Fases 0, 1, 2 y 3 cerradas. |
| ✅ REALIZADO | Gate mínimo | `scripts/gate_0_preflight.py` activo como único gate mínimo local autorizado. |
| ✅ REALIZADO | Saneamiento | Reducir y alinear `current`, `history` y `feature_list`. |
| ✅ REALIZADO | Saneamiento documental | Actualizado `docs/gate_0_preflight_definicion.md` para reflejar `scripts/gate_0_preflight.py` como único gate mínimo local autorizado. |
| 🟡 EN DESARROLLO | Fase 4 | Definir cómo se convertirán procedimientos repetibles y documentación larga en piezas agénticas controladas: skills, agentes, subagentes, auditores, workflows, CLI, gates, scripts, checklists, rules y contratos de entrada/salida. |
| ✅ REALIZADO | Fase 4 - Diseño | Diseñado el contrato conceptual de misiones agénticas en `docs/contrato_misiones_agenticas.md`. |
| ⛔ BLOQUEADO | Runtime técnico | `uv`, `pytest`, workflows y `.agent/` activo. |
| 🟡 EN DESARROLLO | Capas candidatas | Diseño documental de `improve_plan`, `ponytail_review` y `capa_agentica_futura`. |

## Bloqueos vigentes

- `uv` bloqueado.
- `pytest` bloqueado.
- `.agent/` no activo (bloqueada la ejecución de runtime).
- `scripts/` parcialmente activo solo por `scripts/gate_0_preflight.py`; todo script adicional o gate técnico nuevo sigue bloqueado.
- Workflows e implementaciones activas bloqueados.
- CLI bloqueada.
- Fase 4 de implementación no abierta (solo abierta para diseño y especificación documental).

## Próxima acción

Diseñar el mapa de roles y responsabilidades de los agentes y subagentes conceptuales de la Fase 4.
