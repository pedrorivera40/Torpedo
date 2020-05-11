# Reading an excel file using Python
import xlrd
import math
import random
from excel_export import ExcelExport


class Node:
    """
    Node class
    """

    def __init__(self, city, edges, heuristic_value):
        """
        Node constructor

        :param city:
        :type city: String
        :param edges:
        :type edges: List<Edge>
        :param heuristic_value:
        :type heuristic_value: Float
        """
        self.previous = None
        self.time_from_start = math.inf
        self.city = city
        self.edges = edges
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
        Private method to return previous Node

        :param self:
        :returns previous:
        :type heuristic_value: Node
        """
        return self.previous

    def set_previous(self, previous):
        """
        Private method to setting previous Node

        :param self:
        :param previous:
        :type previous: Node
        :returns void:
        """
        self.previous = previous

    def get_time_from_start(self):
        """
        Private method to return time_from_start value

        :param self:
        :returns time_from_start:
        :type time_from_start: Float
        """
        return self.time_from_start

    def set_time_from_start(self, time_from_start):
        """
        Private method to setting traveled_time value

        :param self:
        :param time_from_start:
        :type time_from_start: Float
        :returns void:
        """
        self.time_from_start = time_from_start


class Edge:
    """
    Edge class
    """

    def __init__(self, destination, distance, speed_limit, traffic_delay):
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


class GraphInput:
    """
    Graph Input class, with methods for inputing graph data to our agent
    """

    def mapImport(self, path):
        list_of_nodes = []
        """
        Import graph data through an xlsx or xls file named "Graph.xlsx" or "Graph.xls" in the folder named 'AGENT'
        """
        # To open Workbook
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_index(0)

        # traverse the first column to store all the nodes, with their city name.
        for i in range(0, sheet.nrows):
            city_name = str(sheet.cell_value(i, 0))
            print(city_name)
            #city_heuristic_value = float(sheet.cell_value(i, 1))
            list_of_nodes.append(
                Node(city=city_name, edges=None, heuristic_value=1))

        # After making the list of nodes, we create the edge list for each Node :
        # traverse the first column
        for i in range(0, sheet.nrows):
            nodeEdges = []
            # go through each row
            for j in range(2, sheet.ncols):
                # Check each cell
                cell = sheet.cell_value(i, j)
                # Check if cell is empty, this means the end of a edge list
                if cell is not "":
                    # check if cell contains an edge
                    if cell[0] == '(':
                        # store the tuple information from the cell
                        res = []
                        temp = []
                        for token in cell.split(", "):
                            value = token.replace("(", "").replace(")", "")
                            temp.append(value)
                            if ")" in token:
                                res.append(tuple(temp))
                                temp = []

                        # store cell information
                        destination = None
                       # print(str(res[0][0]))
                        distance = float(res[0][1])
                        speed_limit = int(res[0][2])
                        traffic_delay = float(res[0][3])
                        # reference node from list_of_nodes
                        for node in list_of_nodes:

                            if node.city == str(res[0][0]):
                                destination = node
                                break
                        # no Node was found , could be an error in the Excel file
                        if destination is not None:
                            nodeEdges.append(Edge(destination=destination, distance=distance,
                                                  speed_limit=speed_limit, traffic_delay=traffic_delay))
                            list_of_nodes[i].edges = nodeEdges
                        else:
                            return print("Node not found "+str(res[0][0]))

                else:
                    break

        return list_of_nodes

    def sheetImport(self, path):
        list_of_nodes = []
        """
        Import graph data through an xlsx or xls file named "Graph.xlsx" or "Graph.xls" in the folder named 'AGENT'
        """
        # To open Workbook
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_index(0)

        # traverse the first column to store all the nodes, with their city name.
        for i in range(sheet.nrows):
            city_name = str(sheet.cell_value(i, 0))
            city_heuristic_value = float(sheet.cell_value(i, 1))
            list_of_nodes.append(
                Node(city=city_name, edges=None, heuristic_value=city_heuristic_value))

        # After making the list of nodes, we create the edge list for each Node :
        # traverse the first column
        for i in range(sheet.nrows):
            nodeEdges = []
            # go through each row
            for j in range(2, sheet.ncols):
                # Check each cell
                cell = sheet.cell_value(i, j)
                # Check if cell is empty, this means the end of a edge list
                if cell is not "":
                    # check if cell contains an edge
                    if cell[0] == '(':
                        # store the tuple information from the cell
                        res = []
                        temp = []
                        for token in cell.split(", "):
                            value = token.replace("(", "").replace(")", "")
                            temp.append(value)
                            if ")" in token:
                                res.append(tuple(temp))
                                temp = []

                        # store cell information
                        destination = None
                        distance = float(res[0][1])
                        speed_limit = int(res[0][2])
                        traffic_delay = float(res[0][3])
                        # reference node from list_of_nodes
                        for node in list_of_nodes:

                            if node.city == str(res[0][0]):
                                destination = node
                                break
                        # no Node was found , could be an error in the Excel file
                        if destination is not None:
                            nodeEdges.append(Edge(destination=destination, distance=distance,
                                                  speed_limit=speed_limit, traffic_delay=traffic_delay))
                            list_of_nodes[i].edges = nodeEdges
                        else:
                            return print("Node not found "+str(res[0][0]))

                else:
                    break

        return list_of_nodes

    def createProblem(self, problems, route, list_of_nodes):
        """
        """
        for j in range(0, problems):
            distance = 0.00
            ave_velocity = 0
            speed_limits = 0
            traffic_delay = 0.0
            for i in range(0, (len(route)-1)):
                distance += (GraphRead().distanceBetween(
                    start_node=route[i], end_node=route[i+1], list_of_nodes=list_of_nodes))
                speed_limits += (GraphRead().speed_limit(
                    start_node=route[i], end_node=route[i+1], list_of_nodes=list_of_nodes))
                if distance > 0:
                    traffic_delay += (random.uniform(0.00, 0.50))
                else:
                    traffic_delay = 0
            try:
                ave_velocity = (speed_limits/(len(route) - 1))
            except:
                ave_velocity = 0

            print(" \ndistance: "+str(distance)+" \nave_speed_limit: " +
                  str(ave_velocity)+"\ntraffic_delay: "+str(traffic_delay))
            try:
                print("Generating problems ")
                heuristic_value = (distance/ave_velocity)
                excel_export = ExcelExport('PR_MAP.xls')
                excel_export.select_sheet(str(j))
                excel_export.add_values(
                    [route[0], heuristic_value])
                excel_export.save()

            except:
                heuristic_value = 0
                print("\nHEURISTIC VALUE CALCULATED FOR " +
                      str(route[0])+": "+str(heuristic_value))

                excel_export = ExcelExport('PR_MAP.xls')
                excel_export.select_sheet(str(j))
                excel_export.add_values([route[0], heuristic_value])
                excel_export.save()
        return None


class GraphRead:
    """ 
    """

    def distanceBetween(self, start_node, end_node, list_of_nodes):
        """
        Given a list of nodes, a start node and an end node, gives back the distance travelled 
        Nodes must be adjacent 
        """

        for node in list_of_nodes:
            # print(str(node.get_city()))
            if node.get_city() == start_node:
                edges = node.get_edges()
                for edge in edges:
                    if str(edge.get_destination().get_city()) == str(end_node):
                        return edge.get_distance()
                    #print("Not match "+node.get_city())
                    # print(edge.get_destination().get_city())
                print("Error in Current "+str(node.get_city()) +
                      " Destination "+str(end_node))

                return 'Error'

    def speed_limit(self, start_node, end_node, list_of_nodes):
        """
        Given a list of nodes, a start node and an end node, gives back the distance travelled 
        Nodes must be adjacent 
        """

        for node in list_of_nodes:
            # print(str(node.get_city()))
            if node.get_city() == start_node:
                edges = node.get_edges()
                for edge in edges:
                    if str(edge.get_destination().get_city()) == str(end_node):
                        return edge.get_speed_limit()
                    #print("Not match "+node.get_city())
                    # print(edge.get_destination().get_city())
                print("Current "+str(node.get_city()) +
                      " Destination "+str(end_node))

                return 'Error'

    def traffic_delay(self, start_node, end_node, list_of_nodes):
        """
        Given a list of nodes, a start node and an end node, gives back the distance travelled 
        Nodes must be adjacent 
        """

        for node in list_of_nodes:
            # print(str(node.get_city()))
            if node.get_city() == start_node:
                edges = node.get_edges()
                for edge in edges:
                    if str(edge.get_destination().get_city()) == str(end_node):
                        return edge.get_speed_limit()
                    #print("Not match "+node.get_city())
                    # print(edge.get_destination().get_city())
                print("Current "+str(node.get_city()) +
                      " Destination "+str(end_node))

                return 'Error'

    def heuristicCalculation(self, route, list_of_nodes):
        """
        """
        #print("Calculating route length for route: "+str(route))
        distance = 0.00
        ave_velocity = 0
        speed_limits = 0
        traffic_delay = 0.0
        for i in range(0, (len(route)-1)):
            distance += (self.distanceBetween(
                start_node=route[i], end_node=route[i+1], list_of_nodes=list_of_nodes))
            speed_limits += (self.speed_limit(
                start_node=route[i], end_node=route[i+1], list_of_nodes=list_of_nodes))
            traffic_delay += (self.traffic_delay(
                start_node=route[i], end_node=route[i+1], list_of_nodes=list_of_nodes))
        try:
            ave_velocity = (speed_limits/(len(route) - 1))
        except:
            ave_velocity = 0

        print(" \ndistance: "+str(distance)+" \nave_speed_limit: " +
              str(ave_velocity)+"\ntraffic_delay: "+str(traffic_delay))
        try:
            heuristic_value = (distance/ave_velocity)
        except:
            heuristic_value = 0
        print("\nHEURISTIC VALUE CALCULATED FOR " +
              str(route[0])+": "+str(heuristic_value))
        return heuristic_value
