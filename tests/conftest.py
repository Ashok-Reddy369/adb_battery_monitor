import pytest
from src.battery_tester import ADBBatteryTester

@pytest.fixture(scope="session")
def battery_tester():
    """Global battery tester fixture"""
    return ADBBatteryTester()

@pytest.fixture
def healthy_battery(battery_tester):
    """Mock healthy battery for local testing"""
    return {
        "level": 85,
        "health": "Good", 
        "temperature": 32.0
    }
