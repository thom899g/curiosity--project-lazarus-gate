"""
Lazarus Gate Configuration Manager
Manages all runtime configuration with validation and environment fallbacks
"""
import os
from dataclasses import dataclass
from typing import Optional
from enum import Enum
from dotenv import load_dotenv
import structlog

# Initialize logging
logger = structlog.get_logger()

class TradingMode(Enum):