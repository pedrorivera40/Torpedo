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
            if i == len(self.schedule):
                break

            # OPTIONAL ENDING CONDITION TO BE DISCUSSED (NOT NEEDED)
            # if self.curr.get_city() == self.problem.goal.get_city():
            #     break

            # Pick a random neighbor and calculate the energy diff
            self.next = random.choice(self.curr.get_edges()).get_destination()
            delta_e = self.curr.get_heuristic_value() - self.next.get_heuristic_value()

            # If the energy diff is positive, update the current node as the randomly chosen neighbor.
            # Otherwise, update the the current node as the randomly chosen neighbor with a probability.
            if delta_e > 0:
                if self.next is not self.curr.get_previous():
                    self.next.set_previous(self.curr)
                self.curr = self.next
                nodes_visited.append(self.curr.city)
            else:
                # Probability of updating the current node.
                prob = exp(delta_e / self.schedule[i])
                if random.uniform(0, 1) <= prob:
                    self.bad_choices += 1
                    if self.next is not self.curr.get_previous():
                        self.next.set_previous(self.curr)
                    self.curr = self.next
                    nodes_visited.append(self.curr.city)

        time_end = time.time()  # Stop counting time

        # Starting from the current node, traverse to through the parent of each node until reaching the start node
        # to find the route
        route = [self.curr.get_city()]
        while self.curr.get_city() is not self.problem.start.get_city():
            self.curr = self.curr.get_previous()
            # Prepend to list since we started from the current node
            route.insert(0, self.curr.get_city())

        # Print algorithm analysis
        print('Execution time: %s' % (time_end - time_start, ))
        print('Number of bad choices: %s' % (self.bad_choices, ))
        print('Nodes visited: %s' % (nodes_visited, ))
        print('Route: %s' % (route, ))

        return time_end - time_start  # Return execution time
