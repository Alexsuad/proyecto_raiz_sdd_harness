# File: docs/vision_y_alcance_del_proyecto_raiz.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la visión general, objetivos de largo plazo y alcance del MVP v0.1 para el proyecto raíz.
# Rol: Documento rector de visión, límites y alcance estratégico.
# ──────────────────────────────────────────────────────────────────────

# Visión y Alcance del Proyecto Raíz

**Versión:** v0.1  
**Estado:** Aprobado dentro del cierre de Fase 0 documental  
**Tipo:** Documento rector de visión y estrategia  
**Ubicación:** `docs/vision_y_alcance_del_proyecto_raiz.md`

---

## 1. ¿Qué es el Proyecto Raíz?
El `proyecto_raiz_sdd_harness` es un **arnés (harness) metodológico y procedimental** diseñado para estructurar, auditar y controlar el desarrollo de software asistido por Inteligencia Artificial (IA) y agentes autónomos. 

No se concibe como una aplicación final de cara al usuario del negocio, sino como una infraestructura de reglas, pautas, bitácoras de seguimiento y validaciones deterministas que enmarca la operación de los asistentes agénticos (como Codex y Antigravity) dentro de un repositorio de código. Su finalidad es estandarizar la forma en que el software se especifica, se codifica, se prueba y se consolida, actuando como plantilla base para futuros proyectos derivados.

---

## 2. ¿Qué NO es el Proyecto Raíz?
Para evitar desviaciones de alcance, se definen explícitamente los límites de la naturaleza del arnés:
* **No es una aplicación de negocio:** No produce un software de venta, un sistema de gestión o un servicio de backend para consumidores finales.
* **No es un modelo de lenguaje (LLM):** No entrena ni refina pesos de redes neuronales, ni funciona como API de conversación.
* **No es un plugin cerrado del IDE:** No reemplaza la interfaz de desarrollo del editor de código, sino que convive en el workspace como un conjunto de directrices y scripts de control.
* **No es un motor de contenido:** No automatiza la redacción de prosa publicitaria, blogs de opinión, planes comerciales ni workflows editoriales.

---

## 3. ¿Para qué servirá?
El arnés agéntico cumple con las siguientes funciones estratégicas:
* **Garantizar la reproducibilidad:** Asegurar que cualquier desarrollador humano o agente de IA pueda incorporarse al repositorio y entender de forma inmediata el estado, las decisiones y las prioridades de desarrollo técnico.
* **Establecer control determinista:** Reemplazar la mera especulación conversacional por pruebas estáticas, linters, compilación y suites de tests que verifiquen mecánicamente la estabilidad del software.
* **Preservar el orden LEAN:** Minimizar la burocracia documental limitándola únicamente a la información estructurada que aporte valor directo y funcione como evidencia del cumplimiento del proceso de desarrollo.

---

## 4. ¿Quién lo usará?
* **Desarrolladores humanos (como Directores y Aprobadores):** Mantienen el control absoluto de la arquitectura del software. Resuelven las dudas e imprecisiones de los requisitos en la etapa de aclaraciones, validan los planes de diseño y firman las transiciones de estado críticas de las características (*features*).
* **Asistentes y Agentes de IA (como Ejecutores de Tareas):** Trabajan bajo un alcance predefinido, leen las especificaciones atómicas de `specs/`, proponen código candidato limpio de acuerdo a las directrices de estilo y reportan de forma objetiva los resultados de las validaciones en las sedes físicas aprobadas del repositorio.

---

## 5. ¿Qué problema resuelve?
El arnés combate directamente los vicios de desarrollo surgidos en la codificación interactiva con IA:
* **El "Vibe Coding" o Programación por Impulso:** Evita la inyección desordenada de código sin un diseño previo, un análisis de impacto y una secuencia atómica de tareas.
* **La Autoaprobación y el Maquillaje:** Impide que los agentes validen su propio trabajo técnico o disimulen fallos en pruebas simulando éxitos mediante su razonamiento interno.
* **La Pérdida de Contexto:** Elimina la dependencia de la memoria de las sesiones de conversación a través de bitácoras físicas de progreso (`progress/`) y actas de decisiones arquitectónicas (`docs/adr/`).
* **La Desviación de Arquitectura:** Bloquea la adición casual de librerías globales o la reestructuración arbitraria de bases de datos sin aprobación explícita humana.

---

## 6. Herramientas que soportará inicialmente
El MVP v0.1 reconoce como línea técnica prevista, para fases posteriores autorizadas, los siguientes componentes:
* **Python:** Lenguaje previsto para los futuros scripts, validadores y componentes técnicos del arnés, cuando el plan autorice pasar a fase de ejecución.
* **uv:** Administrador de dependencias y entornos virtuales de Python para garantizar un entorno aislado.
* **pytest:** Framework previsto para futuras pruebas unitarias y de integración locales cuando se autorice la fase técnica.
* **Git:** Sistema de control de versiones obligatorio para el seguimiento y la trazabilidad de los commits modulares.

---

## 7. Qué queda fuera de este MVP
* Integraciones activas con bases de datos en entornos de producción.
* Orquestación autónoma multi-agente en background sin supervisión humana en tiempo real.
* Automatizaciones para el despliegue continuo (CD) en entornos en la nube o pasarelas de pago.
* Plantillas de especificaciones documentales para flujos de trabajo de contenido no técnico.

---

## 8. Criterios para declarar listo el MVP Estructural (Fase 0)
Se considerará finalizada y aprobada la Fase 0 (Consolidación documental del MVP) al cumplir satisfactoriamente con:
* [ ] Cierre y confirmación (commit) de las guías procedimentales del repositorio raíz (Inicio de proyecto, Metodologías y Constitución).
* [ ] Aprobación de la Visión y Alcance del proyecto raíz.
* [ ] Auditoría arquitectónica del repositorio inicial realizada de forma exitosa.
* [ ] Política de zonas y delimitación física de archivos creada.
* [ ] README.md raíz creado o revisado para reflejar el estado real del proyecto.
* [ ] Estructuración clara de la lista de características (*feature list*).
* [ ] Consolidación de un árbol de trabajo Git limpio, con cualquier advertencia o deuda registrada explícitamente en `progress/` si no bloquea la fase.
