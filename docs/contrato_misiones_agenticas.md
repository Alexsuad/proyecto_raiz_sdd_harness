# File: docs/contrato_misiones_agenticas.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el contrato de entrada/salida para misiones agénticas del arnés.
# Rol: Especificación normativa del alcance y límites de las tareas delegadas.
# ──────────────────────────────────────────────────────────────────────

# Contrato de Misiones Agénticas

## 1. Propósito
Este contrato define la estructura obligatoria de entrada, salida, límites y condiciones de control que rigen la ejecución de cualquier tarea o misión delegada a un agente de Inteligencia Artificial (IA) en el repositorio `proyecto_raiz_sdd_harness`. Su fin es evitar la improvisación, el "vibe coding" y asegurar la trazabilidad.

## 2. Cuándo se usa
Este contrato es de obligado cumplimiento antes de iniciar cualquier misión de edición, planificación, diseño, desarrollo de software o validación en el espacio de trabajo. Todo agente debe verificar que cuenta con una definición de misión alineada con este esquema antes de operar.

## 3. Entrada obligatoria de una misión
Toda misión agéntica debe recibir estructuradamente los siguientes parámetros de entrada:
* **nombre_mision**: Identificador único o descriptivo.
* **objetivo**: Qué meta concreta persigue la misión.
* **contexto**: Información de fondo relevante.
* **archivos_a_leer**: Rutas de archivos necesarias para consulta.
* **archivos_permitidos**: Rutas exactas que el agente está autorizado a modificar o crear.
* **archivos_prohibidos**: Rutas que bajo ningún concepto pueden alterarse.
* **acciones_permitidas**: Operaciones CLI o herramientas autorizadas.
* **acciones_prohibidas**: Acciones expresamente vetadas en la sesión.
* **validaciones_obligatorias**: Pruebas técnicas o de consistencia requeridas.
* **criterios_de_stop**: Eventos o fallos que exigen detener la ejecución inmediatamente.
* **reporte_esperado**: Formato y evidencias necesarias para declarar la entrega.

## 4. Salida obligatoria de una misión
Al concluir la misión, el agente debe presentar un reporte estructurado de salida con:
* **archivos_leidos**: Lista de archivos consultados.
* **archivos_modificados**: Rutas que sufrieron cambios (deben coincidir con el allowlist).
* **cambios_aplicados**: Resumen conceptual del trabajo realizado.
* **validaciones_ejecutadas**: Resultados exactos de las pruebas y verificaciones.
* **resultado**: Aprobado / Fallido / Bloqueado.
* **riesgos**: Dudas, deudas técnicas identificadas o posibles efectos colaterales.
* **pendientes**: Acciones necesarias que quedan fuera del alcance actual.
* **estado_final**: Estado operativo de la tarea (`completado`, `bloqueado`, etc.).

## 5. Archivos permitidos
El agente solo puede modificar y crear los archivos declarados expresamente en la entrada `archivos_permitidos`. Tocar cualquier archivo fuera de este allowlist se considera una violación crítica de la gobernanza del arnés.

## 6. Archivos prohibidos
Por defecto, todo archivo del repositorio que no esté listado en `archivos_permitidos` se considera prohibido. Está estrictamente prohibido alterar la configuración base, exclusiones de Git, scripts de gates autorizados y documentos maestros sin una instrucción específica en la entrada.

## 7. Acciones prohibidas
Bajo ninguna circunstancia la misión agéntica autoriza:
* Ejecutar `git add -A` o `git add .` (se exige uso selectivo y atómico de archivos).
* Realizar commits sin el visto bueno y la confirmación explícita del flujo del arnés.
* Hacer push al repositorio remoto sin aprobación previa.
* Crear archivos o carpetas no autorizados en el alcance.
* Activar runtime, plugins, triggers o configuraciones en `.agent/`.
* Crear nuevas skills, agentes, workflows, CLI o scripts ejecutables no programados.
* Utilizar herramientas no autorizadas en esta fase (como `uv` o `pytest`).

## 8. Condiciones de STOP
El agente debe detenerse inmediatamente y reportar el estado al desarrollador humano ante:
* Detección de un árbol de trabajo Git sucio o con modificaciones no esperadas antes de iniciar.
* Fallo en cualquier gate de preflight o verificación determinista.
* Necesidad de alterar un archivo que no figura en el listado de permitidos.
* Ambigüedad o contradicción grave en los requisitos o directrices documentales.
* Riesgo evidente de pérdida de datos o sobrescritura de contenido útil preexistente.

## 9. Validaciones obligatorias
Toda misión debe certificar la ejecución de las siguientes comprobaciones al finalizar:
* Estado de Git mediante `git status --short`.
* Estadísticas del cambio mediante `git diff --stat`.
* Contenido exacto del cambio usando `git diff --unified=0` sobre los archivos modificados.
* Ejecución del preflight local mediante `.venv/bin/python scripts/gate_0_preflight.py` (cuando aplique).

## 10. Evidencia mínima requerida
La evidencia provista por el agente debe ser proporcional al cambio:
* Para cambios menores: Fragmentos del diff y capturas de consola del preflight.
* Para cambios mayores: Historial completo de comandos y salidas de las validaciones.
Se debe evitar adjuntar listados de código o diffs completos innecesariamente largos que saturen el contexto.

## 11. Criterios de aprobación humana
La aprobación final del entregable candidato siempre requerirá el dictamen independiente de un desarrollador humano. Ningún agente puede autoaprobar sus cambios para darlos por consolidados de forma definitiva en la rama principal.

## 12. Relación con `improve_plan`
La futura capacidad `improve_plan` se conceptualiza como la herramienta automatizada para generar planes y contratos de misiones estructurados, asegurando que cada misión posterior cuente con parámetros de entrada limpios y alineados con este contrato.

## 13. Relación con `ponytail_review`
La capacidad `ponytail_review` actuará como un filtro auditor integrado en las validaciones de salida del contrato, evaluando sistemáticamente que la solución propuesta mantenga el estándar de simplicidad y no introduzca sobreingeniería.

## 14. Relación con agentes, subagentes y workflows futuros
Este contrato define la interfaz lógica que guiará el diseño de los agentes y subagentes de la Fase 4. Los workflows representarán la secuencia de pasos por los cuales se transmite y valida este contrato entre los diferentes roles.

## 15. Qué no autoriza este contrato
Este contrato establece el marco de diseño conceptual y documental. No autoriza la implementación de código ejecutable, la activación de runtime técnico agéntico, ni el uso de herramientas bloqueadas.
