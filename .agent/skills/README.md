# File: .agent/skills/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la sede futura de skills reutilizables para agentes.
# Rol: Guía base para organizar capacidades especializadas del arnés agéntico.
# ──────────────────────────────────────────────────────────────────────

# Skills — Capacidades reutilizables para agentes

## 1. Propósito

Esta carpeta será la sede oficial de las skills reutilizables del proyecto raíz `proyecto_raiz_sdd_harness`.

Esta carpeta tiene estado documental. Ningún archivo dentro de esta sede debe considerarse una skill activa hasta que se cree explícitamente una skill validada y autorizada.

Su objetivo es permitir que los agentes ejecuten tareas especializadas siguiendo instrucciones claras, reutilizables, auditables y alineadas con la documentación oficial del repositorio.

## 2. Qué es una skill

Una skill es una capacidad especializada que indica a un agente cómo realizar una tarea repetible.

Cada skill deberá vivir en su propia carpeta y contener un archivo `SKILL.md` con instrucciones específicas, límites, entradas esperadas, salidas esperadas y criterios de validación.

## 3. Relación con la constitución y los adaptadores

Las skills no reemplazan:

- `docs/constitucion_del_proyecto.md`
- `docs/00_mapa_y_gobernanza_documental.md`
- `AGENTS.md`
- `GEMINI.md`
- `.agent/rules/`

Las skills deben aplicar la metodología oficial, no redefinirla ni duplicarla completa.

## 4. Estructura prevista de una skill

Cuando se cree una skill real, deberá seguir esta estructura base:

- `.agent/skills/<skill_id>/SKILL.md`
- `.agent/skills/<skill_id>/README.md` si necesita explicación adicional.
- `.agent/skills/<skill_id>/resources/` si necesita recursos auxiliares.
- `.agent/skills/<skill_id>/examples/` si necesita ejemplos controlados.

No todas las skills necesitarán recursos o ejemplos. Debe evitarse crear estructura vacía sin necesidad.

## 5. Contenido mínimo de `SKILL.md`

Cada `SKILL.md` futuro deberá definir:

- nombre de la skill;
- descripción breve de máximo 250 caracteres;
- propósito;
- cuándo usarla;
- cuándo no usarla;
- entradas necesarias;
- pasos permitidos;
- archivos que puede leer;
- archivos que puede modificar;
- límites de seguridad;
- validaciones requeridas;
- condiciones de bloqueo;
- salida esperada;
- reporte final obligatorio.

## 6. Skills previstas

En fases posteriores se podrán crear skills como:

- `spec_author`: ayuda a crear o revisar specs por feature.
- `implementer`: ayuda a ejecutar implementación candidata desde una spec aprobada.
- `reviewer`: revisa entregables candidatos, evidencia, riesgos y cumplimiento de reglas.
- `qa_reviewer`: revisa validaciones, pruebas, escenarios críticos y bloqueos de QA.
- `documentation_auditor`: detecta duplicación, inconsistencias y problemas de gobernanza documental.

Estas skills no se crean todavía para evitar automatización prematura.

## 7. Qué no debe vivir aquí

Esta carpeta no debe usarse para guardar:

- metodología completa;
- constitución duplicada;
- rules locales;
- workflows;
- scripts ejecutables;
- specs de features;
- reportes de progreso;
- credenciales;
- tokens;
- configuraciones sensibles;
- código de productos derivados.

## 8. Regla de revisión cruzada

Una skill puede incluir autoauditoría como primera revisión interna, pero no puede autoaprobar cambios relevantes.

Cuando una skill produzca un entregable candidato, otro rol, skill, checklist, gate o humano aprobador deberá validar el resultado según el nivel de riesgo.

## 9. Estado actual

- **Estado:** sede documental creada.
- **Skills activas:** ninguna.
- **Pendiente:** crear la primera skill cuando exista una necesidad operativa validada y una estructura mínima suficiente del arnés.