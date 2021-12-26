import unittest

from src.GraphAlgo import GraphAlgo


class A0Test(unittest.TestCase):

    def test_init(self):
        print("test_init")
        g_algo = GraphAlgo()
        graph = g_algo.load_from_json('../data/A2.json')
        self.assertIsNotNone(g_algo)
        self.assertIsNotNone(graph)

    def test_save(self):
        print("test_save")
        g_algo = GraphAlgo()
        file = '../data/A2.json'
        g_algo.load_from_json(file)
        g_algo.save_to_json(file + "_saved")
        file = '../data/A2.json_saved'
        self.assertIsNotNone(file)


    def test_load(self):
        print("test_load")
        #self.ga.save_to_json('../data/A1.json_saved')
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json('../data/A2.json_saved')
        self.assertIsNotNone(g_algo2)
        #self.assertEqual(self.ga.get_graph(), g_algo2.get_graph())

    def test_shortest_path(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A2.json'
        g_algo.load_from_json(file)
        shortPath = g_algo.shortest_path(0, 22)
        self.assertEqual(shortPath, (1.8493571998815432, [0, 21, 22]))
        shortPath = g_algo.shortest_path(27, 1)
        self.assertEqual(shortPath, (4.469872819320036, [27, 7, 8, 26, 1]))
        shortPath = g_algo.shortest_path(2, 18)
        self.assertEqual(shortPath, (9.780065181499051, [2, 1, 0, 16, 15, 14, 17, 18]))
        shortPath = g_algo.shortest_path(10, 16)
        self.assertEqual(shortPath, (6.673544720176219, [10, 9, 23, 22, 21, 0, 16]))
        shortPath = g_algo.shortest_path(10, 10)
        self.assertEqual(shortPath, (0.0, [10]))

    def test_TSP(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        file = '../data/A2.json'
        g_algo.load_from_json(file)
        tsp = g_algo.TSP([1,2,3,30,15])
        self.assertEqual(tsp, [1, 3, 2, 13, 14, 15, 14, 13, 30])
        tsp = g_algo.TSP([1,5,30])
        self.assertEqual(tsp, [1, 2, 6, 5, 6, 7, 8, 9, 10, 11, 20, 30])
        tsp = g_algo.TSP([10,1,27])
        self.assertEqual(tsp, [10, 26, 8, 7, 27, 7, 8, 26, 1])
        tsp = g_algo.TSP([7,4,9,1,16,22])
        self.assertEqual(tsp, [7, 6, 5, 4, 0, 16, 0, 21, 22, 23, 9, 8, 26, 1])
        tsp = g_algo.TSP([5,5])
        self.assertEqual(tsp, [5])


    def test_centerPoint(self):
        print("test_centerPoint")
        g_algo = GraphAlgo()
        file = '../data/A2.json'
        g_algo.load_from_json(file)
        center = g_algo.centerPoint()
        self.assertEqual(center, (0, 7.819910602212574))

if __name__ == '__main__':
    unittest.main()
