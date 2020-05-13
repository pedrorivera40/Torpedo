import xlrd
from Agent.graph import GraphInput, GraphRead
from Agent.problem import Problem
from AStar.astar import AStar
from SimulatedAnnealing.schedules import Schedules
from SimulatedAnnealing.simulated_annealing import SimulatedAnnealing
from Dijkstra.dijkstra import Dijkstra
from excel_export import ExcelExport
START= 1
GOAL = 10
def build_solution_path(problem):

    start = problem.start
    goal = problem.goal
    result = []

    while goal != None and goal.get_city() != start.get_city():
        result.insert(0, goal)
        goal = goal.get_previous()

    result.insert(0, start)
    return result

def simulated_annealing():
           # We select a Temperature cooling schedule.
       linear_schedule = Schedules(50, .00005).get_linear_schedule()
       kirkpatrick_schedule = Schedules(1000, 0.00005).get_kirkpatrick_schedule()
       # We initialize simulated annealing.
       simulated_annealing = SimulatedAnnealing(problem, kirkpatrick_schedule)
       # Start.
       results = simulated_annealing.start()
       #print('nodes visited: %s' % (results['nodes_visited'], ))
       route_time = 0
       for i in range(0, len(results['route']) - 1):
           # Define two nodes for calculating time between them.
           current_node = results['route'][i]
           next_node = results['route'][i + 1]
           # Find the adjacency between current and next.
           for edge in current_node.get_edges():
               if edge.get_destination().get_city() == next_node.get_city():
                   route_time += edge.get_distance() / edge.get_speed_limit() + edge.get_traffic_delay()
                   break
       print("\nROUTE TIME FOR SIMULATED ANNEALING: ", route_time)
       print('ELAPSED TIME FOR SIMULATED ANNEALING: '+ str(results['time']))
       print('PATH CHOSEN BY SIMULATED ANNEALING: %s' % (results['route'], ))
       return results

def a_star():
        solver = AStar()
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
                
        print("\nROUTE TIME FOR A*: ", route_time)
        print("ELAPSED TIME FOR A*: ", elapsed_time)
        print("PATH CHOSEN BY A*: ", route)

def dijkstra():
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

    print("\nROUTE TIME FOR DIJKSTRA: ", route_time)
    print("ELAPSED TIME FOR DIJSKTRA: ", elapsed_time)
    print("PATH CHOSEN BY DIJKSTRA: ", route)


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
            route = build_solution_path(p)
            # print("For Node : "+start_node.get_city() +
            #      "\n The route to the goal is: "+str(route))

            GraphRead().heuristicCalculation(route, list_of_nodes)
        return None

    def __init__(self, problem, list_of_nodes):
        print("Agent created")
        # a_star_solver = AStar()
        # elapsed_time = a_star_solver.search(problem=problem)
        # route = build_solution_path(problem=problem)

        # # print("ELAPSED TIME FOR A*: ", elapsed_time)
        # #print("PATH CHOSEN BY A*: ", route)

        # linear_schedule = Schedules(50, .00005).get_linear_schedule()

        # kirkpatrick_schedule = Schedules(
        #     10, 0.00005).get_kirkpatrick_schedule()

        # # We initialize simulated annealing.

        # simulated_annealing = SimulatedAnnealing(problem, kirkpatrick_schedule)
        # sa_results = simulated_annealing.start()

        # simulated_annealing1 = SimulatedAnnealing(problem, linear_schedule)
        # sa_results1 = simulated_annealing1.start()

        # print(str(GraphRead().heuristicCalculation(
        #     route=sa_results['route'], list_of_nodes=list_of_nodes)))

        # GraphRead().heuristicCalculation(route,list_of_nodes)
      #  print('The difference between performance time is: ')
       # print((sa_results['time'] - elapsed_time))

   
#read from graph and create list of nodes to assign hv to 
nodes = GraphInput().sheetImport("Agent/PR_Graph.xlsx")

# for each node, calculate the fastest route to the goal node 
heuristics =[]
for node in nodes:
     # Define start and end nodes for test.
    start_node = node  #Each node
    goal_node = nodes[10]  # Baya
    # Then we use those nodes to define the problem.
   
    #Creating graph dictionary to be bounded to its corresponding problem.
    # Note this collection is necessary for the Dijkstra's algorithm implementation.
    graph = {}
    for node in nodes:
        graph[node.get_city()] = node
        
    problem = Problem(start=start_node, goal= goal_node,graph= graph)
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
   
    heuristics.append(GraphRead().heuristicCalculation(route =route, list_of_nodes=nodes))

#save into xlsx file 
# excel_export = ExcelExport('Agent/PR_Graph.xlsx')
# excel_export.select_sheet('1')
# excel_export.add_hv_values(heuristics)
# excel_export.save()

#create new list of nodes with heuristic values 

nodes = GraphInput().sheetImport("Agent/PR_Graph.xlsx")
graph = {}
for node in nodes:
    graph[node.get_city()] = node
    
# Puerto Rico start and end nodes...
start_node = nodes[START]  # Mayagüez
goal_node = nodes[GOAL]  # Caguas

# Then we use those nodes to define the problem.
problem = Problem(start_node, goal_node, graph)

dijkstra()

a_star()

simulated_annealing()


for i in range (0,4):
    nodes = GraphInput().random_traffic_import('Agent/PR_Graph.xlsx')
    graph = {}
    for node in nodes:
        graph[node.get_city()] = node
    
# Puerto Rico start and end nodes...
    start_node = nodes[START]  # Mayagüez
    goal_node = nodes[GOAL]  # Caguas

# Then we use those nodes to define the problem.
    problem = Problem(start_node, goal_node, graph)
    
    dijkstra()

    a_star()

    simulated_annealing()
