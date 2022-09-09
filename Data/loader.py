import numpy as np
import pandas as pd
sprite = {
    'Pipeposx': [900, 1300, 1700],
    'Pipeposy': [250, 250, 250],
    'Pipeheight': [120, 120, 120],
    'Turtlex': [1000, 800, 0],
    'Turtley': [166, 166, 0],
    'TColor': ['green', 'red', 'green']
}
df = pd.DataFrame(sprite)

df.to_csv('./Data/1.csv')
