# File: progress/snapshot_estado_2026-06-02.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar un snapshot operativo de lectura rápida del estado actual del arnés tras la auditoría post-hito.
# Rol: Recurso documental informativo temporal, sin autoridad normativa.
# ──────────────────────────────────────────────────────────────────────

# Snapshot Operativo del Arnés (2026-06-02)

## 1. Propósito y Nota de No Autoridad Normativa
Este documento es un snapshot operativo de lectura rápida que registra el estado del repositorio `proyecto_raiz_sdd_harness` tras la auditoría y microcorrecciones del hito de cierre de sesión, correspondiente al commit `7589ac3 docs: corregir coherencia terminologica final`.

*Nota de gobernanza:* Este archivo es estrictamente informativo y de consulta rápida. No es un documento rector del proyecto raíz y no reemplaza a `progress/current.md`, `progress/history.md`, `docs/constitucion_del_proyecto.md` ni `docs/00_mapa_y_gobernanza_documental.md`.

---

## 2. Estado General del Proyecto
El proyecto raíz se encuentra estrictamente en **Fase Documental / MVP Estructural**.

### Qué NO existe todavía (Inexistencias de la fase actual)
- **Código de producto:** No se ha escrito lógica de aplicación ni software derivado.
- **Especificaciones reales (specs):** No existen specs reales de características de producto en `specs/`.
- **Pruebas (tests):** No existen tests reales de software ni de validación automática en `tests/`.
- **Scripts ejecutables:** No hay scripts de automatización en `scripts/`.
- **Gates activos:** No existen herramientas ni validadores deterministas ejecutados automáticamente en CI/CD.
- **Rules activas:** No hay reglas configuradas para aplicarse automáticamente en Antigravity.
- **Workflows activos:** No hay workflows operacionales activos de ejecución agéntica.
- **Skills activas:** No hay habilidades agénticas operativas.

---

## 3. Recursos Documentales Existentes y su Estado
Actualmente existen en el repositorio los siguientes recursos documentales:
- `.agent/rules/00_reglas_locales_mvp_documental.md` (Regla local del MVP).
- `.agent/workflows/sdd_feature_workflow.md` (Flujo de feature).
- `.agent/skills/spec_author/SKILL.md` (Skill de autor de specs).
- `.agent/skills/implementer/SKILL.md` (Skill de implementador).
- `.agent/skills/reviewer/SKILL.md` (Skill de revisor).
- `progress/current.md` (Log de progreso actual).
- `progress/history.md` (Historial de hitos).

### Estado Operativo de estos Recursos
Todos estos archivos y carpetas son **documentales, no activos y no ejecutables**. Carecen de front matter de configuración o metadata activa para Codex/Antigravity, y no poseen autorización para realizar modificaciones operativas sobre código real ni para ejecutar automatizaciones activas.

---

## 4. Estado del Manual Anti-Errores
- El archivo `docs/manual_anti_errores_del_arnes.md` ha sido clasificado formalmente como un **recurso local privado y opcional**.
- Está excluido del índice público mediante `.gitignore`.
- No debe tratarse como un archivo obligatorio en el repositorio público ni ser una entrada bloqueante para el preflight manual o el futuro `gate_0_preflight`.
- Se ha establecido que debe excluirse explícitamente de futuros procesos de compresión, empaquetado o exportación de este arnés (junto con archivos `.zip`).

---

## 5. Reglas Operativas Vigentes para Antigravity
De acuerdo con las reglas locales del MVP, la interacción agéntica se rige por:
- **Uso seguro de modelos:** Utilizar Gemini 3.5 Flash Low obligatoriamente para tareas mecánicas (`git status`, validaciones, stage, commit y push). Los modelos superiores se reservan para análisis complejos previa autorización.
- **Ahorro de tokens en diffs:** No solicitar diffs largos a Antigravity. Si un diff sobrepasa los límites razonables de tokens, el desarrollador humano proporcionará el archivo completo para auditoría externa.
- **Seguridad en Git:** 
  - Queda prohibido usar `git add .` y `git add -A`. Todas las preparaciones de archivos deben ser selectivas por ruta exacta.
  - No realizar commits si en `git status` aparecen archivos fuera del alcance de la tarea.
  - No hacer `git push` si el working tree no está limpio tras el commit.
  - Prohibidos el uso de `git push --force`, rebase o merge automáticos sin aprobación humana expresa.

---

## 6. Riesgos Conocidos o Pendientes
- **Acoplamiento agéntico:** Riesgo de divergencia sintáctica entre Codex y Antigravity en la futura conversión de las sedes conceptuales a formato activo.
- **Deuda técnica documental:** Evitar la creación de ruido estructural innecesario en carpetas no utilizadas (Lean + 5S).

---

## 7. Próximos Caminos Posibles
- Realizar una auditoría formal de compatibilidad de formatos entre Antigravity y Codex.
- Profundizar en la definición documental y el diseño de la estructura de inputs/outputs para futuros gates automáticos.
- Iniciar una primera feature piloto puramente documental (sin código de software real) para testear manualmente el flujo `sdd_feature_workflow.md`.
- Diseñar documentalmente el proceso futuro de exportación del arnés para excluir recursos locales privados antes de cualquier implementación de comandos.
