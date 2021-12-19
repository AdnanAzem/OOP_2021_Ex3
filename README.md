# OOP_2021_Ex3

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


