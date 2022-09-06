import pytest
from src.logic import CombinationsPossibilitiesLogic
from src.wall import WallParams
from src.wardrobe_params import WardrobeParams, WardrobeAgreagator
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
    logic = CombinationsPossibilitiesLogic(wardrobes=aggregator_obj, wall=wall_object)
    return logic


def test_wardrobeAggregator_create_should_create_wardrobes_aggregator(aggregator_obj):
    assert aggregator_obj.wardrobe_contrainer[0].width == 100
    assert aggregator_obj.wardrobe_contrainer[0].price == 20
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


def test_cheepest_combination_should_return_cheepest_solution(app_logic_object):
    app_logic_object.solutions = [
        (50, 50, 50, 50, 50),
        (50, 50, 75, 75),
        (50, 50, 50, 100),
    ]
    assert app_logic_object.find_cheepest_combination == (50, 50, 75, 75)
