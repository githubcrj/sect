import random

from .core.node import Node
from .core.trapezoidal_map import build_graph as _build_graph
from .hints import (Contour,
                    Shuffler)

Node = Node


def trapezoidal(contour: Contour,
                *,
                shuffler: Shuffler = random.shuffle) -> Node:
    return _build_graph(contour, shuffler)
