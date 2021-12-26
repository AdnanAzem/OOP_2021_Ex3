import unittest

from numpy import inf

from src.GraphAlgo import GraphAlgo


class Test500Nodes(unittest.TestCase):
    g_algo = GraphAlgo()
    graph = g_algo.load_from_json('../data/500NodesTest.json')

    def test_init(self):
        print("test_init")
        self.assertIsNotNone(self.g_algo)
        self.assertIsNotNone(self.graph)

    def test_save(self):
        print("test_save")
        file = '../data/500NodesTest.json'
        self.g_algo.load_from_json(file)
        self.g_algo.save_to_json(file + "_saved")
        file = '../data/500NodesTest.json_saved'
        self.assertIsNotNone(file)


    def test_load(self):
        print("test_load")
        self.g_algo.load_from_json('../data/500NodesTest.json_saved')
        self.assertIsNotNone(self.g_algo)

    def test_shortest_path(self):
        print("test_shortest_path")
        shortPath = self.g_algo.shortest_path(250,22)
        print(shortPath)
        #self.assertEqual(shortPath, (inf, []))

    def test_TSP(self):
        print("test_shortest_path")
        tsp = self.g_algo.TSP([20,50,100,30,200,0,400])
        print(tsp)
        #self.assertEqual(tsp, [20,40,30,34,43,50,60,70,80,90,100,110,120,128,138,148,158,166,175,184,192,200,8,492,482,472,462,452,442,432,422,415,408,400,407,416,424,434,444,453,462,472,482,491,2,0])


    def test_centerPoint(self):
        print("test_centerPoint")
        center = self.g_algo.centerPoint()
        print(center)
        #self.assertEqual(center, (90, 30.010373420610506))

if __name__ == '__main__':
    unittest.main()
