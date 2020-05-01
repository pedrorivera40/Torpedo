# Reading an excel file using Python 
import xlrd 

def get_destination(self):
    """
    Private method to return destination Node 
    
    :param self:
    :returns destination:
    :type destination: Node
    """
    return self.destination

def get_distance(self):
    """
    Private method to return distance
    
    :param self:
    :returns distance:
    :type distance: float
    """
    return self.distance

def get_speed_limit(self):
    """
    Private method to return speed_limit
    
    :param self:
    :returns speed_limit:
    :type speed_limit: int
    """
    return self.speed_limit

def get_traffic_delay(self):
    """
    Private method to return traffic_delay
    
    :param self:
    :returns traffic_delay:
    :type traffic_delay: float
    """
    return self.traffic_delay


class Node:
    """
    Node class
    """
    def Node(self,city,edges,heuristic_value):
        """
        Node constructor
    
        :param city: 
        :type city: String
        :param edges:
        :type edges: List<Edge>
        :param heuristic_value:
        :type heuristic_value: Float
        """
        self.city = city
        self.edges= edges
        self.heuristic_value = heuristic_value
        return self
    
 


def get_city(self):
    """
    Private method to return Node city name
    
    :param self:
    :returns city:
    :type city: string
    """
    return self.city

def get_edges(self):
    """
    Private method to return edges list
    
    :param self:
    :returns edges:
    :type edges: List<Edge>
    """
    return self.edges

def get_heuristic_value(self):
    """
    Private method to return heuristic_value
    
    :param self:
    :returns heuristic_value:
    :type heuristic_value: float
    """
    return self.heuristic_value

   
class Edge:
    """
    Edge class
    """
    def Edge(self,destination,distance,speed_limit,traffic_delay):
        """
        Edge constructor
    
        :param destination: 
        :param distance:
        :param speed_limit:
        :param traffic_delay:
        """
        self.destination = destination
        self.distance = distance
        self.speed_limit = speed_limit
        self.traffic_delay = traffic_delay
        return self
    



listOfNodes = []
class GraphInput:
    """
    Graph Input class, with methods for inputing graph data to our agent
    """
    
    def sheetImport(self,path):
        """
        Import graph data through an xlsx or xls file named "Graph.xlsx" or "Graph.xls" in the folder named 'AGENT'
        """
        # To open Workbook 
        wb = xlrd.open_workbook(path) 
        sheet = wb.sheet_by_index(0) 
        
       
        for i in range(sheet.nrows): 
            nodeEdges = [] 
            for j in range(sheet.ncols):
                cell = sheet.cell_value(i, j)
                
                if cell is not "" :
                        if cell[0] == '(' :
                            
                            res = [] 
                            temp = [] 
                            for token in cell.split(", "): 
                                value = token.replace("(", "").replace(")", "")
                                temp.append(value) 
                                if ")" in token: 
                                        res.append(tuple(temp)) 
                                        temp = []
  
                            # printing result 
                            print('edge #'+str(j))
                            print("\tDestination: "+str(res[0][0])+"\n\tDistance: "+str(res[0][1])+"\n\tMax Speed: "+str(res[0][2])+"\n\tTraffic Delay: "+str(res[0][3]))
                            #store cell information 
                            
                            destination =str(res[0][0])
                            distance=str(res[0][1])
                            speed_limit=str(res[0][2])
                            traffic_delay=str(res[0][3])
                            nodeEdges.append(Edge().Edge(destination=destination,distance=distance,speed_limit=speed_limit,traffic_delay=traffic_delay) )
                            
                            
                        else:
                            print("\nNode:\t"+cell)
                            print("\nEdges: ")
            
        listOfNodes.append(Node().Node(city=str(sheet.cell_value(i, 0)) , edges=nodeEdges, heuristic_value= 1 ))
       # print( listOfNodes)
        return listOfNodes 
        
        
nodes = GraphInput().sheetImport("Graph.xlsx")
        
