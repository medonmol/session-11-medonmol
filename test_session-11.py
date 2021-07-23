import math
from Polygon_session_11 import Polygon
from PolygonSequence_session_11 import PolygonSequence
from math import pi, sin
import pytest
import random


@pytest.fixture
def generate_random_number():
    return random.randint(3, 25)


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    try:
        p = Polygon(2, 10)
        assert False, (
            "Creating a Polygon with 2 sides: " " Exception expected, not received"
        )
    except ValueError:
        pass

    n = 3
    R = 1
    p = Polygon(n, R)
    assert p.vertices == n, f"actual: {p.vertices}," f" expected: {n}"
    assert p.edges == n, f"actual: {p.count_edges}, expected: {n}"
    assert p.radius == R, f"actual: {p.circumradius}, expected: {n}"
    assert p.interior_angle == 60, f"actual: {p.interior_angle}," " expected: 60"
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, f"actual: {p.interior_angle}, " " expected: 90"

    assert math.isclose(
        p.edge_length, math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol
    ), (f"actual: {p.edge_length}," f" expected: {math.sqrt(2)}")

    assert math.isclose(
        p.perimeter, 4 * math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol
    ), (f"actual: {p.perimeter}," f" expected: {4 * math.sqrt(2)}")

    assert math.isclose(p.apothem, 0.707, rel_tol=rel_tol, abs_tol=abs_tol), (
        f"actual: {p.perimeter}," " expected: 0.707"
    )
    assert math.isclose(p.area, 2, rel_tol=abs_tol, abs_tol=abs_tol), (
        f"actual: {p.area}," " expected: 2.0"
    )
    p = Polygon(6, 2)
    assert math.isclose(p.edge_length, 2, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120, rel_tol=rel_tol, abs_tol=abs_tol)

    p = Polygon(12, 3)
    assert math.isclose(p.edge_length, 1.55291, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150, rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


def test_polygon():
    tmp = Polygon(4, 1)
    assert tmp.interior_angle == 90  # interior angle of a square


def test_polygon_eq():
    tmp1 = Polygon(10, 2)
    tmp2 = Polygon(10, 2)

    assert tmp1 == tmp2


def test_polygon_gt():
    tmp1 = Polygon(10, 2)
    tmp2 = Polygon(4, 2)

    assert tmp1 > tmp2


def test_polygon_edge_bad_input():
    with pytest.raises(ValueError):
        _ = Polygon("10", 3)


def test_polygon_radius_bad_input():
    with pytest.raises(ValueError):
        _ = Polygon(10, -2)


def test_polygon_update_edges():
    tmp = Polygon(3, 1)
    assert tmp.interior_angle == 60

    tmp.edges = 5
    assert tmp.interior_angle == 108


def test_polyseq():
    tmp = PolygonSequence(10, 1)
    assert tmp.max_edge == 10
    assert len(tmp[:]) == 8  # (since we begin creating polygon with n=3 onwards)


def test_polyseq_len(generate_random_number):
    tmp = PolygonSequence(generate_random_number, 5)
    assert len(tmp) == generate_random_number - 2


def test_polyseq_max_efficiency():
    temp = PolygonSequence(25, 5)
    assert temp.max_efficiency.edges == 25


def test_polyseq_wrong_start():
    tmp = PolygonSequence(10, 4)
    assert len(tmp) == 8


def test_polyseq_reverse_index():
    tmp = PolygonSequence(25, 2)
    assert len(tmp[::-1]) == 23
