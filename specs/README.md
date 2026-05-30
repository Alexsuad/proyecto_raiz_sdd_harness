# File: specs/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la sede de especificaciones operativas por feature.
# Rol: Guía base para organizar requisitos, aclaraciones, diseño, tareas, validación y revisión.
# ──────────────────────────────────────────────────────────────────────

# Specs — Especificaciones operativas por feature

## 1. Propósito

Esta carpeta será la sede oficial de las especificaciones operativas por feature del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es permitir que cada cambio relevante avance con contexto claro, requisitos verificables, diseño revisado, tareas pequeñas, validación definida y cierre con evidencia.

## 2. Fuente de verdad por feature

Cada carpeta `specs/<feature_id>/` será la fuente de verdad operativa para una feature concreta.

El chat, los mensajes temporales del agente o los reportes no versionados no reemplazan la spec aprobada.

## 3. Estructura prevista por feature

Cuando se cree una feature real, su carpeta deberá seguir esta estructura base:

- `specs/<feature_id>/requirements.md`
- `specs/<feature_id>/clarifications.md`
- `specs/<feature_id>/design.md`
- `specs/<feature_id>/tasks.md`
- `specs/<feature_id>/validation.md`
- `specs/<feature_id>/review.md`

## 4. Función de cada archivo

- `requirements.md`: define qué se necesita construir, por qué, para quién y con qué criterios de aceptación.
- `clarifications.md`: registra dudas, preguntas, supuestos, decisiones pendientes o aclaraciones necesarias antes del diseño.
- `design.md`: describe cómo se resolverá técnicamente la feature sin romper arquitectura, contratos ni funcionalidades existentes.
- `tasks.md`: divide el trabajo en tareas pequeñas, ordenadas y verificables.
- `validation.md`: define cómo se comprobará que la implementación candidata funciona y no rompe comportamiento existente.
- `review.md`: registra la revisión cruzada, hallazgos, riesgos, bloqueos y recomendación final.

## 5. Regla de no implementación sin spec suficiente

Ningún agente debe iniciar implementación candidata de una feature relevante sin una spec suficiente y revisada.

Si la tarea es pequeña o de bajo riesgo, podrá usarse una versión reducida del flujo, siempre que exista evidencia mínima, justificación y validación según lo definido en la metodología de software.

## 6. Estado actual

- **Estado:** sede documental creada.
- **Features activas:** ninguna.
- **Pendiente:** crear la primera feature piloto cuando el arnés cuente con estructura mínima suficiente y autorización explícita.