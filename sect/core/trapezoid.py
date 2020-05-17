from typing import Optional

from reprit.base import generate_repr

from sect.hints import Point
from .edge import Edge


class Trapezoid:
    __slots__ = ('left', 'right', 'below', 'above',
                 '_lower_left', '_lower_right', '_upper_left', '_upper_right',
                 'trapezoid_node')

    def __init__(self,
                 left: Point,
                 right: Point,
                 below: Edge,
                 above: Edge) -> None:
        assert left < right, 'Incorrect endpoints order'
        self.left = left
        self.right = right
        self.above = above
        self.below = below
        self._lower_left = None  # type: Optional['Trapezoid']
        self._lower_right = None  # type: Optional['Trapezoid']
        self._upper_left = None  # type: Optional['Trapezoid']
        self._upper_right = None  # type: Optional['Trapezoid']
        self.trapezoid_node = None  # type: Optional['Node']

    __repr__ = generate_repr(__init__)

    def __contains__(self, point: Point) -> bool:
        return (self.below.interior_to_the_left
                and not self.above.interior_to_the_left)

    @property
    def lower_left(self) -> Optional['Trapezoid']:
        return self._lower_left

    @property
    def lower_right(self) -> Optional['Trapezoid']:
        return self._lower_right

    @property
    def upper_left(self) -> Optional['Trapezoid']:
        return self._upper_left

    @property
    def upper_right(self) -> Optional['Trapezoid']:
        return self._upper_right

    @lower_left.setter
    def lower_left(self, value: Optional['Trapezoid']) -> None:
        self._lower_left = value
        if value is not None:
            value._lower_right = self

    @lower_right.setter
    def lower_right(self, value: Optional['Trapezoid']) -> None:
        self._lower_right = value
        if value is not None:
            value._lower_left = self

    @upper_left.setter
    def upper_left(self, value: Optional['Trapezoid']) -> None:
        self._upper_left = value
        if value is not None:
            value._upper_right = self

    @upper_right.setter
    def upper_right(self, value: Optional['Trapezoid']) -> None:
        self._upper_right = value
        if value is not None:
            value._upper_left = self
