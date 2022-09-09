import os
import pandas as pd


linkp = os.path.dirname(os.path.abspath(__file__))


class level():
    def __init__(self, number):
        self.link = os.path.join(linkp, str(number)+".csv")
        self.data = pd.read_csv(self.link)

