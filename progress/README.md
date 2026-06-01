# File: progress/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la sede de seguimiento operativo del arnés.
# Rol: Guía base para registrar estado, avances, bloqueos, historial y cierres con evidencia.
# ──────────────────────────────────────────────────────────────────────

# Progress — Seguimiento operativo del arnés

## 1. Propósito

Esta carpeta será la sede oficial para registrar el seguimiento operativo del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es permitir que el avance del arnés sea trazable, revisable y verificable, evitando depender de la memoria del chat, reportes temporales o respuestas aisladas de agentes.

## 2. Qué información vivirá aquí

En fases posteriores, esta carpeta podrá contener archivos relacionados con:

- estado actual del proyecto;
- feature activa;
- tareas en curso;
- bloqueos detectados;
- decisiones pendientes;
- historial de avances;
- cierres con evidencia;
- resultados de validaciones;
- reportes de revisión.

## 3. Relación con `specs/`

La carpeta `specs/` define la fuente de verdad operativa de cada feature.

La carpeta `progress/` registrará el seguimiento del avance, pero no reemplazará las specs aprobadas.

Si existe diferencia entre una spec aprobada y un reporte de progreso, la spec tendrá prioridad hasta que sea actualizada mediante revisión y evidencia.

## 4. Archivos de seguimiento existentes y previstos

Actualmente existen `current.md` y `history.md` como archivos de seguimiento operativo. En fases posteriores, esta carpeta podrá incorporar archivos adicionales como:

- `current.md`: estado operativo actual del proyecto o de la feature activa.
- `history.md`: historial resumido de avances, closures y cambios relevantes.
- `blocked.md`: bloqueos abiertos, causas y acciones necesarias.
- `decisions_pending.md`: decisiones pendientes de revisión humana o técnica.

`current.md` y `history.md` ya existen; `blocked.md` y `decisions_pending.md` permanecen pendientes hasta que exista una necesidad real.

## 5. Reglas de uso

Todo registro dentro de `progress/` debe ser claro, breve y verificable.

No debe usarse esta carpeta para duplicar la constitución, la metodología, las specs ni los ADR.

Los reportes de progreso deben apuntar a la evidencia correspondiente cuando exista, por ejemplo:

- commits;
- diffs;
- archivos modificados;
- validaciones ejecutadas;
- checklists;
- gates;
- reportes de revisión.

## 6. Estado actual

- **Estado:** sede documental creada.
- **Archivos activos de seguimiento:** `current.md` e `history.md`.
- **Pendiente:** crear `blocked.md` o `decisions_pending.md` solo cuando exista una necesidad real.