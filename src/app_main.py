from src.combinations_logic import CombinationsLogicInterface, CombinationsLogic
from src.calc_score_logic import CalculationLogicInterface, CalculationLogic
from src.data_from_user import aggregator, wall


class App:
    def __init__(
        self,
        calculations: CalculationLogicInterface,
        wardrobe_combinations: CombinationsLogicInterface,
    ):
        self.calculations = calculations
        self.wardrobe_combinations = wardrobe_combinations

    def get_result(self):
        self.wardrobe_combinations.generate_solutions()
        _solutions = self.wardrobe_combinations.solutions
        self.calculations.add_solutions(_solutions)
        return self.calculations.find_cheepest_combination


wardrobe_combinations = CombinationsLogic(wall=wall, wardrobes=aggregator)
calculations = CalculationLogic(wardrobes=aggregator)
app = App(calculations=calculations, wardrobe_combinations=wardrobe_combinations)
print(app.get_result())
