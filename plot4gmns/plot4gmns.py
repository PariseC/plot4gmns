# -*- coding:utf-8 -*-
##############################################################
# Created Date: Sunday, December 4th 2022
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################
import numpy as np
import pandas as pd
from .network import MultiNet
from .func_lib import (
    generate_multi_network_from_csv,
    extract_coordinates_by_network_mode,
    extract_coordinates_by_node_type,
    extract_coordinates_by_link_lane,
    extract_coordinates_by_link_free_speed,
    extract_coordinates_by_link_length,
    extract_coordinates_by_link_lane_distribution,
    extract_coordinates_by_link_capacity_distribution,
    extract_coordinates_by_poi_type,
    extract_coordinates_by_poi_attr_distribution,
    count_demand_matrix,
    extract_coordinates_by_demand_OD)
import seaborn as sns
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.collections import PolyCollection

def fill_network_link(mnet: MultiNet, column: str, value) -> None:
    mnet.link.value[column].fillna(value, inplace=True)

def show_network_by_mode(mnet: MultiNet, modes: tuple = ('all')) -> None:
    """draw network of different modes

    Args:
        mnet (MultiNet): MultiNet object
        modes (tuple, optional): network mode, valid to ('all', 'auto', 'bike', 'walk', 'railway'), Defaults to ('all').
    """
    
    extract_coordinates_by_network_mode(mnet, modes)
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=mnet.style.link_style.linewidth,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        ax.add_collection(
            PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           facecolors=mnet.style.poi_style.facecolor,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0))
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_node_type(mnet: MultiNet, osm_highway: list) -> None:
    """
    draw network of different modes

     Parameters
    ----------
    mnet : MNet object
        a file path
    modes : tuple
        network mode, a valid network mode must belong to [ 'auto', 'bike', 'walk', 'railway']
        users can also simply input 'all' to select all modes

    Returns
    -------
    None

    """
    if isinstance(osm_highway, str):
        osm_highway_ = [osm_highway]
    elif isinstance(osm_highway, list):
        osm_highway_ = osm_highway
    else:
        raise Exception("TypeError: str or list is expected ")
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        extract_coordinates_by_node_type(mnet, osm_highway_)
        for id in range(len(mnet.node.x_coords)):
            x_coords = mnet.node.x_coords[id]
            y_coords = mnet.node.y_coords[id]
            type = osm_highway_[id]
            if len(x_coords) > 0:
                ax.scatter(x_coords,
                           y_coords,
                           marker=mnet.style.node_style.markers[type],
                           c=mnet.style.node_style.colors[type],
                           s=mnet.style.node_style.size,
                           edgecolors=mnet.style.node_style.edgecolors,
                           zorder=2)
    # draw network links
    if mnet.link_loaded:
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=mnet.style.link_style.linewidth,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        ax.add_collection(
            PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           facecolors=mnet.style.poi_style.facecolor,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0))
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_link_lane(mnet: MultiNet, min_lanes: int, max_lanes: int) -> None:
    """
    draw network of different modes

    Parameters
    ----------
    mnet : MNet object
        a file path
    min_lanes : int
        the minimum number of lanes to be displayed
    max_lanes : int
        the maximum number of lanes to be displayed
    Returns
    -------
    None

    """
    if min_lanes > max_lanes:
        print("ValueError: 'min_lanes' should not less than 'max_lanes' ")
    extract_coordinates_by_link_lane(mnet, (min_lanes, max_lanes))
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=mnet.style.link_style.linewidth,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        ax.add_collection(
            PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           facecolors=mnet.style.poi_style.facecolor,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0))
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_link_free_speed(mnet: MultiNet, min_free_speed: int, max_free_speed: int) -> None:
    """
    draw network of different modes

    Parameters
    ----------
    mnet : MNet object
        a file path
    min_free_speed : int
        the minimum free speed of link to be displayed
    max_free_speed : int
        the maximum free speed of link to be displayed
    Returns
    -------
    None

    """
    if min_free_speed > max_free_speed:
        print("ValueError: 'min_lanes' should not less than 'max_lanes' ")
    extract_coordinates_by_link_free_speed(
        mnet, (min_free_speed, max_free_speed))
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=mnet.style.link_style.linewidth,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        ax.add_collection(
            PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           facecolors=mnet.style.poi_style.facecolor,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0))
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_link_length(mnet: MultiNet, min_length: int, max_length: int) -> None:
    """
    draw network of different modes

    Parameters
    ----------
    mnet : MNet object
        a file path
    min_length : int
        the shortest link to be displayed
    max_length : int
        the longest link to be displayed,
    Returns
    -------
    None

    """
    if min_length > max_length:
        print("ValueError: 'min_lanes' should not less than 'max_lanes' ")
    extract_coordinates_by_link_length(mnet, (min_length, max_length))
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=mnet.style.link_style.linewidth,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        ax.add_collection(
            PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           facecolors=mnet.style.poi_style.facecolor,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0))
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_link_lane_distribution(mnet: MultiNet) -> None:
    """
      draw network of different modes

      Parameters
      ----------
      mnet : MNet object
      Returns
      -------
      None

      """
    extract_coordinates_by_link_lane_distribution(mnet,'lanes')
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        max_v, min_v = max(mnet.link.attr_distribution), min(mnet.link.attr_distribution)
        w = np.array(mnet.link.attr_distribution) / max_v * 4.5 + 0.5
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=w,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        ax.add_collection(
            PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           facecolors=mnet.style.poi_style.facecolor,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0))
    # add legend
    proxies = [Line2D([0, 1], [0, 1], color=mnet.style.link_style.linecolor, linewidth=0.5),
               Line2D([0, 1], [0, 1], color=mnet.style.link_style.linecolor, linewidth=5)]
    ax.legend(proxies, ['%s:%.4f' % ('lanes', min_v), '%s:%.4f' % ('lanes', max_v)], loc='upper right')
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_link_capacity_distribution(mnet: MultiNet) -> None:
    """
      draw network of different modes

      Parameters
      ----------
      mnet : MNet object
      Returns
      -------
      None

      """
    extract_coordinates_by_link_lane_distribution(mnet, 'capacity')
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        max_v, min_v = max(mnet.link.attr_distribution), min(mnet.link.attr_distribution)
        w = np.array(mnet.link.attr_distribution) / max_v * 4.5 + 0.5
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=w,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        ax.add_collection(
            PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           facecolors=mnet.style.poi_style.facecolor,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0))
    # add legend
    proxies = [Line2D([0, 1], [0, 1], color=mnet.style.link_style.linecolor, linewidth=0.5),
               Line2D([0, 1], [0, 1], color=mnet.style.link_style.linecolor, linewidth=5)]
    ax.legend(proxies, ['%s:%.4f' % ('lanes', min_v), '%s:%.4f' % ('lanes', max_v)], loc='upper right')
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_poi_type(mnet: MultiNet, poi_type: list or str) -> None:
    """
      draw network of different modes

      Parameters
      ----------
      mnet : MNet object
      poi_type : list/str
        POI types need to display
      Returns
      -------
      None

      """
    if isinstance(poi_type,str):
        poi_type_ = [poi_type]
    elif isinstance(poi_type,list):
        poi_type_ = poi_type
    else:
        raise  Exception("TypeError: str or list is expected ")
    extract_coordinates_by_poi_type(mnet=mnet, poi_type=poi_type_)
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=mnet.style.link_style.linewidth,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        ax.add_collection(
            PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           facecolors=mnet.style.poi_style.facecolor,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0))
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_poi_production_distribution(mnet: MultiNet) -> None:
    """
      draw network of different modes

      Parameters
      ----------
      mnet : MNet object
      Returns
      -------
      None

      """
    extract_coordinates_by_poi_attr_distribution(mnet=mnet,column='production')
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=mnet.style.link_style.linewidth,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        poly_coll = PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           array = np.array(mnet.POI.attr_distribution),
                           cmap = mnet.style.cmap,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0)
        ax.add_collection(poly_coll)
        fig.colorbar(poly_coll, ax=ax)
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_by_poi_attraction_distribution(mnet: MultiNet) -> None:
    """
      draw network of different modes

      Parameters
      ----------
      mnet : MNet object
      Returns
      -------
      None

      """
    extract_coordinates_by_poi_attr_distribution(mnet=mnet,column='attraction')
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    # draw network nodes
    if mnet.node_loaded:
        ax.scatter(mnet.node.x_coords,
                   mnet.node.y_coords,
                   marker=mnet.style.node_style.markers['other'],
                   c=mnet.style.node_style.colors['other'],
                   s=mnet.style.node_style.size,
                   edgecolors=mnet.style.node_style.edgecolors,
                   zorder=2)
    # draw network links
    if mnet.link_loaded:
        ax.add_collection(
            LineCollection(mnet.link.link_coords,
                           colors=mnet.style.link_style.linecolor,
                           linewidths=mnet.style.link_style.linewidth,
                           zorder=1))
    # draw network pois
    if mnet.POI_loaded:
        poly_coll = PolyCollection(mnet.POI.poi_coords,
                           alpha=0.7,
                           array = np.array(mnet.POI.attr_distribution),
                           cmap = mnet.style.cmap,
                           edgecolors=mnet.style.poi_style.edgecolor,
                           zorder=0)
        ax.add_collection(poly_coll)
        fig.colorbar(poly_coll, ax=ax)
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show figure
    plt.show()

def show_network_demand_matrix(mnet: MultiNet,annot: bool = False) -> None:
    """
      draw network of different modes

      Parameters
      ----------
      mnet : MNet object
      annot : bool
        True: show values
      Returns
      -------
      None

      """
    count_demand_matrix(mnet)
    max_vol = np.max(mnet.demand.demand_matrix.reshape(1, -1))
    min_vol = np.min(mnet.demand.demand_matrix.reshape(1, -1))
    labels = [str(i + 1) for i in range(mnet.zone.value.shape[0])]
    df = pd.DataFrame(mnet.demand.demand_matrix, index=labels, columns=labels)

    plt.figure(figsize=(mnet.style.figure_size),dpi=mnet.style.dpi)
    fig = sns.heatmap(data=df, vmax=max_vol, vmin=min_vol, annot=annot, cmap=mnet.style.cmap)
    sns.set(font_scale=1.5)
    plt.rc('font', family='Times New Roman', size=6)
    plt.xlabel('to_zone_id')
    plt.ylabel('from_zone_id')
    plt.tight_layout()
    # show fig
    plt.show()

def show_network_by_demand_OD(mnet: MultiNet, load_zone: bool = True, load_network: bool = False) -> None:
    """
      draw network of different modes

      Parameters
      ----------
      mnet : MNet object
      poi_type : list/str
        POI types need to display
      Returns
      -------
      None

      """
    extract_coordinates_by_demand_OD(mnet, load_zone, load_network)
    fig, ax = plt.subplots(figsize=mnet.style.figure_size, dpi=mnet.style.dpi)
    if load_network:
        # draw network nodes
        if mnet.node_loaded:
            ax.scatter(mnet.node.x_coords,
                       mnet.node.y_coords,
                       marker=mnet.style.node_style.markers['other'],
                       c=mnet.style.node_style.colors['other'],
                       s=mnet.style.node_style.size,
                       edgecolors=mnet.style.node_style.edgecolors,
                       zorder=2)
        # draw network links
        if mnet.link_loaded:
            ax.add_collection(
                LineCollection(mnet.link.link_coords,
                               colors=mnet.style.link_style.linecolor,
                               linewidths=mnet.style.link_style.linewidth,
                               zorder=1))
        # draw network pois
        if mnet.POI_loaded:
            ax.add_collection(
                PolyCollection(mnet.POI.poi_coords,
                               alpha=0.7,
                               facecolors=mnet.style.poi_style.facecolor,
                               edgecolors=mnet.style.poi_style.edgecolor,
                               zorder=0))
    if load_zone:
        ax.add_collection(
            PolyCollection(mnet.zone.zone_coords,
                           facecolors='none',
                           linewidths=mnet.style.zone_style.linewidth,
                           edgecolors=mnet.style.zone_style.edgecolors,
                           zorder=3)
        )
        for label in mnet.zone.zone_names:
            plt.annotate(
                str(label[0]),
                xy=(label[1],label[2]),
                xytext=(label[1], label[2]),
                weight='bold',
                color=mnet.style.zone_style.fontcolor,
                fontsize=mnet.style.zone_style.fontsize)
    # plot network demand flow
    w = np.array(mnet.demand.demand_OD_vol) / max(mnet.demand.demand_OD_vol) * 4.5 + 0.5
    ax.add_collection(LineCollection(mnet.demand.demand_OD_coords, colors='orange', linewidths=w, zorder=2))

    # add legend
    proxies = [Line2D([0, 1], [0, 1], color='orange', linewidth=0.5),
               Line2D([0, 1], [0, 1], color='orange', linewidth=5)]
    ax.legend(proxies, ['%s:%.4f' % ('volume', min(mnet.demand.demand_OD_vol)),
                        '%s:%.4f' % ('volume', max(mnet.demand.demand_OD_vol))])
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input_dir = r"E:\CoderStudio\Py\2022-09-11-open_source_packages\Berlin"

    mnet = generate_multi_network_from_csv(input_dir)

