# File: docs/adr/0001-nucleo-portable-y-adaptadores-agenticos.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar la decisión arquitectónica de mantener el arnés portable y desacoplado de motores agénticos específicos.
# Rol: Registro de decisión arquitectónica (ADR), estado propuesto.
# ──────────────────────────────────────────────────────────────────────

# ADR-0001 — Núcleo portable y adaptadores agénticos

## Estado
Propuesto

## Contexto
El proyecto raíz `proyecto_raiz_sdd_harness` busca construir un arnés metodológico y operativo reutilizable para guiar tareas de desarrollo y gobernanza documental, y no tiene como meta producir una aplicación de software final para el usuario. 

Para habilitar la asistencia automatizada en este entorno, se trabaja actualmente sobre la integración de los runtimes agénticos Antigravity y Codex. No obstante, el arnés no debe acoplarse permanentemente ni depender en exclusiva de una herramienta o motor concreto.

Existe una clara separación funcional dentro del repositorio entre:
- **Núcleo metodológico estable:** Los flujos y reglas generales de calidad del repositorio que deben ser interpretados y aplicados por cualquier agente o desarrollador humano.
- **Adaptadores operativos para motores concretos:** Archivos minimalistas diseñados específicamente como interfaces de inicio o adaptadores de contexto para los motores.
- **Sedes documentales conceptuales no activas:** Carpetas de plantillas y esquemas locales que definen el comportamiento deseado de los agentes sin interactuar directamente con el runtime del motor.

## Decisión
Se establecen las siguientes decisiones arquitectónicas sobre el diseño y la portabilidad del arnés:

1. **Portabilidad del Núcleo:** El núcleo del arnés se mantendrá portable y desacoplado de las herramientas o motores de ejecución específicos de IA.
2. **Componentes del Núcleo Estable:** La metodología base, la gobernanza de documentos, la constitución del proyecto, el directorio de especificaciones (`specs/`), las bitácoras de progreso (`progress/`), y los futuros esquemas y scripts deterministas de gates de validación forman parte de esta base metodológica estable e independiente.
3. **Tratamiento de Motores como Adaptadores:** Codex, Antigravity y cualquier runtime futuro serán tratados como adaptadores externos que consumen el núcleo metodológico, nunca como directores del mismo.
4. **Adaptadores Operativos Ligeros:** 
   - `AGENTS.md` actuará como adaptador operativo ligero de contexto inicial para Codex y agentes compatibles.
   - `GEMINI.md` actuará como adaptador operativo ligero de contexto inicial para Gemini y Antigravity.
5. **Aislamiento de la carpeta `.agent/`:** El directorio `.agent/` en la raíz se mantiene estrictamente como una sede documental y conceptual no activa del arnés.
6. **No Duplicación de Directorios:** No se creará la carpeta `.agents/` (en plural) durante la actual fase de MVP documental.
7. **Rutado de Descubrimiento Futuro:** La carpeta `.agents/` se evaluará en fases posteriores exclusivamente como una posible interfaz o adaptador real de descubrimiento para Codex, solo si se autoriza mediante una decisión explícita.
8. **No Movilidad ni Activación de Skills:** No se moverán, copiarán ni activarán skills desde la sede conceptual `.agent/skills/` hacia rutas activas o directorios de descubrimiento del sistema sin un ADR específico, una auditoría técnica formal y la aprobación explícita del desarrollador humano.
9. **Ausencia de Metadatos Activos:** No se incorporará front matter, parámetros tipados, YAML properties ni metadata activa de configuración a las plantillas conceptuales actuales de reglas, workflows o habilidades.
10. **Preservación del Desacoplamiento:** Cualquier futura integración de adaptadores, scripts o gates activos deberá realizarse garantizando la independencia y portabilidad del núcleo metodológico central.

## Consecuencias

### Consecuencias Positivas (Beneficios)
- **Menor dependencia de proveedores (Lock-in):** Facilita la transición o soporte simultáneo entre diversos proveedores de IA sin comprometer las metodologías del arnés.
- **Mayor portabilidad:** El repositorio sigue siendo una base de conocimientos y directrices técnicas robusta para agentes y humanos, incluso en ausencia de un motor activo.
- **Flexibilidad en el soporte de motores:** Permite la futura integración de Antigravity, Codex, modelos locales de código abierto u otros asistentes de desarrollo.
- **Mitigación del riesgo de refactorización:** Cambios drásticos en las API o esquemas de las herramientas de automatización solo afectarán a los adaptadores, manteniendo a salvo el núcleo metodológico.
- **Control riguroso sobre la activación agéntica:** Reduce significativamente la posibilidad de activaciones involuntarias en el workspace.

### Consecuencias Negativas o Costes (Trade-offs)
- **Mayor disciplina documental:** Exige un esfuerzo continuo del desarrollador y de los asistentes para mantener actualizada la separación entre el núcleo y los adaptadores.
- **Retraso en la automatización directa:** Puede desacelerar integraciones o activaciones de herramientas agénticas, requiriendo validaciones previas a nivel de diseño.
- **Doble mantenimiento conceptual/operativo:** Requiere mantener claras las diferencias entre un archivo puramente conceptual y una interfaz activa del runtime.
- **Complejidad metodológica:** Exige el diseño de matrices de equivalencia antes de proceder a la configuración real de adaptadores.

## Alternativas consideradas
1. **Enfoque Nativo Antigravity:** Organizar todo el arnés alrededor de la estructura exclusiva esperada por Antigravity. *Descartado por limitar la interoperabilidad con Codex y agentes basados en OpenAI.*
2. **Enfoque Nativo Codex:** Organizar el arnés priorizando la estructura y el descubrimiento de `.agents/`. *Descartado por comprometer la portabilidad y dificultar el uso de Gemini/Antigravity.*
3. **Duplicación Preventiva:** Duplicar de forma inmediata la estructura en `.agent/` y `.agents/` desde ahora. *Descartado por violar el criterio de no duplicación y el enfoque Lean, creando ruido estructural prematuro.*
4. **Núcleo Portable y Adaptadores:** Mantener un núcleo portable y desacoplado, tratando a Codex, Antigravity y futuras herramientas como capas de adaptadores externos. *Alternativa elegida por cumplir óptimamente con los requisitos de portabilidad, desacoplamiento y mantenimiento Lean.*

## Reglas derivadas
- Queda terminantemente prohibido crear el directorio `.agents/` sin una decisión de arquitectura autorizada.
- No se permite activar o trasladar skills, rules o workflows hacia rutas de descubrimiento de los runtimes sin una auditoría previa y su correspondiente ADR.
- Ninguna restricción o especificación propia de un runtime o motor agéntico podrá forzar cambios destructivos o dependencias directas en la metodología central estable.
- Los adaptadores operativos (`AGENTS.md` / `GEMINI.md`) deben limitarse a referenciar y conectar con el núcleo metodológico, evitando duplicar directrices o constitución.
- En caso de fallo, inoperabilidad o interrupción de servicio de los motores externos de IA, el núcleo metodológico del arnés debe seguir siendo usable por parte de un programador humano.

## Relación con documentos existentes
Este ADR expande las decisiones de gobernanza y portabilidad arquitectónica esbozadas en:
- [docs/00_mapa_y_gobernanza_documental.md](../00_mapa_y_gobernanza_documental.md) (Sección 5, subordinación y jerarquía).
- [docs/constitucion_del_proyecto.md](../constitucion_del_proyecto.md) (Límites y alcance).
- [docs/02_metodologia_desarrollo_software_sdd_harness.md](../02_metodologia_desarrollo_software_sdd_harness.md) (Harness y adaptadores).
- Adaptadores generales [AGENTS.md](../../AGENTS.md) y [GEMINI.md](../../GEMINI.md).
- [progress/auditoria_compatibilidad_antigravity_codex_2026-06-02.md](../../progress/auditoria_compatibilidad_antigravity_codex_2026-06-02.md) (Hallazgos y riesgos de nomenclatura).

## Estado de implementación
Este ADR registra una decisión de diseño de alto nivel. **No implementa ningún recurso técnico**, no activa habilidades agénticas, no crea la carpeta `.agents/`, no modifica la sede conceptual `.agent/` y no activa reglas de Antigravity en el workspace.

## Criterios para revisar esta decisión en el futuro
Este registro deberá ser evaluado y revisado si:
- Se producen cambios significativos en el formato de descubrimiento de skills de Codex que obliguen a replantear el desacoplamiento.
- Antigravity introduce nuevos estándares incompatibles con adaptadores de texto plano.
- Se autoriza formalmente la transición de la primera skill documental del arnés hacia un estado activo.
- Se aprueba la creación de la carpeta `.agents/` para iniciar pruebas prácticas en Codex.
- Se inicia la codificación de scripts deterministas de gates de validación.
- Se requiera incorporar soporte para modelos de lenguaje locales (LLMs locales) o APIs de nuevos proveedores.
