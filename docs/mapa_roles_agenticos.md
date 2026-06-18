# File: docs/mapa_roles_agenticos.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el mapa conceptual de roles agénticos del arnés.
# Rol: Especificación conceptual y delimitación de funciones de los agentes.
# ──────────────────────────────────────────────────────────────────────

# Mapa de Roles Agénticos

## 1. Propósito
Este documento define el mapa conceptual de roles agénticos del arnés `proyecto_raiz_sdd_harness`. Su objetivo es delimitar la responsabilidad de cada rol dentro del flujo de trabajo, previniendo la superposición de tareas, la improvisación y la autoaprobación de cambios técnicos relevantes.

## 2. Relación con el contrato de misiones agénticas
Toda misión agéntica estructurada según el [docs/contrato_misiones_agenticas.md](./contrato_misiones_agenticas.md) será asignada a un rol o conjunto de roles específicos. Los roles operan como los ejecutores o auditores de los parámetros de entrada y salida del contrato, respetando estrictamente sus allowlists y condiciones de parada.

## 3. Principios de diseño de roles
* **Conceptuales y reusables**: Los roles descritos son definiciones de comportamiento y responsabilidades lógicas; no corresponden todavía a implementaciones o agentes físicos activos.
* **Separación de responsabilidades**: Ningún rol puede autoauditarse ni aprobar de manera definitiva su propio trabajo candidato.
* **Independencia técnica**: Diseñados para ser agnósticos respecto al proveedor del modelo de lenguaje.

## 4. Rol humano director
* **Responsabilidad principal**: Actuar como máxima autoridad de control del proyecto y decisor de última palabra.
* **Qué puede hacer**: Aprobar especificaciones, definir objetivos, resolver ambigüedades, autorizar la creación de archivos nuevos, aprobar commits y pushes.
* **Qué no puede hacer**: Delegar de forma irreversible su firma de aprobación en un agente de IA.
* **Evidencia que entrega**: Aprobaciones explícitas en el chat o firmas manuales de checklists de progreso.

## 5. Agente orquestador
* **Responsabilidad principal**: Coordinar el flujo secuencial de la misión delegada y vigilar las condiciones de STOP.
* **Qué puede hacer**: Delegar sub-tareas a otros agentes y consolidar el reporte de salida del contrato de misiones.
* **Qué no puede hacer**: Modificar código de manera directa o aprobar entregables candidatos.
* **Evidencia que entrega**: Reporte final estructurado de la misión.

## 6. Agente planificador
* **Responsabilidad principal**: Traducir la necesidad humana en un contrato de misión estructurado y autocontenido.
* **Qué puede hacer**: Definir el objetivo, los archivos permitidos, los archivos prohibidos y las validaciones requeridas de la misión.
* **Qué no puede hacer**: Iniciar la implementación o edición de archivos sin aprobación.
* **Evidencia que entrega**: Contrato de misión candidato (alineado con `improve_plan`).

## 7. Agente implementador
* **Responsabilidad principal**: Aplicar modificaciones y generar código candidato o documentación dentro de los límites autorizados.
* **Qué puede hacer**: Modificar los archivos declarados estrictamente en el allowlist.
* **Qué no puede hacer**: Crear archivos no autorizados, ampliar la misión de forma unilateral o activar runtime.
* **Evidencia que entrega**: Diferencias atómicas (`git diff`) y bitácora de cambios.

## 8. Agente auditor documental
* **Responsabilidad principal**: Validar la consistencia, completitud y no duplicación del sistema documental.
* **Qué puede hacer**: Revisar READMEs, ficheros de progreso y guías metodológicas.
* **Qué no puede hacer**: Modificar código de software o gates deterministas.
* **Evidencia que entrega**: Reporte de consistencia documental.

## 9. Agente auditor técnico
* **Responsabilidad principal**: Asegurar el cumplimiento de los gates deterministas y el estado del repositorio.
* **Qué puede hacer**: Ejecutar preflights locales, analizar exclusiones y verificar la limpieza del árbol de Git.
* **Qué no puede hacer**: Modificar especificaciones de negocio o relajar validaciones.
* **Evidencia que entrega**: Logs de ejecución de scripts de validación.

## 10. Auditor de simplicidad / ponytail_review
* **Responsabilidad principal**: Evaluar la solución propuesta bajo los principios de diseño limpio y simplicidad LEAN.
* **Qué puede hacer**: Objetar la inyección de sobreingeniería, capas innecesarias o abstracciones prematuras.
* **Qué no puede hacer**: Codificar alternativas de negocio complejas.
* **Evidencia que entrega**: Dictamen de simplicidad (`ponytail_review` aprobado/bloqueado).

## 11. Documentador mínimo
* **Responsabilidad principal**: Registrar los hitos y mantener el sistema de control vivo actualizado.
* **Qué puede hacer**: Modificar `progress/` y actualizar los estados de las features/capacidades.
* **Qué no puede hacer**: Escribir especificaciones completas de negocio.
* **Evidencia que entrega**: Snapshot actualizado.

## 12. Subagentes permitidos en diseño futuro
Se conceptualizan subagentes para tareas micro-acotadas y de ciclo de vida efímero:
* **lector_de_logs**: Inspecciona logs específicos.
* **verificador_de_diffs**: Revisa líneas de cambio concretas.
* **revisor_consistencia_documental**: Compara dos archivos específicos para evitar duplicaciones.
* **analizador_de_alcance**: Evalúa si un archivo nuevo entra dentro de la política de zonas.
Queda bloqueada cualquier implementación física de estos subagentes.

## 13. Decisiones reservadas al humano
* Apertura o cierre formal de fases del proyecto.
* Creación física de archivos de runtime agéntico, CLI, workflows o skills.
* Autorización de comandos `git commit` y `git push` reales.
* Configuración de variables de entorno, claves de API o credenciales.
* Modificaciones normativas a la constitución y al mapa de gobernanza.

## 14. Evidencia mínima por rol
Cada rol debe registrar en su reporte la fecha, el rol ejecutor, la tarea analizada, el método de validación aplicado y el dictamen con observaciones técnicas explícitas.

## 15. Qué no autoriza este mapa
Este documento establece el marco conceptual y lógico de roles de la Fase 4. No autoriza la programación, codificación, inicialización de dependencias ni activación operativa de agentes, subagentes o runtime de automatización.
