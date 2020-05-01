import random
from math import exp


class SimulatedAnnealing:

    next, T = None, None

    def __init__(self, problem, schedule):
        self.problem = problem
        self.schedule = schedule
        self.curr = problem.start

    def start(self):
        for T in self.schedule:
            if T == 0:
                return self.curr
            self.next = random.choice(self.curr.get_edges()).destination.heuristic_value
            delta_e = self.next - self.curr
            if delta_e > 0:
                self.curr = self.next
            else:
                prob = exp(delta_e / T)
                if random.uniform(0, 1) <= prob:
                    self.curr = self.next
