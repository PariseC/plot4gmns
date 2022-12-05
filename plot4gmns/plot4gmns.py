# -*- coding:utf-8 -*-
##############################################################
# Created Date: Sunday, December 4th 2022
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################

from .network import MultiNet
from .func_lib import (
    generate_multi_network_from_csv,
    extract_coordinates_by_network_mode,
    extract_coordinates_by_node_type,
    extract_coordinates_by_link_lane,
    extract_coordinates_by_link_free_speed,
    extract_coordinates_by_link_length)

from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.collections import PolyCollection


def show_network_by_mode(mnet: MultiNet, modes: tuple = ('all')) -> None:
    """draw network of different modes

    Args:
        mnet (MultiNet): MultiNet object
        modes (tuple, optional): network mode, valid to ('all', 'auto', 'bike', 'walk', 'railway'), Defaults to ('all').
    """
    
    extract_coordinates_by_network_mode(mnet, modes)
    fig, ax = plt.subplots(figsize=mnet.style.figure_szie, dpi=mnet.style.dpi)
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
            PolyCollection([mnet.POI.poi_coords],
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
        print("TypeError: please input a list of node 'osm_highway' ")
        sys.exit(0)
    fig, ax = plt.subplots(figsize=mnet.style.figure_szie, dpi=mnet.style.dpi)
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


def show_network_by_node_production(mnet: MultiNet) -> None:
    """
    draw network of different modes

     Parameters
    ----------
    mnet : MNet object
        a file path

    Returns
    -------
    None

    """


def show_network_by_node_attraction(mnet: MultiNet) -> None:
    pass


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
    fig, ax = plt.subplots(figsize=mnet.style.figure_szie, dpi=mnet.style.dpi)
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
    fig, ax = plt.subplots(figsize=mnet.style.figure_szie, dpi=mnet.style.dpi)
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
    fig, ax = plt.subplots(figsize=mnet.style.figure_szie, dpi=mnet.style.dpi)
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


if __name__ == "__main__":
    input_dir = "../dataset/Berlin"

    mnet = generate_multi_network_from_csv(input_dir)