import unittest

from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class TestGraphAlgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.g = DiGraph()
        for i in range(11):
            cls.g.add_node(i)

        cls.g.add_edge(0, 1, 3.0)
        cls.g.add_edge(1, 2, 2.0)
        cls.g.add_edge(0, 2, 1.0)
        cls.g.add_edge(2, 0, 1.0)
        cls.g.add_edge(2, 1, 1.0)
        cls.g.add_edge(3, 4, 7.0)
        cls.g.add_edge(4, 6, 3.0)
        cls.g.add_edge(6, 5, 2.0)
        cls.g.add_edge(5, 4, 1.0)
        cls.g.add_edge(3, 5, 5.0)
        cls.g.add_edge(4, 3, 1.0)
        cls.g.add_edge(9, 7, 2.0)
        cls.g.add_edge(8, 10, 1.0)
        cls.g.add_edge(7, 9, 7.0)
        cls.g.add_edge(10, 9, 3.0)
        cls.g.add_edge(10, 7, 9.0)
        cls.g.add_edge(7, 8, 2.0)
        cls.g.add_edge(2, 7, 3.0)
        cls.g.add_edge(1, 3, 18.0)
        cls.g.add_edge(9, 5, 2.0)

        cls.ga = GraphAlgo(graph=cls.g)

    def test_shortest_path(self):
        spd = self.ga.shortest_path(1, 3)  # Path between 2 node that in the graph and connected.
        self.assertEqual(15.0, spd[0])
        sp = [1, 2, 7, 8, 10, 9, 5, 4, 3]
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(5, 0)  # Path between 2 node that in the graph and not connected.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(5, 12)  # Path between node in the graph to node that not in the graph.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(11, 7)  # Path between node that not in the graph to node in the graph.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(15, 12)  # Path between 2 node that not in the graph.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(4, 4)  # Path between node in the graph to himself.
        self.assertEqual(0.0, spd[0])
        sp = [4]
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(18, 18)  # Path between node that not in the graph to himself.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])


    def test_save(self):
        self.ga.save_to_json('graph.json')
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json('graph.json')
        self.assertEqual(self.ga.get_graph(), g_algo2.get_graph())

    def test_load(self):
        self.ga.save_to_json('graph.json')
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json('graph.json')
        self.assertEqual(self.ga.get_graph(), g_algo2.get_graph())

    def test_centerPoint(self):
        center = self.ga.centerPoint()
        self.assertEqual(center,(5, 4.0))

    def test_TSP(self):
        tsp =self.ga.TSP([1,8,3])
        self.assertEqual(tsp,[1, 2, 7, 8, 10, 9, 5, 4, 3])

    def test_Shortest_path(self):
        short = self.ga.shortest_path(1,7)
        self.assertEqual(short,(5.0, [1, 2, 7]))
