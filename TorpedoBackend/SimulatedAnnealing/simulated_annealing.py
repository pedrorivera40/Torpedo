import random
from math import exp


class SimulatedAnnealing:

    next, T = None, None

    def __init__(self, problem, schedule):
        self.problem = problem
        self.schedule = schedule
        self.curr = problem.start

    def start(self):
        path = [self.curr.city]
        path_no_repetition = [self.curr.city]
        for i in range(len(self.schedule)):
            if i == len(self.schedule):
                return self.curr
            self.next = random.choice(self.curr.get_edges()).destination
            delta_e = self.curr.heuristic_value - self.next.heuristic_value
            if delta_e > 0:
                self.curr = self.next
                path.append(self.curr.city)
                if self.curr.city not in path_no_repetition:
                    path_no_repetition.append(self.curr.city)
            else:
                prob = exp(delta_e / self.schedule[i])
                if random.uniform(0, 1) <= prob:
                    self.curr = self.next
                    path.append(self.curr.city)
                    if self.curr.city not in path_no_repetition:
                        path_no_repetition.append(self.curr.city)

        print(path)
        print(path_no_repetition)

