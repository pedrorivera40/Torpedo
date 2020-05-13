import xlrd
from Agent.graph import GraphInput, GraphRead
from Agent.problem import Problem
from Dijkstra.dijkstra import Dijkstra


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
nodes = GraphInput().mapImport("Agent/PR_Graph.xlsx")

# Creating graph dictionary to be bounded to its corresponding problem.
# Note this collection is necessary for the Dijkstra's algorithm implementation.

# calculate heuristic values for each node, given graph paramters
for node_start in nodes:
    graph = {}
    for node in nodes:
        graph[node.get_city()] = node

    # Define start and end nodes for test.
    start_node = node_start  #
    goal_node = nodes[12]  # Caguas

    # Then we use those nodes to define the problem.
    problem = Problem(start_node, goal_node, graph)
    solver = Dijkstra()
    elapsed_time = solver.search(problem)
    route = build_solution_path(problem)
    GraphInput().createProblem(problems=1, route=route, list_of_nodes=nodes)


# should create an XMl With the given heuristic values
   # print("\nFrom node : ", start_node.get_city())
   # print("PATH CHOSEN BY DIJKSTRA: ", route)
    #(GraphRead().heuristicCalculation(list_of_nodes=nodes, route=route))
