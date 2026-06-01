# File: docs/preflight_estructural.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir un checklist documental de revisión estructural del arnés.
# Rol: Control previo para verificar que el proyecto raíz mantiene coherencia antes de avanzar.
# ──────────────────────────────────────────────────────────────────────

# Preflight estructural del proyecto raíz

## 1. Propósito

Este documento define un checklist documental para revisar el estado estructural del proyecto raíz `proyecto_raiz_sdd_harness`.

Su objetivo es comprobar que la base del arnés se mantiene coherente, trazable y alineada con el enfoque LEAN antes de crear nuevas piezas operativas.

Este preflight no es un script, no es un gate automatizado y no ejecuta validaciones técnicas. Es una revisión documental previa.

## 2. Cuándo usar este preflight

Debe usarse antes de:

- crear una nueva carpeta estructural;
- crear una primera rule activa;
- crear un primer workflow activo;
- crear una primera skill activa;
- crear un primer gate documental;
- crear scripts de validación;
- crear una primera spec real;
- iniciar una primera feature piloto.

También puede usarse después de una auditoría o cuando exista duda sobre si el proyecto está creciendo demasiado rápido.

## 3. Checklist de estructura base

Antes de avanzar, verificar que existen:

- `docs/00_mapa_y_gobernanza_documental.md`
- `docs/01_metodologia_base_comun.md`
- `docs/02_metodologia_desarrollo_software_sdd_harness.md`
- `docs/constitucion_del_proyecto.md`
- `docs/adr/README.md`
- `docs/gate_0_preflight_definicion.md`
- `AGENTS.md`
- `GEMINI.md`
- `specs/README.md`
- `progress/README.md`
- `progress/current.md`
- `scripts/README.md`
- `tests/README.md`

*Nota sobre recursos privados:* Si existe en el entorno local, se puede verificar `docs/manual_anti_errores_del_arnes.md`. Sin embargo, al ser un archivo local privado excluido de git, su ausencia en el repositorio público no se considera un fallo estructural ni bloquea el preflight.

## 4. Checklist de estado agéntico

Antes de avanzar, verificar que:

- `.agent/rules/README.md` existe solo como sede documental.
- `.agent/workflows/README.md` existe solo como sede documental.
- `.agent/skills/README.md` existe solo como sede documental.
- No existen rules activas.
- No existen workflows activos.
- No existen skills activas.
- No existe `.agent/gates/`.
- No existen gates operativos ni automatizados.

## 5. Checklist de no duplicación

Antes de avanzar, verificar que:

- `AGENTS.md` no duplica la constitución completa.
- `GEMINI.md` no duplica la constitución completa.
- Los README de sede no duplican la metodología completa.
- Las carpetas documentales conceptuales solo explican su propósito, límites y recursos no activos existentes.
- Las reglas importantes siguen viviendo en los documentos oficiales correspondientes.

## 6. Checklist LEAN

Antes de avanzar, verificar que el siguiente cambio:

- tiene una necesidad clara;
- no crea estructura vacía innecesaria;
- no activa automatización prematura;
- no crea recursos que puedan confundirse con activos;
- no obliga a mantener documentos sin uso real;
- aporta control, claridad o trazabilidad.

Si el cambio no supera este checklist, debe posponerse.

## 7. Checklist de bloqueo

Debe bloquearse el avance si se detecta:

- creación de una rule activa sin autorización;
- creación de un workflow activo sin autorización;
- creación de una skill activa sin autorización;
- creación de scripts de gates sin revisión previa;
- modificación de la constitución sin aprobación;
- duplicación normativa entre documentos;
- instrucciones contradictorias entre `AGENTS.md`, `GEMINI.md` y documentos base;
- uso de `.agent/` como sistema activo antes de autorización explícita.

## 8. Resultado esperado

Al finalizar el preflight, el resultado debe clasificarse como:

- **aprobado:** se puede avanzar con el siguiente cambio documental controlado.
- **aprobado con observaciones:** se puede avanzar, pero debe corregirse una observación menor.
- **bloqueado:** no se debe avanzar hasta corregir el problema detectado.

## 9. Estado del documento

- **Estado:** checklist documental inicial.
- **Tipo:** preflight manual.
- **Automatización:** ninguna.
- **Pendiente:** convertir parte de este checklist en un gate determinista cuando el arnés esté listo para scripts.
