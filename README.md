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

---

## 3. Estado actual
El repositorio se encuentra con la **Fase 4 base documental cerrada y auditada a nivel documental y remoto**. La implementación agéntica no ha sido iniciada. La Fase 5, `uv`, `pytest`, nuevos scripts, tests, workflows y la habilitación de runtime en `.agent/` siguen bloqueados hasta autorización humana explícita del Equipo Auditor.

* **Creado e incorporado a Git (Fase 4):**
  - Contrato de misiones agénticas: [docs/contrato_misiones_agenticas.md](./docs/contrato_misiones_agenticas.md)
  - Mapa de roles agénticos: [docs/mapa_roles_agenticos.md](./docs/mapa_roles_agenticos.md)
  - Workflow de misiones agénticas: [docs/workflow_misiones_agenticas.md](./docs/workflow_misiones_agenticas.md)
* **Elementos bloqueados (Sin autorización de arranque):**
  - Inicialización de `uv`, `pytest`, nuevos scripts, tests, y habilitación del runtime en `.agent/` (los archivos de la carpeta `.agent/` son recursos documentales y conceptuales no activos).

---

## 4. Qué leer primero
Para comprender el funcionamiento y los límites del arnés, se recomienda la lectura ordenada de los siguientes documentos:
1. [docs/00_mapa_y_gobernanza_documental.md](./docs/00_mapa_y_gobernanza_documental.md): Estándar de nomenclatura y organización física.
2. [docs/constitucion_del_proyecto.md](./docs/constitucion_del_proyecto.md): Marco normativo con reglas fundamentales no negociables.
3. [docs/vision_y_alcance_del_proyecto_raiz.md](./docs/vision_y_alcance_del_proyecto_raiz.md): Propósitos estratégicos y exclusiones del MVP v0.1.
4. [progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md](./progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md): Checklist vivo del proyecto.
5. [docs/procedimiento_inicio_proyecto_sdd_harness.md](./docs/procedimiento_inicio_proyecto_sdd_harness.md): Guía paso a paso de arranque e intake de proyectos.
6. [docs/politica_zonas_repositorio.md](./docs/politica_zonas_repositorio.md): Clasificación de estados de artefactos y políticas por carpeta.
7. [docs/contrato_misiones_agenticas.md](./docs/contrato_misiones_agenticas.md): Diseño conceptual del contrato de misiones.
8. [docs/mapa_roles_agenticos.md](./docs/mapa_roles_agenticos.md): Mapa de roles conceptuales de la capa agéntica.
9. [docs/workflow_misiones_agenticas.md](./docs/workflow_misiones_agenticas.md): Workflow y ciclo de vida de misiones agénticas.

---

## 5. Zonas principales del repositorio
* [docs/](./docs/): Sede de la documentación base, metodologías, constitución y políticas.
* [progress/](./progress/): `plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md` como checklist vivo, `current.md` como snapshot actual, `feature_list.md` como inventario, `history.md` como mínimo no operativo.
* [.agent/](./.agent/): Estructura conceptual inactiva de workflows, skills y reglas locales.
* [specs/](./specs/): Sede de especificaciones por feature. Activa en modo documental para Fase 1; inactiva para implementación técnica o ejecución automatizada.
* [scripts/](./scripts/): Directorio de scripts deterministas del arnés. Actualmente solo contiene `scripts/gate_0_preflight.py` como gate mínimo local autorizado; los demás scripts y gates siguen bloqueados hasta autorización explícita.
* [tests/](./tests/): Directorio reservado para la suite de pytest e infraestructura de pruebas (inactivo).
* [AGENTS.md](./AGENTS.md) y [GEMINI.md](./GEMINI.md): Adaptadores de contexto pragmáticos y activos para asistentes de IA.

---

## 6. Estado operativo de recursos

### Qué está activo ahora
* Documentación de gobernanza y mapa documental.
* Metodología base común y de desarrollo de software (SDD + Harness).
* Constitución del proyecto raíz y adaptadores operativos mínimos.
* `scripts/gate_0_preflight.py` como único gate mínimo local.
* `progress/` como sistema vivo de control.

### Qué está inactivo o bloqueado
* Fase 5 no abierta.
* `uv`, `pytest`, workflows e implementaciones técnicas activas, y habilitación de runtime en `.agent/` (no hay recursos agénticos activos ni runtime habilitado).
* Ejecución de runtime de las capacidades candidatas de Fase 4.

---

## 7. Reglas de oro del arnés
* **La metodología manda.** Las herramientas de IA ejecutan bajo su alcance. El humano aprueba decisiones críticas y el auditor valida los entregables físicos.
* **El chat no es fuente de verdad.** La memoria de la sesión conversacional es volátil; toda directriz o decisión de diseño aprobada debe persistir en el repositorio.
* **No se modifica fuera del alcance.** Está estrictamente prohibido crear archivos temporales sueltos, inyectar reglas activas (*front matter*) o programar scripts de validaciones antes de que sea autorizado en el plan.

---

## 8. Compatibilidad conceptual
* El diseño del repositorio raíz busca la **portabilidad e independencia**. Las reglas y adaptadores definidos actúan como directrices de comportamiento genéricas para guiar la interacción de Codex, Antigravity u otras herramientas agénticas del ecosistema de IA, sin crear dependencias propietarias o rígidas hacia un único proveedor.

---

## 9. Siguiente paso según el plan
* No abrir Fase 5 ni activar runtime, `uv`, `pytest`, nuevos scripts, tests, workflows o `.agent/` activo sin autorización humana explícita del Equipo Auditor.

---

## 10. Nota sobre distribución de ZIPs
* **Nota sobre empaquetado:** Los ZIP internos de auditoría pueden incluir recursos locales privados si el usuario lo autoriza. Los ZIP exportables o públicos deben excluir `docs/manual_anti_errores_del_arnes.md`.

## 11. Estado del README
* **Estado:** Actualizado para reflejar el cierre auditado de la Fase 4 documental y el bloqueo explícito de Fase 5.
