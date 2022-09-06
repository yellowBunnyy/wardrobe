
expected = 250
wardrobes = [(100, 20), (50, 10), (75, 15)]
wardrobes = [WardrobeParams(width=width, price=price) for width, price in wardrobes]
wardrobes = WardrobeAgreagator(wardrobe_contrainer=wardrobes)
wall = WallParams(width=250)
inst = PossibilitiesLogic(wardrobes=wardrobes, wall=wall)
inst.wardrobe_widths = [50, 75, 100, 120]
print(inst.find_possibilities())
print(inst.solutions)
