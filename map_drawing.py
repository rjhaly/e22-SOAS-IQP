import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import plot
import db_ops
import sipri_info as si

def draw_tl_map(tl_map_df):
    """Draws the "imports minus exports over time" map using Plotly.
    :param pd.DataFrame tl_map_df: Map DataFrame for drawing choropleth map over time.
    :return: None, but creates HTML file
    """
    tl_map_df.astype({'odat': np.int64})
    tl_map_df = tl_map_df.sort_values(by="odat")

    fig = px.choropleth(tl_map_df,
                        locations="iso_alpha",
                        hover_name="sipri_name",
                        color="All",
                        range_color=[tl_map_df["All"].min(), tl_map_df["All"].max()],
                        color_continuous_midpoint=0,
                        animation_group="sipri_name",
                        animation_frame="odat",
                        hover_data=si.WCATS_DICT.keys(),
                        labels=dict(si.WCATS_DICT, **{"odat": "Order Date", "All": "total"}),
                        projection="robinson")

    plot(fig)

def draw_transparency_map(transparency_df):

    fig = px.choropleth(transparency_df,
                        locations=transparency_df.index,
                        hover_name="name",
                        color="Index",
                        hover_data=['Exports/Imports','Military Holdings','National Production','SALW','Total'],
                        projection="robinson")

    plot(fig)

def draw_stockpiles_map(stockpiles_df):
    fig = px.choropleth(stockpiles_df,
                        locations=stockpiles_df.index,
                        hover_name="name",
                        color="Stockpiles",
                        hover_data=['Year','Tanks','Combat vehicles','Artillery','Aircraft','Helicopters','Warships','Missiles/Missile launchers','Stockpiles'],
                        projection="robinson")

    plot(fig)
