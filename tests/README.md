# File: tests/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la sede futura de pruebas del arnés.
# Rol: Guía base para organizar validaciones, pruebas automatizadas y pruebas manuales críticas.
# ──────────────────────────────────────────────────────────────────────

# Tests — Pruebas del arnés

## 1. Propósito

Esta carpeta será la sede oficial de las pruebas del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es permitir que el arnés sea validado con pruebas reproducibles, revisiones controladas y evidencia verificable antes de usarse sobre proyectos reales derivados.

## 2. Qué vivirá en esta carpeta

En fases posteriores, esta carpeta podrá contener pruebas relacionadas con:

- validación de scripts de gates;
- validación de estructura mínima del repositorio;
- validación de specs por feature;
- validación de workflows;
- validación de skills;
- pruebas de integración entre specs, progress y scripts;
- pruebas de regresión del propio arnés;
- pruebas de compatibilidad con Codex y Antigravity.

## 3. Relación con `scripts/`

La carpeta `scripts/` contendrá los scripts deterministas y gates ejecutables.

La carpeta `tests/` contendrá pruebas para comprobar que esos scripts y reglas funcionan correctamente.

Un script de gate no debe considerarse confiable solo porque exista; debe poder probarse o validarse con evidencia.

## 4. Tipos de pruebas previstas

En fases futuras, el arnés podrá incorporar:

- tests unitarios;
- tests de integración;
- smoke tests;
- pruebas de estructura documental;
- pruebas de salida esperada de gates;
- pruebas manuales críticas;
- checklists de validación.

## 5. Qué no debe vivir aquí

Esta carpeta no debe usarse para guardar:

- documentación metodológica;
- specs de features;
- reportes de progreso;
- prompts extensos;
- credenciales;
- tokens;
- configuraciones sensibles;
- archivos temporales;
- código de productos derivados.

## 6. Estado actual

- **Estado:** sede documental creada.
- **Tests activos:** ninguno.
- **Estado actual:** el primer gate mínimo local ya existe: `scripts/gate_0_preflight.py`.
- **Pendiente:** la creación de tests automatizados para este gate sigue bloqueada hasta autorización explícita de una fase futura.
