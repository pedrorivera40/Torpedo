import xlrd
from Agent.graph import GraphInput
from Agent.problem import Problem
from AStar.astar import AStar


def build_solution_path(problem):

    start = problem.start
    goal = problem.goal
    result = []

    while goal != None and goal.get_city() != start.get_city():
        result.insert(0, goal.get_city())
        goal = goal.get_previous()

    result.insert(0, start.get_city())
    return result


# Obtain nodes from graph excel sheet.
nodes = GraphInput().sheetImport("Agent/Graph.xlsx")

# Define start and end nodes for test.
start_node = nodes[00]  # Arad
goal_node = nodes[12]  # Bucharest

# Then we use those nodes to define the problem.
problem = Problem(start_node, goal_node)

solver = AStar()
elapsed_time = solver.search(problem)
route = build_solution_path(problem)

print("ELAPSED TIME FOR A*: ", elapsed_time)
print("PATH CHOSEN BY A*: ", route)
