# File: docs/gate_0_preflight_definicion.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir documentalmente el gate_0_preflight del arnés.
# Rol: Especificación de criterios, entradas, salidas y bloqueos del gate.
# ──────────────────────────────────────────────────────────────────────

# Gate 0 Preflight — Definición documental del gate mínimo local

## Estado actual

`gate_0_preflight.py` ya está implementado en `scripts/gate_0_preflight.py`.

Este script es el único gate mínimo local autorizado del arnés en el estado actual del repositorio.

Su función es verificar condiciones estructurales básicas antes de avanzar o cerrar cambios documentales controlados.

## 1. Propósito

Este documento define la especificación del gate `gate_0_preflight` del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es establecer qué verifica el primer gate estructural antes de permitir que el arnés avance hacia cambios operativos más sensibles.

## 2. Relación con el preflight estructural

El documento `docs/preflight_estructural.md` define el checklist manual actual para revisar la coherencia del repositorio antes de avanzar.

El script `scripts/gate_0_preflight.py` es la implementación operativa y autorizada que automatiza de forma determinista estas revisiones.

## Alcance

El Gate 0 Preflight valida únicamente condiciones mínimas de seguridad estructural del repositorio.

Actualmente verifica:

- existencia de `.gitignore`;
- que `.venv/` esté correctamente ignorado por Git;
- ausencia de archivos de dependencias no autorizados como `requirements.txt`, `pyproject.toml` y `uv.lock`;
- ausencia de configuración de `pytest` como `pytest.ini` y `conftest.py`;
- existencia de documentos mínimos de control;
- que los cambios de Git estén dentro del allowlist documental autorizado.

## Límites

Este gate no reemplaza la auditoría humana.

Este gate no valida calidad metodológica profunda, arquitectura, contenido semántico completo ni coherencia total de todos los documentos.

Este gate no habilita por sí mismo:

- Fase 4;
- `uv`;
- `pytest`;
- nuevos scripts;
- nuevos gates;
- workflows;
- CLI;
- runtime técnico;
- activación real de `.agent/`;
- skills, agentes o subagentes activos.

## Modo mantenimiento

Cuando se modifica `scripts/gate_0_preflight.py`, la validación debe ejecutarse con:

```bash
GATE_PREFLIGHT_MAINTENANCE=1 .venv/bin/python scripts/gate_0_preflight.py
```

El modo normal puede fallar mientras el propio archivo del gate esté modificado.

Después del commit, el gate debe poder ejecutarse en modo normal:

```bash
.venv/bin/python scripts/gate_0_preflight.py
```

## Ejecución

Ejecución normal:

```bash
.venv/bin/python scripts/gate_0_preflight.py
```

Resultado esperado cuando todo está correcto:

```text
>> Verificación exitosa. Todo correcto.
```

## 3. Entradas esperadas

El gate `gate_0_preflight` no recibe parámetros externos.

Su entrada real es el estado actual del repositorio local al momento de ejecutarse.

El script revisa, de forma determinista, los elementos mínimos definidos en su implementación actual:

- existencia de `.gitignore`;
- estado de ignorado de `.venv/`;
- ausencia de archivos de dependencias no autorizados;
- ausencia de configuración de `pytest`;
- existencia de documentos mínimos de control definidos en el propio script;
- estado de cambios de Git contra el allowlist documental autorizado.

## 4. Criterios de aprobación

El gate aprueba cuando todas las verificaciones implementadas en `scripts/gate_0_preflight.py` pasan correctamente.

En el estado actual, eso significa:

- `.gitignore` existe;
- `.venv/` esté correctamente ignorado por Git;
- no existen `requirements.txt`, `pyproject.toml` ni `uv.lock`;
- no existen `pytest.ini` ni `conftest.py`;
- los documentos mínimos definidos en el script existen;
- no hay cambios de Git fuera del allowlist documental autorizado;
- si el propio `scripts/gate_0_preflight.py` está modificado, se usa el modo mantenimiento.

## 5. Criterios de bloqueo

El gate bloquea cuando alguna verificación implementada en `scripts/gate_0_preflight.py` falla.

En el estado actual, bloquea si detecta:

- ausencia de `.gitignore`;
- `.venv/` no ignorado correctamente por Git;
- presencia de `requirements.txt`, `pyproject.toml` o `uv.lock`;
- presencia de `pytest.ini` o `conftest.py`;
- ausencia de documentos mínimos definidos en el script;
- cambios de Git fuera del allowlist documental autorizado;
- modificación de `scripts/gate_0_preflight.py` sin usar modo mantenimiento.

## 6. Evidencia requerida

Cuando el gate se ejecuta, deja evidencia en la salida estándar y la validación puede registrarse en los archivos de progreso:

- fecha de ejecución;
- tipo de revisión;
- archivos revisados;
- resultado: aprobado o bloqueado;
- observaciones detectadas.

## 7. Salida esperada

El resultado del gate se clasifica en uno de estos estados:

- **aprobado:** el proyecto puede avanzar al siguiente cambio documental controlado.
- **bloqueado:** el proyecto no debe avanzar hasta corregir el problema detectado.

## 8. Qué no hace este documento

Este documento no:

- modifica archivos por sí mismo;
- crea nuevos gates no autorizados;
- autoriza automatización adicional fuera del preflight mínimo;
- autoriza implementación sobre código real;
- reemplaza la constitución ni el mapa documental.
