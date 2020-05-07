import xlrd
from Agent.graph import GraphInput,GraphRead
from Agent.problem import Problem
from AStar.astar import AStar
from SimulatedAnnealing.schedules import Schedules
from SimulatedAnnealing.simulated_annealing import SimulatedAnnealing


class Agent:
    """
    """
    def build_graph(self,list_of_nodes,problem):
        """
        """
        9print(str (GraphRead().heuristicCalculation(route =sa_results['route'],list_of_nodes=list_of_nodes )))

        
    def build_solution_path(self,problem):

        start = problem.start
        goal = problem.goal
        result = []
    
        while goal != None and goal.get_city() != start.get_city():
            result.insert(0, goal.get_city())
            goal = goal.get_previous()
    
        result.insert(0, start.get_city())
        return result

    def __init__(self,problem,list_of_nodes):
        
        
            a_star_solver = AStar()
            elapsed_time = a_star_solver.search(problem=problem)
            route = self.build_solution_path(problem=problem)

            # print("ELAPSED TIME FOR A*: ", elapsed_time)
            #print("PATH CHOSEN BY A*: ", route)
        
            linear_schedule = Schedules(50, .00005).get_linear_schedule()

            kirkpatrick_schedule = Schedules(10, 0.00005).get_kirkpatrick_schedule()

            # We initialize simulated annealing.

            simulated_annealing = SimulatedAnnealing(problem, kirkpatrick_schedule)
            sa_results=simulated_annealing.start()

            simulated_annealing1 = SimulatedAnnealing(problem, linear_schedule)
            sa_results1=simulated_annealing1.start()
        
            print(str (GraphRead().heuristicCalculation(route =sa_results['route'],list_of_nodes=list_of_nodes )))
               
            #GraphRead().heuristicCalculation(route,list_of_nodes)
          #  print('The difference between performance time is: ')
           # print((sa_results['time'] - elapsed_time))

nodes = GraphInput().sheetImport("Agent/Graph.xlsx")

# Define start and end nodes for test.
start_node = nodes[00]  # Arad
goal_node = nodes[12]  # Bucharest
       
#print ("Distance between arad and Timisoara: "+str(GraphRead().distanceBetween(start_node,goal_node,nodes)))
# Then we use those nodes to define the problem.
problem = Problem(start_node, goal_node) 
       
agent = Agent(problem=problem,list_of_nodes=nodes)        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        