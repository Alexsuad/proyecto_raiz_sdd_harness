# File: progress/history.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar el historial resumido de avances del proyecto raíz.
# Rol: Memoria operativa versionada para conservar hitos, decisiones y cierres relevantes.
# ──────────────────────────────────────────────────────────────────────

# Historial operativo del proyecto raíz

## 1. Propósito

Este archivo registra los hitos principales del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es conservar una memoria breve, trazable y versionada de los avances importantes, evitando depender de la memoria del chat o de reportes temporales.

Este archivo no reemplaza la constitución, el mapa documental, las specs, los ADR ni los commits de Git.

## 2. Criterio de registro

Solo deben registrarse hitos relevantes, como:

- creación de documentos base;
- creación de adaptadores operativos;
- creación de sedes documentales;
- decisiones de auditoría;
- bloqueos levantados;
- cambios estructurales;
- cambios de estado del arnés;
- creación futura de specs, gates, workflows o skills activos.

No debe usarse este archivo para registrar cada microcorrección menor.

## 3. Historial inicial

### 2026-05-30 — Creación de base documental inicial

Se creó la base documental inicial del proyecto raíz con:

- `docs/00_mapa_y_gobernanza_documental.md`
- `docs/01_metodologia_base_comun.md`
- `docs/02_metodologia_desarrollo_software_sdd_harness.md`
- `docs/constitucion_del_proyecto.md`

Resultado:

- documentación base creada;
- constitución inicial aprobada;
- reglas no negociables definidas;
- metodología común y ruta software inicial establecidas.

### 2026-05-30 — Creación de sede ADR

Se creó:

- `docs/adr/README.md`

Resultado:

- sede oficial para futuras decisiones arquitectónicas;
- ningún ADR activo todavía.

### 2026-05-30 — Creación de adaptadores operativos

Se crearon:

- `AGENTS.md`
- `GEMINI.md`

Resultado:

- adaptador operativo mínimo para Codex y agentes compatibles;
- adaptador operativo mínimo para Gemini y Antigravity;
- ambos archivos quedan subordinados a la constitución y al mapa documental.

### 2026-05-30 — Creación de sedes documentales del arnés

Se crearon las sedes mínimas:

- `specs/README.md`
- `progress/README.md`
- `scripts/README.md`
- `tests/README.md`

Resultado:

- sede futura de specs por feature;
- sede de seguimiento operativo;
- sede futura de scripts y gates deterministas;
- sede futura de pruebas del arnés;
- sin specs reales, scripts reales ni tests activos.

### 2026-05-30 — Creación de sedes documentales `.agent/`

Se crearon:

- `.agent/rules/README.md`
- `.agent/workflows/README.md`
- `.agent/skills/README.md`

Resultado:

- sedes futuras para rules, workflows y skills;
- ningún recurso activo creado;
- no se creó `.agent/gates/`.

### 2026-05-30 — Corrección LEAN sobre `.agent/`

Una auditoría detectó riesgo de sobreingeniería prematura y posible interpretación automática de README como recursos activos.

Se aplicó la corrección:

- eliminación de front matter en `.agent/rules/README.md`;
- eliminación de front matter en `.agent/workflows/README.md`;
- adición de advertencias de estado documental en rules, workflows y skills.

Resultado:

- `.agent/` queda como topología futura;
- no hay rules, workflows ni skills activas;
- se mantiene el principio LEAN;
- se reduce el riesgo de activación prematura.

### 2026-05-30 — Registro de estado actual

Se creó:

- `progress/current.md`

Resultado:

- estado operativo actual documentado;
- fase documental / MVP estructural declarada;
- se establece que no hay automatización activa, gates automatizados, specs reales ni código de producto.

### 2026-05-30 — Creación de preflight estructural

Se creó:

- `docs/preflight_estructural.md`

También se corrigió:

- `.agent/workflows/README.md`

Resultado:

- checklist documental manual para revisar estructura antes de avanzar;
- regla de descripción breve de máximo 250 caracteres reincorporada en workflows;
- no se creó automatización;
- no se creó `.agent/gates/`.

### 2026-05-30 — Consolidación del estado normativo

Se actualizaron:

- `docs/constitucion_del_proyecto.md`
- `docs/00_mapa_y_gobernanza_documental.md`

Motivo:

- una auditoría detectó que ambos documentos aún se declaraban como borradores;
- esto podía reducir su autoridad normativa ante agentes de IA;
- se decidió marcarlos como aprobados para fase documental / MVP estructural.

Resultado:

- constitución vigente para la fase documental actual;
- mapa documental vigente como documento rector;
- bloqueo de auditoría levantado;
- documentos pendientes de revalidación tras la primera feature piloto o cuando se cree el primer recurso activo real del arnés.

### 2026-05-30 — Definición documental de Gate 0

Se creó:

- `docs/gate_0_preflight_definicion.md`

Motivo:

- avanzar desde el checklist manual `docs/preflight_estructural.md` hacia una definición formal del futuro `gate_0_preflight`;
- mantener el enfoque SDD: primero definición documental, luego posible automatización;
- evitar crear scripts o gates activos antes de contar con revisión y autorización explícita.

Resultado:

- primera definición documental de gate creada;
- no se creó `.agent/gates/`;
- no se creó `scripts/gate_0_preflight.py`;
- no se activó automatización;
- el documento queda pendiente de auditoría antes de cualquier implementación futura.

### 2026-05-30 — Corrección de observaciones de auditoría de Gate 0

Se actualizaron:

- `docs/gate_0_preflight_definicion.md`
- `progress/current.md`

Motivo:

- la definición documental de Gate 0 fue revisada;
- el dictamen fue “aprobado con observaciones menores”;
- se procedió a corregir las observaciones detectadas en la auditoría.

Resultado:

- se agregaron definiciones de estado para evitar ambigüedades sobre el rol estrictamente documental de esta fase;
- se incorporó `docs/adr/README.md` como entrada del futuro gate;
- se clarificó en `progress/current.md` que no hay gates operativos ni automatizados activos;
- no se creó `scripts/gate_0_preflight.py`;
- no se creó `.agent/gates/`;
- no se activó automatización;
- el proyecto continúa en fase documental / MVP estructural.

### 2026-05-30 — Actualización de estado de metodologías base

Se actualizaron:

- `docs/01_metodologia_base_comun.md`
- `docs/02_metodologia_desarrollo_software_sdd_harness.md`

Motivo:

- ambos documentos metodológicos aún conservaban estado de borrador inicial;
- `docs/02_metodologia_desarrollo_software_sdd_harness.md` contenía referencias desactualizadas sobre recursos que ya existen en el proyecto;
- era necesario alinear ambos documentos con la fase documental / MVP estructural actual.

Resultado:

- `docs/01_metodologia_base_comun.md` quedó aprobado para fase documental / MVP estructural;
- `docs/02_metodologia_desarrollo_software_sdd_harness.md` quedó aprobado para fase documental / MVP estructural;
- se aclaró que `AGENTS.md`, `GEMINI.md` y `progress/` ya existen como adaptadores y sedes documentales mínimas;
- se mantuvo explícito que no existe autorización para implementación sobre código real ni activación de automatización;
- no se crearon specs reales;
- no se crearon scripts;
- no se crearon tests reales;
- no se creó `.agent/gates/`;
- el proyecto continúa en fase documental / MVP estructural.

### 2026-06-01 — Creación del manual anti-errores del arnés

Se creó:

- `docs/manual_anti_errores_del_arnes.md`

También se actualizó:

- `docs/00_mapa_y_gobernanza_documental.md`

Motivo:

- adaptar un conjunto de lecciones aprendidas al contexto específico del proyecto raíz;
- prevenir errores recurrentes durante la fase documental / MVP estructural;
- reforzar reglas como política primero, código después; revisión de diff; no degradar contenido para pasar auditorías; separación de commits por naturaleza del cambio; y gestión diferida de deuda técnica o agéntica;
- registrar el manual en el mapa documental sin convertirlo en constitución paralela ni en automatización activa.

Resultado:

- manual anti-errores creado como guía operativa subordinada a la constitución y al mapa documental;
- mapa documental actualizado para reconocer el manual;
- `docs/gate_0_preflight_definicion.md` reconocido también en la jerarquía y tabla documental;
- no se creó `.agent/gates/`;
- no se crearon scripts;
- no se crearon tests;
- no se activó automatización.

Nota posterior de contención:
El archivo `docs/manual_anti_errores_del_arnes.md` fue posteriormente reclasificado como material local privado/no versionado hacia adelante. La decisión operativa fue no limpiar historial en esta fase, pero sí evitar que el archivo siga alimentándose en GitHub mediante `.gitignore`.

### 2026-06-01 — Alineación de checklists documentales del arnés

Se actualizaron:

- `docs/preflight_estructural.md`
- `docs/gate_0_preflight_definicion.md`

Motivo:

- corregir las observaciones menores detectadas por la auditoría documental general de contraste realizada con Gemini 3.5 Flash High;
- asegurar que el preflight estructural manual verifique la existencia de `docs/gate_0_preflight_definicion.md`;
- asegurar que el preflight estructural manual verifique la existencia de `docs/manual_anti_errores_del_arnes.md`;
- asegurar que la definición documental de Gate 0 reconozca `docs/manual_anti_errores_del_arnes.md` como entrada esperada del futuro gate.

Resultado:

- checklist de estructura base del preflight actualizado;
- entradas esperadas de Gate 0 actualizadas;
- observaciones menores de auditoría corregidas;
- no se creó `.agent/gates/`;
- no se crearon scripts;
- no se crearon tests;
- no se crearon specs;
- no se activó automatización.

### 2026-06-01 — Preflight estructural manual actualizado aprobado

Se ejecutó:

- `docs/preflight_estructural.md`

Modelo usado:

- Gemini 3.5 Flash High

Motivo:

- validar el estado documental del arnés después de la creación del manual anti-errores;
- validar el estado documental después de alinear los checklists de `docs/preflight_estructural.md` y `docs/gate_0_preflight_definicion.md`;
- confirmar que las observaciones menores detectadas por la auditoría de contraste quedaron corregidas.

Resultado:

- preflight estructural manual aprobado;
- estructura base aprobada;
- estado agéntico inactivo confirmado;
- no existe `.agent/gates/`;
- no existen scripts ejecutables;
- no existen tests reales;
- no existen specs reales;
- no existen rules activas;
- no existen workflows activos;
- no existen skills activas;
- no existen gates operativos ni automatizados;
- no se activó automatización.

Decisión:

- se permite avanzar únicamente con cambios documentales controlados y justificados;
- el siguiente avance sugerido es evaluar la creación de una primera spec piloto documental, sin activar todavía automatización ni código de producto.

### 2026-06-01 — Creación del bloque documental mínimo de skills del arnés

Se crearon y publicaron:

- `.agent/workflows/sdd_feature_workflow.md` (Workflow SDD por feature)
- `.agent/skills/spec_author/SKILL.md` (Skill Spec Author)
- `.agent/skills/implementer/SKILL.md` (Skill Implementer)
- `.agent/skills/reviewer/SKILL.md` (Skill Reviewer)

Commits asociados:

- `52f8c68 docs: crear workflow sdd por feature`
- `1b99a18 docs: crear skill documental spec author`
- `90b8186 docs: crear skill documental implementer`
- `baf9071 docs: crear skill documental reviewer`

Motivo:
- Definir conceptualmente el triángulo de roles mínimos (`spec_author`, `implementer`, `reviewer`) y el flujo lógico de estados y artefactos por feature bajo Spec-Driven Development (SDD).
- Establecer las responsabilidades operativas y límites rígidos de cada rol antes de activar automatizaciones o scripts reales.

Resultado:
- Bloque documental mínimo integrado y validado.
- Todas las piezas se mantienen en estado documental, no activo y no ejecutable, sin front matter y sin autorización de modificación de código real en proyectos derivados.
- Bloqueo de avance controlado: el arnés cuenta con sus directrices conceptuales básicas consolidadas.

### 2026-06-01 — Creación de reglas locales documentales del MVP

Se creó y publicó:

- `.agent/rules/00_reglas_locales_mvp_documental.md` (Regla local documental de MVP)

Commit asociado:

- `21f34ba docs: crear reglas locales documentales del mvp`

Motivo:
- Consolidar las pautas de control del comportamiento de agentes o asistentes de IA, estableciendo límites de alcance, Git seguro, elección eficiente de modelos de lenguaje, diffs cortos, commits atómicos y límites rígidos de la fase documental.

Resultado:
- Regla documental de contexto integrada en el repositorio.
- El archivo se mantiene en estado documental, no activo y no ejecutable, sin front matter ni metadatos activos y sin autorización de modificación en el codebase de código real.
- Aclaración: no se activaron rules reales de Antigravity, no se creó `.agent/gates/`, no se crearon scripts, tests ni specs reales.

## 4. Estado actual resumido

El proyecto se encuentra en fase documental / MVP estructural.

Actualmente existen:

- documentos base;
- constitución;
- sede ADR;
- adaptadores `AGENTS.md` y `GEMINI.md`;
- sedes documentales para specs, progress, scripts, tests;
- sedes documentales para `.agent/rules/`, `.agent/workflows/` y `.agent/skills/`;
- preflight estructural manual;
- workflow SDD por feature documental (`sdd_feature_workflow.md`);
- skills documentales de roles de primer nivel (`spec_author`, `implementer` y `reviewer`);
- primera regla local documental del MVP en `.agent/rules/`.

Actualmente no existen:

- código de producto;
- specs reales;
- features activas;
- rules activas;
- workflows activos;
- skills activas;
- gates operativos o automatizados;
- scripts ejecutables;
- tests reales.

## 5. Próximo paso recomendado
 
 Antes de crear nuevos recursos estructurales, se debe ejecutar el preflight documental definido en:
 
 - `docs/preflight_estructural.md`
 
 El siguiente avance debe estar justificado por una necesidad clara y no debe activar automatización prematura.

---

### 2026-06-08 — Cierre de Fase 0 documental con auditoría aprobada

Se ha cerrado formalmente la **Fase 0 (Consolidación Documental y del MVP Estructural)** del proyecto raíz.

**Detalles del Hito:**
- **Commit de Cierre:** `0f2ae3e74561e3ef6129aff3b601901377ce2d3f` (publicado en GitHub).
- **Reporte de Auditoría final:** Creado y aprobado en [progress/auditoria_final_cierre_fase_0_2026-06-07.md](./auditoria_final_cierre_fase_0_2026-06-07.md).
- **Acciones aplicadas:** Sincronización completa de los documentos de estado (`plan_implementacion_v0_1`, `feature_list.md`, `README.md`, `current.md` y `history.md`) para registrar el estado cerrado de la fase.

**Observación y Deuda Controlada:**
- El archivo privado local `docs/manual_anti_errores_del_arnes.md` está correctamente excluido en Git via `.gitignore`, pero sigue presentándose como una alerta de contención física en la empaquetación ZIP del workspace.

**Próximo Estado del Proyecto:**
- La Fase 0 queda oficialmente **cerrada**.
- La Fase 1 (Spec Piloto Documental) queda en estado **pendiente de autorización humana explícita** para su apertura. Se mantienen bloqueadas las suites de testeo (`pytest`), entornos de ejecución (`uv`), gates automatizados o inyección de código.

---

### 2026-06-08 — Apertura controlada de Fase 1 y creación de spec piloto F-013

Se ha abierto la **Fase 1 (Spec Piloto Documental)** de forma controlada y se ha creado físicamente la especificación piloto en la carpeta `specs/f_013_gate_manual_futuro/`.

**Detalles del Hito:**
- **Commit Asociado:** ccfac0b2b2a265672f614f91991a0ca465fc9206 (ccfac0b)
- **Ruta de Spec:** `specs/f_013_gate_manual_futuro/`
- **Archivos creados:**
  * `requirements.md`: define alcance, roles y bloqueos explícitos.
  * `design.md`: detalla estados de transición y bloque de firma en texto.
  * `tasks.md`: registra tareas atómicas documentales pendientes.
  * `validation.md`: pauta de validación procedimental y casos manuales.
  * `review.md`: plantilla de dictamen final.
- **Estado de la Spec:** Candidata y en revisión (`review.md` en estado `abierto` / pendiente de dictamen).

**Restricciones de Seguridad:**
- Se confirma que no se han creado scripts, lógicas de software, ni gates ejecutables.
- El runtime técnico, `pytest` y `uv` se mantienen estrictamente bloqueados.
- Las skills de background y workflows automáticos en `.agent/` siguen sin activarse.
- No se declara finalizada la feature F-013 ni se declara cerrada la Fase 1.

---

### 2026-06-08 — Registro de revisión documental de F-013

Se ha registrado formalmente el dictamen de la revisión de la especificación piloto **F-013 — Gate manual futuro** en el repositorio.

**Detalles del Hito:**
- **Commit Asociado:** 17aeb1a2527f932c9bb84489a3701958ea628b5f (Trazabilidad previa: 424576a5ce2b24781905aa584c879db3ab0f1084)
- **Archivo modificado:** `specs/f_013_gate_manual_futuro/review.md`
- **Resumen:** Registro del dictamen de la revisión documental de la feature piloto F-013 (`APROBADO CON OBSERVACIONES MENORES`), definiendo las pautas de control del gate manual y los bloqueos metodológicos vigentes.

**Restricciones de Seguridad:**
- Se confirma que no se ha habilitado ni creado ninguna lógica de software, scripts ni gates técnicos.
- La ejecución del runtime, tests con `pytest` o administración con `uv` sigue totalmente bloqueada.
- No se declara completada la feature F-013 ni se cierra la Fase 1 de forma autónoma.

---

### 2026-06-08 — Cierre documental de F-013

Se ha declarado formalmente la especificación piloto **F-013 — Gate manual futuro** como completada documentalmente, sin habilitar ningún componente técnico.

**Detalles del Hito:**
- **Commit pendiente de consolidación:** Microfase 1.8
- **Commit base de pre-cierre:** `e46870d1c3bf6f3c9f8b681a1579e6257a94c0ce`
- **Archivos modificados:** `specs/f_013_gate_manual_futuro/{requirements,design,tasks,validation,review}.md`, `progress/{current,feature_list,history}.md`, y `README.md`.
- **Resumen:** Cierre documental de la feature F-013. Se cambia el estado de los documentos de la spec de "Candidato" a "Completado documentalmente", se actualiza la lista oficial de features y se definen los siguientes pasos de forma coherente.

**Restricciones de Seguridad:**
- El gate manual futuro queda definido estrictamente a nivel documental; no se implementó ningún gate técnico.
- No se creó código de producto ni scripts ejecutables en `scripts/`.
- No se modificaron ni activaron configuraciones, rules, workflows ni skills en `.agent/`.
- No se activó runtime técnico, suite de test con `pytest` ni entorno con `uv`.
- La Fase 1 sigue abierta de forma controlada hasta una posterior decisión formal de cierre.
- La Fase 2 se mantiene estrictamente bloqueada.

---

### 2026-06-08 — Cierre formal de Fase 1

Se ha cerrado formalmente la **Fase 1 (Spec Piloto Documental)** del proyecto raíz en sentido documental.

**Detalles del Hito:**
- **Commit pendiente de consolidación:** Microfase 1.9
- **Resumen:** Declaración de cierre formal de la Fase 1 tras completarse documentalmente la especificación piloto **F-013 — Gate manual futuro** (consolidada en commit `585d1c5478c0092b882d9b8d66150acabda4f59b`). Se actualizan los documentos de control y el plan de implementación v0.1.

**Restricciones de Seguridad:**
- No se abrió la Fase 2, la cual queda pendiente de autorización humana explícita.
- No se creó código de producto ni scripts en `scripts/`.
- No se activó runtime técnico, suite de test con `pytest` ni entorno con `uv`.
- No se modificó ni activó nada en la carpeta `.agent/`.
