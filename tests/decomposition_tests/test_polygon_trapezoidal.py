from typing import Tuple

from hypothesis import given
from orient.planar import (Relation,
                           point_in_polygon)

from sect.decomposition import (Graph,
                                Location,
                                polygon_trapezoidal)
from sect.hints import Point
from tests.utils import Polygon
from . import strategies


@given(strategies.polygons)
def test_basic(polygon: Polygon) -> None:
    border, holes = polygon

    assert isinstance(polygon_trapezoidal(border, holes), Graph)


@given(strategies.polygons_with_points)
def test_contains(polygon_with_point: Tuple[Polygon, Point]) -> None:
    polygon, point = polygon_with_point
    border, holes = polygon

    result = polygon_trapezoidal(border, holes)

    assert ((point in result)
            is (point_in_polygon(point, polygon) is not Relation.DISJOINT))


@given(strategies.polygons_with_points)
def test_locate(polygon_with_point: Tuple[Polygon, Point]) -> None:
    polygon, point = polygon_with_point
    border, holes = polygon

    result = polygon_trapezoidal(border, holes)

    location = result.locate(point)
    relation = point_in_polygon(point, polygon)
    assert (location is Location.EXTERIOR) is (relation is Relation.DISJOINT)
    assert (location is Location.BOUNDARY) is (relation is Relation.COMPONENT)
    assert (location is Location.INTERIOR) is (relation is Relation.WITHIN)
