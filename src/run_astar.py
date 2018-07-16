from city_graph import *
from astar import astar


def main():
    goal = ing
    heuristic = Heuristic(goal)
    nodes = astar(m, city_graph.neighbors, goal, city_graph.cost, heuristic)
    for node in nodes:
        print(node)


if __name__ == "__main__":
    main()
