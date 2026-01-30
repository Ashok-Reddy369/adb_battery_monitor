#!/bin/bash
# ADB Battery Monitor - Complete Python 3.9 Setup
# Ashok@VTA064L - One-click project setup

set -e  # Exit on error
cd ~/Desktop/adb_battery_monitor

echo "🧹 Cleaning old venv..."
rm -rf venv

echo "📦 Installing Python 3.9 + dependencies..."
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.9 python3.9-venv python3.9-dev

echo "🐍 Creating Python 3.9 venv..."
python3.9 -m venv venv
source venv/bin/activate

echo "📥 Installing packages..."
pip install --upgrade pip setuptools wheel
pip install "pure-python-adb>=0.4.0" pytest==7.4.3 pandas==2.0.3 openpyxl==3.1.2

echo "✅ Setup complete!"
echo "=================================="
python --version
pytest --version
pip list | grep adb

echo "🎉 VSCode: Ctrl+Shift+P → 'Python: Select Interpreter' → ./venv/bin/python"
echo "📱 Connect Android (USB debugging ON) → pytest tests/ -v"

