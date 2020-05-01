from graph import Node


def getStart(self):
    """
    Private method to return start Node
    
    :param self:
    :returns start:
    :type start: Node
    """
    return self.start

def getGoal(self):
    """
    Private method to return goal Node
    
    :param self:
    :returns goal:
    :type goal: Node
    """
    return self.goal

    
class Problem:
    """
    Problem class
    """
    def Problem(self,start,goal):
        """
        Problem constructor
    
        :param start: 
        :param goal:
        """
        self.start = start
        self.goal = goal 
        return self