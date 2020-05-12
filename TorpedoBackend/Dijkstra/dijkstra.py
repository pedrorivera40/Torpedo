import math
from Agent.graph import Node, Edge
from time import time


class Dijkstra:
    """
    Dijkstra search class.

    This class implements Dijkstra's shortest-path algorithm for finding the fastest
    routes from start to each node in a graph. It minimizes traveled time based based 
    on speed limit, distance between nodes, and traffic delay between these nodes.

    @author Pedro Luis Rivera Gómez
    """

    # This code segment is based on the following pseudocode for Djikstra's shortest
    # path algorithm:
    # http://www.gitta.info/Accessibiliti/en/html/Dijkstra_learningObject1.html
    def search(self, problem):
        """
        :param self:
        :param problem:
        :type problem: Problem
        :returns delta_t: execution time for the search method.
        """

        # Take the start time for search execution.
        start_time = time()

        source = problem.get_start()
        graph = problem.get_graph()
        shortest_times = {}

        # Initialize distances array, setting source distance to 0, and others to INF.
        for node in graph:
            shortest_times[graph[node].get_city()] = math.inf

        shortest_times[source.get_city()] = 0

        while len(graph) != 0:

            # Step 1. Find the node in graph with shortest time.
            min_time = math.inf
            min_node = None

            for node in graph:
                if shortest_times[graph[node].get_city()] < min_time:
                    min_node = graph[node]

            graph.pop(min_node.get_city(), 0)

            # Step 2. Iterate through each of its adjacencies.
            for edge in min_node.get_edges():

                target = edge.get_destination()
                time_to_target = shortest_times[min_node.get_city(
                )] + (edge.get_distance() / edge.get_speed_limit()) + edge.get_traffic_delay()

                # If we found a better path, then update it's distance and previous.
                if target.get_city() not in shortest_times or time_to_target < shortest_times[target.get_city()]:
                    shortest_times[target.get_city()] = time_to_target
                    target.previous = min_node

        # Return execution time.
        return time() - start_time
