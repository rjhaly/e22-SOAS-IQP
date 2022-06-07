import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import plot
import sipri_info as si


def draw_tl_map(tl_map_df, is_import):
    """Draws the "imports and exports over time" map using Plotly.
    :param pd.DataFrame tl_map_df: Map DataFrame for drawing choropleth map over time.
    :param boolean is_import: True is data is imports, False if exports
    :return: None, but creates HTML file
    """
    tl_map_df.astype({'odat': np.int64})
    tl_map_df = tl_map_df.sort_values(by="odat")

    if is_import:
        title = "Imports"
        color = "blues"
    else:
        title = "Exports"
        color = "reds"

    fig = px.choropleth(tl_map_df,
                        locations="iso_alpha",
                        hover_name="sipri_name",
                        color="All",
                        range_color=[tl_map_df["All"].min(), tl_map_df["All"].max()],
                        color_continuous_midpoint=0,
                        animation_group="sipri_name",
                        animation_frame="odat",
                        hover_data=si.WCATS_DICT.keys(),
                        labels=dict(si.WCATS_DICT, **{"odat": "Year", "All": "Total"}),
                        title="Major Conventional Weapon " + title + " over time from SIPRI",
                         color_continuous_scale=color,
                        projection="robinson")

    plot(fig)


def draw_transparency_map(transparency_df):
    """Draws the "Transparency indicator" map using Plotly.
    :param pd.DataFrame transparency_df: Map DataFrame for drawing choropleth map.
    :return: None, but creates HTML file
    """
    fig = px.choropleth(transparency_df,
                        locations=transparency_df.index,
                        hover_name="name",
                        color="Total Reports",
                        hover_data=['Exports/Imports', 'Military Holdings', 'National Production', 'SALW'],
                        title="Transparency Indicator: Number of voluntary UNROCA weapon reports 1992-2020",
                         color_continuous_scale="greens",
                        projection="robinson")

    plot(fig)


def draw_stockpiles_map(stockpiles_df):
    """Draws the "Stockpiles" map using Plotly.
    :param pd.DataFrame stockpiles_df: Map DataFrame for drawing choropleth map.
    :return: None, but creates HTML file
    """
    fig = px.choropleth(stockpiles_df,
                        locations=stockpiles_df.index,
                        hover_name="https://www.unroca.org/",
                        color="Total Recorded Munition Sum",
                        hover_data=['Most recent year (1992-2019)', 'I. Battle tanks', 'II. Armoured combat vehicles',
                                    'III. Large calibre artillery systems', 'IV. Combat aircraft',
                                    'V. Attack helicopters', 'VI. Warships', 'VII. Missiles and missile launchers'],
                        title="Major Conventional Weapon Stockpiles from UNROCA",
                         color_continuous_scale="purples",
                        projection="robinson")

    plot(fig)
