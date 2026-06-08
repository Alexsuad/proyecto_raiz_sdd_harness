# File: specs/f_013_gate_manual_futuro/requirements.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir los requisitos funcionales y restricciones del Gate Manual Futuro.
# Rol: Spec de requerimientos de la feature F-013 en estado candidato.
# ──────────────────────────────────────────────────────────────────────

# Requerimientos — F-013: Gate manual futuro

**Versión:** v0.1-candidato  
**Estado:** Candidato (Fase 1 - Spec Piloto Documental)  
**Tipo:** Especificación de Requerimientos (SDD)  
**Ubicación:** `specs/f_013_gate_manual_futuro/requirements.md`

---

## 1. Propósito

El propósito de esta especificación es definir los requisitos del **Gate Manual Futuro (F-013)**. Este gate establece un mecanismo de control de calidad y gobernanza documental en el que cualquier transición entre fases del proyecto requiere la revisión del Equipo Auditor Procedimental cuando aplique y la aprobación explícita del desarrollador humano antes de autorizar pasos adicionales.

Esta especificación se mantiene exclusivamente en el plano **documental y procedimental**, sirviendo como piloto para el flujo de Desarrollo Basado en Especificaciones (SDD) del arnés.

---

## 2. Problema que resuelve

En proyectos de desarrollo asistidos por inteligencia artificial, los agentes pueden incurrir en autoaprobaciones apresuradas o descontroladas de cambios de fase críticos (por ejemplo, pasar de diseño a implementación de código sin validación humana o con inconsistencias estructurales). 

Este gate manual resuelve la falta de control determinista sobre el ciclo de vida documental y técnico del proyecto al obligar a realizar una pausa de seguridad en la que un humano debe auditar los entregables y estampar su firma/dictamen en un formato legible, versionado y auditable en texto Markdown.

---

## 3. Roles involucrados

* **Desarrollador Humano (Human Reviewer):** Posee la autoridad máxima para aprobar o rechazar una transición de fase estampando su dictamen explícito en el archivo de revisión.
* **Equipo Auditor Procedimental (Procedural Auditor):** Rol encargado de realizar el dry-run o validación de cumplimiento documental antes de que la propuesta llegue al Desarrollador Humano.
* **Agente de IA (Antigravity/Gemini):** Desarrolla los artefactos, ejecuta auditorías internas preliminares, genera el listado de evidencias y solicita de manera formal la revisión del gate, absteniéndose de autoaprobar el paso de fase.

---

## 4. Requisitos funcionales

* **RF-013-01: Estructura estándar del Gate Manual:** Se debe definir una plantilla estándar en texto plano/Markdown para que el agente registre la solicitud de apertura de gate.
* **RF-013-02: Registro obligatorio de Evidencias:** La solicitud de apertura de gate debe listar de forma atómica y explícita los entregables de la fase actual con sus respectivas rutas relativas y hashes de commit/diff asociados.
* **RF-013-03: Dictamen Humano Mandatorio:** El gate solo puede cerrarse con la firma manual en texto del desarrollador humano utilizando una de las opciones predefinidas.
* **RF-013-04: Gestión de Estados del Gate:** El gate debe soportar los siguientes estados:
  * `abierto`: Solicitado por el agente y pendiente de revisión.
  * `aprobado`: Aprobado explícitamente por el humano, permitiendo la apertura de la siguiente fase.
  * `bloqueado`: Rechazado debido a omisiones críticas de calidad o seguridad.
  * `requiere_aclaracion`: Devuelto por dudas funcionales o falta de información.
  * `requiere_replanificacion`: Devuelto por desviación del alcance o la arquitectura.

---

## 5. Requisitos no funcionales

* **RNF-013-01: Legibilidad y simplicidad (LEAN):** Toda la información, solicitud y firmas del gate deben ser legibles y modificables de manera directa en Markdown sin dependencias de interfaces web complejas ni herramientas de software externas.
* **RNF-013-02: Trazabilidad documental:** Los enlaces a los archivos y evidencias de validación deben usar rutas relativas del repositorio (evitando rutas absolutas de la máquina local del desarrollador).
* **RNF-013-03: Inmutabilidad por convención:** Una vez aprobado el gate, el bloque de firma y las evidencias asociadas no deben modificarse, sirviendo como un registro de auditoría estático en el historial de Git.

---

## 6. Fuera de alcance

* Queda fuera de alcance cualquier automatización basada en código ejecutable (`.py`, `.js`, etc.) para verificar los requisitos del gate.
* No se desarrollarán validadores automáticos de sintaxis ni de commits que ejecuten hooks de Git en background.
* Queda excluida la integración técnica con la carpeta `.agent/` o cualquier skill activa que tome decisiones autónomas de paso de fase.

---

## 7. Criterios de aceptación

* **CA-013-01:** La especificación piloto define con claridad el bloque de firma en texto plano que debe rellenar el desarrollador humano.
* **CA-013-02:** Se establece la prohibición explícita de que el agente pueda escribir su propia firma o autoevaluarse como aprobado.
* **CA-013-03:** Se documentan las rutas relativas oficiales para el almacenamiento de evidencias dentro del flujo SDD.
* **CA-013-04:** El plan de trabajo asociado no contiene ninguna tarea de desarrollo técnico ni activación de dependencias de software.

---

## 8. Bloqueos y restricciones técnicas explícitas

> [!IMPORTANT]
> **ESTA FEATURE ES EXCLUSIVAMENTE DOCUMENTAL.**
> * Se prohíbe la creación o programación de scripts en la carpeta `scripts/` para automatizar este gate.
> * Se prohíbe inicializar suites de test con `pytest`, configurar entornos virtuales con `uv` o instalar dependencias de software.
> * Queda estrictamente bloqueado el uso de cualquier runtime técnico o la modificación de código ejecutable en el repositorio.
