from typing import List, Tuple
from abc import ABC, abstractclassmethod
from src.wardrobe import WardrobeAgreagator


class CalculationLogicInterface(ABC):
    @abstractclassmethod
    def add_solutions(self):
        pass

    @abstractclassmethod
    def find_cheepest_combination(self):
        pass


class CalculationLogic(CalculationLogicInterface):
    def __init__(self, wardrobes: WardrobeAgreagator) -> None:
        self.wardrobes = wardrobes
        self.mapper = wardrobes.maped_wardrobe_width_to_price
        self.solutions = None

    def add_solutions(self, solutions: List[Tuple]) -> None:
        self.solutions = solutions

    @property
    def find_cheepest_combination(self) -> Tuple:
        _best_solution = self.solutions[0]
        _best_score = self.get_summary_price_from_solution(_best_solution)
        for _solution in self.solutions[1:]:
            new_score = self.get_summary_price_from_solution(_solution)
            if new_score < _best_score:
                _best_score = new_score
                _best_solution = _solution
        return _best_solution

    def get_summary_price_from_solution(self, solution: Tuple):
        return sum(self.mapper.get(value, None) for value in solution)
