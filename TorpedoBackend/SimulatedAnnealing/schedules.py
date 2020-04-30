class Schedules:

    t_initial = None  # Initial Temperature
    t_final = None  # Final Temperature

    def __init__(self, t_initial, t_final):
        self.t_initial = t_initial
        self.t_final = t_final

    # Notice that in Kirkpatrick's cooling scheme the temperature will always approach zero but will NEVER
    # reach it.
    def get_kirkpatrick_schedule(self):
        schedule = []
        curr = self.t_initial
        while curr >= self.t_final:
            schedule.append(curr)
            curr = 0.95 * curr
        return schedule

    def get_linear_schedule(self, rate=1):
        schedule = []
        curr = self.t_initial
        while curr >= self.t_final:
            schedule.append(curr)
            curr -= rate
        return schedule
