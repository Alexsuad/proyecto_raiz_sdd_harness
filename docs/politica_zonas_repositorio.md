# File: docs/politica_zonas_repositorio.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la política oficial de zonas físicas, clasificación y ciclo de vida del repositorio.
# Rol: Documento de política operativa subordinado al mapa de gobernanza y la constitución del proyecto.
# ──────────────────────────────────────────────────────────────────────

# Política de Zonas del Repositorio

**Versión:** v0.1  
**Estado:** Aprobado dentro del cierre de Fase 0 documental  
**Tipo:** Política operativa documental  
**Ubicación:** `docs/politica_zonas_repositorio.md`

---

## 1. Propósito del documento
Esta política define la utilización de las zonas físicas del repositorio `proyecto_raiz_sdd_harness` y establece las directrices que rigen el ciclo de vida de todos los archivos y carpetas del proyecto. Su aplicación tiene como fin evitar el crecimiento desordenado del repositorio, prevenir la duplicación redundante de contenido, impedir la contaminación del núcleo (*core*) con archivos privados y evitar la activación involuntaria o prematura de artefactos agénticos planificados para fases técnicas futuras.

---

## 2. Principio rector de zonas
Todo control, revisión o reorganización del repositorio debe ceñirse estrictamente a la siguiente pauta obligatoria:

> **Regla de no improvisación en el ordenamiento:**
> No se limpia, mueve, borra ni reorganiza la topología del repositorio guiándose por palabras clave, temas arbitrarios o intuiciones de desarrollo de la IA. Cualquier intervención sobre archivos debe clasificarse estrictamente por su zona designada, ciclo de vida aplicable, evidencia técnica contrastada, estado del artefacto y contar con aprobación humana explícita previa.

---

## 3. Estados posibles de un artefacto
Para gobernar el ciclo de desarrollo, cada archivo del sistema debe encajar en una de las siguientes clasificaciones de estado:
* **Activo:** Documento o recurso que rige de manera efectiva la operación del arnés actual o el flujo inmediato autorizado.
* **Candidato:** Borrador, propuesta técnica u hoja de ruta en revisión que carece de definitividad hasta que sea firmado por el desarrollador humano.
* **Futuro / Inactivo:** Estructuras, scripts o specs previstos para etapas posteriores y cuyo runtime o ejecución lógica está bloqueado en esta fase.
* **Referencia:** Documento complementario o históricos que sirven como base conceptual.
* **Privado / Local:** Archivo utilitario personal utilizado en la máquina del programador humano.
* **Excluido:** Recursos de configuración o entorno que no deben ser seguidos ni indexados bajo el control de versiones.
* **Legacy:** Artefactos obsoletos que se mantienen deshabilitados de la jerarquía activa por motivos históricos o de trazabilidad.

---

## 4. Zonas oficiales del repositorio
La estructura del arnés se compone de las siguientes carpetas físicas delimitadas:
* **Raíz del repositorio:** Aloja exclusivamente archivos de compatibilidad y adaptadores indispensables (`AGENTS.md`, `GEMINI.md`, `README.md`, `.gitignore`, `.gitattributes`).
* **`/docs`**: Sede de documentos de gobernanza, metodologías comunes, políticas y especificaciones normativas.
* **`/docs/adr/`**: Sede de decisiones arquitectónicas numeradas e históricas.
* **`/progress`**: Carpeta destinada a la memoria externa del avance y al control vivo del repositorio.
* **`/.agent/`**: Estructura de diseño conceptual y no activo para workflows, reglas locales y skills de soporte.
* **`/specs`**: Zona futura para especificaciones por feature.
* **`/scripts`**: Zona parcialmente activa para scripts deterministas del arnés. Solo `scripts/gate_0_preflight.py` está activo. Los demás scripts y gates siguen bloqueados.
* **`/tests`**: Zona futura para el marco de testing y tests del arnés.
* **Futuras zonas de output/evidencia:** Espacio lógico para reportes automáticos y evidencias físicas (ej. `/output`), inactivo hasta su aprobación formal en fases posteriores.
* **Archivos privados/locales excluidos:** Ficheros no versionados que viven de manera aislada en el working tree local de la máquina.

---

## 5. Política específica para `docs/`
* **Función:** Contiene únicamente documentos de carácter normativo, directrices metodológicas, actas constitucionales, procedimientos operativos estandarizados y políticas de gobernanza.
* **Restricción:** No debe utilizarse para almacenar archivos privados locales, configuraciones personales, secretos, claves ni salidas o volcados de datos generados temporalmente durante la codificación.

---

## 6. Política específica para `progress/`
* **Función:** Sistema vivo de control del arnés. Contiene el checklist vivo, el snapshot actual, el inventario de features y el historial mínimo no operativo.
* **Restricción:** No sustituye a la jerarquía de `/docs`. Las pautas metodológicas estables de desarrollo no deben ser definidas aquí; este espacio se limita a registrar el control operativo del proyecto.

---

## 7. Política específica para `.agent/`
* **Función:** Durante la Fase Documental del MVP, la carpeta `.agent/` y todos sus subdirectorios (`workflows/`, `skills/`, `rules/`) se definen de manera estricta como **sedes conceptuales candidatas e inactivas**.
* **Restricción:** Su existencia no habilita ni autoriza bajo ningún concepto el uso de prompts automatizados, demonios en ejecución, automatización del IDE o inyección de reglas de procesamiento agéntico. Cualquier activación técnica posterior requerirá una especificación y aprobación explícita humana previa.

---

## 8. Política específica para `specs/`
* **Función:** Sede de especificaciones atómicas por característica técnica utilizando Spec-Driven Development.
* **Restricción:** Inactiva en la Fase 0. Queda estrictamente prohibido redactar specs de features reales del arnés o proyectos derivados hasta que la consolidación documental finalice y el plan de implementación lo autorice.

---

## 9. Política específica para `scripts/` y `tests/`
* **Función:** `scripts/` es una zona parcialmente activa. Actualmente solo `scripts/gate_0_preflight.py` está autorizado como gate mínimo local. `tests/` sigue reservado para pruebas futuras.
* **Restricción:** Bloqueado: nuevos scripts adicionales, nuevos gates, suites de tests, `uv`, `pytest`, workflows, CLI y runtime. Excepción autorizada: `scripts/gate_0_preflight.py`.

---

## 10. Política para archivos privados/locales (Alerta de Contención)
Tomando como caso de estudio el archivo local opcional privado docs/manual_anti_errores_del_arnes.md:
* **Directriz:** Al estar ignorado formalmente en Git (`.gitignore:9`), el sistema no lo rastrea, lo que previene inyecciones accidentales en el historial. Sin embargo, su presencia local expone el riesgo de filtraciones en empaquetados externos (ZIP).
* **Restricción:** El arnés prohíbe realizar intervenciones físicas (borrado, traslado o desactivación local) sobre este o cualquier archivo privado en esta etapa. Se registra este riesgo únicamente como una alerta de contención metodológica.

---

## 11. Política de exportación ZIP o paquetes compartibles
Cualquier proceso o script de exportación que se cree en el futuro para empaquetar el repositorio y compartir entregables debe excluir de forma mandatoria:
* Archivos explícitamente ignorados bajo el archivo `.gitignore` del proyecto.
* Archivos locales privados u hojas de notas no oficiales.
* Historiales de copias o archivos `.zip` anteriores que inflen de manera innecesaria el volumen del entregable.
* Variables de entorno, secretos, llaves criptográficas o archivos `.env`.
* Recursos obsoletos o copias temporales (`tmp/`, `sandbox/`).
* *Nota:* Esta política regula la lógica de exclusiones, pero no autoriza la codificación o creación de scripts de empaquetado en esta fase.

### Política de empaquetado ZIP

- Los ZIP internos de auditoría pueden incluir archivos privados solo si Alex lo autoriza explícitamente.
- Los ZIP públicos, compartibles o entregables deben excluir manuales privados, ZIPs previos, archivos temporales, outputs locales y cualquier archivo ignorado por Git.
- `docs/manual_anti_errores_del_arnes.md`, si existe localmente, no debe formar parte de entregables públicos ni paquetes compartibles.

---

## 12. Política de saneamiento futuro
Para evitar alteraciones descontroladas en el repositorio, se establecen los siguientes límites normativos para cualquier saneamiento físico futuro:
* **Detectar no es borrar:** Identificar un archivo redundante o fuera de lugar no faculta a su eliminación directa.
* **Clasificar no es mover:** Categorizar la naturaleza de un archivo no autoriza a modificar su ruta en el disco.
* **Recomendar no es ejecutar:** Detectar áreas de mejora en la arquitectura se registra como sugerencia de avance, sin intervención manual de la IA.
* **Procedimiento:** Cualquier limpieza, movimiento o baja física de archivos requiere de forma obligatoria un plan de acción independiente, un diff de revisión previa, aprobación explícita del programador humano y reporte final con evidencias.

---

## 13. Relación con el plan de implementación
Esta política se alinea con el control vivo de `progress/`. `scripts/` es una zona parcialmente activa; solo `scripts/gate_0_preflight.py` está autorizado y el resto de scripts, gates, suites de tests, `uv`, `pytest`, workflows, CLI y runtime técnico siguen bloqueados hasta autorización explícita.

---

## 14. Criterios de aceptación
* [ ] Se define de manera precisa la función específica de cada directorio y zona oficial.
* [ ] Se distinguen y aíslan las definiciones operativas de los estados *Activo*, *Candidato*, *Futuro* y *Privado/Local*.
* [ ] Se prohíbe explícitamente la ejecución de limpiezas o saneamientos físicos en base a intuición o palabras clave de la IA.
* [ ] Se documenta como caso de estudio el riesgo de exportación de archivos privados locales ignorados.
* [ ] No se autoriza ninguna acción física destructiva sobre el working tree.
* [ ] Se mantiene el bloqueo sobre la ejecución del runtime técnico.

---

## 15. Estado del documento
* **Estado:** Aprobado dentro del cierre de Fase 0 documental
