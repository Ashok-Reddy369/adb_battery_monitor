from ppadb.client import Client as AdbClient
import re

class ADBBatteryTester:
    BATTERY_HEALTH_MAP = {
        1: "Unknown",
        2: "Good",
        3: "Overheat",
        4: "Dead",
        5: "Over Voltage",
        6: "Failure",
        7: "Cold",
    }

    def __init__(self, serial=None):
        self.client = AdbClient(host="127.0.0.1", port=5037)
        self.devices = self.client.devices()
        self.device = self.devices[0] if not serial else self.client.device(serial)

    def get_battery_stats(self):
        """Extract battery health, level, temperature"""
        raw = self.device.shell("dumpsys battery")
        stats = {}

        for line in raw.splitlines():
            if "level:" in line:
                m = re.search(r"level:\s*(\d+)", line)
                if m:
                    stats["level"] = int(m.group(1))

            elif "health:" in line:
                m = re.search(r"health:\s*(\d+)", line)
                if m:
                    code = int(m.group(1))
                    stats["health"] = self.BATTERY_HEALTH_MAP.get(code, "Unknown")

            elif "temperature:" in line:
                m = re.search(r"temperature:\s*(\d+)", line)
                if m:
                    stats["temperature"] = int(m.group(1)) / 10

        # Safety check
        required = ["level", "health", "temperature"]
        missing = [k for k in required if k not in stats]
        if missing:
            raise RuntimeError(f"Incomplete battery stats: missing {missing}")

        return stats

    def is_healthy(self, stats):
        return (
            stats.get("health") in ["Good", "Excellent"]
            and stats.get("level", 0) > 20
            and stats.get("temperature", 100) < 45
        )
