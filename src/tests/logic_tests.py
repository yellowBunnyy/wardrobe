import pytest
from src.combinations_logic import CombinationsLogic
from src.calc_score_logic import CalculationLogic
from src.wall import WallParams
from src.wardrobe import WardrobeParams, WardrobeAgreagator
from src.app_main import App
import pdb


@pytest.fixture(scope="class")
def wall_object():
    wall = WallParams(width=250)
    return wall


@pytest.fixture(scope="class")
def wardrobe_object():
    wardrobe = WardrobeParams(width=50, price=40)
    return wardrobe


@pytest.fixture(scope="class")
def aggregator_obj():
    wardrobes = [(100, 90), (50, 59), (75, 62)]
    wardrobes = [WardrobeParams(width=width, price=price) for width, price in wardrobes]
    return WardrobeAgreagator(wardrobe_contrainer=wardrobes)


@pytest.fixture(scope="class")
def app_logic_object(wall_object, aggregator_obj):
    logic = CombinationsLogic(wardrobes=aggregator_obj, wall=wall_object)
    return logic


@pytest.fixture(scope="class")
def calc_score_obj(aggregator_obj):
    calculations = CalculationLogic(wardrobes=aggregator_obj)
    return calculations


def test_wardrobeAggregator_was_crated_should_return_wardrobes_aggregator(
    aggregator_obj,
):
    assert aggregator_obj.wardrobe_contrainer[0].width == 100
    assert aggregator_obj.wardrobe_contrainer[0].price == 90
    assert aggregator_obj.wardrobe_contrainer[1].width == 50
    assert aggregator_obj.wardrobe_contrainer[2].width == 75


def test_wardrobeAggregator_create_maper(aggregator_obj):
    assert aggregator_obj.maped_wardrobe_width_to_price == {100: 90, 50: 59, 75: 62}


def test_find_all_combinations_arrange_wardrobe_return_list_with_solutions(
    app_logic_object,
):
    app_logic_object.wardrobe_widths = [50, 75, 100, 120]
    app_logic_object.find_possibilities()
    assert app_logic_object.solutions[:5] == [
        [50, 50, 50, 50, 50],
        [50, 50, 50, 100],
        [50, 50, 75, 75],
        [50, 50, 100, 50],
        [50, 75, 50, 75],
    ]


def test_can_put_wardrobe_to_container_should_return_true_if_is_posible(
    app_logic_object,
):
    app_logic_object.wardrobe_container = [50, 50, 100]
    app_logic_object.wall.width = 250
    wardrobe_width = 50
    assert app_logic_object.can_put_wardrobe_to_container(wardrobe_width)


def test_can_put_wardrobe_to_container_should_return_false_if_is_not_possible(
    app_logic_object,
):
    app_logic_object.wardrobe_container = [50, 50, 100, 50]
    app_logic_object.wall.width = 250
    wardrobe_width = 50
    assert not app_logic_object.can_put_wardrobe_to_container(wardrobe_width)


def test_sort_values_in_list_should_return_sorted_list_with_lists(app_logic_object):
    solutions = [
        [50, 50, 50, 50, 50],
        [50, 50, 50, 100],
        [50, 50, 75, 75],
        [50, 50, 100, 50],
        [50, 75, 50, 75],
    ]
    expected = [
        (50, 50, 50, 50, 50),
        (50, 50, 50, 100),
        (50, 50, 75, 75),
        (50, 50, 50, 100),
        (50, 50, 75, 75),
    ]
    assert app_logic_object.sort_wardrobe_solutions(solutions) == expected


def test_remove_duplications_from_container_with_solutions(app_logic_object):
    solutions = [
        [50, 50, 50, 50, 50],
        [50, 50, 50, 100],
        [50, 50, 75, 75],
        [50, 50, 100, 50],
        [50, 75, 50, 75],
        [50, 75, 50, 75],
        [50, 75, 50, 75],
    ]
    expected = [(50, 50, 50, 50, 50), (50, 50, 75, 75), (50, 50, 50, 100)]
    assert app_logic_object.remove_duplications(solutions) == expected


def test_calculate_summary_price_from_solution_should_return_summary_price(
    calc_score_obj,
):
    solution = (50, 50, 75)
    assert calc_score_obj.get_summary_price_from_solution(solution=solution) == 180


def test_cheepest_combination_should_return_cheepest_solution(calc_score_obj):
    calc_score_obj.solutions = [
        (50, 50, 50, 50, 50),
        (50, 50, 75, 75),
        (50, 50, 50, 100),
    ]
    assert calc_score_obj.find_cheepest_combination == (50, 50, 75, 75)


def test_generate_solutions(app_logic_object):
    expected = [
        (50, 50, 75, 75),
        (50, 50, 50, 100),
        (50, 50, 50, 50, 50),
        (75, 75, 100),
        (50, 100, 100),
    ]
    app_logic_object.generate_solutions()
    for sol in app_logic_object.solutions:
        assert sol in expected



def test_get_best_solution_for_solve_task(app_logic_object, calc_score_obj):
    app_logic_object.generate_solutions()
    solutions = app_logic_object.solutions
    calc_score_obj.add_solutions(solutions=solutions)
    app = App(calculations=calc_score_obj, wardrobe_combinations=app_logic_object)
    assert app.get_result() == (75, 75, 100)
