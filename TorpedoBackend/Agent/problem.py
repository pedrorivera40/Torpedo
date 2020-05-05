from graph import Node


class Problem:
    """
    Problem class
    """

    def __init__(self, start, goal):
        """
        Problem constructor

        :param start: 
        :param goal:
        """
        self.start = start
        self.goal = goal

    def get_start(self):
        """
        Private method to return start Node

        :param self:
        :returns start:
        :type start: Node
        """
        return self.start

    def get_goal(self):
        """
        Private method to return goal Node

        :param self:
        :returns goal:
        :type goal: Node
        """
        return self.goal
