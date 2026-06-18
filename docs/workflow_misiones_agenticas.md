# File: docs/workflow_misiones_agenticas.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el workflow conceptual de misiones agénticas del arnés.
# Rol: Especificación conceptual del flujo de trabajo y transiciones de misiones.
# ──────────────────────────────────────────────────────────────────────

# Workflow Conceptual de Misiones Agénticas

## 1. Propósito
Este documento define el workflow conceptual que conecta el [docs/contrato_misiones_agenticas.md](./contrato_misiones_agenticas.md) con el [docs/mapa_roles_agenticos.md](./mapa_roles_agenticos.md). Su objetivo es estructurar las etapas secuenciales por las que pasa una misión delegada a una Inteligencia Artificial, garantizando el control del desarrollador humano.

## 2. Relación con el contrato de misiones agénticas
El workflow describe la secuencia temporal para dar cumplimiento a los parámetros de entrada y salida del contrato de misiones. Regula el proceso desde la redacción de los requisitos de entrada hasta la validación y consolidación de los resultados de salida.

## 3. Relación con el mapa de roles agénticos
El workflow distribuye las responsabilidades en cada paso a los roles definidos en el mapa de roles, asegurando que participen los agentes adecuados (Planificador, Implementador, Auditores) y reservando las decisiones de firma al Humano Director.

## 4. Principios del workflow
* **Seguridad y Control Humano**: Toda transición crítica, commit o push requiere visto bueno humano explícito.
* **Trazabilidad estricta**: Cada etapa del flujo debe dejar evidencia verificable en el repositorio.
* **Independencia técnica**: Agnóstico de la herramienta de IA (Codex, Antigravity, etc.).

## 5. Flujo general de una misión
El ciclo de vida de una misión sigue la siguiente secuencia lógica:
```text
1. Solicitud humana -> 2. Planeación -> 3. Validación previa -> 4. Ejecución controlada 
-> 5. Auditoría -> 6. Revisión simplicidad -> 7. Reporte final -> 8. Aprobación humana
-> 9. Commit y push controlado
```

## 6. Etapa 1 — Solicitud humana
* **Descripción**: El Humano Director plantea una necesidad o un objetivo al arnés.
* **Roles involucrados**: Humano Director y Agente Orquestador.

## 7. Etapa 2 — Planeación de la misión
* **Descripción**: El Agente Planificador convierte la solicitud en una misión autocontenida usando el formato de contrato de misiones (mejorado conceptualmente por `improve_plan`).
* **Roles involucrados**: Agente Planificador.

## 8. Etapa 3 — Validación previa
* **Descripción**: Se verifica la limpieza del área de trabajo (estado Git) y que la misión candidatos no viole las exclusiones.
* **Roles involucrados**: Agente Auditor Técnico.

## 9. Etapa 4 — Ejecución controlada
* **Descripción**: El Agente Implementador realiza los cambios estrictamente autorizados en el allowlist del contrato de misiones.
* **Roles involucrados**: Agente Implementador.

## 10. Etapa 5 — Auditoría documental/técnica
* **Descripción**: Se ejecutan las validaciones obligatorias de Git (diffs) y los gates deterministas locales autorizados.
* **Roles involucrados**: Agente Auditor Documental y Agente Auditor Técnico.

## 11. Etapa 6 — Revisión de simplicidad
* **Descripción**: Se audita el código o documentación candidato para asegurar que no inyecta sobreingeniería ni capas innecesarias.
* **Roles involucrados**: Auditor de Simplicidad (`ponytail_review`).

## 12. Etapa 7 — Reporte final
* **Descripción**: El Agente Orquestador consolida los resultados y evidencias de salida en un reporte final y actualiza el snapshot en `progress/`.
* **Roles involucrados**: Agente Orquestador y Documentador Mínimo.

## 13. Etapa 8 — Aprobación humana
* **Descripción**: El Humano Director evalúa el reporte final, los diffs y el cumplimiento de los objetivos para dar su dictamen.
* **Roles involucrados**: Humano Director.

## 14. Etapa 9 — Commit y push controlado
* **Descripción**: Tras la aprobación, se realiza el commit selectivo de los cambios y el push correspondiente de manera manual o asistida.
* **Roles involucrados**: Humano Director y Agente Orquestador.

## 15. Condiciones de STOP
La misión detendrá su flujo inmediatamente si ocurre:
* Árbol Git sucio no esperado antes de iniciar.
* Fallo en cualquier gate local.
* Intento de modificar archivos no autorizados en el allowlist.
* Ambigüedad técnica en el objetivo o supuestos.
* Necesidad de crear archivos nuevos no registrados.
* Necesidad de usar runtime bloqueado (`uv`, `pytest`, `.agent/`).

## 16. Evidencia mínima por etapa
* **Planeación**: Plantilla de misión candidatos.
* **Ejecución**: Listado de archivos intervenidos.
* **Auditoría**: Salida de comandos `git status`, `git diff --stat` y `git diff --unified=0`.
* **Aprobación**: Mensaje del dictamen aprobatorio del humano.

## 17. Qué no autoriza este workflow
Este documento modela el flujo de trabajo conceptual y documental. No autoriza la programación, codificación, instalación de dependencias, automatización activa en segundo plano en `.agent/` ni uso de CLI lógicas en esta fase.
