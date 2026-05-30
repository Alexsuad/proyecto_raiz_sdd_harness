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
- **Estado actual:** fase documental / MVP estructural.
- **Código de producto:** no existe.
- **Features activas:** ninguna.
- **Automatización activa:** ninguna.
- **Gates automatizados activos:** ninguno.

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

- rules activas;
- workflows activos;
- skills activas;
- gates operativos o automatizados;
- specs de features reales;
- scripts ejecutables;
- tests reales del arnés.

## 5. Estado de `.agent/`

La carpeta `.agent/` existe únicamente como estructura documental futura.

Las carpetas internas:

- `.agent/rules/`
- `.agent/workflows/`
- `.agent/skills/`

no deben interpretarse como recursos activos de Antigravity.

Su función actual es indicar dónde vivirán esos recursos cuando exista una necesidad operativa validada, autorización explícita y revisión correspondiente.

No debe crearse `.agent/gates/` todavía.

## 6. Decisión de auditoría aplicada

Se recibió una observación de auditoría sobre posible sobreingeniería prematura por la existencia de carpetas `.agent/`.

La decisión tomada fue mantener esas carpetas como sedes documentales mínimas, pero corregir el riesgo de interpretación automática eliminando metadatos tipo front matter de los README y agregando advertencias explícitas de estado documental.

Esta decisión deja el proyecto en un estado intermedio controlado:

- se mantiene la topología futura del arnés;
- no se activan recursos operativos prematuros;
- se reduce el riesgo de que Antigravity interprete README como reglas, workflows o skills activas;
- se conserva el principio LEAN.

## 7. Límites operativos vigentes

Hasta nueva autorización explícita, no se debe:

- crear `.agent/gates/`;
- crear rules activas;
- crear workflows activos;
- crear skills activas;
- crear scripts de gates;
- crear specs de features reales;
- ejecutar agentes sobre código real de proyectos derivados;
- modificar la constitución sin revisión y aprobación;
- convertir las sedes documentales en automatización activa.

## 8. Próximo paso recomendado

El siguiente paso recomendado es revisar el estado completo del repositorio y decidir si conviene crear una primera definición documental de gate o si antes debe consolidarse un checklist de preflight en documentación.

No debe avanzarse a automatización activa hasta que exista autorización explícita y revisión del impacto.

## 9. Definición documental de Gate 0

- **Fecha:** 2026-05-30.
- **Documento creado:** `docs/gate_0_preflight_definicion.md`.
- **Tipo:** definición documental previa de gate.
- **Estado:** creado, pendiente de auditoría.
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

- **Fecha:** 2026-05-30.
- **Documento usado:** `docs/preflight_estructural.md`.
- **Tipo de revisión:** preflight manual documental.
- **Resultado:** aprobado.
- **Evidencia:** revisión de estructura base, estado agéntico, no duplicación y criterio LEAN.
- **Observaciones:** no existen rules activas, workflows activos, skills activas, gates operativos o automatizados, scripts ejecutables, specs reales ni código de producto.
- **Decisión:** se permite avanzar únicamente con cambios documentales controlados y justificados.
- **Restricción vigente:** no activar automatización, no crear `.agent/gates/` y no crear recursos operativos activos sin autorización explícita.
