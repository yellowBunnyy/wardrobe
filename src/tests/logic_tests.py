from unittest import TestCase
import pytest
from src.logic import AppLogic
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
def aggr():
    wardrobes = [(100, 20), (50, 10), (75, 15)]
    wardrobes = [WardrobeParams(width=width, price=price) for width, price in wardrobes]
    return WardrobeAgreagator(wardrobe_contrainer=wardrobes)


@pytest.fixture(scope="class")
def logic_object(wall_object, wardrobe_object):
    logic = AppLogic(wardrobe=wardrobe_object, wall=wall_object)
    return logic


def test_wardrobeAggregator_create_should_cretre_aggregator(aggr):
    assert aggr.wardrobe_contrainer[0].width == 100
    assert aggr.wardrobe_contrainer[0].price == 20
    assert aggr.wardrobe_contrainer[1].width == 50
    assert aggr.wardrobe_contrainer[2].width == 75


# def test_allowed_posibilities_list(logic_object):
#     expected = [[50, 50, 50, 50, 50], [50, 50, 50, 100], [50, 50, 75, 75], [50, 50, 100, 50], [50, 75, 50, 75]]
#     logic_object.find_possibilities()
#     assert logic_object.solutions[:6] == expected
