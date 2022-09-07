from src.wall import WallParams
from src.wardrobe import WardrobeParams, WardrobeAgreagator


wall = WallParams(width=250)
wardrobe1 = WardrobeParams(width=50, price=59)
wardrobe2 = WardrobeParams(width=75, price=62)
wardrobe3 = WardrobeParams(width=100, price=90)
wardrobe4 = WardrobeParams(width=120, price=111)
aggregator = WardrobeAgreagator(
    wardrobe_contrainer=[wardrobe1, wardrobe2, wardrobe3, wardrobe4]
)
