import unittest

from src.GraphAlgo import GraphAlgo


class A0Test(unittest.TestCase):

    def test_init(self):
        print("test_init")
        g_algo = GraphAlgo()
        graph = g_algo.load_from_json('../data/A0.json')
        self.assertIsNotNone(g_algo)
        self.assertIsNotNone(graph)

    def test_save(self):
        print("test_save")
        g_algo = GraphAlgo()
        file = '../data/A0.json'
        g_algo.load_from_json(file)
        g_algo.save_to_json(file + "_saved")
        file = '../data/A0.json_saved'
        self.assertIsNotNone(file)


    def test_load(self):
        print("test_load")
        #self.ga.save_to_json('../data/A1.json_saved')
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json('../data/A0.json_saved')
        self.assertIsNotNone(g_algo2)
        #self.assertEqual(self.ga.get_graph(), g_algo2.get_graph())

    def test_shortest_path(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A0.json'
        g_algo.load_from_json(file)
        shortPath = g_algo.shortest_path(0, 3)
        self.assertEqual(shortPath, (4.3086815935816, [0, 1, 2, 3]))
        shortPath = g_algo.shortest_path(3, 1)
        self.assertEqual(shortPath, (2.8136021362086723, [3, 2, 1]))
        shortPath = g_algo.shortest_path(2, 7)
        self.assertEqual(shortPath, (7.075480502869546, [2, 3, 4, 5, 6, 7]))
        shortPath = g_algo.shortest_path(10, 5)
        self.assertEqual(shortPath, (6.876636893080519, [10, 9, 8, 7, 6, 5]))
        shortPath = g_algo.shortest_path(10, 10)
        self.assertEqual(shortPath, (0.0, [10]))

    def test_TSP(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A0.json'
        g_algo.load_from_json(file)
        tsp = g_algo.TSP([1,2,3])
        self.assertEqual(tsp, [1, 3, 2])
        tsp = g_algo.TSP([1,5,10])
        self.assertEqual(tsp, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        tsp = g_algo.TSP([10,1])
        self.assertEqual(tsp, [10, 0, 1])
        tsp = g_algo.TSP([7,4,9,1])
        self.assertEqual(tsp, [7, 6, 5, 4, 10, 0, 1, 0, 10, 9])
        tsp = g_algo.TSP([5,5])
        self.assertEqual(tsp, [5])


    def test_centerPoint(self):
        print("test_centerPoint")
        g_algo = GraphAlgo()
        file = '../data/A0.json'
        g_algo.load_from_json(file)
        center = g_algo.centerPoint()
        self.assertEqual(center, (7, 6.806805834715163))

if __name__ == '__main__':
    unittest.main()
