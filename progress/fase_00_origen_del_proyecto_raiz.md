# File: progress/fase_00_origen_del_proyecto_raiz.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar formalmente el Intake Inicial (Fase 00) del proyecto raíz.
# Rol: Registro documental de origen, objetivos iniciales y limitaciones de la iniciativa.
# ──────────────────────────────────────────────────────────────────────

# Fase 00 — Origen del Proyecto Raíz (Intake Inicial)

## 1. Datos básicos del proyecto
* **Nombre provisional del proyecto:** `proyecto_raiz_sdd_harness`
* **Impulsor o solicitante:** Desarrollador humano / Administrador del sistema.
* **Fecha de registro:** 2026-06-07
* **Estado del Intake:** Incorporado como evidencia documental de Fase 0 cerrada con observaciones controladas.

---

## 2. Necesidad, problema o riesgo que origina el proyecto
El desarrollo de software asistido por Inteligencia Artificial y agentes autónomos (como Codex o Antigravity) frecuentemente sufre de desviaciones debido a la falta de un marco de control estructurado:
* **Falta de gobernanza:** Modificación de archivos sin orden claro, lo que introduce regresiones invisibles en el codebase.
* **Ambigüedad en requerimientos:** Agentes que asumen o inventan lógicas de negocio al encontrar zonas grises en los prompts del usuario.
* **Falta de validación determinista:** Confianza excesiva en que el código "debería funcionar" según la IA, omitiendo la ejecución de suites de pruebas locales y análisis estáticos de calidad.
* **Maquillaje de resultados:** Trazas de depuración u ocultación de fallos en pruebas reales cuando se interactúa con proveedores o APIs de terceros.
* **Pérdida de la memoria del proceso:** Dependencia absoluta del historial del chat conversacional, el cual se volatiliza al iniciar una nueva sesión.

El proyecto raíz nace para resolver esta problemática construyendo un **arnés agéntico y procedimental** reutilizable.

---

## 3. Usuarios finales del sistema
* **Desarrolladores humanos:** Quienes guían y aprueban de forma explícita las decisiones críticas de arquitectura, diseño y cambios de fase.
* **Agentes de Inteligencia Artificial (Codex, Antigravity, etc.):** Operan bajo las directrices del arnés, leyendo especificaciones atómicas (`specs/`), respetando las políticas de no maquillaje y reportando evidencias físicas en las sedes aprobadas del repositorio, como `progress/`, reportes de validación o una futura zona de outputs cuando sea definida.

---

## 4. Resultado mínimo esperado (MVP v0.1)
El éxito del proyecto raíz se define por contar con una estructura capaz de:
1. Regular los flujos de cambio bajo la metodología **Spec-Driven Development (SDD)**.
2. Contar con un proceso de validación determinista que impida a la IA realizar modificaciones directas en el software sin pasar gates específicos.
3. Disponer de bitácoras físicas de progreso (`progress/`) independientes de la conversación.
4. Definir, en una fase posterior autorizada, un validador preliminar (`gate_0_preflight.py`) para revisar el estado del workspace antes de ejecutar tareas técnicas.

---

## 5. Alcance negativo (Qué NO debe hacer el proyecto)
* No diseñará planes de negocio comerciales ni estudios financieros.
* No generará contenido publicitario, copys de marketing ni campañas de comunicación.
* No desarrollará sistemas agénticos de carácter editorial o de redacción de prosa no técnica.
* No permitirá la auto-modificación autónoma o descontrolada de las directrices normativas (constitución y adaptadores) por parte de las IAs.

---

## 6. Restricciones iniciales del proyecto
* **Entorno:** Sistema operativo Windows interactuando con subentornos de desarrollo Linux vía WSL.
* **Herramientas de ejecución:** Uso mandatorio de `uv` como gestor de entornos virtuales y dependencias de Python (prohibiendo la instalación de dependencias globales).
* **Seguridad:** Prohibición absoluta de versionar credenciales, variables `.env` o llaves criptográficas en texto plano.
* **Control de cambio:** Todo cambio debe registrarse en Git de forma modular, dividiendo las modificaciones conceptuales de las mecánicas en commits separados.

---

## 7. Información faltante o pendientes de definición
* Determinación del componente piloto específico sobre el cual se testeará el primer flujo de Spec-Driven Development de extremo a extremo en la Fase 3 del plan.
* Plantillas definitivas de archivos markdown para la carpeta `specs/` (requirements, design, tasks, validation, etc.).

---

## 8. Recomendación de avance
* **Dictamen:** **Avanzar a Fase 0 (Visión y Alcance)**.
* **Motivo:** Los orígenes, usuarios y límites negativos de la iniciativa del repositorio raíz están formalizados y son coherentes con las pautas de gobernanza documental y constitución aprobadas. El proyecto está listo para definir detalladamente su Visión y Alcance oficial.
