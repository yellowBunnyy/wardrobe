from dataclasses import dataclass
from typing import List, Dict

@dataclass
class WardrobeParams:
    # params in cm unit.
    width: int
    price: float


@dataclass
class WardrobeAgreagator:
    wardrobe_contrainer: List[WardrobeParams]

    @property
    def get_wardrobe_width(self) -> List[int]:
        return [wardrobe.width for wardrobe in self.wardrobe_contrainer]

    @property
    def maped_wardrobe_width_to_price(self)-> Dict:
        return {wardrobe.width: wardrobe.price for wardrobe in self.wardrobe_contrainer}

