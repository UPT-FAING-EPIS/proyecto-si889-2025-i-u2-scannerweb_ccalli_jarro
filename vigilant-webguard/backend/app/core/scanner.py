import uuid
import subprocess
import glob
import os
from datetime import datetime
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parent.parent.parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def cleanup_old_reports():
    """Elimina todos los archivos de reporte existentes para mantener solo el más reciente"""
    try:
        # Buscar todos los archivos JSON de reportes
        report_files = glob.glob(str(RESULTS_DIR / "scan_*.json"))
        for file_path in report_files:
            os.remove(file_path)
            print(f"Eliminado archivo anterior: {file_path}")
    except Exception as e:
        print(f"Error al limpiar archivos anteriores: {e}")

def get_output_path(tool: str, scan_id: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return RESULTS_DIR / f"scan_{tool}_{scan_id}_{timestamp}.json"

def run_tool(tool, cmd, scan_id):
    output_file = get_output_path(tool, scan_id)
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return {
            "scan_id": scan_id,
            "tool": tool,
            "status": "success" if res.returncode == 0 else "error",
            "output_file": str(output_file),
            "returncode": res.returncode,
            "stdout": res.stdout,
            "stderr": res.stderr
        }
    except subprocess.TimeoutExpired:
        return {"scan_id": scan_id, "tool": tool, "status": "timeout", "output_file": None}
    except Exception as e:
        return {"scan_id": scan_id, "tool": tool, "status": "exception", "error": str(e)}

def scan_target(target_url: str, engine: str = "wapiti"):
    # Limpiar archivos anteriores antes de generar el nuevo reporte
    cleanup_old_reports()
    
    scan_id = uuid.uuid4().hex
    if engine == "wapiti":
        # Parámetros optimizados para velocidad:
        # --max-depth 2: Limita la profundidad de escaneo
        # --max-files-per-dir 50: Limita archivos por directorio
        # --max-links-per-page 100: Limita enlaces por página
        # --timeout 10: Timeout más corto
        # --verify-ssl 0: Deshabilita verificación SSL para velocidad
        cmd = [
            "wapiti", "-u", target_url, 
            "-f", "json", 
            "-o", str(get_output_path("wapiti", scan_id)),
            "--max-depth", "2",
            "--max-files-per-dir", "50", 
            "--max-links-per-page", "100",
            "--timeout", "10",
            "--verify-ssl", "0",
            "--max-scan-time", "300"  # Máximo 5 minutos
        ]
        return run_tool("wapiti", cmd, scan_id)
    elif engine == "nikto":
        # Parámetros optimizados para Nikto
        cmd = [
            "nikto", "-h", target_url, 
            "-o", str(get_output_path("nikto", scan_id)), 
            "-Format", "txt",
            "-Tuning", "1,2,3,4,5",  # Solo pruebas básicas
            "-timeout", "10"
        ]
        return run_tool("nikto", cmd, scan_id)
    else:
        return {"scan_id": scan_id, "status": "error", "error": f"Motor '{engine}' no soportado"}
