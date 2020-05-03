import random
from math import exp


class SimulatedAnnealing:

    next, T = None, None

    def __init__(self, problem, schedule):
        self.problem = problem
        self.schedule = schedule
        self.curr = problem.start

    def start(self):
        for i in range(len(self.schedule)):
            if i == len(self.schedule):
                return self.curr
            self.next = random.choice(self.curr.get_edges()).destination
            print('%s randomly chosen' % (self.next.city, ))
            delta_e = self.next.heuristic_value - self.curr.heuristic_value
            if delta_e > 0:
                self.curr = self.next
            else:
                prob = exp(delta_e / self.schedule[i])
                if random.uniform(0, 1) <= prob:
                    self.curr = self.next
