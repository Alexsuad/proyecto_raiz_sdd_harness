# File: README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Servir como puerta de entrada oficial y mapa de navegación del repositorio raíz.
# Rol: README principal del repositorio subordinado al mapa de gobernanza y la constitución del proyecto.
# ──────────────────────────────────────────────────────────────────────

# proyecto_raiz_sdd_harness

Este repositorio es un proyecto raíz (o arnés) diseñado para iniciar, planificar, especificar, validar y revisar proyectos de desarrollo de software asistidos por Inteligencia Artificial (IA) utilizando la metodología **Spec-Driven Development (SDD)** y validaciones técnicas deterministas.

---

## 1. ¿Qué es este repositorio?
Es una **base metodológica, documental y estructural** reutilizable. Funciona como un arnés de gobernanza diseñado para ser replicado o adaptado en futuros proyectos reales de desarrollo de software, asegurando que humanos y agentes agénticos colaboren bajo estándares consistentes de calidad, orden LEAN y trazabilidad.

---

## 2. ¿Qué NO es este repositorio?
* **No es una aplicación final:** No contiene código de negocio ejecutable ni interfaces orientadas a usuarios finales.
* **No es un runtime agéntico activo:** No ejecuta subagentes automáticos de fondo, ni gestiona procesos en segundo plano.
* **No es un paquete instalable todavía:** No es una biblioteca de Python o un módulo de distribución técnica en esta fase.
* **No contiene gates lógicos activos:** Las automatizaciones técnicas están bloqueadas y no se deben realizar ejecuciones de scripts en esta etapa.

---

## 3. Estado actual
El repositorio se encuentra con la **Fase 0 documental cerrada con observaciones controladas**, la **Fase 1 (Spec Piloto Documental)** formalmente **cerrada en sentido documental**, y la **Fase 2 (Preparación mínima para hacer verificable el arnés)** abierta de forma controlada.
El entorno virtual mínimo `.venv` fue creado y validado localmente (aislamiento verificado), sin instalar dependencias ni activar uv o pytest. No hay desarrollo funcional autorizado, ni runtime activo, ni scripts activos, ni gates ejecutables activos. La carpeta `.agent/` sigue sin activación técnica.

* **Creado e incorporado a Git:**
  - Plan de implementación v0.1: [progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md](./progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md)
  - Procedimiento de inicio: [docs/procedimiento_inicio_proyecto_sdd_harness.md](./docs/procedimiento_inicio_proyecto_sdd_harness.md)
  - Origen / Intake del proyecto raíz: [progress/fase_00_origen_del_proyecto_raiz.md](./progress/fase_00_origen_del_proyecto_raiz.md)
  - Visión y alcance del proyecto raíz: [docs/vision_y_alcance_del_proyecto_raiz.md](./docs/vision_y_alcance_del_proyecto_raiz.md)
  - Auditoría arquitectónica interna: [progress/auditoria_arquitectonica_interna_2026-06-07.md](./progress/auditoria_arquitectonica_interna_2026-06-07.md)
  - Política de zonas del repositorio: [docs/politica_zonas_repositorio.md](./docs/politica_zonas_repositorio.md)
  - Auditoría final de cierre de Fase 0: [progress/auditoria_final_cierre_fase_0_2026-06-07.md](./progress/auditoria_final_cierre_fase_0_2026-06-07.md)
  - Registro de revisión de Spec F-013 (Gate manual futuro): [specs/f_013_gate_manual_futuro/review.md](./specs/f_013_gate_manual_futuro/review.md)
* **Elementos bloqueados (Sin autorización de arranque):**
  - Inicialización de entornos de ejecución con `uv`, pytest, scripts deterministas en `scripts/`, gates lógicos automatizados, especificaciones ejecutables reales y habilidades agénticas activas.

---

## 4. Qué leer primero
Para comprender el funcionamiento y los límites del arnés, se recomienda la lectura ordenada de los siguientes documentos:
1. [docs/00_mapa_y_gobernanza_documental.md](./docs/00_mapa_y_gobernanza_documental.md): Estándar de nomenclatura y organización física.
2. [docs/constitucion_del_proyecto.md](./docs/constitucion_del_proyecto.md): Marco normativo con reglas fundamentales no negociables.
3. [docs/vision_y_alcance_del_proyecto_raiz.md](./docs/vision_y_alcance_del_proyecto_raiz.md): Propósitos estratégicos y exclusiones del MVP v0.1.
4. [progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md](./progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md): Plan rector de prioridades y orden de ejecución.
5. [docs/procedimiento_inicio_proyecto_sdd_harness.md](./docs/procedimiento_inicio_proyecto_sdd_harness.md): Guía paso a paso de arranque e intake de proyectos.
6. [docs/politica_zonas_repositorio.md](./docs/politica_zonas_repositorio.md): Clasificación de estados de artefactos y políticas por carpeta.

---

## 5. Zonas principales del repositorio
* [docs/](./docs/): Sede de la documentación base, metodologías, constitución y políticas.
* [progress/](./progress/): Seguimiento operativo, plan de implementación v0.1 y registros de hitos.
* [.agent/](./.agent/): Estructura conceptual inactiva de workflows, skills y reglas locales.
* [specs/](./specs/): Sede de especificaciones por feature. Activa en modo documental para Fase 1; inactiva para implementación técnica o ejecución automatizada.
* [scripts/](./scripts/): Directorio reservado para futuros scripts deterministas y gates de validación (inactivo).
* [tests/](./tests/): Directorio reservado para la suite de pytest e infraestructura de pruebas (inactivo).
* [AGENTS.md](./AGENTS.md) y [GEMINI.md](./GEMINI.md): Adaptadores de contexto pragmáticos y activos para asistentes de IA.

---

## 6. Estado operativo de recursos

### Qué está activo ahora
* Documentación de gobernanza y mapa documental.
* Metodología base común y de desarrollo de software (SDD + Harness).
* Constitución del proyecto raíz y adaptadores operativos mínimos.
* Procedimiento de inicio de proyectos, plan de implementación v0.1, política de zonas y reporte de auditoría final de cierre de Fase 0.
* Bitácoras físicas e informe de auditoría arquitectónica interna.

### Qué está inactivo o bloqueado
* Especificaciones de features reales.
* Scripts ejecutables y gates lógicos automatizados.
* Runtime técnico y configuración activa agéntica de fondo.
* Activación operativa de skills o workflows en el IDE.
* Suite de testing local y código de producto candidato.

---

## 7. Reglas de oro del arnés
* **La metodología manda.** Las herramientas de IA ejecutan bajo su alcance. El humano aprueba decisiones críticas y el auditor valida los entregables físicos.
* **El chat no es fuente de verdad.** La memoria de la sesión conversacional es volátil; toda directriz o decisión de diseño aprobada debe persistir en el repositorio.
* **No se modifica fuera del alcance.** Está estrictamente prohibido crear archivos temporales sueltos, inyectar reglas activas (*front matter*) o programar scripts de validaciones antes de que sea autorizado en el plan.

---

## 8. Compatibilidad conceptual
El diseño del repositorio raíz busca la **portabilidad e independencia**. Las reglas y adaptadores definidos actúan como directrices de comportamiento genéricas para guiar la interacción de Codex, Antigravity u otras herramientas agénticas del ecosistema de IA, sin crear dependencias propietarias o rígidas hacia un único proveedor.

---

## 9. Siguiente paso según el plan
El siguiente hito es la verificación mínima reproducible y cierre de Fase 2 (Microfase 2.3), ejecutando un smoke test básico sobre el entorno virtual.

---

## 10. Estado del README
* **Estado:** Aprobado en la Fase 1 - Spec Piloto Documental.
