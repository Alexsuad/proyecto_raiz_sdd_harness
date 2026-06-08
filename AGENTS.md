# File: AGENTS.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Servir como adaptador operativo mínimo para Codex y agentes de IA.
# Rol: Instrucciones y restricciones de primer nivel para la interacción agéntica.
# ──────────────────────────────────────────────────────────────────────

# AGENTS.md — Adaptador operativo para agentes

## 1. Propósito

Este documento proporciona las instrucciones operativas mínimas y de primer nivel dirigidas a Codex, asistentes virtuales y agentes de inteligencia artificial compatibles. Su objetivo es asegurar que toda intervención agéntica en el espacio de trabajo respete la estructura, jerarquía y estándares de calidad definidos en la documentación oficial del repositorio.

## 2. Fuente de verdad

La fuente de verdad definitiva del proyecto raíz reside de forma exclusiva en los documentos aprobados y consolidados de la carpeta de documentación:
- [docs/00_mapa_y_gobernanza_documental.md](./docs/00_mapa_y_gobernanza_documental.md)
- [docs/constitucion_del_proyecto.md](./docs/constitucion_del_proyecto.md)
- [docs/01_metodologia_base_comun.md](./docs/01_metodologia_base_comun.md)
- [docs/02_metodologia_desarrollo_software_sdd_harness.md](./docs/02_metodologia_desarrollo_software_sdd_harness.md)

Este archivo (`AGENTS.md`) actúa únicamente como un adaptador operativo y de contexto; no sustituye, no reemplaza y no puede contradecir a los documentos base de gobernanza citados.

## 3. Orden obligatorio antes de trabajar

Antes de proponer o ejecutar cualquier modificación en el repositorio, todo agente debe seguir estrictamente este orden de validación conceptual:
1. **Analizar la tarea:** Leer detenidamente la solicitud del usuario para entender su propósito conceptual.
2. **Identificar límites:** Distinguir con precisión qué archivos y carpetas están expresamente permitidos y cuáles están prohibidos para la tarea en curso.
3. **Revisar referencias:** Consultar los documentos metodológicos o de gobernanza relevantes antes de operar.
4. **Categorizar la intervención:** Determinar si la tarea es de naturaleza documental, metodológica, de diseño del arnés, especificación de feature (`specs/`), escritura de código o validación técnica.
5. **Detenerse ante ambigüedad:** No proceder con ninguna modificación si el alcance, requerimiento o límites asignados resultan ambiguos o poco claros. En tal caso, solicitar aclaraciones al desarrollador humano.

## 4. Reglas operativas básicas

El comportamiento del agente dentro del entorno de desarrollo debe ajustarse a las siguientes reglas operativas:
- **Respetar el alcance:** Trabajar única y exclusivamente dentro del alcance de archivos y tareas explícitamente autorizadas por el usuario.
- **No creación arbitraria:** Abstenerse de crear directorios o archivos adicionales que no hayan sido expresamente solicitados.
- **Resguardo documental:** No modificar bajo ninguna circunstancia los documentos metodológicos de la carpeta `docs/` sin una instrucción directa y explícita para ello.
- **No redundancia:** No duplicar las reglas de la constitución en este ni en otros adaptadores operativos locales.
- **No improvisar ni inventar:** No inventar rutas, archivos, funciones, dependencias, decisiones de diseño, estados de avance ni comandos del sistema.
- **Evidencia obligatoria:** No reportar ni marcar una tarea como completada o definitiva sin haber obtenido y documentado evidencia técnica verificable y reproducible.
- **Trazabilidad de bloqueos:** Detenerse y reportar de forma prioritaria cualquier bloqueo, duda razonable, conflicto de arquitectura o riesgo funcional detectado.
- **Política de Commits:** No realizar commits ni pushes individuales por cada microfase local; consolidar el trabajo en un único commit/push al cierre de cada fase o bloque funcional real tras revisión humana.
- **Revisión Documental de Cierre:** Al finalizar cada fase, es obligatorio leer y actualizar la documentación rectora y de estado (`README.md`, `AGENTS.md`, `GEMINI.md`, `progress/` y utilidades) para evitar información desactualizada en el repositorio.

## 5. Estado actual del arnés

El proyecto se encuentra en una etapa de Producto Mínimo Viable (MVP). La Fase 3 ha sido implementada y publicada.
- **Verificación Estructural Activa:** El arnés ya cuenta con una verificación mínima preflight automatizada que se ejecuta localmente mediante `.venv/bin/python scripts/gate_0_preflight.py` (o con `GATE_PREFLIGHT_MAINTENANCE=1` si se requiere modificar dicho script).
- **Herramientas Bloqueadas:** No se permite activar, instalar o utilizar `pytest`, `uv`, GitHub Actions ni automatizaciones de `.agent/` sin autorización y firma humana explícitas.
- **Restricción de modificación de código:** Debido a que las plantillas de especificaciones, adaptadores de sistema y skills de soporte aún no se encuentran operativos en proyectos derivados, los agentes no deben modificar bajo ningún concepto código real de dichos proyectos.

## 6. Revisión y cierre

Al concluir cualquier tarea, el agente debe presentar un reporte final obligatorio estructurado con los siguientes elementos:
- **Archivos creados o modificados:** Rutas de los archivos intervenidos.
- **Resumen de cambios:** Descripción conceptual de las modificaciones aplicadas.
- **Validaciones realizadas:** Evidencia, revisiones, diff, checklist o comandos ejecutados, según aplique.
- **Riesgos o dudas:** Riesgos potenciales o consideraciones a tener en cuenta.
- **Confirmación de archivos no tocados:** Declaración de que no se afectó ningún recurso fuera del alcance.
- **Estado final:** Declaración explícita del estado de la tarea (`completado` o `bloqueado`).

## 7. Instrucciones para futuras fases

A medida que el proyecto avance y se habiliten las plantillas de `specs/`, la estructura agéntica ejecutable (`.agent/skills/`, `.agent/workflows/`), los scripts locales de gates (`scripts/`) o los tableros de control (`progress/`), este archivo adaptador operativo deberá actualizarse.
- **Directriz de actualización:** Toda futura referencia a estos nuevos elementos técnicos y operativos deberá realizarse mediante enlaces relativos directos, evitando la duplicación del contenido o reglas metodológicas en este documento.
