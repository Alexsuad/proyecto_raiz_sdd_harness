# File: progress/current.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar el estado operativo actual del arnés.
# Rol: Punto de control para evitar ambigüedad sobre qué existe, qué está activo y qué está pendiente.
# ──────────────────────────────────────────────────────────────────────

# Estado actual del proyecto raíz

## 1. Propósito

Este archivo registra el estado operativo actual del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es dejar evidencia clara de qué partes del arnés existen como documentación, qué partes están activas, qué partes siguen pendientes y qué límites deben respetar los agentes antes de continuar.

## 2. Estado general

- **Proyecto:** `proyecto_raiz_sdd_harness`
- **Tipo de proyecto:** proyecto raíz metodológico y agéntico.
- **Objetivo:** construir una base reutilizable para futuros proyectos de desarrollo de software con SDD, documentación gobernada, adaptadores operativos, skills, workflows y gates.
- **Estado actual:** Fase 1 abierta de forma controlada. Spec piloto F-013 creada como candidata documental en revisión.
- **Último commit confirmado:** ccfac0b2b2a265672f614f91991a0ca465fc9206 (ccfac0b)
- **Siguiente paso:** revisión humana de la spec F-013, especialmente `review.md`.
- **Código de producto:** No existe (bloqueado).
- **Features activas:** Ninguna (bloqueado).
- **Automatización activa:** Ninguna (bloqueado).
- **Gates automatizados activos:** Ninguno (bloqueado).
- **Suite de pruebas (pytest/uv):** Inactivo/bloqueado.

## 3. Estructura documental creada

Actualmente existen las siguientes sedes documentales:

- `docs/`: documentación base, constitución y ADR.
- `specs/`: sede futura de specs por feature.
- `progress/`: seguimiento operativo del arnés.
- `scripts/`: sede futura de scripts y gates deterministas.
- `tests/`: sede futura de pruebas del arnés.
- `.agent/rules/`: sede futura de reglas locales para Antigravity.
- `.agent/workflows/`: sede futura de workflows operativos.
- `.agent/skills/`: sede futura de skills reutilizables.

## 4. Recursos activos actualmente

Actualmente solo se consideran activos:

- documentos base versionados;
- adaptadores operativos mínimos `AGENTS.md` y `GEMINI.md`;
- README de sedes documentales;
- este archivo de estado actual.

No existen todavía:

- rules activas (la regla local `.agent/rules/00_reglas_locales_mvp_documental.md` existe en estado documental e inactivo);
- workflows activos (el workflow `.agent/workflows/sdd_feature_workflow.md` existe en estado puramente documental e inactivo);
- skills activas (las skills de `spec_author`, `implementer` y `reviewer` existen en `.agent/skills/` en estado documental e inactivo);
- gates operativos o automatizados;
- specs de features reales;
- scripts ejecutables;
- tests reales del arnés.

## 5. Estado de `.agent/`

La carpeta `.agent/` alberga la estructura documental conceptual del arnés.

Actualmente contiene las siguientes piezas documentales del triángulo mínimo de roles, flujo y reglas del MVP:
- **Workflow SDD por feature:** [.agent/workflows/sdd_feature_workflow.md](../.agent/workflows/sdd_feature_workflow.md)
- **Skill Spec Author:** [.agent/skills/spec_author/SKILL.md](../.agent/skills/spec_author/SKILL.md)
- **Skill Implementer:** [.agent/skills/implementer/SKILL.md](../.agent/skills/implementer/SKILL.md)
- **Skill Reviewer:** [.agent/skills/reviewer/SKILL.md](../.agent/skills/reviewer/SKILL.md)
- **Regla local documental:** [.agent/rules/00_reglas_locales_mvp_documental.md](../.agent/rules/00_reglas_locales_mvp_documental.md)

Estas piezas siguen siendo:
- documentales;
- no activas;
- no ejecutables;
- sin front matter;
- sin metadata activa;
- sin triggers, globs, `alwaysApply` ni configuración equivalente;
- sin autorización para modificar código real en proyectos derivados;
- sin autorización para automatización real;
- pendientes de futura activación o adaptación formal en los adaptadores operativos.

No debe crearse `.agent/gates/` todavía si el proyecto sigue en MVP documental.

## 6. Decisión de auditoría aplicada

Se recibió una observación de auditoría sobre posible sobreingeniería prematura por la existencia de carpetas `.agent/`.

La decisión tomada fue mantener esas carpetas como sedes documentales mínimas, pero corregir el riesgo de interpretación automática eliminando metadatos tipo front matter de los README y agregando advertencias explícitas de estado documental.

Esta decisión deja el proyecto en un estado intermedio controlado:

- se mantiene la topología futura del arnés;
- no se activan recursos operativos prematuros;
- se reduce el riesgo de que Antigravity interprete README como reglas, workflows o skills activas;
- se conserva el principio LEAN.

## 7. Límites operativos vigentes

Hasta nueva autorización explícita y firma humana, se mantienen estrictamente bloqueados y no operativos:
- specs reales;
- scripts de gates o runtime (en `/scripts`);
- gates ejecutables y suite de testing local (`pytest`/`uv`);
- configuración activa agéntica de fondo o daemon;
- activación operativa de skills o workflows en el IDE;
- cualquier modificación física del código o el working tree.

## 8. Próximo paso recomendado

El próximo hito recomendado es:
- Revisar y auditar de forma humana la spec piloto F-013 (`specs/f_013_gate_manual_futuro/review.md`) para dictaminar su aprobación.
- Mantener estrictamente bloqueada cualquier inicialización de código técnico o automatización en background.

## 9. Definición documental de Gate 0

- **Fecha:** 2026-05-30.
- **Documento creado:** `docs/gate_0_preflight_definicion.md`.
- **Tipo:** definición documental previa de gate.
- **Estado:** definición documental creada y corregida tras observaciones de auditoría; no activa.
- **Automatización:** ninguna.
- **Gate activo:** no.
- **Script asociado:** no existe `scripts/gate_0_preflight.py`.
- **Decisión:** el documento puede usarse como base conceptual para una futura implementación determinista, pero no autoriza crear scripts, `.agent/gates/` ni automatización activa.
- **Restricción vigente:** antes de convertir esta definición en script o gate operativo real, debe pasar auditoría documental y requerir autorización explícita.

## 10. Estado normativo consolidado

- **Fecha:** 2026-05-30.
- **Resultado:** constitución y mapa documental aprobados para fase documental / MVP estructural.
- **Documentos consolidados:**
  - `docs/constitucion_del_proyecto.md`
  - `docs/00_mapa_y_gobernanza_documental.md`
- **Motivo:** una auditoría detectó que ambos documentos aún se declaraban como borradores, lo que podía debilitar su autoridad normativa ante agentes de IA.
- **Decisión:** ambos documentos quedan vigentes para la fase documental actual, sin declararse definitivos para fases futuras.
- **Restricción vigente:** deberán revalidarse tras la primera feature piloto o cuando se cree el primer recurso activo real del arnés.

## 11. Estado del archivo

- **Estado:** creado como punto de control operativo.
- **Uso:** referencia rápida del estado actual del arnés.
- **Pendiente:** actualizar después de cada cambio estructural relevante del proyecto raíz.

## 12. Último preflight estructural

- **Fecha:** 2026-06-01.
- **Documento usado:** `docs/preflight_estructural.md`.
- **Tipo de revisión:** preflight manual estructural actualizado.
- **Modelo usado:** Gemini 3.5 Flash High.
- **Resultado:** aprobado.
- **Evidencia:** verificación de estructura base, estado agéntico, no duplicación, criterio LEAN, ausencia de automatización activa y working tree limpio.
- **Observaciones:** no existen `.agent/gates/`, scripts ejecutables, tests reales, specs reales, rules activas, workflows activos, skills activas ni gates operativos o automatizados.
- **Decisión:** se permite avanzar únicamente con cambios documentales controlados y justificados.
- **Restricción vigente:** no activar automatización, no crear `.agent/gates/` y no crear recursos operativos activos sin autorización explícita.
