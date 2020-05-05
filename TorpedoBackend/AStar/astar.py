import math
from Agent.graph import Node, Edge
from time import time


class AStar:
    """
    AStar search class.

    This class implements the A* algorithm for the path-finding problem.
    Its optimization function F(node) is based on a time-based heuristic
    value that denotes the estimated time from the current node to the 
    goal state. The time from start value for a successor node is 
    assigned based on the path cost (time) from source to current node,
    and the path cost from current to successor based on speed limit,
    distance between the two nodes, and traffic delay between these nodes.

    @author Pedro Luis Rivera Gómez
    """

    def search(self, problem):
        """
        :param self: 
        :param problem: 
        :type problem: Problem
        :returns delta_t: execution time for the search method. 
        """

        # Take the start time for search execution.
        start_time = time()

        start_node = problem.start
        start_node.set_time_from_start(0)
        goal_node = problem.goal

        # Initialized open and closed lists.
        open_list = [start_node]
        closed_list = []

        while len(open_list) != 0:

            min_f = math.inf
            current = None

            # Find the node in the open list with smallest value for F(node).
            for node in open_list:
                # Calculating F(node).
                f_value = node.get_heuristic_value() + node.get_time_from_start()
                if f_value < min_f:
                    min_f = f_value
                    current = node

            # *** Remove min node from open list. ***
            open_list.remove(current)

            # If the goal is reached, end loop.
            if current.get_city() == goal_node.get_city():
                break

            for edge in current.get_edges():
                # Calculate time it would take from start node to successor.
                successor = edge.get_destination()
                time_to_successor = current.get_time_from_start() + (edge.get_distance() *
                                                                     (1 / edge.get_speed_limit())) + edge.get_traffic_delay()

                if successor in open_list:
                    # If previous parent was a better candidate, continue.
                    if successor.get_time_from_start() <= time_to_successor:
                        continue

                elif successor in closed_list:
                    # If previous parent was a better candidate, continue.
                    if successor.get_time_from_start() <= time_to_successor:
                        continue

                    # Otherwise, move successor from closed to open list.
                    closed_list.remove(successor)
                    open_list.append(successor)

                else:
                    # Node has not been previously considered. Add it to open list.
                    open_list.append(successor)

                # Set node parent.
                successor.set_time_from_start(time_to_successor)
                successor.set_previous(current)

            # After analyzing current node, add it to closed list.
            closed_list.append(current)

        # Return execution time.
        return time() - start_time
