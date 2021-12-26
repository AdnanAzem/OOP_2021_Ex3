import unittest

from src.GraphAlgo import GraphAlgo


class G_10_80Test(unittest.TestCase):
    g_algo = GraphAlgo()
    graph = g_algo.load_from_json('../data/100NodesTest.json')

    def test_init(self):
        print("test_init")
        self.assertIsNotNone(self.g_algo)
        self.assertIsNotNone(self.graph)

    def test_save(self):
        print("test_save")
        file = '../data/100NodesTest.json'
        self.g_algo.load_from_json(file)
        self.g_algo.save_to_json(file + "_saved")
        file = '../data/100NodesTest.json_saved'
        self.assertIsNotNone(file)


    def test_load(self):
        print("test_load")
        self.g_algo.load_from_json('../data/100NodesTest.json_saved')
        self.assertIsNotNone(self.g_algo)

    def test_shortest_path(self):
        print("test_shortest_path")
        shortPath = self.g_algo.shortest_path(98,15)
        self.assertEqual(shortPath, (1.2281845618857088, [98, 15]))

    def test_TSP(self):
        print("test_shortest_path")
        tsp = self.g_algo.TSP([20,50,96,30,2])
        self.assertEqual(tsp, [20, 40, 30, 40, 50, 12, 2, 12, 96])


    def test_centerPoint(self):
        print("test_centerPoint")
        center = self.g_algo.centerPoint()
        self.assertEqual(center, (96, 5.762368245598537))

if __name__ == '__main__':
    unittest.main()
