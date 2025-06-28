import uuid
import subprocess
from datetime import datetime
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parent.parent.parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

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
    scan_id = uuid.uuid4().hex
    if engine == "wapiti":
        cmd = ["wapiti", "-u", target_url, "-f", "json", "-o", str(get_output_path("wapiti", scan_id))]
        return run_tool("wapiti", cmd, scan_id)
    elif engine == "nikto":
        cmd = ["nikto", "-h", target_url, "-o", str(get_output_path("nikto", scan_id)), "-Format", "txt"]
        return run_tool("nikto", cmd, scan_id)
    else:
        return {"scan_id": scan_id, "status": "error", "error": f"Motor '{engine}' no soportado"}
