# File: docs/constitucion_del_proyecto.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Establecer las reglas no negociables y límites normativos del proyecto raíz.
# Rol: Documento constitucional rector de gobernanza y límites del arnés.
# ──────────────────────────────────────────────────────────────────────

# Constitución del proyecto raíz

## 1. Propósito del documento

Este documento define la constitución del proyecto raíz `proyecto_raiz_sdd_harness` y establece las reglas y principios fundamentales no negociables que rigen su desarrollo. Estas directrices son de obligado cumplimiento para todos los actores que interactúen con el repositorio: desarrolladores humanos, agentes de inteligencia artificial, herramientas de automatización, workflows y adaptadores operativos de contexto. Su fin último es mantener la coherencia, la gobernanza, la trazabilidad y la calidad metodológica verificable del arnés.

## 2. Relación con el mapa y la metodología

Este documento actúa como la base normativa del proyecto raíz y se relaciona con el ecosistema de la siguiente manera:
- **Subordinación documental:** Se subordina de forma directa al mapa de gobernanza detallado en [docs/00_mapa_y_gobernanza_documental.md](./00_mapa_y_gobernanza_documental.md).
- **Aplicación de principios:** Adopta y operacionaliza los principios metodológicos transversales definidos en [docs/01_metodologia_base_comun.md](./01_metodologia_base_comun.md).
- **Complemento técnico:** Complementa la metodología de software plasmada en [docs/02_metodologia_desarrollo_software_sdd_harness.md](./02_metodologia_desarrollo_software_sdd_harness.md), transformando sus directrices en reglas duras y límites de diseño.
- **Independencia operativa:** Define la capa normativa superior y no reemplaza a los archivos operativos locales (`AGENTS.md`, `GEMINI.md`), ni a los recursos ejecutables o de diseño como skills (`.agent/skills/`), workflows (`.agent/workflows/`) o especificaciones por feature (`specs/`).
- **No duplicación normativa:** Esta constitución define reglas no negociables. Los adaptadores operativos, rules, skills, workflows y specs deben referenciarla y aplicarla, pero no copiarla completa ni reinterpretarla como una fuente normativa paralela.

## 3. Regla de fuente de verdad

La única fuente oficial de verdad y conocimiento técnico en este proyecto reside en los documentos y especificaciones aprobados, consolidados y versionados dentro del repositorio Git.
- **Exclusiones:** El chat de comunicación, la memoria temporal de las sesiones de conversación, los comentarios efímeros o las declaraciones directas de los agentes no constituyen bajo ninguna circunstancia una fuente oficial de verdad.
- **Punteros:** Cualquier duda de interpretación debe ser contrastada con la documentación oficial del repositorio.

## 4. Regla de no improvisación

Queda estrictamente prohibida la ejecución de cualquier cambio relevante por impulso, basado en prompts informales o como decisión de desarrollo tomada de forma aislada y unilateral por los agentes de IA.
- **Requisitos de cambio:** Todo cambio relevante en el repositorio debe estar sustentado formalmente en una necesidad documentada, contar con contexto claro, objetivos específicos, límites de alcance precisos y un mecanismo explícito de verificación y validación técnica.

## 5. Regla de entregable candidato

Todo artefacto o resultado generado por una inteligencia artificial o agente de desarrollo —incluyendo documentos de diseño, código fuente, skills, scripts de gates o workflows— se considerará estrictamente un "entregable candidato" (preliminar).
- **Falta de definitividad:** Ningún entregable se considerará consolidado o definitivo simplemente porque un agente o herramienta de IA lo declare como finalizado o completado en sus mensajes.
- **Requisito de aceptación:** Deberá someterse al proceso formal de validación y auditoría correspondiente a su naturaleza antes de ser aceptado.

## 6. Regla de autonomía controlada

Los agentes de inteligencia artificial gozan de autonomía limitada para la ejecución y resolución de tareas de bajo impacto, poco riesgo y que cuenten con criterios de aceptación claros y explícitos.
- **Elevación y revisión obligatoria:** Ante cualquier duda razonable, sospecha de impacto funcional imprevisto, riesgo técnico en el código, afectación a la arquitectura del sistema, alteración de datos reales, modificación de permisos, incremento potencial de costes, despliegues en entornos de producción o integraciones de terceros, el agente debe detenerse y elevar la decisión a una revisión humana o a una revisión cruzada formal antes de continuar.

## 7. Regla de revisión cruzada

Bajo el principio de que quien produce un entregable no puede ser el único encargado de validarlo y declararlo definitivo, todo cambio debe superar un filtro de revisión independiente.
- **Autoauditoría:** La autoauditoría interna realizada por el propio agente sirve como primer filtro o verificación inicial de calidad, pero de ningún modo sustituye ni equivale al visto bueno o aprobación final de cambios con impacto técnico relevante.
- **Validación independiente:** La aprobación final requerirá una revisión independiente realizada por otro rol (desarrollador humano, agente revisor independiente o gates automáticos configurados).

## 8. Regla de validación y gates

Los gates (puntos de control y calidad) definidos para el proyecto —ya sean documentales, técnicos, manuales o automatizados— son de cumplimiento obligatorio en todas las transiciones del ciclo de vida de desarrollo.
- **Comportamiento ante fallos:** Si un gate de validación falla, el flujo de desarrollo se detiene inmediatamente. Está prohibido saltarse el gate o intentar aplicar parches rápidos a ciegas en el código para forzar su cumplimiento; se debe diagnosticar el error, corregir el entregable candidato o replanificar el diseño.

## 9. Regla de código candidato

Cualquier cambio propuesto al código fuente del sistema (código candidato) debe alinearse con criterios estrictos de calidad y mantenimiento antes de consolidarse en la rama principal:
- **Preservación y no regresión:** Debe conservar intacta la funcionalidad preexistente y evitar activamente la introducción de regresiones. Esta preservación debe validarse con pruebas unitarias, pruebas de integración, smoke test, checklist o validación manual documentada, según el tipo, riesgo e impacto del cambio.
- **Limpieza y legibilidad:** Debe ser limpio, estructurado y seguir las reglas de formato del proyecto.
- **No redundancia:** No debe incorporar código muerto, comentarios redundantes u obsoletos, duplicación innecesaria ni trazas de depuración persistentes (como prints o logs no estructurados).
- **Evidencia verificable:** Debe superar la validación determinista local, la revisión cruzada obligatoria y aportar evidencia reproducible de su correcto funcionamiento.

## 10. Regla de documentación mínima necesaria

De acuerdo con el enfoque LEAN, se debe evitar la burocracia inútil, pero esto no exime bajo ningún concepto de documentar el desarrollo.
- **Inclusión obligatoria:** La documentación mínima necesaria (especificaciones, justificación de aclaraciones, diseño técnico de características, planes de pruebas, reportes de validación y registros de decisiones) se considera parte integral e imprescindible del entregable.
- **Cierre de tareas:** Ningún cambio en el software o su arquitectura podrá cerrarse formalmente sin su documentación correspondiente.

## 11. Regla de seguridad y datos sensibles

Cualquier propuesta de cambio o acción operativa que involucre la gestión de credenciales, datos personales, información confidencial, permisos de acceso y roles, variables de entorno sensibles, configuraciones de seguridad, pasarelas de pago, costes de infraestructura o integraciones con servicios externos críticos exige un protocolo de seguridad reforzado.
- **Requisito obligatorio:** Requiere una revisión detallada de diseño técnico, aprobación humana explícita y validación manual exhaustiva documentada por parte de un desarrollador humano.

## 12. Regla de dependencias y arquitectura

Se prohíbe explícitamente agregar nuevas dependencias de librerías, realizar cambios estructurales en la arquitectura limpia, modificar contratos de APIs o alterar los modelos o estructuras de base de datos sin una justificación técnica documentada y la aprobación del desarrollador humano.
- **Registro histórico:** Si la decisión es aprobada por su alta importancia técnica, deberá quedar documentada y registrada cronológicamente mediante un Architecture Decision Record (ADR) una vez que la carpeta de gobernanza técnica `docs/adr/` esté habilitada en el repositorio.

## 13. Regla de compatibilidad con Codex y Antigravity

El diseño metodológico y las normas del proyecto raíz deben garantizar la portabilidad y la independencia de la plataforma.
- **Adaptadores:** Los archivos y directrices como `AGENTS.md`, `GEMINI.md`, reglas locales de contexto, skills y workflows actúan estrictamente como adaptadores operativos para ajustar la ejecución en Codex, Antigravity u otras herramientas de IA.
- **Subordinación:** En ningún caso estos adaptadores podrán duplicar, contradecir o ignorar las normas establecidas en esta constitución ni en los documentos base de la carpeta `docs/`.

## 14. Regla de trazabilidad

Toda modificación relevante, decisión estructural, aprobación, cambio en el estado de una feature, bloqueo detectado o cierre de tarea debe dejar un rastro claro y verificable en el repositorio.
- **Tipos de evidencia:** La trazabilidad se respaldará mediante registros físicos como diferencias de Git (diffs), commits atómicos bien documentados, reportes automáticos de pruebas, checklists firmados por humanos o actualizaciones formales de la documentación de seguimiento del avance.

## 15. Regla de límites del MVP actual

El proyecto se encuentra en una etapa de Producto Mínimo Viable (MVP).
- **Límites de uso:** Mientras no se encuentren definidas y aprobadas las plantillas documentales para la carpeta `specs/`, los adaptadores operativos para las IAs (`AGENTS.md`, `GEMINI.md`), las skills de soporte básicas y los scripts correspondientes a los gates de calidad técnicos y automatizados, el arnés de desarrollo no podrá ser utilizado por agentes de implementación automática para modificar código real de proyectos derivados. En ningún caso podrá usarse sobre producción sin aprobación humana explícita, gates mínimos y validación documentada.
- **Usos permitidos actuales:** Durante esta fase, su aplicación se restringe estrictamente a tareas de planificación, documentación conceptual, simulaciones en entornos locales y de desarrollo controlados, y pruebas piloto sin impacto directo en producción.

## 16. Regla de modificación de la constitución

La constitución del proyecto raíz representa el núcleo normativo de estabilidad de la gobernanza, por lo que no puede ser modificada de manera casual o improvisada.
- **Requisitos de cambio:** Cualquier enmienda o actualización a este documento debe cumplir rigurosamente los siguientes pasos:
  1. Justificación y explicación explícita del motivo del cambio.
  2. Revisión técnica cruzada exhaustiva.
  3. Evidencia clara de aprobación en el control de cambios de Git.
  4. Garantía de no contradicción con el mapa de gobernanza documental principal ([docs/00_mapa_y_gobernanza_documental.md](./00_mapa_y_gobernanza_documental.md)).
  5. Aprobación explícita del administrador humano antes de considerarse vigente en el repositorio.

## 17. Estado del documento

- **Estado:** Borrador inicial.
- **Uso:** Reglas no negociables del proyecto raíz.
- **Pendiente:** Someter el documento a auditoría técnica contra las metodologías descritas en `01` y `02` para ajustar detalles normativos tras finalizar la primera prueba real del arnés agéntico.
