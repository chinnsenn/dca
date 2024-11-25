from dataclasses import dataclass
from enum import Enum
import numpy as np
from typing import Dict, List

class Currency(Enum):
    CNY = ("CNY", "¥")
    USD = ("USD", "$")
    EUR = ("EUR", "€")
    GBP = ("GBP", "£")
    JPY = ("JPY", "¥")

    def __init__(self, code: str, symbol: str):
        self.code = code
        self.symbol = symbol

class InvestmentFrequency(Enum):
    HALF_MONTHLY = ("半月度", 24)
    MONTHLY = ("月度", 12)
    QUARTERLY = ("季度", 4)
    HALF_YEARLY = ("半年度", 2)
    YEARLY = ("年度", 1)

    def __init__(self, label: str, periods_per_year: int):
        self.label = label
        self.periods_per_year = periods_per_year