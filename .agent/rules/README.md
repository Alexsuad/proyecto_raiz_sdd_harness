# File: .agent/rules/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la sede futura de reglas operativas locales para Antigravity.
# Rol: Guía base para organizar restricciones, criterios de comportamiento y reglas de ejecución del agente.
# ──────────────────────────────────────────────────────────────────────

# Rules — Reglas operativas locales para Antigravity

## 1. Propósito

Esta carpeta será la sede oficial de las reglas operativas locales de Antigravity para el proyecto raíz `proyecto_raiz_sdd_harness`.

Esta carpeta tiene estado documental. Ningún archivo dentro de esta sede debe considerarse una rule activa hasta que se cree explícitamente una regla operativa validada y autorizada.

Su objetivo es permitir que Antigravity trabaje con restricciones claras, contexto controlado y límites operativos alineados con la documentación oficial del repositorio.

## 2. Relación con la constitución y los adaptadores

Las reglas locales de esta carpeta no reemplazan:

- `docs/constitucion_del_proyecto.md`
- `docs/00_mapa_y_gobernanza_documental.md`
- `AGENTS.md`
- `GEMINI.md`

Las reglas locales deben actuar como una capa operativa breve para Antigravity, referenciando los documentos oficiales sin duplicarlos completos.

## 3. Qué vivirá en esta carpeta

Actualmente contiene una primera regla local documental no activa. En fases posteriores, esta carpeta podrá incorporar reglas adicionales relacionadas con:

- alcance permitido por tipo de tarea;
- comportamiento esperado del agente;
- restricciones para modificar documentos base;
- reglas de no duplicación;
- reglas de reporte final;
- límites para creación de archivos y carpetas;
- criterios para detenerse ante ambigüedad o riesgo;
- reglas específicas para trabajar con specs, workflows, skills y gates.

## 4. Qué no debe vivir aquí

Esta carpeta no debe usarse para guardar:

- metodología completa;
- constitución duplicada;
- prompts extensos;
- specs de features;
- workflows;
- skills;
- scripts ejecutables;
- reportes de progreso;
- credenciales;
- tokens;
- configuraciones sensibles.

## 5. Regla de brevedad

Cada regla local debe ser breve, clara y accionable.

Si una regla necesita explicación larga, debe vivir en un documento oficial dentro de `docs/` y la rule debe limitarse a referenciarla.

## 6. Estado actual

- **Estado:** sede documental creada.
- **Recursos documentales existentes:** [00_reglas_locales_mvp_documental.md](./00_reglas_locales_mvp_documental.md) (Regla local documental de MVP, no activa).
- **Rules activas:** ninguna.
- **Pendiente:** activación futura o adaptación formal al formato ejecutable del motor agéntico correspondiente solo tras autorización explícita.