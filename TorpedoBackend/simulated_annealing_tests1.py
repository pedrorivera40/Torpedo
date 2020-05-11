import xlrd
from Agent.graph import GraphInput
from Agent.problem import Problem
from SimulatedAnnealing.schedules import Schedules
from SimulatedAnnealing.simulated_annealing import SimulatedAnnealing
from excel_export import ExcelExport


excel_export = ExcelExport('test_results.xls')
excel_export.add_sheet('simulated_annealing')
excel_export.add_headers(['Execution Time', 'Number of Nodes Visited', 'Number of Bad Choices', 'Route'])

# Perform test 100 times.
# for i in range(100):

# First we find the start/goal nodes.
# nodes = GraphInput().sheetImport("Agent/Graph.xlsx") # Romania graph...

nodes = GraphInput().sheetImport("Agent/PR_Graph.xlsx") # Puerto Rico graph...

# Creating graph dictionary to be bounded to its corresponding problem.
# Note this collection is necessary for the Dijkstra's algorithm implementation.
graph = {}

for node in nodes:
    graph[node.get_city()] = node

# Romania start and end nodes...
# start_node = nodes[00]  # Arad
# goal_node = nodes[12]  # Bucharest

# Puerto Rico start and end nodes...
start_node = nodes[49]  # Mayagüez
goal_node = nodes[12]  # Caguas

# Then we use those nodes to define the problem.

problem = Problem(start_node, goal_node, graph)

# We select a Temperature cooling schedule.

linear_schedule = Schedules(50, .00005).get_linear_schedule()

kirkpatrick_schedule = Schedules(1000, 0.00005).get_kirkpatrick_schedule()

# We initialize simulated annealing.

simulated_annealing = SimulatedAnnealing(problem, kirkpatrick_schedule)

# Start.
print("HERE")
results = simulated_annealing.start()
print(results)

# excel_export.add_values([results['time'], len(results['nodes_visited']), results['bad_choices'], results['route']])

# excel_export.save()
