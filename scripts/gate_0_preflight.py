# scripts/gate_0_preflight.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Verificación automatizada mínima del arnés.
# Rol: Gate determinista básico sin dependencias externas para auditoría local.
# ──────────────────────────────────────────────────────────────────────

import os
import sys
import subprocess

# Archivos y rutas clave
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MINIMUM_DOCUMENTS = [
    "README.md",
    "progress/current.md",
    "progress/feature_list.md",
    "progress/history.md",
    "progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md"
]

FORBIDDEN_DEPENDENCIES = [
    "requirements.txt",
    "pyproject.toml",
    "uv.lock"
]

FORBIDDEN_PYTEST = [
    "pytest.ini",
    "conftest.py"
]

ALLOWED_MODIFIED_FILES = [
    "README.md",
    "docs/00_mapa_y_gobernanza_documental.md",
    "docs/contrato_misiones_agenticas.md",
    "docs/gate_0_preflight_definicion.md",
    "docs/politica_zonas_repositorio.md",
    "progress/README.md",
    "progress/current.md",
    "progress/feature_list.md",
    "progress/history.md",
    "progress/plan_implementacion_v0_1_proyecto_raiz_sdd_harness.md",
    "scripts/README.md"
]

MAINTENANCE_ALLOWED_FILES = [
    "scripts/gate_0_preflight.py",
    "AGENTS.md",
    "GEMINI.md",
    "scripts/README.md"
]

def print_result(check_name, success, message=""):
    status = "OK" if success else "FAIL"
    print(f"[{status}] {check_name}: {message}")

def check_gitignore_exists():
    path = os.path.join(ROOT_DIR, ".gitignore")
    exists = os.path.exists(path)
    print_result("Existe .gitignore", exists, "Encontrado" if exists else "No se encuentra el archivo .gitignore en la raíz")
    return exists

def check_venv_ignored():
    try:
        # Usar git check-ignore -q .venv/ como fuente de verdad
        result = subprocess.run(
            ["git", "check-ignore", "-q", ".venv/"],
            cwd=ROOT_DIR
        )
        # Si devuelve código de salida 0, significa que .venv/ está efectivamente ignorado
        ignored = (result.returncode == 0)
        print_result("Ignorado de .venv", ignored, ".venv/ está correctamente ignorado por Git" if ignored else ".venv/ no está ignorado por Git")
        return ignored
    except Exception as e:
        print_result("Ignorado de .venv", False, f"Error al ejecutar git check-ignore: {e}")
        return False

def check_unauthorized_files():
    found_any = False
    for filename in FORBIDDEN_DEPENDENCIES:
        path = os.path.join(ROOT_DIR, filename)
        if os.path.exists(path):
            print_result(f"Archivo prohibido: {filename}", False, f"Se ha detectado {filename}")
            found_any = True
    
    success = not found_any
    if success:
        print_result("Archivos de dependencias", True, "No se detectan requirements.txt, pyproject.toml ni uv.lock")
    return success

def check_pytest_files():
    found_any = False
    for filename in FORBIDDEN_PYTEST:
        path = os.path.join(ROOT_DIR, filename)
        if os.path.exists(path):
            print_result(f"Archivo de pytest prohibido: {filename}", False, f"Se ha detectado {filename}")
            found_any = True
    
    success = not found_any
    if success:
        print_result("Archivos de pytest", True, "No se detectan pytest.ini ni conftest.py")
    return success

def check_required_documents():
    missing = []
    for rel_path in MINIMUM_DOCUMENTS:
        path = os.path.join(ROOT_DIR, rel_path)
        if not os.path.exists(path):
            missing.append(rel_path)
    
    success = len(missing) == 0
    print_result("Documentos mínimos", success, "Todos presentes" if success else f"Faltan: {', '.join(missing)}")
    return success

def check_unauthorized_git_changes(maintenance_mode):
    try:
        # Ejecutar git status --short
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True
        )
        
        lines = result.stdout.strip().split("\n")
        unauthorized = []
        
        # Unir las listas de permitidos dependiendo del modo
        allowed_list = list(ALLOWED_MODIFIED_FILES)
        if maintenance_mode:
            allowed_list.extend(MAINTENANCE_ALLOWED_FILES)
            
        for line in lines:
            if not line.strip():
                continue
            
            # Formato clásico de git status --short: "XY path" o "XY "path""
            parts = line.strip().split(maxsplit=1)
            if len(parts) < 2:
                continue
            
            status_code, filepath = parts[0], parts[1].strip('"')
            # Normalizar barra para Windows / Linux
            filepath_norm = filepath.replace("\\", "/")
            
            # Omitir archivos que estén en la lista de permitidos
            is_allowed = False
            for allowed in allowed_list:
                if filepath_norm == allowed:
                    is_allowed = True
                    break
            
            if not is_allowed:
                unauthorized.append(f"{filepath_norm} ({status_code})")
        
        success = len(unauthorized) == 0
        print_result("Cambios de Git autorizados", success, "Ningún cambio no autorizado" if success else f"Cambios no autorizados detectados en: {', '.join(unauthorized)}")
        return success
        
    except Exception as e:
        print_result("Cambios de Git autorizados", False, f"Error al ejecutar git status: {e}")
        return False

def main():
    print("=== INICIANDO PREFLIGHT GATE 0 ===")
    
    # Comprobar modo mantenimiento
    maintenance_mode = os.environ.get("GATE_PREFLIGHT_MAINTENANCE") == "1"
    if maintenance_mode:
        print("[NOTA] Modo mantenimiento ACTIVO. Se permiten modificaciones temporales en el script de preflight.")
        
    checks = [
        check_gitignore_exists(),
        check_venv_ignored(),
        check_unauthorized_files(),
        check_pytest_files(),
        check_required_documents(),
        check_unauthorized_git_changes(maintenance_mode)
    ]
    
    print("==================================")
    if all(checks):
        print(">> Verificación exitosa. Todo correcto.")
        sys.exit(0)
    else:
        print(">> VERIFICACIÓN FALLIDA. Se detectaron incumplimientos críticos.")
        sys.exit(1)

if __name__ == "__main__":
    main()
