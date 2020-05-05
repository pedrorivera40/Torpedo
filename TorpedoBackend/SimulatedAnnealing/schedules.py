class Schedules:

    temp_initial = None  # Initial Temperature
    temp_final = None  # Final Temperature

    def __init__(self, temp_initial, temp_final):
        self.temp_initial = temp_initial
        self.temp_final = temp_final

    # Notice that in Kirkpatrick's cooling scheme the temperature will always approach zero but will NEVER
    # reach it.
    def get_kirkpatrick_schedule(self, alpha=0.95):
        schedule = []
        curr = self.temp_initial
        while curr >= self.temp_final:
            schedule.append(curr)
            curr = alpha * curr
        return schedule

    def get_linear_schedule(self, rate=1):
        schedule = []
        curr = self.temp_initial
        while curr >= self.temp_final:
            schedule.append(curr)
            curr -= rate
        return schedule
