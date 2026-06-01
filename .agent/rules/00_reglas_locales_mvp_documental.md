# File: .agent/rules/00_reglas_locales_mvp_documental.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir las reglas locales documentales y de contexto para la interacción de agentes en el MVP.
# Rol: Regla local documental y no activa (no ejecutable) del arnés.
# ──────────────────────────────────────────────────────────────────────

# Reglas locales del MVP documental

## Descripción
Pautas operativas y de control diseñadas para regular el comportamiento de los agentes de IA en el repositorio, definiendo límites de Git, uso de modelos y contención metodológica.

---

## 1. Propósito
Este documento define las reglas de conducta operativa que deben seguir los agentes o asistentes de IA (como Antigravity) al interactuar con este repositorio. Su fin es evitar la ejecución de cambios fuera del alcance, estandarizar el uso seguro de Git, optimizar el uso de tokens mediante la elección del modelo idóneo y mantener el aislamiento de la fase documental.

## 2. Estado actual
* **Estado actual:** Documental / No activa / No ejecutable.
* **Límite operativo:** Este archivo no es una regla activa de Antigravity (no posee metadatos de configuración o glob triggers de comportamiento activo). Funciona únicamente como directriz de consulta conceptual de solo lectura durante la actual fase de Producto Mínimo Viable (MVP).

## 3. Fuentes de verdad
El agente debe contrastar sus decisiones de contexto con los siguientes documentos rectores:
- [docs/constitucion_del_proyecto.md](../../docs/constitucion_del_proyecto.md) (Reglas no negociables).
- [docs/00_mapa_y_gobernanza_documental.md](../../docs/00_mapa_y_gobernanza_documental.md) (Mapa documental, jerarquía y fuente de verdad).
- [progress/current.md](../../progress/current.md) (Punto de control de estado operativo).

## 4. Regla de fase documental / MVP estructural
El repositorio se encuentra estrictamente en fase documental y estructural. Ningún agente debe intentar escribir código de producto ni activar configuraciones ejecutables en el workspace. El enfoque exclusivo es la elaboración y auditoría de la documentación del arnés.

## 5. Regla de no automatización activa
Queda prohibido activar o configurar hooks agénticos, disparadores de ejecución en segundo plano, tareas automáticas programadas de Antigravity u otros runtimes. Todo flujo de transiciones (como los definidos en los workflows) debe ser conceptualizado e inspeccionado de manera manual.

## 6. Regla de no modificación de código real
Los agentes de IA no tienen autorización para realizar modificaciones operativas sobre código fuente real de proyectos derivados o en producción. La estructura de código permanece congelada durante la actual fase.

## 7. Regla de alcance estricto
El agente debe ceñirse única y exclusivamente a las rutas de archivos que el desarrollador humano defina como "permitidos" en cada solicitud. Está terminantemente prohibido crear, alterar, renombrar o eliminar cualquier archivo o directorio catalogado bajo las rutas "prohibidas".

## 8. Regla de modelos y ahorro de tokens
Para maximizar la eficiencia y optimizar el uso de los recursos de cómputo, se establecen las siguientes reglas de selección de modelo:
- **Gemini 3.5 Flash Low:** Debe utilizarse de forma obligatoria para tareas mecánicas o repetitivas de bajo riesgo cognitivo. Esto incluye la ejecución de comandos `git status`, comandos de validación, preparación de archivos (*stage*), creación de commits y publicaciones con `git push`.
- **Gemini 3.5 Flash Medium:** Solo debe emplearse para tareas de creación documental técnica, síntesis conceptual compleja o resolución de inconsistencias profundas que realmente lo requieran y que cuenten con autorización del humano.
- **Modelos superiores (High):** No se deben utilizar para tareas de administración, microcorrecciones o automatizaciones mecánicas repetitivas. Su uso queda restringido a revisiones de contraste estructural globales.
- **Ahorro de tokens en diffs:** Si un diff de Git es grande, el agente no debe intentar imprimirlo o volcarlo en el chat en su totalidad. El desarrollador humano entregará el archivo completo para auditoría externa si es necesario.

## 9. Regla de diffs cortos y archivos largos
Cuando se requiera revisar el estado del código o la documentación:
- Se debe priorizar la lectura acotada de líneas específicas con las herramientas del IDE en lugar de imprimir bloques masivos en el chat.
- Si el agente necesita validar un archivo largo que sobrepasa los límites de lectura ordinaria de la sesión, debe solicitar al humano que le provea el archivo completo o las secciones pertinentes, o usar herramientas locales de búsqueda cuando estén autorizadas para ir a las líneas de interés.

## 10. Regla de commits atómicos
Para conservar la trazabilidad y limpieza del historial de Git, cada cambio en el repositorio debe confirmarse de forma atómica:
- No se deben mezclar modificaciones de distinta naturaleza en el mismo commit (por ejemplo, correcciones de estilo mezcladas con adiciones estructurales de workflows).
- Cada commit debe resolver una única tarea del ciclo de vida y estar acompañado de un mensaje claro que use prefijos del estándar convencional (ej. `docs:`, `chore:`).

## 11. Regla de Git segura
El uso de Git por parte de los asistentes técnicos de Git se rige por las siguientes restricciones:
- **Prohibición de adiciones masivas:** No se permite usar `git add .` ni `git add -A`. Todos los archivos se deben preparar de forma selectiva especificando sus rutas exactas.
- **Contención de alcance:** Si la salida de `git status --short` muestra archivos modificados, eliminados o sin rastrear que se encuentran fuera del alcance de la tarea, el agente debe detenerse, cancelar el commit y reportar el estado de bloqueo al desarrollador humano.
- **Limpieza antes del push:** No se debe ejecutar `git push` si el working tree del repositorio muestra archivos modificados o sin rastrear pendientes tras haber realizado el commit.
- **Operaciones prohibidas:** Queda prohibida la ejecución de `git push --force`, rebase de ramas, resolución automática de fusiones (*merge*) y cambios de rama sin autorización expresa.

## 12. Regla de no duplicación documental
De acuerdo con el principio de fuente de verdad del arnés, ninguna regla, directriz o estándar debe duplicarse en su totalidad en múltiples archivos. Si un concepto ya reside en la constitución o metodología principal, este documento de reglas debe limitarse a referenciarlo mediante enlaces relativos directos.

## 13. Regla de revisión cruzada
El agente no se autoaprueba. Todo reporte o propuesta de cambio generada debe considerarse un "entregable candidato" en espera de la aprobación del desarrollador humano o de la auditoría independiente de un revisor técnico.

## 14. Regla de bloqueo
Ante la aparición de cualquier duda de requerimientos, incompatibilidades con la constitución o comportamientos imprevistos en el entorno del repositorio, el agente debe pausar la tarea, clasificar el estado como `blocked` y documentar de forma explícita el motivo.

## 15. Límites del MVP actual
Queda estrictamente prohibido realizar cualquiera de las siguientes acciones en el espacio de trabajo actual:
- Crear el directorio `.agent/gates/`.
- Crear o programar scripts de ejecución de gates automatizados (como `scripts/gate_0_preflight.py`).
- Crear pruebas unitarias o tests de software reales.
- Crear directorios de especificaciones reales de features dentro de `specs/`.
- Habilitar o activar reglas, workflows o skills operativas en Antigravity.
- Alterar el comportamiento del software de proyectos derivados.
- Modificar este documento para que actúe como configuración ejecutable.

## 16. Nota de compatibilidad futura
Cuando esta regla pase de estado documental a estado activo, deberá adaptarse formalmente a la sintaxis del motor agéntico correspondiente. Esto incluirá la adición de metadatos o glob triggers requeridos (como `name`, `description`, `trigger`, `glob`, `alwaysApply` o equivalentes), validando la integración segura en Codex, Antigravity u otros runtimes autorizados.

Mientras el proyecto continúe en fase documental / MVP estructural, este archivo carecerá de front matter y no se interpretará como recurso ejecutable.
