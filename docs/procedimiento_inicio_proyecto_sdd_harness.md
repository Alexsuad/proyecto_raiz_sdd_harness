# File: docs/procedimiento_inicio_proyecto_sdd_harness.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir los pasos y checklist para iniciar un nuevo proyecto bajo la metodología SDD y el arnés agéntico.
# Rol: Procedimiento operativo estandarizado para el arranque de proyectos derivados.
# ──────────────────────────────────────────────────────────────────────
# Procedimiento de inicio de proyecto SDD + Harness

**Versión:** v0.1  
**Estado:** Aprobado para fase documental  
**Tipo:** Procedimiento operativo documental  
**Ubicación:** `docs/procedimiento_inicio_proyecto_sdd_harness.md`

---

## 1. Propósito del documento

Este documento define el procedimiento oficial para iniciar un proyecto desde cero usando el sistema SDD + Harness.

Su objetivo es evitar que un proyecto comience directamente con código, prompts sueltos, agentes improvisados, carpetas creadas sin criterio o documentos sin sede clara.

El procedimiento guía el paso desde una idea inicial hasta un proyecto organizado, con contexto mínimo, clasificación, documentación base, criterios de salida y evidencias verificables.

---

## 2. Cuándo se usa este procedimiento y límites del MVP actual

Este procedimiento se usa cuando se quiere iniciar:

- un nuevo proyecto de software;
- un proyecto asistido por IA;
- un sistema con agentes, skills, workflows o gates;
- un repositorio raíz reutilizable;
- una automatización técnica;
- una herramienta interna;
- una feature relevante dentro de un proyecto existente, si su impacto lo justifica.

> [!IMPORTANT]
> **Límites del MVP actual:**
> El MVP actual de este procedimiento y del arnés de desarrollo se enfoca en proyectos de desarrollo de software bajo la metodología **Spec-Driven Development (SDD)**. Cabe aclarar que elementos como la inicialización virtual con `uv`, suite de tests locales con `pytest`, herramientas de línea de comandos `CLI` y scripts locales de gates pertenecen a una línea técnica prevista o futura, pero no están activos en el estado actual del repositorio salvo `scripts/gate_0_preflight.py` (el cual es el único gate mínimo local activo). En el estado actual: `uv` está bloqueado, `pytest` está bloqueado, la `CLI` está bloqueada y la creación de scripts nuevos de gates está bloqueada.
> 
> Quedan estrictamente **fuera del alcance** de esta versión del arnés:
> - Planes de negocio, análisis comerciales, estudios de mercado o financieros.
> - Proyectos documentales extensos o de carácter general no técnico.
> - Sistemas editoriales de redacción de prosa, copys de marketing o campañas de comunicación.
> - Sistemas agénticos y de procesamiento de texto cuyo entregable principal sea la generación de prosa o contenido escrito largo no técnico.

---

## 3. Qué problema evita

Este procedimiento evita los siguientes riesgos:

- empezar a programar sin entender la necesidad;
- usar la conversación como única fuente de verdad;
- crear archivos sin gobernanza;
- mezclar documentación, runtime, scripts, tests y outputs;
- convertir ideas candidatas en reglas activas;
- depender de una herramienta concreta como Codex, Antigravity u otra;
- permitir que la IA complete huecos por su cuenta;
- avanzar sin evidencia;
- declarar listo un proyecto que solo está parcialmente definido.

La regla base es:

**Primero se entiende y documenta. Después se especifica. Solo al final se implementa.**

---

## 4. Principio rector y flujo procedimental

Todo proyecto iniciado con este sistema debe respetar esta regla:

**La metodología manda. Las herramientas ejecutan. El humano aprueba. El auditor valida.**

Esto significa que Codex, Antigravity, ChatGPT, Gemini, Claude u otra herramienta pueden apoyar el proceso, pero no deben convertirse en la arquitectura del proyecto.

### 4.1. Flujo Fuente → Análisis → Decisión
Toda propuesta de cambio técnico o incorporación de nuevos requerimientos debe nacer de una justificación documentada. Se debe trazar de forma rigurosa la procedencia del cambio (Usuario, QA, Seguridad o Arquitectura), analizar las alternativas de diseño e impacto en el sistema, y materializar la decisión final mediante un registro permanente en el repositorio (ej. un ADR en `docs/adr/` o en especificaciones técnicas de la carpeta `specs/`).

### 4.2. Responsable del flujo procedimental
El rol líder (Orquestador) se define como el máximo garante de velar por el cumplimiento de la metodología paso a paso. Es su responsabilidad verificar que las transiciones de estado y la creación de artefactos se apeguen estrictamente al orden LEAN y a las pautas de esta guía, impidiendo que los agentes comiencen la codificación antes de cerrar las especificaciones previas.

---

## Tabla resumen del flujo procedimental

Esta tabla ofrece una visión de alto nivel del flujo procedimental del arnés para orientar de forma rápida a humanos y agentes sobre qué se requiere, qué se hace y qué se espera obtener en cada paso de inicio:

| Fase | Entrada necesaria | Actividad principal | Salida esperada | Decisión posible | Evidencia mínima |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fase 00 — Intake inicial** | Idea o necesidad técnica inicial informal | Capturar la necesidad, objetivos, usuarios y restricciones resolviendo preguntas mínimas | Registro de intake estructurado | **Avanzar** (a Fase 01), **Aclarar** (pedir más datos) o **Detener** | Archivo físico de intake en `progress/fase_00_...` |
| **Fase 01 — Espejo del proyecto** | Registro de intake de la Fase 00 | Redactar una interpretación conceptual objetiva y clara de lo entendido | Espejo del proyecto revisable | **Ajustar** entendimiento o **Confirmar** para continuar | Sección de confirmación de alcance y supuestos aprobada |
| **Fase 02 — Organización del contexto** | Fuentes, referencias e inputs iniciales | Organizar y clasificar de forma física las fuentes de referencia en el repositorio | Repositorio estructurado y limpio | **Consolidar** en Git o **Solicitar** información faltante | Archivos de referencia y adaptadores versionados en Git |
| **Fase 03 — Clasificación del proyecto** | Tipo de entregable y complejidad | Asignar la profundidad proporcional del flujo procedimental (Tipo 1 al 5) | Clasificación y profundidad definidas | **Aprobar** nivel de flujo LEAN o **Replanificar** | Tabla de clasificación registrada y justificada |
| **Fase 04 — Documentación base mínima** | Clasificación de flujo aprobada | Crear o confirmar los documentos maestros de gobernanza, normas y límites | Set documental mínimo configurado | **Aprobar** documentos base o **Ajustar** normas | Documentos rectores en `docs/` (`constitucion.md`, README, mapa) |
| **Gate de salida** | Set documental de Fase 04 y checklists | Comprobar manual y estáticamente el cumplimiento y orden de las reglas de inicio | Dictamen de salida y control estructural | **Avanzar** a especificación/visión o **Bloquear** avance técnico | Checklist de `docs/preflight_estructural.md` verificado |
| **Control input/output** | Entradas de validación y definición de salidas | Asegurar la trazabilidad y correspondencia determinista de los reportes generados | Evidencias físicas registradas en sedes oficiales | **Aprobar** entregable con evidencia o **Exigir** corrección | Archivo de reporte o bitácora de progreso actualizado |

---

## Guía rápida para usar este procedimiento

Esta guía rápida está orientada a facilitar el uso directo del procedimiento para el **usuario final** del arnés:

1. **Presentación de la idea:** Traiga una necesidad o idea inicial de desarrollo técnico de software.
2. **Responder el Intake:** Complete las 9 preguntas mínimas del Intake (Fase 00) para delimitar qué se busca y qué se excluye.
3. **Revisar el Espejo:** Lea y confirme el documento espejo generado. Este debe reflejar fielmente su requerimiento técnico.
4. **Confirmar Entendimiento:** Ajuste o apruebe el espejo. Corrija activamente cualquier brecha de interpretación.
5. **Validar Límites:** Asegúrese de definir claramente el *Alcance* y el *Fuera de Alcance* para mantener el desarrollo LEAN.
6. **Tomar Decisión:** Elija si el proyecto está listo para **Avanzar**, si requiere **Aclarar** datos pendientes, o si debe **Detenerse**.
7. **Control Procedimental:** Bajo ningún concepto inicie la especificación de specs de features en `specs/` o la escritura de código si el inicio procedimental de estas fases no está debidamente cerrado y firmado.

---

## 5. Fase 00 — Intake inicial

### 5.1. Objetivo

Capturar la necesidad inicial antes de crear estructura, specs, scripts o código.

El intake no busca resolver todo el proyecto.

Busca responder con claridad:

- qué se quiere construir;
- por qué se quiere construir;
- para quién se construye;
- qué problema resuelve;
- qué resultado mínimo se espera;
- qué restricciones ya existen;
- qué información falta.

### 5.2. Preguntas mínimas

El intake debe responder, como mínimo:

1. ¿Cuál es el nombre provisional del proyecto?
2. ¿Qué necesidad, problema, riesgo u oportunidad origina el proyecto?
3. ¿Quién impulsa o solicita el proyecto?
4. ¿Quién usará el resultado?
5. ¿Qué resultado mínimo se espera obtener?
6. ¿Qué NO debe hacer el proyecto?
7. ¿Qué restricciones técnicas, legales, económicas o de tiempo existen?
8. ¿Qué información todavía falta?
9. ¿El proyecto debe avanzar, aclararse o detenerse?

### 5.3. Gate de Suficiencia de Entrada

Antes de abrir una spec, diseño técnico, tareas o implementación candidata, debe verificarse si la necesidad inicial contiene información suficiente para planear sin inventar componentes técnicos.

Este gate evalúa exclusivamente la suficiencia y claridad de la necesidad y el producto. Puede bloquear el avance cuando esa claridad es insuficiente, pero no impone arquitectura, stack, librerías, scripts, gates técnicos ni estructura interna del proyecto.

El gate puede producir cuatro estados:

- **APTO PARA PLANEAR:** la necesidad, el usuario, el resultado esperado, los límites y los criterios de éxito son suficientemente claros para abrir planeación proporcional.
- **ACLARACIÓN REQUERIDA:** existe una necesidad válida, pero falta información relevante sobre usuario, interfaz, datos, seguridad, entorno, validación, restricciones o criterios de éxito.
- **NO APLICA / REDIRIGIR:** la solicitud puede ser válida, pero no corresponde al alcance del flujo actual y debe tratarse por otro repositorio, fase, procedimiento o responsable.
- **NO INTERVENIR:** la solicitud no justifica acción dentro del proyecto, no requiere intervención del arnés o no debe avanzar por falta de pertinencia, autorización o valor suficiente.

Si falta información para decidir, no se debe avanzar inventando arquitectura ni componentes técnicos. Deben generarse preguntas concretas y quedar registrada la aclaración pendiente.

El sistema no debe asumir frontend, backend, login, base de datos, despliegue, infraestructura, proveedor externo o complejidad técnica por costumbre.

Cada componente técnico debe justificarse por una necesidad, usuario, riesgo, restricción o criterio de validación.

Esta decisión no abre Fase 5, no activa runtime agéntico, no habilita `.agent/`, no crea skills nuevas, no crea scripts y no modifica la arquitectura técnica del repositorio.

### 5.4. Resultado esperado

El resultado de esta fase puede quedar en un documento de progreso, una sección de visión o una plantilla de intake, según el tamaño del proyecto.

En el proyecto raíz actual, esta información puede documentarse en:

`progress/fase_00_origen_del_proyecto_raiz.md`

---

## 6. Fase 01 — Espejo del proyecto

### 6.1. Objetivo

Convertir la idea inicial en una interpretación revisable.

El espejo sirve para devolver al humano una versión clara de lo entendido antes de avanzar.

No debe ser una reescritura creativa.

Debe funcionar como una confirmación de entendimiento.

### 6.2. Contenido mínimo

El espejo debe incluir:

1. Resumen del proyecto en lenguaje claro.
2. Objetivo principal.
3. Objetivos secundarios, si existen.
4. Alcance inicial.
5. Fuera de alcance.
6. Supuestos detectados.
7. Riesgos iniciales.
8. Preguntas abiertas.
9. Decisión requerida para avanzar.

### 6.3. Regla de control

Si el espejo no refleja correctamente la intención del proyecto, no se debe avanzar a visión, specs ni implementación.

Primero se corrige el entendimiento.

---

## 7. Fase 02 — Organización del contexto

### 7.1. Objetivo

Ordenar las fuentes, conversaciones, documentos, referencias y decisiones iniciales para evitar que el proyecto dependa de memoria conversacional.

### 7.2. Clasificación mínima del contexto

El contexto debe clasificarse en:

- decisiones aprobadas;
- supuestos;
- dudas abiertas;
- fuentes de referencia;
- documentos activos;
- documentos candidatos;
- ideas futuras;
- elementos fuera de alcance.

### 7.3. Regla de fuente de verdad

La conversación puede ayudar a pensar, pero no debe ser la única fuente oficial.

Toda decisión importante debe quedar registrada en un documento del repositorio.

---

## 8. Fase 03 — Clasificación del tipo de proyecto

### 8.1. Objetivo

Definir qué tipo de flujo necesita el proyecto.

No todos los proyectos requieren el mismo nivel de documentación, specs, gates o validaciones.

### 8.2. Tipos iniciales

El proyecto puede clasificarse como:

| Tipo | Descripción | Profundidad sugerida |
|---|---|---|
| Tipo 1 | Proyecto documental o analítico (Fuera del MVP actual / Referencia futura) | Flujo ligero (No aplicable en v0.1) |
| Tipo 2 | Software simple o utilidad menor | Mini-spec o checklist |
| Tipo 3 | Software con lógica relevante | SDD por feature |
| Tipo 4 | Proyecto con datos, seguridad, producción o integraciones | SDD completo + validación reforzada |
| Tipo 5 | Proyecto raíz, sistema agéntico o arnés | Gobernanza estricta + auditoría |

### 8.3. Regla de proporcionalidad

Ser LEAN no significa omitir fases.

Significa ajustar la profundidad de cada fase al riesgo real del proyecto.

---

## 9. Fase 04 — Documentación base mínima

### 9.1. Objetivo

Crear o confirmar los documentos mínimos que permitirán gobernar el proyecto.

Antes de crear specs, scripts, skills o gates, el proyecto debe tener una base documental clara.

### 9.2. Documentos mínimos recomendados

Para un proyecto SDD + Harness, la base mínima debe incluir:

- mapa o gobernanza documental;
- metodología base o reglas comunes;
- visión y alcance;
- constitución del proyecto, si aplica;
- README inicial;
- feature list o backlog inicial, si aplica;
- carpeta de progreso o historial, si aplica.

### 9.3. Para el proyecto raíz actual

En este proyecto raíz, la base documental debe relacionarse con:

- `docs/00_mapa_y_gobernanza_documental.md`;
- `docs/01_metodologia_base_comun.md`;
- `docs/02_metodologia_desarrollo_software_sdd_harness.md`;
- `docs/constitucion_del_proyecto.md`;
- `AGENTS.md`;
- `GEMINI.md`;
- `progress/`;
- `specs/`.

Este procedimiento no reemplaza esos documentos.

Solo explica cómo debe iniciarse un proyecto antes de usarlos.

---

## 10. Fase 05 — Gate de salida del inicio

### 10.1. Objetivo

Definir cuándo un proyecto está listo para pasar de inicio a planeación formal o specs.

### 10.2. Checklist mínimo

Antes de avanzar, debe comprobarse:

- [ ] La necesidad inicial está descrita.
- [ ] El objetivo principal está claro.
- [ ] Existe una primera definición de alcance.
- [ ] Existe una primera definición de fuera de alcance.
- [ ] El tipo de proyecto fue clasificado.
- [ ] Las dudas importantes están registradas.
- [ ] Las decisiones aprobadas están separadas de los supuestos.
- [ ] La documentación base mínima fue creada o identificada.
- [ ] No se ha creado código, runtime, scripts, skills o gates antes de tiempo.
- [ ] Existe una recomendación clara de siguiente paso.

### 10.3. Resultados posibles

El gate de salida puede terminar en uno de estos estados:

| Estado | Significado |
|---|---|
| `avanzar_a_fase_0` | Hay contexto suficiente para crear visión y alcance. |
| `requiere_aclaracion` | Faltan datos relevantes antes de avanzar. |
| `bloqueado` | Hay contradicciones o riesgos que impiden continuar. |
| `detener` | El proyecto no debe continuar en este momento. |

---

## 11. Evidencias obligatorias

Cada inicio de proyecto debe dejar evidencias mínimas.

Las evidencias pueden incluir:

- documento de intake;
- espejo del proyecto;
- visión inicial;
- listado de fuentes usadas;
- decisiones aprobadas;
- dudas abiertas;
- clasificación del proyecto;
- gate de salida;
- reporte final de la tarea.

La evidencia debe permitir que un auditor entienda por qué el proyecto avanzó.

---

## 12. Relación con SDD

Este procedimiento ocurre antes de la implementación y antes de las specs completas.

El flujo general es:

```text
Idea inicial
↓
Intake
↓
Espejo
↓
Organización del contexto
↓
Clasificación del proyecto
↓
Documentación base mínima
↓
Gate de salida
↓
Visión y alcance
↓
Feature list
↓
Spec por feature
↓
Implementación candidata
↓
Validación
↓
Revisión
↓
Cierre con evidencia
```

La spec no debe nacer de una idea desordenada.

Debe nacer de un proyecto mínimamente entendido, clasificado y documentado.

---

## 13. Relación con Codex y Antigravity: Controles agénticos del arnés

Este procedimiento no depende de una herramienta concreta.

Codex, Antigravity u otros entornos pueden ayudar a ejecutar tareas, pero siempre bajo alcance definido.

Antes de pedirle a un agente operativo que modifique archivos, la tarea debe declarar:

- objetivo;
- archivos permitidos;
- archivos prohibidos;
- documentos que debe leer;
- cambios esperados;
- riesgos;
- criterio de aceptación;
- evidencia final esperada.

Si una herramienta necesita ampliar el alcance, debe detenerse y reportarlo como pendiente fuera de alcance.

### 13.1. Orquestador como rol procedimental
El rol de Orquestador se concibe únicamente como una directriz lógica de control de flujo en la secuencia del ciclo de vida del desarrollo. No representa un agente de IA autónomo en ejecución constante ni un daemon técnico en background. Las tareas de orquestación (comprobación de estados, paso de gates) se realizan de manera guiada y asistida por las herramientas en su interacción con el programador humano.

### 13.2. Memoria externa del proceso
Los agentes no deben depender de la memoria volátil de la conversación del chat como fuente de verdad. El estado del proyecto, hitos, bloqueos y decisiones de diseño deben persistir en los archivos físicos del repositorio localizados en la carpeta `progress/` (`current.md`, `history.md`) y en `docs/adr/`. 

### 13.3. Control Input/Output
Todo script, gate o automatización técnica posterior debe contar con una definición explícita de sus entradas admitidas (inputs) y estructurar sus reportes, resultados y evidencias físicas (outputs). Las salidas y evidencias deberán registrarse en la zona oficial de evidencias definida y aprobada para la fase correspondiente. Mientras esa zona no exista, la evidencia se registrará en el documento de progreso, reporte o sede documental autorizada por el plan, garantizando la repetibilidad determinista.

### 13.4. Self-improving loop controlado
El bucle de auto-mejora (*self-improving loop*) del arnés se restringe a la optimización estructurada de reglas y especificaciones metodológicas. Queda terminantemente prohibido que los agentes de IA se auto-modifiquen o alteren de manera libre sus reglas de comportamiento locales, adaptadores operativos (`AGENTS.md`, `GEMINI.md`) o la constitución del repositorio sin la revisión cruzada de la auditoría y la firma final del desarrollador humano.

---

## 14. Límites de este documento

Este documento no crea:

- plantillas;
- specs;
- scripts;
- gates automáticos;
- skills;
- workflows;
- runtime;
- CLI;
- adaptadores;
- pruebas automatizadas;
- carpetas adicionales.

Solo define el procedimiento inicial para que esos elementos se creen más adelante en el orden correcto.

---

## 15. Estado del documento

Este documento queda en estado:

`aprobado_fase_documental`

Cualquier mejora futura debe respetar su propósito:

**definir cómo iniciar proyectos, no sustituir toda la metodología SDD + Harness.**
