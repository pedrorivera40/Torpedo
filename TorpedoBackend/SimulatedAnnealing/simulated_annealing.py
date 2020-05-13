import random
from math import exp
import time


class SimulatedAnnealing:

    next, T = None, None
    bad_choices = 0  # Counter

    def __init__(self, problem, schedule):
        self.problem = problem
        self.schedule = schedule
        self.curr = problem.start

    def start(self):

        time_start = time.time()  # Start counting time
        nodes_visited = [self.curr.city]

        for i in range(len(self.schedule)):

            # Escape for-loop if we reach the end of the cooling scheme.
            if i == len(self.schedule) or self.curr.get_city() == self.problem.get_goal().get_city():
                break

            # Pick a random neighbor and calculate the energy diff
            self.next = random.choice(self.curr.get_edges()).get_destination()
            delta_e = self.curr.get_heuristic_value() - self.next.get_heuristic_value()

            # If the energy diff is positive, update the current node as the randomly chosen neighbor.
            # Otherwise, update the the current node as the randomly chosen neighbor with a probability.
            if delta_e > 0:
                self.curr.set_next(self.next)
                self.curr = self.next
                nodes_visited.append(self.curr.city)
            else:
                # Probability of updating the current node.
                prob = exp(delta_e / self.schedule[i])
                if random.uniform(0, 1) <= prob:
                    self.bad_choices += 1
                    self.curr.set_next(self.next)
                    self.curr = self.next
                    nodes_visited.append(self.curr.city)

        time_end = time.time()  # Stop counting time

        # Starting from the start node, traverse through the child until reaching the goal node to find the route.
        counter = 0  # This counter is used to avoid infinite loops.
        route = []
        self.curr = self.problem.start
        while (self.curr.get_next() is not None) and \
                (self.curr.get_city() is not self.problem.goal.get_city()) and counter < len(nodes_visited):
            route.append(self.curr)
            self.curr = self.curr.get_next()
            counter += 1
        route.append(self.curr)

        # Print algorithm analysis
        # print('Execution time: %s' % (time_end - time_start, ))
        # print('Number of bad choices: %s' % (self.bad_choices, ))
        # print('Nodes visited: %s' % (nodes_visited, ))
        # print('Route: %s' % (route, ))
        response = {"time": (time_end - time_start), "bad_choices": self.bad_choices,
                    "nodes_visited": nodes_visited, "route": route}
        return response  # Return performance parameters
