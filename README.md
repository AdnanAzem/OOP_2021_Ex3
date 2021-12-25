# OOP_2021_Ex3

<h2>Part 1:</h2>
<h2>Ex3 contains the following classes: </h2>

<ul>
  <li><b>NodeData</b> - representing a vertex in the graph.</li>
  <li><b>EdgeData</b> - representing a edge in the graph.</li>
  <li><b>DiGraph</b>- implementing GraphInterface- representing a directed weighted graph.</li>
  <li><b>GraphAlgo</b>- implementing GraphAlgoInterface interface.</li>
</ul>

<hr>

<h2>Graph implementation</h2>

DiGraph class represents a directed weighted graph, represented by a dictionary. The reason we chose to represent the graph in a dictionary is because it allows easy access to each node in the graph, therefor questions like whether two nodes are connected and how many edges are in the graph can be answered in O(1). Adding a new node to the graph, or connecting two nodes in the graph with an edge, can also be done easily in O(1). Connecting simply requires adding each of the nodes to the other node's neighbors list with the wanted weight, and removing an edge requires removing each of the nodes from the other node's neighbors list.

![1](https://user-images.githubusercontent.com/88532380/146683277-3d0431bc-5173-4d1c-9695-f2cb47665f31.png)

<hr>

<h2>Part 2:</h2>
<h2>the basic functions in graph :</h2>
<ul>
  <li><b>add node</b> - add a new node to the graph</li>
  <li><b>add_edge</b> - add a new edge to the graph between two vertices</li>
  <li><b>get_all v</b> - return a dictionary contains all the graph vertices</li>
  <li><b>remove node</b> - remove a vertex from the graph</li>
  <li><b>remove edge</b> - remove an edge between two vertices</li>
  <li><b>all_in_edges_of_node</b> - returns a dictionary of all nodes connected to the given node.</li>
  <li><b>all_out_edeges_of_node</b> - returns a dictionary of all nodes connected from the given node.</li>
  <li><b>e_size</b> - return the number of edges in the graph</li>
  <li><b>v_size</b> - returns the number of vertices in the graph</li>
  <li><b>get_mc</b> - return the number of changes computed on the graph</li>
</ul>

<h3>the graph class includes functions such as:</h3>
<ul>
<li><b>__def __init (self):</b> this method initilizes a new directed weighted graph.</li>

<li><b>def v_size(self) -> int:</b> this method returns the number of nodes in the graph.</li>

<li><b>def e_size(self) -> int:</b> this method returns the number of edges in the graph</li>

<li><b>def get_all_v(self) -> dict:</b> this method returns a dict with all the nodes in the graph, with the ID of each node ass the key and the node_data itself as the value.</li>

<li><b>def get_all_v(self) -> dict:</b> this method returns a dict with all the nodes in the graph, with the ID of each node ass the key and the node_data itself as the value.</li>

<li><b>def all_in_edges_of_node(self, id1: int) -> dict:</b> this method returns a dict contains all the edges that comming to the given node.</li>

<li><b>def add_edge(self, id1: int, id2: int, weight: float) -> bool:</b> this method connect between the two given nodes with the given weight. if the weight is not positive, or if there is already an edge between the two nodes, or if one of them does not exist in the graph, the method does nothing and simply returns false. else, the method add the ID of the src node to the outedges dictionary of the graph, and add the ID of the dest to the Inedges dictionary of the graph. returns true.</li>

<li><b>def add_node(self, node_id: int, pos: tuple = None) -> bool:</b> this nethod creates a new node with the given id, and add it to the graph. it creates a new inner dictionery for each of the edge list for the new node, and returns true.</li>

<li><b>def remove_node(self, node_id: int) -> bool:</b> this method removes the node woth the given ID from the graph, and delete all its edges, coming out andd comming in. first, the method delete the node from the nodes dictionary, and then runs on each of its neighbors and pop the node from the list of neighbors of its neighbors. if the node removed successfully, the method returns true. if there is no such node the method returns false and simply does nothing.</li>

<li><b>def remove_edge(self, node_id1: int, node_id2: int) -> bool:</b> this method removes the edge between the two given nodes from the graph. if there is no such edge, or one of the nodes does not exist, the method returns false and does nothing delede from the dictionery of the inner edges the src node,and delede from the dictionery of the out edges the dest node, returns true.</li>
</ul>

<hr>

<h1>Algorithms</h1>
GraphAlgo class represents the regular Graph Theory algorithms including:
<ul>
  <li>load_from_json(file)</li>
  <li>save_to_json(file)</li>
  <li>shortestPath(int src, int dest) -> (float, list)</li>
  <li>TSP(self, node_lst: List[int]) -> (List[int], float):</li>
  <li>centerPoint(self) -> (int, float):</li>
  <li>plot_graph()</li>
</ul>

<hr>

<h2>The Dijkstra algorithm</h2>
The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes,[7] but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph,

![2](https://user-images.githubusercontent.com/88532380/146683804-7c8c4155-0dbc-4195-9dd0-1a925c659eae.gif)

<h2>Part 3:</h2>
In this part we were required to comparison of runtime of 4 different algorithms(shortest_path, TSP, center, Load & Save) on a directed weighted graph between 2 implementations: our implementation in java (Ex2 project), our implementation in python (this project). The comparisons are in this wiki page project.<br>
<a href="https://github.com/AdnanAzem/OOP_2021_Ex3/wiki/Comparisons">Click for more informations</a>

