# File: .agent/workflows/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la sede futura de workflows operativos para Antigravity.
# Rol: Guía base para organizar flujos reutilizables de trabajo agéntico.
# ──────────────────────────────────────────────────────────────────────

# Workflows — Flujos operativos para Antigravity

## 1. Propósito

Esta carpeta será la sede oficial de los workflows operativos de Antigravity para el proyecto raíz `proyecto_raiz_sdd_harness`.

Esta carpeta tiene estado documental. Ningún archivo dentro de esta sede debe considerarse un workflow activo hasta que se cree explícitamente un workflow validado y autorizado.

Su objetivo es permitir que tareas repetibles del arnés se ejecuten con pasos claros, límites definidos, entradas esperadas, salidas verificables y cierre con evidencia.

## 2. Relación con la constitución y los adaptadores

Los workflows no reemplazan:

- `docs/constitucion_del_proyecto.md`
- `docs/00_mapa_y_gobernanza_documental.md`
- `AGENTS.md`
- `GEMINI.md`

Todo workflow debe respetar la constitución, el mapa documental, las reglas operativas y los límites del MVP actual.

## 3. Qué vivirá en esta carpeta

En fases posteriores, esta carpeta podrá contener workflows relacionados con:

- creación de una spec por feature;
- revisión de una spec;
- preparación de implementación candidata;
- revisión cruzada;
- validación de gates;
- cierre con evidencia;
- actualización de progress;
- auditoría documental puntual.

## 4. Qué no debe vivir aquí

Esta carpeta no debe usarse para guardar:

- metodología completa;
- constitución duplicada;
- rules locales;
- skills;
- scripts ejecutables;
- specs de features;
- reportes de progreso;
- credenciales;
- tokens;
- configuraciones sensibles.

## 5. Regla de diseño de workflows

Todo workflow futuro debe definir de forma clara:

- descripción breve de máximo 250 caracteres;
- propósito;
- cuándo usarlo;
- entradas necesarias;
- pasos permitidos;
- archivos que puede leer;
- archivos que puede modificar;
- salidas esperadas;
- validaciones requeridas;
- condiciones de bloqueo;
- reporte final obligatorio.

## 6. Workflows previstos

Además del workflow conceptual ya creado, en fases posteriores se podrán crear o activar formalmente workflows como:

- `sdd_feature_workflow.md`: ya existe como flujo conceptual no activo de una feature desde requisitos hasta revisión.
- `spec_review_workflow.md`: revisión controlada de una spec antes de implementación.
- `gate_review_workflow.md`: validación de resultados de gates y bloqueos.
- `documentation_audit_workflow.md`: auditoría documental puntual.

Estos workflows no deben interpretarse como activos; cualquier activación futura requiere autorización explícita.

## 7. Estado actual

- **Estado:** sede documental creada.
- **Recursos documentales existentes:** [sdd_feature_workflow.md](./sdd_feature_workflow.md) (Flujo conceptual de feature piloto, no activo).
- **Workflows activos:** ninguno.
- **Pendiente:** activación futura o adaptación formal al formato ejecutable del motor agéntico correspondiente solo tras autorización explícita.