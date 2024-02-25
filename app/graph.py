from altair import Chart
from altair import Tooltip
import pandas as pd
from pandas import DataFrame


chart_properties = {"width": 400, "height": 400, "background": "white", "padding": 5}


def chart(input_df: DataFrame, input_x: str, input_y: str, input_target: str) -> Chart:
    graph = Chart(
        input_df,
        title=f"{input_y} by {input_x} for {input_target}",
        height=chart_properties["height"],
        width=chart_properties["width"],
        background=chart_properties["background"],
        padding=chart_properties["padding"],

        ).mark_circle(size=50).encode(
        x=f"{input_x}:Q",
        y=f"{input_y}:Q",
        color=f"{input_target}:N",
        tooltip=Tooltip(input_df.columns.values.tolist())
        ).interactive()
    return graph
