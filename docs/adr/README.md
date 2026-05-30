# File: docs/adr/README.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el propósito, uso y estado de los Architecture Decision Records.
# Rol: Índice y guía base para el registro de decisiones arquitectónicas.
# ──────────────────────────────────────────────────────────────────────

# ADR — Architecture Decision Records

## 1. Propósito

Esta carpeta constituye la sede oficial destinada a albergar de manera exclusiva y estructurada todos los registros de decisiones arquitectónicas (Architecture Decision Records, o ADR) que se adopten en el desarrollo y mantenimiento del proyecto raíz `proyecto_raiz_sdd_harness`.

## 2. Qué es un ADR

Un ADR es un documento breve y acotado en el tiempo que registra de forma formal y estructurada una decisión técnica o de diseño relevante en la arquitectura de un sistema. Cada registro de decisión detalla:
- El contexto técnico, de negocio o metodológico que motivó la decisión.
- Las distintas opciones y alternativas tecnológicas analizadas y evaluadas.
- La justificación de la alternativa seleccionada.
- Las consecuencias y compromisos resultantes a corto, medio y largo plazo.

## 3. Cuándo crear un ADR

Deberá crearse obligatoriamente un nuevo registro ADR cuando una propuesta técnica o decisión de diseño altere o afecte significativamente a alguno de los siguientes elementos:
- La arquitectura general del sistema (patrones de diseño, flujos de datos globales).
- La adición, reemplazo o eliminación de dependencias técnicas y librerías externas importantes.
- La definición o modificación de los contratos de APIs y servicios del sistema.
- Cambios estructurales en la jerarquía y organización de carpetas del repositorio.
- Cambios o modificaciones estructurales en los modelos de base de datos o almacenamiento de datos.
- Requisitos, políticas o implementaciones que impacten la seguridad y el control de accesos.
- La integración de herramientas de software o plataformas de terceros en el proyecto.
- Cambios en el diseño lógico de las gates de calidad, las habilidades operativas (skills) o los flujos de trabajo (workflows) centrales del arnés.
- Cualquier otra decisión técnica cuyos impactos operativos o financieros resulten difíciles de revertir en fases de desarrollo avanzadas.

## 4. Cuándo no crear un ADR

No será necesario el desarrollo de un registro ADR para cambios que no alteren la arquitectura base, tales como:
- Correcciones menores de bugs o parches de código de bajo riesgo.
- Cambios tipográficos, ortográficos o de estilo en la documentación técnica.
- Ajustes documentales simples o actualizaciones de seguimiento de avance.
- Tareas experimentales y pruebas piloto locales no consolidadas en el codebase principal.
- Cambios técnicos temporales u operativos rápidos que no afecten ni comprometan a largo plazo el comportamiento o estructura del software.

## 5. Estado actual

- **Estado:** Sede documental creada.
- **ADR activos:** Ninguno (0 activos).
- **Pendiente:** Definir y normalizar la plantilla oficial de ADR en cuanto se presente y apruebe la primera decisión arquitectónica real del repositorio.
