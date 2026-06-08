# File: progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar el Plan de implementación v0.1 actualizado como fuente oficial de orden para continuar el trabajo del repositorio.
# Rol: Plan rector de implementación y prioridades de desarrollo para la v0.1.
# ──────────────────────────────────────────────────────────────────────

# Plan de implementación v0.1 — Proyecto Raíz SDD Harness

## 1. Propósito del plan
Este documento define la hoja de ruta oficial y el plan de implementación v0.1 del proyecto `proyecto_raiz_sdd_harness`. Actúa como la fuente oficial de orden para guiar los pasos de desarrollo técnico, asegurando la coherencia entre las reglas de gobernanza documental, los límites de la constitución del proyecto y el desarrollo progresivo del arnés agéntico bajo el enfoque de Spec-Driven Development (SDD), priorizando el cierre de la etapa documental sobre la implementación técnica.

## 2. Estado actual del repositorio
A la fecha actual de este plan, el repositorio se encuentra en la **Fase Documental / MVP Estructural**.
* **Elementos creados y vigentes:**
  - Gobernanza y mapa documental: `docs/00_mapa_y_gobernanza_documental.md`
  - Metodología base común: `docs/01_metodologia_base_comun.md`
  - Metodología específica de desarrollo de software: `docs/02_metodologia_desarrollo_software_sdd_harness.md`
  - Marco normativo: `docs/constitucion_del_proyecto.md`
  - Guía de arranque: `docs/procedimiento_inicio_proyecto_sdd_harness.md`
  - Registro de progreso: `progress/current.md` y `progress/history.md`
  - Estructura conceptual no activa de agentes en `.agent/` (workflows, skills y rules).
* **Ausencias operativas:** No existe código de producto ejecutable, scripts de gates automáticos, specs de features piloto activas ni automatizaciones de agentes habilitadas.

## 3. Alcance cerrado del MVP actual
El alcance del Producto Mínimo Viable (MVP) v0.1 está estrictamente restringido al **desarrollo técnico asistido por IA**:
* Diseño y despliegue del flujo de desarrollo de software utilizando **Spec-Driven Development (SDD) + Harness agéntico**.
* Soporte principal enfocado en **Python** (entornos de ejecución con `uv`, scripts locales y validaciones).
* Creación de herramientas deterministas locales: scripts de automatización, APIs internas, herramientas de línea de comandos (CLI), validadores estructurales y de contenido.
* Definición e implementación de Gates (documentales, manuales y automatizados mediante suites de tests).
* Pruebas de integración de software y smoke tests deterministas.

## 4. Fuera de alcance del MVP actual
Se excluyen explícitamente de esta versión los siguientes elementos:
* Planes de negocio, análisis comerciales, estudios de mercado y proyecciones financieras.
* Proyectos puramente documentales a largo plazo o de carácter general.
* Sistemas editoriales de redacción de contenido, workflows de copy o automatizaciones de marketing.
* Procesamiento masivo de texto, bots de conversación y sistemas agénticos cuyo producto final o propuesta de valor principal sea únicamente la generación de prosa o texto estructurado no técnico.

## 5. Rol del Equipo Auditor Procedimental
El **Equipo Auditor Procedimental** es un rol metodológico clave del arnés encargado de:
* Auditar la calidad, consistencia y trazabilidad del producto metodológico, las guías procedimentales y la documentación del proyecto.
* Asegurar que todo cambio o avance cumpla de forma rigurosa con los principios del mapa documental y la constitución del proyecto.
* Validar que la información técnica sea útil, comprensible y accionable tanto para el desarrollador humano como para la integración con sistemas asistidos por IA.
* Auditar el rastro de trazabilidad del repositorio (Git status, diferencias de diff, checklists firmados) antes de aprobar una transición de fase o declarar una feature como completada (`done`).
* Reportar de forma objetiva las desviaciones técnicas o procedimentales para activar la regla de replanificación cuando sea necesario.
* *Nota:* Este rol no actúa como auditor técnico de la lógica del runtime o de los gates ejecutables automatizados, sino como salvaguarda del cumplimiento de la metodología y la calidad del entregable final.

## 6. Ajustes procedimentales aprobados
Para garantizar la calidad en el desarrollo híbrido (IA + determinismo), se implementan los siguientes ajustes operativos:
* **Flujo Fuente → Análisis → Decisión:** Toda propuesta o requerimiento debe identificar de manera explícita su fuente de origen (Usuario, QA, Seguridad, Arquitectura), realizar un análisis de alternativas técnicas sin improvisar, y culminar en una decisión formal justificada (como un ADR en `docs/adr/`).
* **Responsable del flujo procedimental:** El rol líder (Orquestador) se responsabiliza de asegurar el cumplimiento paso a paso de cada fase metodológica del ciclo SDD.
* **Checklist de preparación antes de avanzar:** Se requiere la verificación obligatoria del preflight estructural (`docs/preflight_estructural.md`) y la confirmación de limpieza del workspace antes de admitir cambios o crear nuevos archivos en el repositorio.
* **Memoria externa del proceso:** Se utiliza la carpeta `progress/` (en particular `current.md` y `history.md`) como el cuaderno de bitácora oficial que preserva el estado del repositorio de manera persistente, evitando depender del historial de la sesión del chat.
* **Ciclo de mejora continua controlado:** Las ineficiencias o bugs de diseño detectados se corrigen mediante un bucle cerrado de retroalimentación donde se actualizan de forma ordenada las guías metodológicas o de estilo de código, sin introducir cambios ad-hoc sobre el código bajo prueba.
* **Control Input/Output:** Cada proceso o script de validación técnica debe declarar con precisión sus datos de entrada esperados y los artefactos de salida (evidencias, reportes, logs estructurados) que se registrarán en sedes aprobadas de evidencia, como progress/, reportes de validación o una futura zona de outputs cuando sea definida formalmente.

## 7. Orquestador como rol procedimental
* El Orquestador se define en esta fase únicamente como un **rol procedimental y lógico** dentro del flujo metodológico.
* No existe como agente de IA activo, script ejecutable o demonio en ejecución en background.
* Las actividades asociadas a la orquestación (vigilar transiciones, guiar el orden de ejecución) serán ejecutadas de forma asistida por el desarrollador humano y por los agentes en sus sesiones activas de desarrollo.

## 8. Self-improving loop como mejora continua controlada
* El bucle de auto-mejora (*self-improving loop*) del arnés se limita exclusivamente a la **mejora continua controlada de procesos y reglas**.
* Está estrictamente prohibido que la inteligencia artificial se auto-modifique de manera libre o autónoma (ej. alterar su propia constitución, reescribir reglas locales críticas o reconfigurar adaptadores de seguridad sin aprobación).
* Cualquier ajuste en los adaptadores operativos (`AGENTS.md`, `GEMINI.md`) o reglas locales de comportamiento debe ser propuesto por la IA, validado mediante auditoría y aprobado explícitamente por el programador humano.

## 9. Orden actualizado de ejecución
De acuerdo con el enfoque LEAN de consolidación por capas de valor, el desarrollo técnico del arnés se llevará a cabo bajo el siguiente orden:

1. **Fase 0: Consolidación documental (MVP Estructural) — [EN CURSO]**
   - Ajustar y refinar el procedimiento operativo de inicio de proyectos derivados. — [COMPLETADO]
   - Crear el origen del proyecto raíz (`progress/fase_00_origen_del_proyecto_raiz.md`). — [COMPLETADO]
   - Crear la visión y alcance oficial del repositorio raíz (`docs/vision_y_alcance_del_proyecto_raiz.md`). — [COMPLETADO]
   - Realizar la auditoría arquitectónica interna inicial del repositorio (`progress/auditoria_arquitectonica_interna_2026-06-07.md`). — [COMPLETADO]
   - Definir la política de zonas de trabajo y restricción del espacio de archivos. — [COMPLETADO]
   - Ajustar el `README.md` principal con la arquitectura resultante. — [COMPLETADO]
   - Crear la lista oficial de características del arnés (*feature list*). — [COMPLETADO]
   - Auditoría final de cierre de la Fase 0. — [CREADA / EN REVISIÓN]
2. **Fase 1: Spec Piloto Documental — [PENDIENTE]**
   - Crear la especificación funcional y técnica para la primera característica piloto en `specs/`, en estado puramente documental y aprobado por el humano.
3. **Fase 2: Preparación del entorno de pruebas deterministas locales — [FASE POSTERIOR NO ACTIVA]**
   - Configuración de la infraestructura técnica (inicialización virtual con Python y `uv`).
   - Configuración del marco de testing determinista (`pytest`).
4. **Fase 3: Diseño e implementación de la validación automatizada — [FASE POSTERIOR NO ACTIVA]**
   - Desarrollo del script `scripts/gate_0_preflight.py` para la revisión estática de dependencias, entornos y archivos prohibidos.
5. **Fase 4: Codificación candidata de la feature piloto — [FASE POSTERIOR NO ACTIVA]**
6. **Fase 5: Validación cruzada y ejecución de gates de código — [FASE POSTERIOR NO ACTIVA]**

## 10. Qué está completado
* Constitución del proyecto raíz aprobada.
* Mapa de gobernanza y subordinación documental establecido.
* Metodología base común y metodología de desarrollo de software definidas.
* Procedimiento operativo oficial para el inicio de proyectos derivados documentado y ajustado con controles procedimentales.
* Registro del origen del proyecto raíz (`progress/fase_00_origen_del_proyecto_raiz.md`) creado.
* Visión y alcance del repositorio raíz (`docs/vision_y_alcance_del_proyecto_raiz.md`) definidos y consolidados en Git.
* Auditoría arquitectónica interna del repositorio registrada (`progress/auditoria_arquitectonica_interna_2026-06-07.md`).
* Sedes documentales del arnés organizadas (`specs/`, `progress/`, `scripts/`, `tests/`, `docs/adr/`).
* Estructura agéntica conceptual mínima y no activa en `.agent/` (workflows, skills y reglas locales iniciales).
* Política de zonas de trabajo y restricción del espacio de archivos definida.
* `README.md` principal ajustado.
* Lista de características (`feature_list.md`) creada.

## 11. Qué está pendiente
* **Pendientes inmediatos (Fase 0 - Documental/Procedimental):**
  - Revisión y aprobación formal (commit) de la auditoría final de cierre de la Fase 0.
* **Pendientes de fases técnicas posteriores (Inactivos en este momento):**
  - Configuración del entorno de pruebas unitarias locales en `tests/`.
  - Programación del script determinista `scripts/gate_0_preflight.py`.
  - Diseños de plantillas de especificaciones en `specs/`.

## 12. Qué queda bloqueado por ahora
* La ejecución o despliegue automático de agentes en entornos de producción.
* La creación de automatizaciones en background que modifiquen el código de proyectos derivados sin control humano.
* El desarrollo de cualquier módulo del arnés no alineado con el alcance cerrado del MVP v0.1 (ej. motores de generación de texto o analítica comercial).
* La creación de la carpeta `.agent/gates/`, la inicialización del entorno técnico de testing y la creación de scripts ejecutables de automatización hasta que la consolidación documental de la Fase 0 esté plenamente finalizada y aprobada por el auditor humano.

## 13. Restricciones de ejecución
* No se modificará la constitución ni el mapa de gobernanza sin una revisión formal previa y un registro explícito en el ADR del proyecto.
* Se prohíbe el uso de librerías globales de Python; todo script técnico futuro debe ejecutarse bajo el entorno virtual de `uv` (`uv run ...`).
* No se incorporarán credenciales, API keys ni secretos en texto plano en ningún archivo del repositorio.
* Las respuestas de APIs y stubs utilizadas para tests de integración no deben ser simuladas o "maquilladas" por el razonamiento del agente si los servicios reales fallan.

## 14. Criterios de aceptación por fase
* **Para avanzar de Fase Documental (Fase 0) a Spec Piloto (Fase 1):** Cierre y aprobación de todos los documentos requeridos de la Fase 0 (procedimiento de inicio, origen, visión, auditoría arquitectónica, política de zonas, README, feature list y auditoría final de cierre de Fase 0).
* **Para avanzar a Entorno de Pruebas (Fase 2):** Aprobación y firma de la Spec Piloto por parte del desarrollador humano.
* **Para avanzar a Script de Validaciones (Fase 3):** Configuración exitosa del entorno virtual con `uv` y `pytest`.
* **Para avanzar a Codificación (Fase 4):** Script `gate_0_preflight.py` funcional y reportando sin falsos positivos.
* **Para avanzar a Cierre y Consolidación (Fase 5):** Pruebas unitarias al 100% de éxito, validación por revisión cruzada y reporte de evidencias del arnés documentado sin fallos.
