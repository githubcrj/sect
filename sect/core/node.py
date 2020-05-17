from abc import (ABC,
                 abstractmethod)
from typing import (List,
                    Optional)

from sect.hints import (Point,
                        Segment)
from .trapezoid import Trapezoid


class Node(ABC):
    __slots__ = '_parents',

    def __init__(self) -> None:
        self._parents = []  # type: List['Node']

    @abstractmethod
    def search_segment(self, segment: Segment) -> Optional[Trapezoid]:
        """
        Recursive search for the trapezoid
        which contains the left endpoint of the given segment.
        """

    @abstractmethod
    def search_point(self, point: Point) -> 'Node':
        """
        Recursive search for the node which contains the given point.
        """

    def replace_with(self, other: 'Node') -> None:
        """
        Replaces the node with given one in all parents.
        """
        while self._parents:
            self._parents[0]._replace_child(self, other)

    def _add_parent(self, parent: 'Node') -> None:
        assert parent is not None, 'Null parent'
        assert parent is not self, 'Cannot be parent of self'
        self._parents.append(parent)

    def _remove_parent(self, parent: 'Node') -> None:
        self._parents.remove(parent)

    @abstractmethod
    def _replace_child(self, current: 'Node', replacement: 'Node') -> None:
        """
        Replaces child node with given one.
        """
