import xlrd
from Agent.graph import GraphInput
from Agent.problem import Problem
from Dijkstra.dijkstra import Dijkstra


def build_solution_path(problem):

    start = problem.start
    goal = problem.goal
    result = []

    while goal != None and goal.get_city() != start.get_city():
        result.insert(0, goal)
        goal = goal.get_previous()

    result.insert(0, start)
    return result


# Obtain nodes from graph excel sheet.
# nodes = GraphInput().sheetImport("Agent/Graph.xlsx") # Romania graph...

nodes = GraphInput().sheetImport("Agent/PR_Graph.xlsx") # Puerto Rico graph...

# Creating graph dictionary to be bounded to its corresponding problem.
# Note this collection is necessary for the Dijkstra's algorithm implementation.
graph = {}

for node in nodes:
    graph[node.get_city()] = node

# Define start and end nodes for test.

# Romania start and end nodes...
# start_node = nodes[00]  # Arad
# goal_node = nodes[12]  # Bucharest

# Puerto Rico start and end nodes...
start_node = nodes[1]  # Mayagüez
goal_node = nodes[10]  # Caguas

# Then we use those nodes to define the problem.
problem = Problem(start_node, goal_node, graph)

solver = Dijkstra()
elapsed_time = solver.search(problem)
route = build_solution_path(problem)

route_time = 0
for i in range(0, len(route) - 1):
    # Define two nodes for calculating time between them.
    current_node = route[i]
    next_node = route[i + 1]

    # Find the adjacency between current and next.
    for edge in current_node.get_edges():
        if edge.get_destination().get_city() == next_node.get_city():
            route_time += edge.get_distance() / edge.get_speed_limit() + edge.get_traffic_delay()
            break

print("ROUTE TIME FOR DIJKSTRA: ", route_time)
print("ELAPSED TIME FOR DIJSKTRA: ", elapsed_time)
print("PATH CHOSEN BY DIJKSTRA: ", route)
