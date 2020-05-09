import xlrd
import xlwt
from xlutils.copy import copy
from TorpedoBackend.Agent.graph import Node, Edge

print('Map Builder')

map_name = input('Type the name of the map: ')

cities = input('Type the name of all cities separated by comma: ')

cities = cities.split(',')

dic = {}

for i in range(len(cities)):
    cities[i] = cities[i].lstrip()  # Remove leading spaces (if any)
    heuristic_value = input('Type the heuristic value for %s: ' % (cities[i],))
    city = Node(cities[i], None, heuristic_value)
    dic[cities[i]] = city

for city in cities:

    neighbors = input('Type the name of the neighbors for %s separated by comma: ' % (city, ))
    if neighbors != '':
        neighbors = neighbors.split(',')

        edges = []

        for i in range(len(neighbors)):

            neighbors[i] = neighbors[i].lstrip()  # Remove leading spaces (if any)
            distance = input('Type the distance to %s: ' % (neighbors[i],))
            speed_limit = input('Type the speed limit to %s: ' % (neighbors[i],))
            traffic_delay = input('Type the traffic_delay to %s: ' % (neighbors[i],))
            edges.append(Edge(dic[neighbors[i]], distance, speed_limit, traffic_delay))

        dic[city].edges = edges


workbook = copy(xlrd.open_workbook('Agent/Graph.xlsx'))
sheet = workbook.add_sheet(map_name)

for i in range(len(cities)):
    sheet.write(i, 0, cities[i])  # First column insert city
    sheet.write(i, 1, dic[cities[i]].heuristic_value)  # Second column insert heuristic value
    neighbors = dic[cities[i]].edges
    for j in range(len(neighbors)):
        destination = neighbors[j].destination.city
        distance = neighbors[j].distance
        speed_limit = neighbors[j].speed_limit
        traffic_delay = neighbors[j].traffic_delay
        neighbor = '(%s, %s, %s, %s)' % (destination, distance, speed_limit, traffic_delay, )
        sheet.write(i, 2 + j, neighbor)

workbook.save('Agent/Graph.xls')
