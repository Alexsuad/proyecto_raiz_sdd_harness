# File: progress/auditoria_arquitectonica_interna_2026-06-07.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar la auditoría arquitectónica interna del repositorio a fecha de 2026-06-07.
# Rol: Reporte de auditoría y análisis de coherencia de las piezas documentales del arnés.
# ──────────────────────────────────────────────────────────────────────

# Auditoría Arquitectónica Interna (2026-06-07)

**Versión:** v0.1  
**Estado:** Incorporado como evidencia documental de Fase 0 cerrada con observaciones controladas.  
**Tipo:** Reporte operativo de control  
**Ubicación:** `progress/auditoria_arquitectonica_interna_2026-06-07.md`

---

## 1. Propósito de la auditoría
Esta auditoría interna tiene como objetivo inventariar y clasificar todas las carpetas y archivos existentes en el repositorio `proyecto_raiz_sdd_harness` a fecha de 2026-06-07. Se busca verificar el cumplimiento estricto del orden LEAN, clasificar los artefactos de acuerdo a su estado operativo real y detectar discrepancias de diseño o riesgos metodológicos antes de avanzar en la Fase 0 del plan de implementación.

---

## 2. Clasificación y estado de la estructura del repositorio

A continuación se realiza el análisis físico por directorios y archivos, clasificándolos en:
* **Activo:** Elemento que rige o documenta de forma efectiva la operación actual.
* **Candidato:** Propuesta o borrador sujeto a revisión humana y que carece de definitividad en el ciclo de vida.
* **Futuro / Inactivo:** Estructura o archivo reservado para fases técnicas posteriores; no operativo en esta fase.
* **Referencia:** Documento de consulta metodológica o actas históricas.

### 2.1. Directorio `/docs` (Gobernanza y Metodologías)
* **`00_mapa_y_gobernanza_documental.md`**
  - *Estado:* **Activo / Referencia**
  - *Descripción:* Documento rector de la organización de archivos. Vigente y estable para el MVP documental.
* **`01_metodologia_base_comun.md`**
  - *Estado:* **Activo / Referencia**
  - *Descripción:* Principios metodológicos transversales (LEAN, entregable candidato). Aprobado y vigente.
* **`02_metodologia_desarrollo_software_sdd_harness.md`**
  - *Estado:* **Activo / Referencia**
  - *Descripción:* Metodología de software específica. Actualizada recientemente con las pautas de pruebas reales y no maquillaje de resultados.
* **`constitucion_del_proyecto.md`**
  - *Estado:* **Activo / Referencia**
  - *Descripción:* Marco constitucional que define las reglas no negociables del arnés. Aprobada y vigente.
* **`procedimiento_inicio_proyecto_sdd_harness.md`**
  - *Estado:* **Activo**
  - *Descripción:* Guía operativa paso a paso de arranque de proyectos. Incorpora las secciones obligatorias de controles procedimentales y agénticos.
* **`vision_y_alcance_del_proyecto_raiz.md`**
  - *Estado:* **Activo**
  - *Descripción:* Define el propósito e hitos finales del MVP v0.1. Aprobada y vigente en el control de versiones.
* **`gate_0_preflight_definicion.md`**
  - *Estado:* **Referencia / Futuro**
  - *Descripción:* Definición puramente conceptual y documental de las condiciones de entrada del primer gate técnico. Inactivo a nivel de runtime.
* **`preflight_estructural.md`**
  - *Estado:* **Activo (Checklist manual)**
  - *Descripción:* Checklist de control estructural que los agentes deben validar manualmente en sus respuestas.
* **Subdirectorio `/docs/adr/`**
  - *Estado:* **Referencia / Futuro**
  - *Descripción:* Sede vacía (únicamente contiene un `README.md` explicativo) para futuras actas de arquitectura.

### 2.2. Adaptadores operativos de arranque (Raíz)
* **`AGENTS.md`**
  - *Estado:* **Activo**
  - *Descripción:* Adaptador mínimo de comportamiento para Codex y herramientas compatibles.
* **`GEMINI.md`**
  - *Estado:* **Activo**
  - *Descripción:* Adaptador mínimo de comportamiento para Gemini y Antigravity.

### 2.3. Directorio de configuración de agentes `/.agent/`
* **`/.agent/workflows/sdd_feature_workflow.md`**
  - *Estado:* **Candidato inactivo / Futuro**
  - *Descripción:* Flujo de trabajo SDD detallado. Carece de metadatos de automatización y de configuración activa en el IDE. Es un borrador de diseño conceptual.
* **`/.agent/skills/` (spec_author, implementer, reviewer)**
  - *Estado:* **Candidato inactivo / Futuro**
  - *Descripción:* Contratos de comportamiento previstos para roles agénticos. Se mantienen en formato puramente documental y marcados como inactivos en sus READMEs.
* **`/.agent/rules/00_reglas_locales_mvp_documental.md`**
  - *Estado:* **Candidato inactivo / Futuro**
  - *Descripción:* Pautas de comportamiento de agentes. Mapeado conceptualmente pero no activo en la configuración del runtime agéntico.

### 2.4. Directorio de seguimiento `/progress`
* **`current.md` y `history.md`**
  - *Estado:* **Activo**
  - *Descripción:* Seguimiento del estado del arnés e hitos operativos consolidados de manera física y persistente.
* **`plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md`**
  - *Estado:* **Activo**
  - *Descripción:* Hoja de ruta v0.1 priorizando el cierre LEAN de la Fase 0 documental.
* **`fase_00_origen_del_proyecto_raiz.md`**
  - *Estado:* **Activo**
  - *Descripción:* Intake Inicial del repositorio que documenta el problema raíz y alcance negativo.

### 2.5. Directorios Técnicos `/specs`, `/scripts` y `/tests`
* **`/specs`**
  - *Estado:* **Futuro / Inactivo**
  - *Descripción:* Directorio vacío (con `README.md` de sede). Destinado a albergar especificaciones de features piloto.
* **`/scripts`**
  - *Estado:* **Futuro / Inactivo**
  - *Descripción:* Directorio vacío (con `README.md` de sede). Destinado a albergar el script de validación `gate_0_preflight.py` en fases técnicas posteriores.
* **`/tests`**
  - *Estado:* **Futuro / Inactivo**
  - *Descripción:* Directorio vacío (con `README.md` de sede). Destinado a albergar los archivos de pytest e infraestructura de pruebas.

---

## 3. Análisis de posibles contradicciones o duplicidades
* **Gobernanza vs. Adaptadores:** Se verifica que `AGENTS.md` y `GEMINI.md` se subordinan correctamente a la Constitución y al Mapa Documental (`docs/00`). Hacen referencias relativas sin duplicar el marco normativo.
* **Estado de la automatización:** Existe consistencia a lo largo del repositorio: la carpeta `progress/`, las guías de inicio, las metodologías y la definición del plan coinciden unánimemente en declarar que **no existe automatización activa, scripts ejecutables ni gates lógicos integrados en background en esta fase**.
* **Coherencia de la carpeta `.agent/`:** Se cumple la directriz LEAN surgida tras la última auditoría de control: se eliminaron metadatos activos de formato *front matter* para evitar que los asistentes del IDE interpreten de forma prematura estos archivos de diseño conceptual como reglas de comportamiento del sistema.

---

## 4. Evaluación de riesgos metodológicos y técnicos
1. **Alerta de contención del manual privado (`docs/manual_anti_errores_del_arnes.md`):** 
   * *Estado:* No trackeado e ignorado formalmente por Git (`.gitignore:9`).
   * *Riesgo:* Git no sigue el archivo, por lo que no hay riesgo de inyección accidental en commits en el repositorio remoto. Sin embargo, su presencia local puede filtrarse si el proceso de exportación externa (ZIP) del usuario incluye archivos ignorados por Git.
   * *Acción procedimental:* Mantener el archivo bajo exclusión y no realizar modificaciones, traslados o borrados del archivo físico sin autorización previa del desarrollador humano.
2. **Riesgo de activación de metadatos agénticos:** Que en futuras ediciones se reincorporen etiquetas *front matter* (ej. `alwaysApply: true`, `globs: [...]`) en los archivos de la carpeta `.agent/rules/`, lo que activaría reglas de comportamiento del IDE antes de cerrar la Fase 0.
3. **Imprecisión de transición de Fase 0 a Fase 1:** Que se intente inicializar el entorno técnico (`uv init`, pytest, scripts de gates) antes de cerrar completamente el checklist documental de la Fase 0, lo que debilitaría la disciplina LEAN aprobada en el plan de orden.

---

## 5. Acciones y recomendaciones
* **Acción 1 (Alerta de Contención):** Mantener `docs/manual_anti_errores_del_arnes.md` tal y como está, sin alteración física (no borrar, no mover, no renombrar) de acuerdo a las reglas de Git ignore.
* **Acción 2:** Mantener bajo estricta supervisión del Equipo Auditor Procedimental que ningún asistente incorpore front matter de ejecución en `/.agent/rules/`, `/.agent/workflows/` ni `/.agent/skills/` hasta la aprobación explícita de la fase de automatización.
* **Acción 3:** Proceder de manera ordenada con las siguientes piezas documentales de la Fase 0 (Delimitación de zonas de trabajo y lista de características/feature list) antes de dar por cerrada esta etapa.
* **Importante:** Está estrictamente prohibido mover, borrar o retirar físicamente archivos o directorios de zonas de trabajo en esta etapa sin una instrucción de control directa y autorizada.

---

## 6. Dictamen de la auditoría
* **Dictamen:** **Candidato pendiente de auditoría**
* **Conclusión:** El repositorio se ajusta de forma general a los principios de gobernanza documental, subordinación constitucional y orden LEAN vigentes, aunque la Fase 0 todavía mantiene pendientes documentales antes de su cierre. Este reporte se mantiene en revisión y no constituye una regla de aprobación final hasta que sea validado y consolidado por el desarrollador humano.
