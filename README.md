# OOP_2021_Ex3

<h2>Ex3 contains the following classes: </h2>

<p>NodeData - representing a vertex in the graph.</p>
<p>EdgeData - representing a edge in the graph.</p>
<p>DiGraph- implementing GraphInterface- representing a directed weighted graph.</p>
<p>GraphAlgo- implementing GraphAlgoInterface interface.</p>

<hr>

<h2>Graph implementation</h2>

DiGraph class represents a directed weighted graph, represented by a dictionary. The reason we chose to represent the graph in a dictionary is because it allows easy access to each node in the graph, therefor questions like whether two nodes are connected and how many edges are in the graph can be answered in O(1). Adding a new node to the graph, or connecting two nodes in the graph with an edge, can also be done easily in O(1). Connecting simply requires adding each of the nodes to the other node's neighbors list with the wanted weight, and removing an edge requires removing each of the nodes from the other node's neighbors list.

![1](https://user-images.githubusercontent.com/88532380/146683277-3d0431bc-5173-4d1c-9695-f2cb47665f31.png)

<hr>

<h2>the basic functions in graph :</h2>
<p>add node - add a new node to the graph</p>
<p>add_edge - add a new edge to the graph between two vertices</p>
<p>get_all v_ - return a dictionary contains all the graph vertices</p>
<p>remove node - remove a vertex from the graph</p>
<p>remove edge - remove an edge between two vertices</p>
<p>all_in_edges_of_node - returns a dictionary of all nodes connected to the given node.</p>
<p>all_out_edeges_of_node - returns a dictionary of all nodes connected from the given node.</p>
<p>e_size - return the number of edges in the graph</p>
<p>v_size - returns the number of vertices in the graph</p>
<p>get_mc - return the number of changes computed on the graph</p>
