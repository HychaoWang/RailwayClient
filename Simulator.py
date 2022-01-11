import pandas as pd


class Simulator:
    time = 0
    pos = 0
    v = 0
    model = 'NRM'

    def __init__(self):
        super(Simulator, self).__init__()
        # self.data = self.get_all_data()

    def get_all_data(self):
        path = 'data/data1.csv'
        raw = pd.read_csv(path)
        p = raw[self.model + '_position']
        v = raw[self.model + '_velocity']
        dict = {}
        for i in range(len(p)):
            dict[p[i]] = v[i]
        return dict

    def update(self):
        dict = self.get_all_data()
        key = list(dict.keys())[self.time]
        self.pos = key
        self.v = dict[key]
        self.time += 1

    def emit_data(self):
        self.update()
        p = self.pos
        speed = self.v
        return p, speed

    def set_model(self, m):
        self.model = m
        self.get_all_data()

