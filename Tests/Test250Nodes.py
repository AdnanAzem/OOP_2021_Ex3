import unittest

from src.GraphAlgo import GraphAlgo


class Test250Nodes(unittest.TestCase):
    g_algo = GraphAlgo()
    graph = g_algo.load_from_json('../data/250NodesTest.json')

    def test_init(self):
        print("test_init")
        self.assertIsNotNone(self.g_algo)
        self.assertIsNotNone(self.graph)

    def test_save(self):
        print("test_save")
        file = '../data/250NodesTest.json'
        self.g_algo.load_from_json(file)
        self.g_algo.save_to_json(file + "_saved")
        file = '../data/250NodesTest.json_saved'
        self.assertIsNotNone(file)


    def test_load(self):
        print("test_load")
        self.g_algo.load_from_json('../data/250NodesTest.json_saved')
        self.assertIsNotNone(self.g_algo)

    def test_shortest_path(self):
        print("test_shortest_path")
        shortPath = self.g_algo.shortest_path(13,223)
        self.assertEqual(shortPath, (4.518360792526323, [13, 243, 233, 223]))

    def test_TSP(self):
        print("test_shortest_path")
        tsp = self.g_algo.TSP([20,240,17,30,159])
        self.assertEqual(tsp, [20, 10, 240, 20, 30, 26, 17, 248, 239, 229, 219, 209, 199, 189, 179, 169, 159])


    def test_centerPoint(self):
        print("test_centerPoint")
        center = self.g_algo.centerPoint()
        self.assertEqual(center, (98, 15.009852581748293))

if __name__ == '__main__':
    unittest.main()
