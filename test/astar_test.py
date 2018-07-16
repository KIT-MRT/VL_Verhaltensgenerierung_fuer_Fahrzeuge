from astar import astar
from city_graph import *


class TestHeuristic(object):
    def test_simple(self):
        goal = City('', 1, 2)
        node = City('', 2, 4)
        h = Heuristic(goal)
        assert h(node) == sqrt(5)


class TestGraph(object):
    def test_return_weigts(self):
        weight_actual = city_graph.cost(m, a)
        weight_desired = m2a
        assert weight_actual == weight_desired

    def test_return_neighbors(self):
        neighbors_actual = set(city_graph.neighbors(m))
        neighbors_desired = set([a, ing])
        assert neighbors_actual == neighbors_desired


class TestAStar(object):
    def test_empty_graph(self):
        start = City('', 0, 0)
        goal = start
        graph = Graph({})
        heuristic = Heuristic(goal)
        path_actual = astar(start, graph.neighbors, goal, graph.cost, heuristic)
        path_expected = []
        assert path_expected == path_actual

    def test_single_node(self):
        start = City('', 0, 0)
        goal = start
        graph = Graph({start: {goal: 0}})
        heuristic = Heuristic(goal)
        path_actual = astar(start, graph.neighbors, goal, graph.cost, heuristic)
        path_expected = []
        assert path_expected == path_actual

    def test_start_node_not_in_graph(self):
        start = City('', 0, 0)
        goal = start
        graph = Graph({goal: {start: 1}})
        heuristic = Heuristic(goal)
        path_actual = astar(start, graph.neighbors, goal, graph.cost, heuristic)
        path_expected = []
        assert path_expected == path_actual

    def test_two_nodes(self):
        start = City('', 0, 0)
        goal = City('', 1, 0)
        graph = Graph({start: {goal: 1}})
        heuristic = Heuristic(goal)
        path_actual = astar(start, graph.neighbors, goal, graph.cost, heuristic)
        path_expected = [goal]
        assert path_expected == path_actual

    def test_m_2_a(self):
        goal = a
        heuristic = Heuristic(goal)
        path_actual = astar(m, city_graph.neighbors, goal, city_graph.cost, heuristic)
        path_desired = [a]
        assert path_desired == path_actual

    def test_m_2_ul(self):
        goal = ul
        heuristic = Heuristic(goal)
        path_actual = astar(m, city_graph.neighbors, goal, city_graph.cost, heuristic)
        path_desired = [a, ul]
        assert path_desired == path_actual

    def test_m_2_s(self):
        goal = s
        heuristic = Heuristic(goal)
        path_actual = astar(m, city_graph.neighbors, goal, city_graph.cost, heuristic)
        path_desired = [a, ul, s]
        assert path_desired == path_actual

    def test_m_2_ka(self):
        goal = ka
        heuristic = Heuristic(goal)
        path_actual = astar(m, city_graph.neighbors, goal, city_graph.cost, heuristic)
        path_desired = [a, ul, s, ka]
        assert path_desired == path_actual










