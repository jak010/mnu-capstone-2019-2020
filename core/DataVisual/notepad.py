import os
import pandas as pd

from collections import Counter

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE

from flask import render_template
# bokeh visualized setup process
def processVisualizedData():
    train_path = os.getcwd()+"/core/csvDataSet/TrainSet.csv"
    data_set = pd.read_csv(train_path)

    x_data = []
    y_data = []

    process_figure = figure(title="Process ",
                   x_axis_type="log",
                   tools="pan, wheel_zoom, box_zoom, reset, previewsave",
                   )

    for key, val in Counter(data_set["process"]).items():
        x_data.append(key)
        y_data.append(val)

    x = sorted(x_data, reverse=True)  # process
    y = sorted(y_data, reverse=True)  # counter

    process_figure.diamond(
        x,y, color="red", legend="TEST"
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(process_figure)
    return script,div,js_resources,css_resources


