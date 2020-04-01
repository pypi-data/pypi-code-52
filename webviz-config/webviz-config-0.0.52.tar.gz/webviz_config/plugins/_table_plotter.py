from pathlib import Path
from collections import OrderedDict
from typing import Optional, List, Dict, Any

import numpy as np
import pandas as pd
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash import Dash
import webviz_core_components as wcc

from .. import WebvizPluginABC
from ..webviz_store import webvizstore
from ..common_cache import CACHE


# pylint: disable=too-many-instance-attributes
class TablePlotter(WebvizPluginABC):
    """### TablePlotter

Adds a plotter to the webviz instance, using tabular data from a provided csv file.
If feature is requested, the data could also come from a database.

* `csv_file`: Path to the csv file containing the tabular data. Either absolute
              path or relative to the configuration file.
* `plot_options`: A dictionary of plot options to initialize the plot with
* `lock`: If `True`, only the plot is shown, all dropdowns for changing
          plot options are hidden.
"""

    def __init__(
        self,
        app: Dash,
        csv_file: Path,
        plot_options: dict = None,
        filter_cols: list = None,
        lock: bool = False,
    ):

        super().__init__()

        self.plot_options = plot_options if plot_options else {}
        self.lock = lock
        self.csv_file = csv_file
        self.data = get_data(self.csv_file)
        self.set_filters(filter_cols)
        self.columns = list(self.data.columns)
        self.numeric_columns = list(
            self.data.select_dtypes(include=[np.number]).columns
        )
        self.plotly_theme = app.webviz_settings["theme"].plotly_theme
        self.set_callbacks(app)

    def set_filters(self, filter_cols: Optional[list]) -> None:
        self.filter_cols = []
        self.use_filter = False
        if filter_cols:
            for col in filter_cols:
                if col in self.data.columns:
                    if self.data[col].nunique() != 1:
                        self.filter_cols.append(col)
            if self.filter_cols:
                self.use_filter = True

    def add_webvizstore(self) -> List[tuple]:
        return [(get_data, [{"csv_file": self.csv_file}])]

    @property
    def plots(self) -> dict:
        """A list of available plots and their options"""
        return {
            "scatter": ["x", "y", "size", "color", "facet_col"],
            "histogram": [
                "x",
                "y",
                "color",
                "facet_col",
                "barmode",
                "barnorm",
                "histnorm",
            ],
            "bar": ["x", "y", "color", "facet_col"],
            "scatter_3d": ["x", "y", "z", "size", "color"],
            "line": ["x", "y", "color", "line_group", "facet_col"],
            "line_3d": ["x", "y", "z", "color"],
            "box": ["x", "y", "color", "facet_col"],
            "violin": ["x", "y", "color", "facet_col"],
            "scatter_matrix": ["dimensions", "size", "color"],
            "parallel_coordinates": ["dimensions"],
            "parallel_categories": ["dimensions"],
            "density_contour": ["x", "y", "color", "facet_col"],
        }

    @property
    def plot_args(self) -> dict:
        """A list of possible plot options and their default values"""
        return OrderedDict(
            {
                "x": {
                    "options": self.columns,
                    "value": self.plot_options.get("x", self.columns[0]),
                    "multi": False,
                },
                "y": {
                    "options": self.columns,
                    "value": self.plot_options.get("y", self.columns[0]),
                    "multi": False,
                },
                "z": {
                    "options": self.columns,
                    "value": self.plot_options.get("z", self.columns[0]),
                    "multi": False,
                },
                "size": {
                    "options": self.numeric_columns,
                    "value": self.plot_options.get("size", None),
                    "multi": False,
                },
                "color": {
                    "options": self.columns,
                    "value": self.plot_options.get("color", None),
                    "multi": False,
                },
                "facet_col": {
                    "options": self.columns,
                    "value": self.plot_options.get("facet_col", None),
                    "multi": False,
                },
                "line_group": {
                    "options": self.columns,
                    "value": self.plot_options.get("line_group", None),
                    "multi": False,
                },
                "barmode": {
                    "options": ["stack", "group", "overlay", "relative"],
                    "value": self.plot_options.get("barmode", "stack"),
                    "multi": False,
                },
                "barnorm": {
                    "options": ["fraction", "percent"],
                    "value": self.plot_options.get("barnorm", None),
                    "multi": False,
                },
                "histnorm": {
                    "options": [
                        "percent",
                        "propability",
                        "density",
                        "propability density",
                    ],
                    "value": self.plot_options.get("histnorm", None),
                    "multi": False,
                },
                "trendline": {
                    "options": self.numeric_columns,
                    "value": None,
                    "multi": False,
                },
                "dimensions": {
                    "options": self.columns,
                    "value": self.plot_options.get("dimensions", self.columns),
                    "multi": True,
                },
            }
        )

    def filter_layout(self) -> Optional[list]:
        """Makes dropdowns for each dataframe column used for filtering."""
        if not self.use_filter:
            return None
        df = self.data
        dropdowns = [html.H4("Set filters")]
        for col in self.filter_cols:
            if df[col].dtype == np.float64 or df[col].dtype == np.int64:
                min_val = df[col].min()
                max_val = df[col].max()
                mean_val = df[col].mean()
                dropdowns.append(
                    html.Div(
                        children=[
                            html.Details(
                                open=True,
                                children=[
                                    html.Summary(col.lower().capitalize()),
                                    dcc.RangeSlider(
                                        id=self.uuid(f"filter-{col}"),
                                        min=min_val,
                                        max=max_val,
                                        step=(max_val - min_val) / 10,
                                        marks={
                                            min_val: f"{min_val:.2f}",
                                            mean_val: f"{mean_val:.2f}",
                                            max_val: f"{max_val:.2f}",
                                        },
                                        value=[min_val, max_val],
                                    ),
                                ],
                            )
                        ]
                    )
                )
            else:
                elements = list(self.data[col].unique())
                dropdowns.append(
                    html.Div(
                        children=[
                            html.Details(
                                open=True,
                                children=[
                                    html.Summary(col.lower().capitalize()),
                                    dcc.Dropdown(
                                        id=self.uuid(f"filter-{col}"),
                                        options=[
                                            {"label": i, "value": i} for i in elements
                                        ],
                                        value=elements,
                                        multi=True,
                                    ),
                                ],
                            )
                        ]
                    )
                )
        return dropdowns

    def plot_option_layout(self) -> List[html.Div]:
        """Renders a dropdown widget for each plot option"""
        divs = []
        # The plot type dropdown is handled separate
        divs.append(
            html.Div(
                style=self.style_options_div,
                children=[
                    html.H4("Set plot options"),
                    html.P("Plot type"),
                    dcc.Dropdown(
                        id=self.uuid("plottype"),
                        clearable=False,
                        options=[{"label": i, "value": i} for i in self.plots],
                        value=self.plot_options.get("type", "scatter"),
                    ),
                ],
            )
        )
        # Looping through all available plot options
        # and renders a dropdown widget
        for key, arg in self.plot_args.items():
            divs.append(
                html.Div(
                    style=self.style_options_div,
                    id=self.uuid(f"div-{key}"),
                    children=[
                        html.P(key),
                        dcc.Dropdown(
                            id=self.uuid(f"dropdown-{key}"),
                            clearable=False,
                            options=[{"label": i, "value": i} for i in arg["options"]],
                            value=arg["value"],
                            multi=arg["multi"],
                        ),
                    ],
                )
            )
        return divs

    @property
    def style_options_div(self) -> Dict[str, str]:
        """Style for active plot options"""
        return {"display": "grid"}

    @property
    def style_options_div_hidden(self) -> Dict[str, str]:
        """Style for hidden plot options"""
        return {"display": "none"}

    @property
    def layout(self) -> html.Div:
        return html.Div(
            children=[
                wcc.FlexBox(
                    children=[
                        html.Div(
                            id=self.uuid("selector-row"),
                            style={"display": "none"}
                            if self.lock
                            else {"width": "15%"},
                            children=self.plot_option_layout(),
                        ),
                        wcc.Graph(
                            id=self.uuid("graph-id"),
                            style={"height": "80vh", "width": "60%"},
                        ),
                        html.Div(style={"width": "15%"}, children=self.filter_layout()),
                    ],
                )
            ]
        )

    @property
    def plot_output_callbacks(self) -> List[Output]:
        """Creates list of output dependencies for callback
        The outputs are the graph, and the style of the plot options"""
        outputs = []
        outputs.append(Output(self.uuid("graph-id"), "figure"))
        for plot_arg in self.plot_args.keys():
            outputs.append(Output(self.uuid(f"div-{plot_arg}"), "style"))
        return outputs

    @property
    def plot_input_callbacks(self) -> List[Input]:
        """Creates list of input dependencies for callback
        The inputs are the plot type and the current value
        for each plot option
        """
        inputs = []
        inputs.append(Input(self.uuid("plottype"), "value"))
        for plot_arg in self.plot_args.keys():
            inputs.append(Input(self.uuid(f"dropdown-{plot_arg}"), "value"))
        for filtcol in self.filter_cols:
            inputs.append(Input(self.uuid(f"filter-{filtcol}"), "value"))
        return inputs

    def set_callbacks(self, app: Dash) -> None:
        @app.callback(self.plugin_data_output, [self.plugin_data_requested])
        def _user_download_data(data_requested: Optional[int]) -> str:
            return (
                WebvizPluginABC.plugin_data_compress(
                    [
                        {
                            "filename": "table_plotter.csv",
                            "content": get_data(self.csv_file).to_csv(),
                        }
                    ]
                )
                if data_requested
                else ""
            )

        @app.callback(self.plot_output_callbacks, self.plot_input_callbacks)
        def _update_output(*args: Any) -> tuple:
            """Updates the graph and shows/hides plot options"""
            plot_type = args[0]
            # pylint: disable=protected-access
            plotfunc = getattr(px._chart_types, plot_type)
            plotargs = {}
            div_style = []
            data = self.data
            # Filter dataframe if filter columns are available
            if self.use_filter:
                plot_inputs = args[1 : -len(self.filter_cols)]
                filter_inputs = args[-len(self.filter_cols) :]
                data = filter_dataframe(data, self.filter_cols, filter_inputs)
            else:
                plot_inputs = args[1:]
            for name, plot_arg in zip(self.plot_args.keys(), plot_inputs):
                if name in self.plots[plot_type]:
                    plotargs[name] = plot_arg
                    div_style.append(self.style_options_div)
                else:
                    div_style.append(self.style_options_div_hidden)
            return (plotfunc(data, template=self.plotly_theme, **plotargs), *div_style)


@CACHE.memoize(timeout=CACHE.TIMEOUT)
@webvizstore
def get_data(csv_file: Path) -> pd.DataFrame:
    return pd.read_csv(csv_file, index_col=None)


@CACHE.memoize(timeout=CACHE.TIMEOUT)
def filter_dataframe(
    dframe: pd.DataFrame, columns: list, column_values: List[list]
) -> pd.DataFrame:
    df = dframe.copy()
    if not isinstance(columns, list):
        columns = [columns]
    for filt, col in zip(column_values, columns):
        if isinstance(filt, list):
            if df[col].dtype == np.float64 or df[col].dtype == np.int64:
                df = df.loc[df[col].between(filt[0], filt[1])]
            else:
                df = df.loc[df[col].isin(filt)]
        else:
            df = df.loc[df[col] == filt]
    return df
