# File: docs/gate_0_preflight_definicion.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir documentalmente el futuro gate_0_preflight del arnés.
# Rol: Especificación previa de criterios, entradas, salidas y bloqueos antes de automatizar el gate.
# ──────────────────────────────────────────────────────────────────────

# Gate 0 — Definición documental de preflight estructural

## 1. Propósito

Este documento define, de forma documental y no automatizada, el futuro `gate_0_preflight` del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es establecer qué deberá verificar el primer gate estructural antes de permitir que el arnés avance hacia cambios operativos más sensibles, como la creación de una spec real, una rule activa, un workflow activo, una skill activa, un script de validación o una primera feature piloto.

Este documento no es un script, no es un gate automatizado y no activa ningún recurso agéntico.

## 2. Relación con el preflight estructural

El documento `docs/preflight_estructural.md` define el checklist manual actual para revisar la coherencia del repositorio antes de avanzar.

Este documento toma ese checklist como base y lo transforma en una definición formal del futuro `gate_0_preflight`.

La relación es la siguiente:

- `docs/preflight_estructural.md`: checklist manual actual.
- `docs/gate_0_preflight_definicion.md`: definición documental del futuro gate.
- `scripts/gate_0_preflight.py`: posible implementación futura, todavía no autorizada.

## 3. Definiciones de estado del gate

Para evitar ambigüedad, este proyecto distingue entre:

- **Definición documental de gate:** documento que describe qué debería revisar un gate futuro, sin ejecutar validaciones.
- **Gate operativo:** gate autorizado como parte del flujo de trabajo, aunque pueda ejecutarse manualmente.
- **Gate automatizado:** gate implementado mediante script o herramienta determinista.
- **Script ejecutable de gate:** archivo de código que realiza validaciones concretas, por ejemplo `scripts/gate_0_preflight.py`.

El documento actual solo es una definición documental de gate. No debe interpretarse como gate operativo, gate automatizado ni script ejecutable.

## 4. Cuándo se usará este gate

Cuando exista una versión activa del `gate_0_preflight`, deberá ejecutarse antes de:

- crear una primera spec real;
- crear una rule activa;
- crear un workflow activo;
- crear una skill activa;
- crear una definición operativa activa de gate;
- crear scripts de validación;
- activar automatización;
- permitir que un agente actúe sobre código real de un proyecto derivado;
- iniciar una primera feature piloto del arnés.

Mientras el gate no exista como script, esta definición solo servirá como guía documental.

## 5. Entradas esperadas

El futuro `gate_0_preflight` deberá revisar, como mínimo, la existencia y coherencia de estos elementos:

- `docs/00_mapa_y_gobernanza_documental.md`
- `docs/constitucion_del_proyecto.md`
- `docs/01_metodologia_base_comun.md`
- `docs/02_metodologia_desarrollo_software_sdd_harness.md`
- `docs/preflight_estructural.md`
- `docs/adr/README.md`
- `AGENTS.md`
- `GEMINI.md`
- `specs/README.md`
- `progress/README.md`
- `progress/current.md`
- `progress/history.md`
- `scripts/README.md`
- `tests/README.md`
- `.agent/rules/README.md`
- `.agent/workflows/README.md`
- `.agent/skills/README.md`

## 6. Criterios de aprobación

El gate podrá aprobar el avance si se cumplen estas condiciones:

- los documentos base existen;
- la constitución y el mapa documental están aprobados para fase documental / MVP estructural;
- `AGENTS.md` y `GEMINI.md` existen y funcionan como adaptadores operativos mínimos;
- `specs/`, `progress/`, `scripts/` y `tests/` existen solo como sedes documentales cuando aplique;
- `.agent/rules/`, `.agent/workflows/` y `.agent/skills/` existen solo como sedes documentales futuras no activas;
- no existe `.agent/gates/`, salvo autorización explícita posterior;
- no existen rules activas;
- no existen workflows activos;
- no existen skills activas;
- no existen scripts ejecutables de gates;
- no existen specs reales sin autorización;
- no existe código de producto;
- `progress/current.md` refleja el estado operativo real del arnés;
- `progress/history.md` registra los hitos relevantes sin convertirse en una bitácora excesiva;
- no hay contradicciones evidentes entre documentos normativos, adaptadores y sedes documentales.

## 7. Criterios de bloqueo

El gate deberá bloquear el avance si detecta cualquiera de estas situaciones:

- falta un documento base obligatorio;
- `AGENTS.md` o `GEMINI.md` contradicen la constitución;
- el mapa documental no refleja la estructura real del repositorio;
- `progress/current.md` está desactualizado frente al estado real del proyecto;
- existe `.agent/gates/` sin autorización explícita;
- existe una rule activa sin autorización;
- existe un workflow activo sin autorización;
- existe una skill activa sin autorización;
- existe un script de gate sin revisión previa;
- existe una spec real sin autorización;
- existe código de producto en el proyecto raíz;
- un README de sede contiene metadatos que puedan interpretarse como recurso activo;
- se detecta duplicación normativa grave entre documentos;
- se intenta avanzar hacia automatización sin evidencia de revisión documental.

## 8. Evidencia requerida

Cuando el gate se ejecute manualmente o en una futura versión automatizada, deberá dejar evidencia mínima de:

- fecha de ejecución;
- tipo de revisión;
- archivos revisados;
- resultado: aprobado, aprobado con observaciones o bloqueado;
- observaciones detectadas;
- decisión tomada;
- siguiente paso permitido;
- responsable o agente que ejecutó la revisión.

Mientras el gate sea documental, esta evidencia podrá registrarse en `progress/current.md` o `progress/history.md`.

## 9. Salida esperada

El resultado del gate deberá clasificarse en uno de estos estados:

- **aprobado:** el proyecto puede avanzar al siguiente cambio documental controlado.
- **aprobado con observaciones:** el proyecto puede avanzar, pero debe corregir observaciones menores antes de activar recursos operativos.
- **bloqueado:** el proyecto no debe avanzar hasta corregir el problema detectado.

## 10. Relación futura con scripts

Este documento podrá servir como base para crear un script futuro:

- `scripts/gate_0_preflight.py`

Ese script solo podrá crearse cuando exista autorización explícita y cuando el proyecto esté listo para convertir parte del checklist manual en validación determinista.

La creación futura del script deberá respetar:

- la constitución;
- el mapa documental;
- el preflight estructural;
- el estado actual registrado en `progress/current.md`;
- el principio de no automatización prematura.

## 11. Qué no hace este documento

Este documento no:

- ejecuta validaciones;
- modifica archivos;
- crea gates activos;
- crea scripts;
- crea `.agent/gates/`;
- autoriza automatización;
- autoriza implementación sobre código real;
- reemplaza el preflight estructural manual;
- reemplaza la constitución ni el mapa documental.

## 12. Estado del documento

- **Estado:** definición documental inicial.
- **Tipo:** especificación previa de gate.
- **Automatización:** ninguna.
- **Gate activo:** no.
- **Pendiente:** auditar esta definición antes de convertirla en script o en gate operativo real.
