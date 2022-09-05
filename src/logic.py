from .wardrobe_params import WardrobeAgreagator, WardrobeParams
from .wall import WallParams


class AppLogic:
    def __init__(self, wardrobes: WardrobeAgreagator = None, wall: WallParams = None):
        self.wardrobe_widths = wardrobes.get_wardrobe_width
        self.wall = wall
        self.wardrobe_container = []
        self.solutions = []

    def find_possibilities(self):
        for wardrobe_width in self.wardrobe_widths:
            if self.can_put_wardrobe_to_container(wardrobe_width):
                self.wardrobe_container.append(wardrobe_width)
                self.find_possibilities()
                if sum(self.wardrobe_container) == self.wall.width:
                    cp = self.wardrobe_container.copy()
                    self.wardrobe_container.append(cp)
                self.wardrobe_container.pop()

    def can_put_wardrobe_to_container(self, wardrobe_width):
        return sum(self.wardrobe_container) + wardrobe_width <= self.wall.width

    def remove_duplications(self):
        pass

    def get_sorted_data(self):
        pass


expected = 250

inst = AppLogic()
inst.wardrobe_widths = [50, 75, 100, 120]
