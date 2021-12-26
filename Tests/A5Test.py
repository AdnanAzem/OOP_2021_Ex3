import unittest

from src.GraphAlgo import GraphAlgo


class A0Test(unittest.TestCase):

    def test_init(self):
        print("test_init")
        g_algo = GraphAlgo()
        graph = g_algo.load_from_json('../data/A5.json')
        self.assertIsNotNone(g_algo)
        self.assertIsNotNone(graph)

    def test_save(self):
        print("test_save")
        g_algo = GraphAlgo()
        file = '../data/A5.json'
        g_algo.load_from_json(file)
        g_algo.save_to_json(file + "_saved")
        file = '../data/A5.json_saved'
        self.assertIsNotNone(file)


    def test_load(self):
        print("test_load")
        #self.ga.save_to_json('../data/A1.json_saved')
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json('../data/A5.json_saved')
        self.assertIsNotNone(g_algo2)
        #self.assertEqual(self.ga.get_graph(), g_algo2.get_graph())

    def test_shortest_path(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A5.json'
        g_algo.load_from_json(file)
        shortPath = g_algo.shortest_path(0, 33)
        self.assertEqual(shortPath, (10.825353805051655, [0, 2, 3, 13, 14, 29, 30, 31, 32, 21, 33]))
        shortPath = g_algo.shortest_path(27, 2)
        self.assertEqual(shortPath, (5.4816317292326495, [27, 29, 14, 13, 3, 2]))
        shortPath = g_algo.shortest_path(5, 39)
        self.assertEqual(shortPath, (5.309728161990876, [5, 13, 14, 15, 39]))
        shortPath = g_algo.shortest_path(34, 16)
        self.assertEqual(shortPath, (6.88689973509148, [34, 22, 23, 24, 25, 16]))
        shortPath = g_algo.shortest_path(10, 10)
        self.assertEqual(shortPath, (0.0, [10]))

    def test_TSP(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A5.json'
        g_algo.load_from_json(file)
        tsp = g_algo.TSP([1,2,3,30,15,47])
        self.assertEqual(tsp, [1, 3, 2, 29, 14, 15, 14, 29, 30, 29, 14, 15, 39, 40, 41, 42, 43, 44, 46, 47])
        tsp = g_algo.TSP([1,5,30,15,7,36])
        self.assertEqual(tsp, [1, 6, 7, 6, 5, 29, 14, 15, 31, 36, 31, 30])
        tsp = g_algo.TSP([46,27,33,5,20])
        self.assertEqual(tsp, [46, 21, 20, 29, 30, 31, 32, 21, 33, 29, 14, 13, 5, 13, 14, 29, 27])
        tsp = g_algo.TSP([7,4,46,16])
        self.assertEqual(tsp, [7, 11, 13, 4, 44, 43, 42, 41, 40, 39, 15, 16, 15, 39, 40, 41, 42, 43, 44, 46])
        tsp = g_algo.TSP([5,5])
        self.assertEqual(tsp, [5])


    def test_centerPoint(self):
        print("test_centerPoint")
        g_algo = GraphAlgo()
        file = '../data/A5.json'
        g_algo.load_from_json(file)
        center = g_algo.centerPoint()
        self.assertEqual(center, (40, 9.291743173960954))

if __name__ == '__main__':
    unittest.main()
