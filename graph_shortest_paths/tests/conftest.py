import pytest

from graph_shortest_paths.domain.builders import cascavel_graph, regional_graph


@pytest.fixture(scope="module")
def small_graph():
    return cascavel_graph()


@pytest.fixture(scope="module")
def big_graph():
    return regional_graph()
