import xlrd
from Agent.graph import GraphInput
from Agent.problem import Problem
from SimulatedAnnealing.schedules import Schedules
from SimulatedAnnealing.simulated_annealing import SimulatedAnnealing

# First we find the start/goal nodes.
nodes = GraphInput().sheetImport("Agent/Graph.xlsx")

# Creating graph dictionary to be bounded to its corresponding problem.
# Note this collection is necessary for the Dijkstra's algorithm implementation.
graph = {}

for node in nodes:
    graph[node.get_city()] = node

start_node = nodes[0]  # Arad
goal_node = nodes[8]  # Bucharest

# Then we use those nodes to define the problem.

problem = Problem(start_node, goal_node, graph)

# We select a Temperature cooling schedule.

linear_schedule = Schedules(50, .00005).get_linear_schedule()

kirkpatrick_schedule = Schedules(10, 0.00005).get_kirkpatrick_schedule()

# We initialize simulated annealing.

simulated_annealing = SimulatedAnnealing(problem, kirkpatrick_schedule)

# Start.
simulated_annealing.start()
