import sys
import os
from flask import render_template, Blueprint
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

# Add the directory
sys.path.insert(0, '/Users/jiocllic/Desktop/BapsfWork/myflaskapp/myflaskapp/')

from MSI_generator.fake_data import FakeMSI

bp = Blueprint('my_blueprint', __name__)

def create_plot():
    # Instantiate FakeMSI class and generate shot data
    fake_msi = FakeMSI()
    fake_shot = fake_msi.generate_shot()

    # Use discharge_current as y values
    y = fake_shot['discharge_current'].tolist()

    # Assume time is the index of each discharge_current value
    x = list(range(len(y)))

    data = [
        go.Bar(
            x=x,  # assign x as the list of indices
            y=y,  # assign y as the list of discharge_current values
            marker=dict(color='black')  # set bar color to blue
        )
    ]

    # add a layout
    layout = go.Layout(
        title='Discharge Current over Time',  # Graph title
        xaxis=dict(title='Time'),  # x-axis label
        yaxis=dict(title='Discharge Current'),  # y-axis label
        paper_bgcolor='white',  # set background color for the area including graph title and labels
        plot_bgcolor='white',  # set background color for the plot area
    )

    fig = go.Figure(data=data, layout=layout)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/datashots')
def datashots():
    bar = create_plot()
    return render_template('datashots.html', plot=bar)
