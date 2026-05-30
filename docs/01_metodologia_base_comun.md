# File: docs/01_metodologia_base_comun.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir los principios metodológicos comunes y transversales del proyecto raíz.
# Rol: Base metodológica general subordinada al mapa de gobernanza documental.
# ──────────────────────────────────────────────────────────────────────

# 01 — Metodología base común

## 1. Propósito del documento
Este documento define los principios comunes que regirán cualquier proyecto derivado del proyecto raíz. Establece las bases conceptuales de trabajo para que los proyectos derivados mantengan un estándar común de orden, agilidad, verificación y colaboración eficaz entre personas y agentes de inteligencia artificial.

## 2. Relación con el mapa de gobernanza documental
Este documento se subordina jerárquicamente a [docs/00_mapa_y_gobernanza_documental.md](./00_mapa_y_gobernanza_documental.md). Su función no es definir el orden de las carpetas, la nomenclatura ni las reglas de auditoría de archivos, sino establecer los lineamientos metodológicos generales de trabajo. Por lo tanto, no debe duplicar las reglas de organización documental ya asentadas en el mapa de gobernanza.

## 3. Naturaleza del proyecto raíz
El objetivo del proyecto raíz no es crear una aplicación final orientada al usuario final, sino estructurar un sistema de trabajo metodológico, documental y agéntico reutilizable. Funciona como un arnés metodológico y operativo diseñado para ser replicado en futuros proyectos reales de desarrollo de software, asegurando que todos sigan las mismas pautas de calidad y trazabilidad.

## 4. Principio LEAN
El proyecto debe avanzar de manera iterativa utilizando cambios pequeños, útiles, revisables y reversibles. Se debe evitar a toda costa la burocracia innecesaria, la duplicación de código o texto, y la documentación excesiva que no aporte valor práctico directo. El objetivo es maximizar la eficiencia y la claridad del repositorio. Aplicar LEAN no significa omitir especificaciones necesarias, gates, evidencias ni revisiones. En este proyecto, la documentación mínima necesaria para entender, validar y cerrar un cambio no se considera burocracia: se considera parte del entregable.

## 5. Principio de entregable candidato
Cualquier resultado generado por una inteligencia artificial o por un agente de desarrollo se considera un elemento preliminar (o candidato) hasta que pase por las validaciones correspondientes. Ejemplos de entregables candidatos:
- **Documento candidato:** Un borrador de especificación o metodología redactado por la IA pendiente de lectura y ajuste.
- **Código candidato:** Funciones o archivos de código propuestos por el agente que aún no han sido compilados, probados ni aprobados. Deben estar diseñados para preservar la funcionalidad existente, evitar regresiones, mantenerse limpios y no incluir código muerto, duplicado o innecesario. Antes de considerarse código definitivo, deben pasar validación técnica, revisión cruzada y evidencia verificable.
- **Skill candidata:** Instrucciones operativas o prompts de soporte que no se han validado en escenarios de ejecución.
- **Workflow candidato:** Un flujo multi-agente propuesto que no ha sido auditado.
- **Script candidato:** Herramientas locales o scripts de automatización no verificados en el entorno de ejecución real.

## 6. Principio "IA propone, sistema verifica, humano aprueba"
Este principio define los roles de interacción dentro del ciclo de desarrollo:
- **La IA propone:** El agente de inteligencia artificial investiga, diseña, documenta, redacta propuestas, implementa cambios en código o realiza revisiones técnicas preliminares.
- **El sistema verifica:** Se utilizan herramientas deterministas locales (como compiladores, linters, conjuntos de pruebas automatizadas o scripts verificadores) para asegurar mecánicamente que las propuestas de la IA son válidas y estables.
- **El humano aprueba:** El desarrollador o auditor humano valida las decisiones de diseño clave, los cierres de fases importantes y otorga el visto bueno definitivo antes de consolidar los cambios en el proyecto.

## 7. Principio de fuente de verdad
De acuerdo con el principio rector de fuente de verdad definido en [docs/00_mapa_y_gobernanza_documental.md](./00_mapa_y_gobernanza_documental.md), cada pieza de información del proyecto debe tener una única sede principal donde reside. Cabe destacar que el chat o la memoria de la conversación con la IA no constituyen una fuente de verdad del proyecto; únicamente los documentos y archivos aprobados y versionados en el repositorio Git representan la realidad oficial y actual de la iniciativa.

## 8. Principio de trazabilidad
Toda decisión importante de diseño, cambio estructural en la documentación o código, o cierre de fase en el ciclo de trabajo debe dejar evidencia verificable. Esto permite reconstruir la historia del proyecto y entender los motivos de cada cambio de dirección técnica o metodológica.

## 9. Principio anti-vibe coding
Se prohíbe el desarrollo de software o documentación guiado por impulsos, prompts sueltos o cambios improvisados sobre la marcha. Toda modificación relevante debe partir de una necesidad justificada, apoyarse en el contexto existente, definir un objetivo claro, marcar sus límites de alcance y contar con un mecanismo de validación explícito.

## 10. Principio de gates
Un gate (o puerta de control) es un punto de validación obligatorio que debe cruzarse antes de avanzar a la siguiente etapa de desarrollo. Un gate puede ser documental (por ejemplo, tener un plan de pruebas firmado), técnico (compilar correctamente), manual (aprobación humana escrita) o automatizado (tests unitarios exitosos). Si un gate falla, el proceso se detiene inmediatamente y no se permite continuar hasta corregir la falla o replanificar.

## 11. Principio de no duplicación
Una regla de negocio, decisión técnica, configuración o criterio organizativo debe vivir en un único documento maestro asignado. Si otros documentos o adaptadores operativos necesitan citar ese criterio, deben hacer una referencia directa mediante un enlace o puntero, en lugar de copiar el texto completo, reduciendo el riesgo de desactualizaciones en el futuro.

## 12. Principio de revisión cruzada
El creador o productor de un entregable no puede ser la única entidad encargada de validarlo y darlo por definitivo. Siempre debe existir un mecanismo de revisión independiente, que puede ser la revisión por un desarrollador humano, la auditoría de un agente revisor diferente, el paso por un checklist riguroso, o la ejecución de pruebas automatizadas.

## 13. Principio de cierre con evidencia
Una tarea, fase o requerimiento no se da por concluido por la simple declaración escrita del agente de desarrollo. El cierre de cada actividad debe estar respaldado por evidencia tangible y reproducible, tal como una diferencia de Git (diff), un reporte de validación o ejecución de tests cuando aplique, una lista de control (checklist) completada con rigor, o un commit específico en el historial de control de versiones.

## 14. Alcance actual y límites
Este documento define únicamente los principios metodológicos base y de interacción. Quedan explícitamente fuera del alcance de este archivo los siguientes desarrollos, los cuales se abordarán en entregas metodológicas específicas posteriores:
- Metodología específica para el desarrollo de software (arquitectura, ciclo SDD, QA).
- Metodología de proyectos documentales y agénticos (prompts, flujos de IA).
- Especificaciones funcionales y técnicas por feature (`specs/`).
- Habilidades y contratos agénticos (`.agent/skills/`).
- Flujos de trabajo multi-agente (`.agent/workflows/`).
- Adaptadores operativos inmediatos como `AGENTS.md` o `GEMINI.md`.
- Scripts locales de automatización, linters o gates técnicos (`scripts/`).

## 15. Estado del documento
- **Estado:** Borrador inicial.
- **Uso:** Base metodológica común para proyectos y documentos posteriores.
- **Pendiente:** Validar los principios transversales contra el documento maestro del arnés original y ajustar según los resultados de la primera prueba de integración.
