# Reading an excel file using Python 
import xlrd 



class Node:
    """
    Node class
    """
  
    def __init__(self,city,edges,heuristic_value,previous):
        """
        Node constructor
    
        :param city: 
        :type city: String
        :param previous: 
        :type previous: Node
        :param edges:
        :type edges: List<Edge>
        :param heuristic_value:
        :type heuristic_value: Float
        """
        self.previous = None
        self.city = city
        self.edges= edges
        self.heuristic_value = heuristic_value
     
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

    def get_previous(self):
        """
        Private method to return prvious Node
    
        :param self:
        :returns previous:
        :type heuristic_value: Node
        """
        return self.previous
   
   
     
class Edge:
    """
    Edge class
    """ 
    def __init__(self,destination,distance,speed_limit,traffic_delay):
        """
        Edge constructor
    
        :param destination: 
        :type destination: Node
        :param distance:
        :tpye distance: Float
        :param speed_limit:
        :type speed_limit: Integer
        :param traffic_delay:
        """
        self.destination = destination
        self.distance = distance
        self.speed_limit = speed_limit
        self.traffic_delay = traffic_delay
         
    def get_destination(self):
        """
        Private method to return destination Node 
    
        :param self:
        :returns destination:
        :type destination: Node
        """
        return self

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

   
    
   




class GraphInput:
    """
    Graph Input class, with methods for inputing graph data to our agent
    """
    
    def sheetImport(self,path):
        listOfNodes = []
        """
        Import graph data through an xlsx or xls file named "Graph.xlsx" or "Graph.xls" in the folder named 'AGENT'
        """
        # To open Workbook 
        wb = xlrd.open_workbook(path) 
        sheet = wb.sheet_by_index(0) 
        
        #traverse the first column to store all the nodes, with their city name.
        #TODO: We need to calculate the heuristic_value 
        for i in range(sheet.nrows):
            city_name = str(sheet.cell_value(i, 0))
            city_heuristic_value = float(sheet.cell_value(i, 1))
            listOfNodes.append(Node(previous=None,city=city_name, edges=None, heuristic_value=city_heuristic_value))
        
        #for node in listOfNodes:
            #print("Creating node list, adding: "+ str(node.city))
        #After making the list of nodes, we create the edge list for each Node :
        #traverse the first column
        for i in range(sheet.nrows): 
            nodeEdges = [] 
            #go through each row 
            for j in range(2, sheet.ncols):
                #Check each cell
                cell = sheet.cell_value(i, j)
                #Check if cell is empty, this means the end of a edge list
                if cell is not "" :
                        #check if cell contains an edge
                        if cell[0] == '(' :
                            #store the tuple information from the cell
                            res = [] 
                            temp = [] 
                            for token in cell.split(", "): 
                                value = token.replace("(", "").replace(")", "")
                                temp.append(value) 
                                if ")" in token: 
                                        res.append(tuple(temp)) 
                                        temp = []
  
                            # printing result 
                            #print('edge #'+str(j))
                            #print("\tDestination: "+str(res[0][0])+"\n\tDistance: "+str(res[0][1])+"\n\tMax Speed: "+str(res[0][2])+"\n\tTraffic Delay: "+str(res[0][3]))
                            #store cell information 
                            destination =None
                            distance=float(res[0][1])
                            speed_limit=int(res[0][2])
                            traffic_delay=float(res[0][3])
                            #reference node from listOfNodes
                            for node in listOfNodes:
                                #print(node.city+" is being compared with "+str(res[0][0]))
                                if node.city == str(res[0][0]):
                                    destination = node
                                    break
                            #no Node was found , could be an error in the Excel file
                            if destination is not None:
                                nodeEdges.append(Edge(destination=destination,distance=distance,speed_limit=speed_limit,traffic_delay=traffic_delay) )
                                listOfNodes[i].edges = nodeEdges
                            else:
                                return print("Node not found "+str(res[0][0]))
                       
                           
                        #else:
                            #cell contains a node, we ignore this cell 
                            #print("\nNode:\t"+cell)
                            #print("\nEdges: ")
                else:
                    break
                
       # print( listOfNodes)
        return listOfNodes 
        
        
#nodes = GraphInput().sheetImport("Graph.xlsx")
        
