import xlrd
from TorpedoBackend.Agent.graph import GraphInput
from TorpedoBackend.Agent.problem import Problem
from TorpedoBackend.SimulatedAnnealing.schedules import Schedules
from TorpedoBackend.SimulatedAnnealing.simulated_annealing import SimulatedAnnealing

# First we find the start/goal nodes.
nodes = GraphInput().sheetImport("../Agent/Graph.xlsx")

start_node = nodes[00]  # Arad
goal_node = nodes[12]  # Bucharest

# Then we use those nodes to define the problem.

problem = Problem(start_node, goal_node)

# We select a Temperature cooling schedule.

linear_schedule = Schedules(50, .00005).get_linear_schedule()

kirkpatrick_schedule = Schedules(10, 0.00005).get_kirkpatrick_schedule()

# We initialize simulated annealing.

simulated_annealing = SimulatedAnnealing(problem, kirkpatrick_schedule)

# Start.
simulated_annealing.start()



