import unittest

from src.GraphAlgo import GraphAlgo


class A0Test(unittest.TestCase):

    def test_init(self):
        print("test_init")
        g_algo = GraphAlgo()
        graph = g_algo.load_from_json('../data/A4.json')
        self.assertIsNotNone(g_algo)
        self.assertIsNotNone(graph)

    def test_save(self):
        print("test_save")
        g_algo = GraphAlgo()
        file = '../data/A4.json'
        g_algo.load_from_json(file)
        g_algo.save_to_json(file + "_saved")
        file = '../data/A4.json_saved'
        self.assertIsNotNone(file)


    def test_load(self):
        print("test_load")
        #self.ga.save_to_json('../data/A1.json_saved')
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json('../data/A4.json_saved')
        self.assertIsNotNone(g_algo2)
        #self.assertEqual(self.ga.get_graph(), g_algo2.get_graph())

    def test_shortest_path(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A4.json'
        g_algo.load_from_json(file)
        shortPath = g_algo.shortest_path(0, 33)
        self.assertEqual(shortPath, (7.693742575385171, [0, 1, 2, 30, 31, 32, 33]))
        shortPath = g_algo.shortest_path(27, 2)
        self.assertEqual(shortPath, (4.593497952276543, [27, 28, 30, 2]))
        shortPath = g_algo.shortest_path(5, 39)
        self.assertEqual(shortPath, (8.412767490145846, [5, 6, 7, 8, 9, 10, 39]))
        shortPath = g_algo.shortest_path(34, 16)
        self.assertEqual(shortPath, (8.94479836642034, [34, 33, 32, 7, 6, 15, 16]))
        shortPath = g_algo.shortest_path(10, 10)
        self.assertEqual(shortPath, (0.0, [10]))

    def test_TSP(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A4.json'
        g_algo.load_from_json(file)
        tsp = g_algo.TSP([1,2,3,30,15,39])
        self.assertEqual(tsp, [1, 2, 3, 2, 30, 31, 32, 7, 6, 15, 6, 7, 8, 9, 10, 39])
        tsp = g_algo.TSP([1,5,30,15,7,36])
        self.assertEqual(tsp, [1, 31, 32, 7, 6, 15, 6, 5, 4, 3, 2, 30, 31, 32, 33, 35, 36])
        tsp = g_algo.TSP([10,1,27,38,5])
        self.assertEqual(tsp, [10, 2, 30, 28, 27, 2, 3, 4, 5, 4, 3, 2, 1, 2, 30, 31, 32, 33, 35, 36, 37, 38])
        tsp = g_algo.TSP([7,4,9,38,16,22])
        self.assertEqual(tsp, [7, 6, 5, 4, 10, 39, 38, 39, 10, 9, 19, 20, 21, 22, 21, 20, 19, 16])
        tsp = g_algo.TSP([5,5])
        self.assertEqual(tsp, [5])


    def test_centerPoint(self):
        print("test_centerPoint")
        g_algo = GraphAlgo()
        file = '../data/A4.json'
        g_algo.load_from_json(file)
        center = g_algo.centerPoint()
        self.assertEqual(center, (6, 8.071366078651435))

if __name__ == '__main__':
    unittest.main()
