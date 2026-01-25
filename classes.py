from typing import Optional
import sympy
import scipy
import numpy as np
from dataclasses import dataclass


@dataclass
class Policy:
    price: int | float
    profit_per_policy: Optional[int | float] = None
    policy_volume: int | float
    elasticity: int | float
    loss: Optional[int | float] = None
    expenses: Optional[int | float] = None
    quote_volume = Optional[int | float] = None
    close_rate: Optional[int | float] = None

    @property
    def _total_profit_per_policy(self) -> int | float:
        if self.profit_per_policy is None:
            self._profit = self.price - (self.expenses + self.loss)
            return self._profit * self.close_rate * self.quote_volume
        else:
            return self.profit_per_policy * self.policy_volume

    def __iter__(self):
        return iter(
            (
                self.price,
                self.policy_volume,
                self.elasticity,
                self._total_profit_per_policy,
            )
        )


class P_And_C_Calculations:

    def __init__(self):
        pass

    def maximize_profit(self, policy_a: Policy, policy_b: Policy) -> float:
        pass
        # init_price_a, policy_vol_a, elasticity_a, total_profit_a = policy_a
        # init_price_b, policy_vol_b, elasticity_b, total_profit_b = policy_b
        # strike_a = policy_vol_a * (1 + elasticity_a * ())

    def maximize_volume(self, policy_a: Policy, policy_b: Policy) -> float:
        pass

    def graph_results(self):
        pass
