# Manual anti-errores del arnés

Este documento reúne las directrices operativas y lecciones aprendidas aplicables al desarrollo y mantenimiento del proyecto `proyecto_raiz_sdd_harness`. Funciona como una guía de control para evitar la repetición de errores del pasado, adaptando el material de referencia a la fase actual y definiendo el comportamiento esperado de desarrolladores y agentes de inteligencia artificial.

---

## 1. Propósito

El propósito de este manual es establecer directrices operativas claras para mitigar errores de diseño, comunicación, trazabilidad y control en el repositorio. Actúa como un marco preventivo para que las lecciones extraídas de fallos anteriores se conviertan en salvaguardas explícitas del sistema.

Este manual está optimizado específicamente para el estado actual del arnés: **Fase documental / MVP estructural**.

---

## 2. Relación con la constitución y el mapa documental

Este documento no es un marco normativo independiente ni una constitución paralela. Su relación con el sistema documental es de estricta subordinación:
*   **Subordinación jerárquica:** Se subordina de forma directa a la [Constitución del proyecto](./constitucion_del_proyecto.md) y al [Mapa y gobernanza documental](./00_mapa_y_gobernanza_documental.md).
*   **No duplicación:** No duplica ni redefine las reglas establecidas en los documentos rectores anteriores. En su lugar, las complementa proporcionando un enfoque pragmático y de prevención de errores operativos.
*   **No reemplazo de controles existentes:** Este manual no sustituye el `preflight_estructural.md`, la definición documental de `gate_0_preflight` ni los futuros gates del arnés. Su función es orientar la prevención de errores, no reemplazar los controles formales.
*   **Restricción de la fase actual:** Se establece explícitamente que este manual **no autoriza** la creación de scripts de automatización, carpetas de control activo (`.agent/gates/`), reglas activas (`.agent/rules/`), workflows activos (`.agent/workflows/`) ni skills activas (`.agent/skills/`). Todo el contenido operativo de este documento sirve de guía conceptual y metodológica para el trabajo actual y la planificación de futuras fases.

---

## 3. Errores que este arnés debe evitar

A partir de la experiencia en el desarrollo de la arquitectura agéntica, se han clasificado y priorizado los siguientes errores clave a evitar en este repositorio:

### A. Pérdida de requisitos en cascada `[CRÍTICO]`
*   **Definición:** El requisito inicial o el input base del usuario se diluye, malinterpreta o desaparece a medida que se avanza en las fases de análisis o redacción de especificaciones.
*   **Prevención:** Se debe realizar una auditoría cruzada sistemática que verifique que el contenido de salida mapea exactamente con las solicitudes de entrada.

### B. Declarar éxito sin prueba o validación real `[CRÍTICO]`
*   **Definición:** El agente de desarrollo declara finalizada una tarea basándose en criterios literarios o asunciones, sin presentar una evidencia objetiva o verificación de que el cambio funciona en el entorno real.
*   **Prevención:** Todo cambio debe acompañarse de una validación explícita (como un diff de Git, comprobación de estado o ejecución de comandos deterministas).

### C. Mezcla de capas conceptuales y técnicas `[IMPORTANTE]`
*   **Definición:** Crossover de responsabilidades donde las tareas de redacción, la infraestructura técnica, la lógica de negocio, la UI o el control de calidad se acoplan en un único bloque o archivo.
*   **Prevención:** Mantener la separación de responsabilidades y modularidad documental y técnica en el repositorio según el Mapa Documental.

### D. Redacción con identidad equivocada o colonización táctica `[CRÍTICO]`
*   **Definición:** El sistema de IA confunde la identidad del proyecto raíz (que es un arnés metodológico y agéntico) con casos tácticos, ejemplos de uso particular o identidades de proyectos derivados, permitiendo que un ejemplo "colonice" el contenido general.
*   **Prevención:** Mantener límites claros de sede documental. Los ejemplos y casos tácticos solo deben vivir en sus secciones de casos de uso o anexos, sin filtrarse a los documentos metodológicos principales como reglas universales.

### E. Memoria externa o contexto contaminado `[CRÍTICO]`
*   **Definición:** Utilización de resúmenes, contextos de ejecución o memorias de chat que arrastran de forma implícita datos obsoletos, sectores de negocio anteriores o nombres que no corresponden al proyecto actual.
*   **Prevención:** Limpiar el contexto operativo de la IA y asegurar que solo consuma el marco estructurado de este repositorio.

### F. Gates que reportan fallos pero no bloquean el flujo `[CRÍTICO]`
*   **Definición:** Herramientas, linters o scripts de validación futura que reportan un estado `FAIL` en su salida de texto pero devuelven un código de salida exitoso (`EXIT 0`), engañando al flujo automatizado.
*   **Prevención:** Asegurar que todo script o validador detenga el flujo y devuelva un código de error real (`EXIT > 0`) ante cualquier fallo.

### G. Dependencia de rutas locales no portables `[IMPORTANTE]`
*   **Definición:** Inclusión de rutas absolutas locales a la máquina de desarrollo (ej. `C:/Users/nombre/...` o `/home/usuario/...`) en documentos activos del repositorio, rompiendo la portabilidad.
*   **Prevención:** Usar exclusivamente rutas relativas locales para referencias cruzadas dentro de la estructura del proyecto.

---

## 4. Reglas anti-error aplicables en la fase documental actual

Durante la fase documental y de MVP estructural, se aplican de forma obligatoria las siguientes pautas manuales:

1.  **El reporte del agente no sustituye el diff:** La autoevaluación o reporte que escribe el agente sobre su propio éxito es solo una referencia preliminar. El revisor humano debe auditar siempre la evidencia cruda: el diff real de Git (`git diff`) y el estado actual del repositorio (`git status`).
2.  **Diferenciar evidencia histórica de documento activo:** Los documentos históricos (como un log de ejecución, actas de decisión del chat o reportes de ejecución con fecha fija) pueden retener detalles contextuales y rutas locales propias de la ejecución. Por el contrario, los documentos activos y normativos (como especificaciones, metodologías o este manual) deben estar totalmente limpios de acoplamiento local y usar enlaces relativos portables.
3.  **No degradar contenido para pasar auditorías automáticas:** Está prohibido simplificar conceptos, omitir especificaciones clave o debilitar reglas de negocio o metodológicas con el único fin de evitar falsos positivos o superar restricciones sintácticas de linters o scripts validadores automáticos.
4.  **No crear agentes, skills, rules o gates activos:** En la fase de MVP estructural no se permite la creación de automatizaciones operativas. Las carpetas `.agent/rules/`, `.agent/workflows/` y `.agent/skills/` permanecen únicamente como sedes documentales futuras inactivas.
5.  **Evitar el "vibe coding" documental:** Toda modificación en los documentos debe responder a un objetivo específico alineado con el avance del arnés, evitando cambios cosméticos o modificaciones impulsivas sobre metodologías consolidadas.

---

## 5. Reglas anti-error para futuras automatizaciones

Cuando el proyecto avance hacia fases operativas y de automatización técnica, se deberán implementar los siguientes criterios de control:

1.  **Política primero, código después:** Ninguna automatización, linter o gate basado en scripts (como un futuro `scripts/gate_0_preflight.py`) podrá programarse sin que exista previamente una política o regla documental formalmente especificada y aprobada en la gobernanza. El código es solo el brazo ejecutable de la política.
2.  **Toda automatización debe nacer de una regla documentada:** Se prohíbe introducir scripts deterministas independientes que controlen la calidad del repositorio sin estar explícitamente justificados en el manual operativo y el mapa de gobernanza.
3.  **Bloqueo estricto de gates:** Los scripts validadores deben forzar la detención inmediata del pipeline ante fallos conceptuales o de sintaxis. El estado de la validación textual (`FAIL`) debe coincidir exactamente con el código de salida de error (`EXIT 1`).
4.  **Validar el pipeline antes de perfeccionarlo:** Es prioritario validar el funcionamiento del pipeline completo (de punta a punta o end-to-end) antes de optimizar los filtros específicos, prompts maestros o el rendimiento de sus componentes.

---

## 6. Deuda técnica o agéntica diferida

*   **Pauta de control:** Si durante una tarea de edición o revisión se detectan incoherencias secundarias, erratas menores o inconsistencias de formato en otros archivos del repositorio que estén fuera del alcance de la tarea autorizada, **se prohíbe corregirlos de forma impulsiva**.
*   **Acción requerida:** Estos hallazgos deben reportarse y registrarse formalmente como "deuda técnica o agéntica diferida" para su resolución en un bloque o tarea específicos. Esto protege la trazabilidad de los commits y evita mezclar naturalezas de cambios no relacionados en un mismo envío.
*   **Separación de commits por naturaleza de cambio:** Los commits deben ser atómicos y específicos. No se deben empaquetar cambios metodológicos, correcciones de rutas locales y registros de avance dentro de un mismo commit.

---

## 7. Criterios para convertir una lección en regla, gate, skill o workflow

No todas las lecciones aprendidas deben traducirse en el mismo tipo de componente. Se aplicarán las siguientes directrices de diseño:

*   **Regla (Rule):** Se creará cuando la restricción sea transversal, permanente y afecte a todo el sistema o al comportamiento general del agente (ej. "idioma de respuesta obligatorio", "no inventar rutas").
*   **Gate:** Se definirá cuando se requiera un punto de control bloqueante e infranqueable entre fases del ciclo de desarrollo (ej. "no avanzar a codificación sin spec aprobada").
*   **Skill:** Se diseñará cuando represente una capacidad técnica o cognitiva modular, acotada, reutilizable y repetible, que reciba unas entradas definidas y devuelva un formato de salida predecible (ej. "script para extraer enlaces locales").
*   **Workflow:** Se estructurará cuando se requiera coordinar una secuencia de pasos lógicos o interacciones complejas de orquestación multi-agente o humano-máquina.

El origen de cualquiera de estos componentes debe estar explícitamente trazado a una lección aprendida, un error documentado, una necesidad validada, una auditoría o una decisión registrada del proyecto.

---

## 8. Estado del documento

*   **Estado:** Aprobado para fase documental / MVP estructural.
*   **Uso:** Guía operativa anti-errores del arnés, subordinada a la Constitución del proyecto.
*   **Restricción operativa:** Documento puramente conceptual; no autoriza la creación de scripts, automatizaciones ni carpetas de control activo `.agent/gates/` durante la fase actual.
*   **Próxima revisión:** Programada al finalizar el MVP documental y antes de la primera prueba piloto del arnés.
