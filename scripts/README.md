# File: scripts/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la sede futura de scripts y gates deterministas del arnés.
# Rol: Guía base para organizar validaciones automatizadas, preflight checks y utilidades de control.
# ──────────────────────────────────────────────────────────────────────

# Scripts — Gates deterministas y utilidades de validación

## 1. Propósito

Esta carpeta será la sede oficial de los scripts deterministas del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es permitir que el arnés pueda verificar condiciones objetivas mediante comandos, validaciones automáticas, checks reproducibles y gates ejecutables.

## 2. Qué vivirá en esta carpeta

En fases posteriores, esta carpeta podrá contener scripts relacionados con:

- validación de estructura mínima del repositorio;
- revisión de archivos obligatorios;
- comprobación de specs por feature;
- verificación de estados permitidos;
- validación de gates documentales;
- validación previa a implementación;
- validación posterior a revisión;
- utilidades de soporte para reportes o auditorías.

## 3. Relación con los gates

Los gates son puertas de control que determinan si una tarea puede avanzar o debe detenerse.

Los scripts de esta carpeta podrán implementar gates como:

- `gate_0_preflight.py`: [IMPLEMENTADO] verificación mínima local de estructura, documentos base y exclusión de dependencias de testing.
- `gate_spec_ready.py`: validación de que una spec contiene los archivos y campos mínimos requeridos.
- `gate_pre_implementation.py`: validación previa a permitir implementación candidata.
- `gate_review.py`: validación previa al cierre o aprobación final de una tarea.

El script de preflight ya está implementado, mientras que los demás scripts no se crean todavía para evitar automatización prematura.

## 4. Regla de salida de los gates

Cuando existan scripts de gates, deberán seguir una regla simple:

- si la validación pasa, el script debe terminar correctamente;
- si la validación falla, el script debe bloquear el avance y devolver una salida no exitosa;
- si falta información crítica, el script debe reportar el bloqueo de forma clara.

El objetivo es que el resultado sea verificable por una persona, por Codex, por Antigravity o por cualquier herramienta compatible.

## 5. Qué no debe vivir aquí

Esta carpeta no debe usarse para guardar:

- prompts extensos;
- documentación metodológica;
- specs de features;
- reportes de progreso;
- archivos temporales;
- credenciales;
- tokens;
- configuraciones sensibles;
- código de productos derivados.

## 6. Estado actual

- **Estado:** script de validación mínima operativa creado.
- **Scripts activos:** `gate_0_preflight.py` (verificación estructural mínima local ejecutable desde `.venv`, sin `pytest`, `uv` ni dependencias externas).
- **Gates activos:** `gate_0_preflight.py`.
- **Pendiente:** definir alcance y criterios de cierre de Fase 4 para la feature piloto.