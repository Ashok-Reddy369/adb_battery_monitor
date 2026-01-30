import pytest
from src.battery_tester import ADBBatteryTester
from src.adb_log_collector import ADBLogCollector
from src.report_generator import BatteryReport


@pytest.mark.device
def test_adb_connection(battery_tester):
    assert battery_tester.devices, "No ADB devices connected"
    print(f" Connected: {battery_tester.device.serial}")

@pytest.mark.battery
@pytest.mark.device
def test_battery_health(battery_tester, caplog):
    caplog.set_level("INFO")

    #  Battery stats
    stats = battery_tester.get_battery_stats()

    #  Text adb logs
    adb_logs = ADBLogCollector()
    log_file = adb_logs.collect_logcat()

    #  Text report
    report = BatteryReport(report_dir="reports/text")
    report.generate(
        stats=stats,
        adb_log_file=log_file,
        device_serial=battery_tester.device.serial
    )

    # 4️⃣ HTML verdict
    assert stats["health"] in ["Good", "Excellent"]

@pytest.mark.battery
def test_battery_parser(healthy_battery):
    tester = ADBBatteryTester()
    assert tester.is_healthy(healthy_battery)
