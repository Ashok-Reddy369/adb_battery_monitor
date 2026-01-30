from datetime import datetime
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class BatteryReport:
    def __init__(self, report_dir="reports"):
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(exist_ok=True)

    def generate(self, stats, adb_log_file, device_serial):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = self.report_dir / f"battery_report_{ts}.txt"

        logger.info(f" Generating battery report → {report_file}")

        with open(report_file, "w") as f:
            f.write("ADB BATTERY HEALTH REPORT\n")
            f.write("=" * 40 + "\n")
            f.write(f"Timestamp     : {datetime.now()}\n")
            f.write(f"Device Serial : {device_serial}\n\n")

            f.write("Battery Stats:\n")
            for k, v in stats.items():
                f.write(f"  {k:<12}: {v}\n")

            f.write("\nADB Logs:\n")
            f.write(f"  {adb_log_file}\n")

            verdict = "PASS" if stats["health"] in ["Good", "Excellent"] else "FAIL"
            f.write("\nFinal Verdict:\n")
            f.write(f"  Battery Health: {verdict}\n")

        return report_file
