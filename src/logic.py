from typing import List, Tuple
from src.wardrobe_params import WardrobeAgreagator, WardrobeParams
from src.wall import WallParams
import pdb


class CalculateScore:
    pass



class CombinationsPossibilitiesLogic:
    def __init__(self, wardrobes: WardrobeAgreagator, wall: WallParams):
        self.wardrobe_widths = wardrobes.get_wardrobe_width
        self.wall = wall
        self.wardrobe_container = []
        self.solutions = []


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
    
    def sort_wardrobe_solutions(self, wardrobe_solutions:List[List]) -> List[Tuple]:
        self.solutions = [tuple(sorted(solution)) for solution in wardrobe_solutions]
        return self.solutions

    @property
    def find_cheepest_combination(self):
        mapper = wardrobes.maped_wardrobe_width_to_price
        calc_score = lambda : sum(mapper.get(value, None) for value in best_solution)
        best_solution_index = 0
        best_solution = self.solutions[best_solution_index]
        best_solution_score = sum(mapper.get(value, None) for value in best_solution)
        for solution in self.solutions[1:]:
            if 

            

            
            return min(sum(mapper.get(value, None) for value in solution) for solution in self.solutions)
    


wardrobes = [(100, 20), (50, 10), (75, 15)]
wardrobes = [WardrobeParams(width=width, price=price) for width, price in wardrobes]
wardrobes = WardrobeAgreagator(wardrobe_contrainer=wardrobes)
wall = WallParams(width=250)
single_wardrobe = wardrobes.wardrobe_contrainer[0].price
