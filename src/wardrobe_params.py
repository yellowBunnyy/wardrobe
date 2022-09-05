from dataclasses import dataclass
from typing import List

@dataclass
class WardrobeParams:
    # params in cm unit.
    width: int
    price: float


@dataclass
class WardrobeAgreagator:
    wardrobe_contrainer: List[WardrobeParams]
    @property
    def get_wardrobe_width(self):
        return [wardrobe.width for wardrobe in self.wardrobe_contrainer]

