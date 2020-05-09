import xlrd
from Agent.graph import GraphInput, GraphRead
from Agent.problem import Problem
from AStar.astar import AStar
from SimulatedAnnealing.schedules import Schedules
from SimulatedAnnealing.simulated_annealing import SimulatedAnnealing
from Dijkstra.dijkstra import Dijkstra


class Agent:
    """
    """

    def build_graphs(self, list_of_nodes, problem):
        """
        """
        goal_node = problem.get_goal()

        # for each node we want to get the fastest path and calculate
        #  the huristic value for it:

        for node in list_of_nodes:
            p = Problem(start=node, goal=goal_node, graph=graph)
            route = self.build_solution_path(p)
            # print("For Node : "+start_node.get_city() +
            #      "\n The route to the goal is: "+str(route))

            GraphRead().heuristicCalculation(route, list_of_nodes)
        return None

    def build_solution_path(self, problem):

        start = problem.start
        goal = problem.goal
        print("From "+str(start.get_city())+" to "+str(goal.get_city()))
        result = []

        while goal != None and goal.get_city() != start.get_city():
            print("INSERTING NODE TO ROUTE "+str(result))
            result.insert(0, goal.get_city())
            goal = goal.get_previous()

        result.insert(0, start.get_city())
        print("insert status: "+str(result))
        return result

    def __init__(self, problem, list_of_nodes):

        a_star_solver = AStar()
        elapsed_time = a_star_solver.search(problem=problem)
        route = self.build_solution_path(problem=problem)

        # print("ELAPSED TIME FOR A*: ", elapsed_time)
        #print("PATH CHOSEN BY A*: ", route)

        linear_schedule = Schedules(50, .00005).get_linear_schedule()

        kirkpatrick_schedule = Schedules(
            10, 0.00005).get_kirkpatrick_schedule()

        # We initialize simulated annealing.

        simulated_annealing = SimulatedAnnealing(problem, kirkpatrick_schedule)
        sa_results = simulated_annealing.start()

        simulated_annealing1 = SimulatedAnnealing(problem, linear_schedule)
        sa_results1 = simulated_annealing1.start()

        # print(str(GraphRead().heuristicCalculation(
        #     route=sa_results['route'], list_of_nodes=list_of_nodes)))

        # GraphRead().heuristicCalculation(route,list_of_nodes)
      #  print('The difference between performance time is: ')
       # print((sa_results['time'] - elapsed_time))


nodes = GraphInput().sheetImport("Agent/Graph.xlsx")

graph = {}
for node in nodes:
    graph[node.get_city()] = node

# Define start and end nodes for test.
start_node = nodes[00]  # Arad
goal_node = nodes[12]  # Bucharest

#print ("Distance between arad and Timisoara: "+str(GraphRead().distanceBetween(start_node,goal_node,nodes)))
# Then we use those nodes to define the problem.
problem = Problem(start_node, goal_node, graph)

agent = Agent(problem=problem, list_of_nodes=nodes)

agent.build_graphs(list_of_nodes=nodes, problem=problem)
