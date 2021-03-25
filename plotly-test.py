#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     22/03/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
import plotly

plotly.tools.set_credentials_file(username = 'jeandavid54', api_key = 'qcQaSwY4ins2ePHs0RhL')
#plotly.offline.init_notebook_mode(connected=True)
import plotly.offline as py

print(plotly.__version__)

import plotly.figure_factory as ff
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")
table = ff.create_table(df)
py.plot(table, filename='table.html')          #iplot if in jupyter notebook

import plotly.graph_objs as go
data = [go.Bar(x=df.School, y=df.Women)]
py.plot(data, filename='women-bar.html')
