from typing import List, Tuple
from abc import ABC, abstractclassmethod
from src.wardrobe import WardrobeAgreagator
from src.wall import WallParams



class CombinationsLogicInterface(ABC):
    @abstractclassmethod
    def find_possibilities(self):
        pass
    @abstractclassmethod
    def can_put_wardrobe_to_container(self, wardrobe_width: int):
        pass
    @abstractclassmethod
    def remove_duplications(self, wardrobe_solutions: List[Tuple]):
        pass
    @abstractclassmethod
    def sort_wardrobe_solutions(self, wardrobe_solutions: List[List]):
        pass
    @abstractclassmethod
    def generate_solutions(self):
        pass


class CombinationsLogic(CombinationsLogicInterface):
    def __init__(self, wardrobes: WardrobeAgreagator, wall: WallParams):
        self.wardrobe_widths = wardrobes.get_wardrobe_width
        self.wall = wall
        self.wardrobe_container = []
        self.solutions = []

    def generate_solutions(self):
        self.find_possibilities()
        self.solutions = self.remove_duplications(self.solutions)

    def find_possibilities(self) -> None:
        for wardrobe_width in self.wardrobe_widths:
            if self.can_put_wardrobe_to_container(wardrobe_width):
                self.wardrobe_container.append(wardrobe_width)
                self.find_possibilities()
                if sum(self.wardrobe_container) == self.wall.width:
                    cp = self.wardrobe_container.copy()
                    self.solutions.append(cp)
                self.wardrobe_container.pop()

    def can_put_wardrobe_to_container(self, wardrobe_width: int) -> bool:
        return sum(self.wardrobe_container) + wardrobe_width <= self.wall.width

    def remove_duplications(self, wardrobe_solutions: List[Tuple]) -> List[Tuple]:
        return list(set(self.sort_wardrobe_solutions(wardrobe_solutions)))

    def sort_wardrobe_solutions(self, wardrobe_solutions: List[List]) -> List[Tuple]:
        self.solutions = [tuple(sorted(solution)) for solution in wardrobe_solutions]
        return self.solutions
