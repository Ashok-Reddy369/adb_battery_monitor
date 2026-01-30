import subprocess

def get_battery_level():
    """
    Returns battery percentage as integer using adb.
    """
    result = subprocess.run(
        ["adb", "shell", "dumpsys", "battery"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    if result.returncode != 0:
        raise RuntimeError("ADB command failed")

    for line in result.stdout.splitlines():
        if "level" in line:
            return int(line.split(":")[1].strip())

    raise ValueError("Battery level not found")

