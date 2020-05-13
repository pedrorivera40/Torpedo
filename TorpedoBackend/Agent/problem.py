class Problem:
    """
    Problem class
    """

    def __init__(self, start, goal, graph):
        """
        Problem constructor

        :param start: 
        :param goal:
        :param graph:
        """
        self.start = start
        self.goal = goal
        self.graph = graph

    def set_start(self, start):
        """
        """
        self.start = start

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

    def get_graph(self):
        """
        Public method to return graph list

        :param self:
        :returns graph:
        :type graph: dict
        """
        return self.graph
