#Jupiter - we can run code segment wise / block wise
# pip install jupyter // installation

#jupyter-notebook - this command will open our current project folders in browser. this is a service. service means anything u people can see in a browser.
# Also I can see both input and output when i open the older jupiter file

#ipynb - Interactive Python Notebook

import pandas as pd

#Below line is to basically display all rows
pd.set_option("display.max_rows", None)
try:
    file_reading = pd.read_csv("diamonds.csv")
    print(file_reading)
    column_names = file_reading.columns
    print(column_names)
except Exception as ex:
    print(ex)