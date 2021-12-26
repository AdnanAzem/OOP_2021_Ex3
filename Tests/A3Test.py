import unittest

from src.GraphAlgo import GraphAlgo


class A0Test(unittest.TestCase):

    def test_init(self):
        print("test_init")
        g_algo = GraphAlgo()
        graph = g_algo.load_from_json('../data/A3.json')
        self.assertIsNotNone(g_algo)
        self.assertIsNotNone(graph)

    def test_save(self):
        print("test_save")
        g_algo = GraphAlgo()
        file = '../data/A3.json'
        g_algo.load_from_json(file)
        g_algo.save_to_json(file + "_saved")
        file = '../data/A3.json_saved'
        self.assertIsNotNone(file)


    def test_load(self):
        print("test_load")
        #self.ga.save_to_json('../data/A1.json_saved')
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json('../data/A3.json_saved')
        self.assertIsNotNone(g_algo2)
        #self.assertEqual(self.ga.get_graph(), g_algo2.get_graph())

    def test_shortest_path(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A3.json'
        g_algo.load_from_json(file)
        shortPath = g_algo.shortest_path(0, 33)
        self.assertEqual(shortPath, (5.390098539186627, [0, 1, 2, 32, 33]))
        shortPath = g_algo.shortest_path(27, 2)
        self.assertEqual(shortPath, (4.293557694490976, [27, 7, 6, 2]))
        shortPath = g_algo.shortest_path(5, 44)
        self.assertEqual(shortPath, (3.8975456639642716, [5, 6, 7, 44]))
        shortPath = g_algo.shortest_path(48, 16)
        self.assertEqual(shortPath, (9.304560466788129, [48, 5, 6, 2, 1, 0, 16]))
        shortPath = g_algo.shortest_path(10, 10)
        self.assertEqual(shortPath, (0.0, [10]))

    def test_TSP(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A3.json'
        g_algo.load_from_json(file)
        tsp = g_algo.TSP([1,2,3,30,15,44])
        self.assertEqual(tsp, [1, 3, 2, 31, 30, 13, 14, 15, 39, 40, 41, 42, 43, 44])
        tsp = g_algo.TSP([1,5,30,15,48])
        self.assertEqual(tsp, [1, 48, 5, 13, 14, 15, 14, 13, 30])
        tsp = g_algo.TSP([10,1,27,48,5])
        self.assertEqual(tsp, [10, 7, 6, 5, 26, 8, 7, 27, 7, 8, 26, 1, 2, 6, 5, 48])
        tsp = g_algo.TSP([7,4,9,47,16,22])
        self.assertEqual(tsp, [7, 5, 48, 47, 48, 5, 4, 0, 21, 22, 23, 9, 23, 22, 21, 0, 16])
        tsp = g_algo.TSP([5,5])
        self.assertEqual(tsp, [5])


    def test_centerPoint(self):
        print("test_centerPoint")
        g_algo = GraphAlgo()
        file = '../data/A3.json'
        g_algo.load_from_json(file)
        center = g_algo.centerPoint()
        self.assertEqual(center, (2, 8.182236568942237))

if __name__ == '__main__':
    unittest.main()
