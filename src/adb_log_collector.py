import subprocess
from datetime import datetime
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class ADBLogCollector:
    def __init__(self, log_dir="adb_logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

    def collect_logcat(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logfile = self.log_dir / f"logcat_{timestamp}.txt"

        logger.info(f"📥 Collecting adb logcat → {logfile}")

        with open(logfile, "w") as f:
            subprocess.run(
                ["adb", "logcat", "-d"],
                stdout=f,
                stderr=subprocess.STDOUT
            )

        return logfile
