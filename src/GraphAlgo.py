import heapq
import heapq as hq
import queue
import sys
from typing import List, Dict
from jsonEncoders import graphEncoder
import json
import matplotlib.pyplot as plt
import numpy as np
from src.GraphInterface import GraphInterface
from src import GraphAlgoInterface, Node
from src.DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface.GraphAlgoInterface):
    """
    This class implements GraphAlgoInterface.
    It represents a Directed Weighted Graph Theory algorithms.
    """

    def __init__(self, graph: DiGraph = None):
        """ Constructor. """
        self.__graph = graph

    def __ceil__(self):
        print('called')

    def get_graph(self) -> GraphInterface:
        """
        @return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    def isConnected(self):
        if(self.__graph != None and self.__graph.v_size()):
            return True
        if (self.__graph != None and self.__graph.v_size() == 1):
            return True
        if (self.graph == None):
            return True
        for myNode in self.__graph.get_all_v():
            n = myNode
            if (self.__graph.all_out_edges_of_node(n.getKey()) == None or self.__graph.all_out_edges_of_node(n.getKey()).size() == 0):
                return False


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from given node id1 to given node id2. using Dijkstra's Algorithm.
        @param id1: The source node id.
        @param id2: The destination node id.
        @return: The distance of the path (infinite if None),
                 a list of the nodes ids that the path goes through (empty list if None).
        """
        if not (id1 in self.__graph.get_all_v().keys()) or not (id2 in self.__graph.get_all_v().keys()):
            return float('inf'), []
        if id1 == id2:
            return 0.0, [id1]
        prev = {k: None for k in self.__graph.get_all_v().keys()}
        self.dijkstra(id1, id2, prev)
        if self.__graph.get_all_v().get(id2).get_tag() is float('inf'):
            return float('inf'), []
        path = []
        if prev.get(id2) is not None:
            path.insert(0, id2)
            node0 = prev.get(id2).get_key()
            while node0 != id1:
                path.insert(0, node0)
                node0 = prev.get(node0).get_key()
            path.insert(0, node0)
        return self.__graph.get_all_v().get(id2).get_tag(), path

    def dijkstra(self, src: int, dest: int, prev: dict):
        """
        Implements the Dijkstra's algorithm.
        Dijkstra is an algorithm for finding the shortest paths between two nodes in a graph.
        """
        visited = {k: False for k in self.__graph.get_all_v().keys()}
        nodes = []
        for n in self.__graph.get_all_v().values():
            if n.get_key() == src:
                n.set_tag(0.0)
                nodes.append(n)
            else:
                n.set_tag(float('inf'))
        hq.heapify(nodes)
        while nodes:
            rm = hq.heappop(nodes)
            if rm.get_key() == dest:
                return
            visited[rm.get_key()] = True
            if self.__graph.all_out_edges_of_node(rm.get_key()) is not None:
                for neighbor, weighted in self.__graph.all_out_edges_of_node(rm.get_key()).items():
                    node_neighbor = self.__graph.get_all_v().get(neighbor)
                    if visited[node_neighbor.get_key()] is False:
                        dist = rm.get_tag() + weighted
                        if dist < node_neighbor.get_tag():
                            node_neighbor.set_tag(dist)
                            prev[neighbor] = rm
                            hq.heappush(nodes, node_neighbor)

    def max_shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from given node id1 to given node id2. using Dijkstra's Algorithm.
        @param id1: The source node id.
        @param id2: The destination node id.
        @return: The distance of the path (infinite if None),
                 a list of the nodes ids that the path goes through (empty list if None).
        """
        if not (id1 in self.__graph.get_all_v().keys()) or not (id2 in self.__graph.get_all_v().keys()):
            return float('inf'), []
        if id1 == id2:
            return 0.0, [id1]
        prev = {k: None for k in self.__graph.get_all_v().keys()}
        self.dijkstra2(id1, id2, prev)
        if self.__graph.get_all_v().get(id2).get_tag() is float('inf'):
            return float('inf'), []
        path = []
        if prev.get(id2) is not None:
            path.insert(0, id2)
            node0 = prev.get(id2).get_key()
            while node0 != id1:
                path.insert(0, node0)
                node0 = prev.get(node0).get_key()
            path.insert(0, node0)
        return self.__graph.get_all_v().get(id2).get_tag(), path

    def dijkstra2(self, src: int, dest: int, prev: dict):
        """
        Implements the Dijkstra's algorithm.
        Dijkstra is an algorithm for finding the shortest paths between two nodes in a graph.
        """
        visited = {k: False for k in self.__graph.get_all_v().keys()}
        nodes = []
        for n in self.__graph.get_all_v().values():
            if n.get_key() == src:
                n.set_tag(0.0)
                nodes.append(n)
            else:
                n.set_tag(float('inf'))
        hq.heapify(nodes)
        while nodes:
            rm = hq.heappop(nodes)
            if rm.get_key() == dest:
                return
            visited[rm.get_key()] = True
            if self.__graph.all_out_edges_of_node(rm.get_key()) is not None:
                for neighbor, weighted in self.__graph.all_out_edges_of_node(rm.get_key()).items():
                    node_neighbor = self.__graph.get_all_v().get(neighbor)
                    if visited[node_neighbor.get_key()] is False:
                        dist = weighted + rm.get_tag()

                        if dist < node_neighbor.get_tag():
                            node_neighbor.set_tag(dist)
                            prev[neighbor] = rm
                            hq.heappush(nodes, node_neighbor)


    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @return: True if the loading was successful, False if not.
        """
        try:
            with open(file_name) as complex_data:
                data = complex_data.read()
                self.__graph = json.loads(data, object_hook=self.deserialize_objects)
                return True
        except ValueError:
            print('Decoding JSON has failed')
            return False
        except IOError:
            print('not found')
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False if not.
        """
        try:
            with open(file_name, 'w') as f:
                json.dump(self.__graph, f, cls=graphEncoder.GraphSerialize, indent=4)
                return True
        except TypeError:
            print("Unable to serialize the object")
            return False

        except IOError:
            print('not found')
            return False

    @staticmethod
    def deserialize_objects(obj):
        if 'Edges' in obj and 'Nodes' in obj:
            graph_result = DiGraph()

            for node in obj['Nodes']:
                if 'pos' in node:
                    graph_result.add_node(node['id'], eval(node['pos']) if type(node['pos']) is str else node['pos'])
                else:
                    graph_result.add_node(node['id'])

            for edge in obj['Edges']:
                graph_result.add_edge(edge['src'], edge['dest'], edge['w'])
            return graph_result

        return obj

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node,
        assuming the graph is strongly connected.
        :return: The nodes id, min-maximum distance
        """
        min_max_sp = 999999  # the minimum from the maximum shortest paths
        chosen_node = -1  # ID of the center

        for node in self.__graph.get_all_v().values():

            max_sp = self.max_shortest_path(node.get_key())
            if max_sp < min_max_sp:
                min_max_sp = max_sp
                chosen_node = node.get_key()

        return chosen_node, min_max_sp

    def max_shortest_path(self, key) -> float:
        """
        This method finds the shortest paths from given node to all other
        nodes in the graph using dijkstra algorithm.
        the method return the maximum shortest path it finds.
        """
        self.reset_tags()  # reset all tags to 0 -> NOT VISITED

        source = key
        deltas: Dict[int, float] = {}  # represent the 2D array of distances in dijkstra algorithm
        priority_q: [] = []  # a list representing the priority Queue we used in EX2

        total_dist = -1  # init the return dist
        path = []

        # in case one of the nodes is not in the graph
        if source not in self.__graph.getNodes():
            return sys.maxsize

        heapq.heappush(priority_q, (0.0, self.get_graph().get_all_v().get(source)))
        deltas[source] = 0.0

        while len(priority_q) > 0:

            node_distance, node = heapq.heappop(priority_q)  # Extract node with minimum delta(dist) and its delta

            node.tag = 1

            # iterate over the neighbors of node (out edges)
            for ngbr_id, ngbr_w in self.__graph.all_out_edges_of_node(node.get_key()).items():

                neighbour: Node = self.__graph.get_all_v().get(ngbr_id)  # neighbor node

                if neighbour.tag == 1:  # if the node already visited, skip him
                    continue

                new_neighbour_delta = deltas.get(node.get_key()) + ngbr_w  # calculating the new delta
                self.relax(new_neighbour_delta, deltas, neighbour, priority_q, ngbr_id, node)  # relax the map

        # Reset tags back to 0 when finished
        self.reset_tags()
        # find the maximum path from node to any node
        max_sp = -1
        for w in deltas.values():
            if w > max_sp:
                max_sp = w

        return max_sp

    def reset_tags(self):
        """
        This method reset all the graph's Node's tags to 0 -> NOT VISITED YET
        """
        for n in self.__graph.get_all_v().values():
            n.tag = 0  # NOT VISITED YET

    def relax(self, new_neighbour_delta: float, deltas: Dict[int, float], neighbour: Node, priority_q: list,
              ngbr_id: int, node: Node):
        if new_neighbour_delta < deltas.get(ngbr_id, float("inf")):
            heapq.heappush(priority_q, (new_neighbour_delta, neighbour))
            deltas[ngbr_id] = new_neighbour_delta
            neighbour.tag = 2  # node is queued
            neighbour.info = "{}".format(node.get_key())  # update the info so it contain its parent key so we

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        temp = []  # temp node list
        weight = 0
        if len(node_lst) == 0:  # check if the node's list is empty
            return None
        currNode = node_lst[0]
        temp.append(currNode)
        visitedNodes = []
        while len(node_lst) != 0:  # while there are still unvisited cities
            visitedNodes.append(currNode)  # add the current node to visitedNode list
            min_distance = sys.maxsize
            nextNode = currNode
            if currNode in node_lst:
                node_lst.remove(currNode)
            path = []  # init ans list of nodes

            for node in node_lst:  # go all over the unvisited nodes, calculate the closest one
                if node not in visitedNodes:
                    # print(self.shortest_path(currNode, node)[1])
                    short_path_result = self.shortest_path(currNode, node)
                    curr_distance = short_path_result[0]
                    if curr_distance < min_distance:
                        min_distance = curr_distance
                        nextNode = node
                        path = short_path_result[1]  # add the closest node to path list
                        currNode = nextNode

            for node in path:  # The closest node's path (out of all cities) is appended to the list which is to be returned
                if node is not path[0]:  # add all vertices if they are not the first item in the 'path' list
                    temp.append(node)
                    visitedNodes.append(node)
                    if node in node_lst:
                        node_lst.remove(node)

        if len(temp) == 0:
            return None
        for i in range(1, len(temp)):
            weight += self.__graph.get_out_Edge_Weight(temp[i-1], temp[i])
        return temp, weight


    def plot_graph(self) -> None:
        """
        Plots the graph. using matplotlib library.
        """
        plt.title('Graph')
        random_poses = {}

        for node in self.__graph.get_all_v().values():
            if node.get_pos() is None:
                while True:
                    x_r = np.random.rand(1)
                    y_r = np.random.rand(1)
                    z_r = np.random.rand(1)
                    x = x_r[0]
                    y = y_r[0]
                    z = z_r[0]

                    if x not in random_poses or y not in random_poses[x] or z not in random_poses[x][y]:
                        if x not in random_poses:
                            random_poses[x] = {}
                        if y not in random_poses[x]:
                            random_poses[x][y] = {}
                        if z not in random_poses[x][y]:
                            random_poses[x][y] = z
                        node.set_pos((x, y, z))
                        break
            else:
                x = node.get_pos()[0]
                y = node.get_pos()[1]
                z = node.get_pos()[2]
                if x not in random_poses or y not in random_poses[x] or z not in random_poses[x][y]:
                    if x not in random_poses:
                        random_poses[x] = {}
                    if y not in random_poses[x]:
                        random_poses[x][y] = {}
                    if z not in random_poses[x][y]:
                        random_poses[x][y] = z

            plt.plot(x, y, 'ro')
            plt.annotate(node.get_key(),  # this is the text
                         (x, y),  # this is the point to label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or center

        for node in self.__graph.get_all_v().values():
            if self.__graph.all_out_edges_of_node(node.get_key()) is not None:
                for dest in self.__graph.all_out_edges_of_node(node.get_key()).keys():
                    plt.annotate("",
                                 xy=(self.__graph.get_all_v()[dest].get_pos()[0],
                                     self.__graph.get_all_v().get(dest).get_pos()[1]), xycoords='data',
                                 xytext=(node.get_pos()[0], node.get_pos()[1]), textcoords='data',
                                 arrowprops=dict(arrowstyle="->",
                                                 color='blue',
                                                 connectionstyle="arc3"),
                                 )
        plt.show()



