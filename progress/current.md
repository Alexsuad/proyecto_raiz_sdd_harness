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
- gates definidos;
- gates automatizados;
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

## 9. Estado del archivo

- **Estado:** creado como punto de control operativo.
- **Uso:** referencia rápida del estado actual del arnés.
- **Pendiente:** actualizar después de cada cambio estructural relevante del proyecto raíz.