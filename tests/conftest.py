import sys
import os

import pytest

# Add parent directory to path to import src module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
