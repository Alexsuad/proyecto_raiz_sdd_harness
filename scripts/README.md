# File: scripts/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la sede de scripts y gates deterministas del arnés. Actualmente solo `scripts/gate_0_preflight.py` está autorizado como gate mínimo local.
# Rol: Guía breve para organizar validaciones deterministas y utilidades de control.
# ──────────────────────────────────────────────────────────────────────

# Scripts — Gates deterministas y utilidades de validación

## 1. Propósito

Esta carpeta es la sede de los scripts deterministas del proyecto raíz `proyecto_raiz_sdd_harness`.

## 2. Estado

Activo:
- `scripts/gate_0_preflight.py`

Bloqueado:
- nuevos scripts;
- nuevos gates;
- suites de tests;
- CLI;
- workflows;
- `uv`;
- `pytest`;
- runtime técnico.

## 3. Regla

`scripts/gate_0_preflight.py` es el único gate mínimo local autorizado. Todo script adicional queda bloqueado hasta autorización explícita.
