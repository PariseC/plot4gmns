# -*- coding: utf-8 -*-
import os
from pathlib import Path
from typing import Union

target_files = ['node.csv', 'link.csv', 'poi.csv']
required_files = ['node.csv', 'link.csv', ]

optional_files = ['poi.csv', 'demand.csv']

# GMNS data elements with geometry information
gmns_basic_data_elements = ["node.csv", "link.csv", "geometry.csv", "zone.csv"]
gmns_advanced_data_elements = ["location.csv", "lane.csv", "movement.csv"]
gmns_elements = gmns_basic_data_elements + gmns_advanced_data_elements + optional_files

required_columns = {
    'node': ['x_coord', 'y_coord'],
    'link': ['geometry'],
    'zone': ['geometry'],  # boundary or geometry
    'zone_boundary': ['boundary'],  # boundary
    'geometry': ["geometry"],

    'poi': ['geometry'],
    'location': ["x_coord", "y_coord"],

    'demand': ['geometry'],

    'lane': ["geometry"],
    'movement': ["geometry"],
}

network_modes = ['all', 'bike', 'walk', 'auto', 'railway']


class NodeStyle:
    def __init__(self):
        self.size = 10
        self.edgecolors = 'none'
        self.markers = {
            'traffic_signals': 'd',
            'bus_stop': 's',
            'crossing': '>',
            'elevator': 's',
            'give_way': '^',
            'turning_circle': 's8',
            'other': 'o'}
        self.colors = {
            'traffic_signals': 'red',
            'bus_stop': 'green',
            'crossing': 'black',
            'elevator': 's',
            'give_way': 'darkorange',
            'turning_circle': 'blue',
            'other': 'black'}


class LinkStyle:
    def __init__(self):
        self.linewidth = 0.8
        self.linecolor = 'violet'


class POIStyle:
    def __init__(self):
        self.facecolor = 'y'
        self.edgecolor = 'black'


class DemandStyle:
    def __init__(self):
        self.linewidth = 1
        self.linecolor = 'b'


class ZoneStyle:
    def __init__(self):
        self.linewidth = 1
        self.edgecolors = 'blue'
        self.fontsize = 10
        self.fontcolor = 'r'


class LocationStyle:
    def __init__(self):
        self.size = 8
        self.facecolor = 'orange'
        self.edgecolor = 'black'


class LaneStyle:
    def __init__(self):
        self.linewidth = 1
        self.linecolor = 'green'


class MovementStyle:
    def __init__(self):
        self.linewidth = 1
        self.linecolor = 'brown'


class GeometryStyle:
    def __init__(self):
        self.linewidth = 1
        self.linecolor = 'gray'


class Style:
    def __init__(self):
        self.figure_size = (10, 8)
        self.dpi = 150
        self.cmap = 'jet'
        self.node_style = NodeStyle()
        self.link_style = LinkStyle()
        self.poi_style = POIStyle()
        self.demand_style = DemandStyle()
        self.zone_style = ZoneStyle()
        self.location_style = LocationStyle()
        self.lane_style = LaneStyle()
        self.movement_style = MovementStyle()
        self.geometry_style = GeometryStyle()


def path2linux(path: Union[str, Path]) -> str:
    """Convert a path to a linux path, linux path can run in windows, linux and mac"""
    try:
        return path.replace("\\", "/")
    except Exception:
        return str(path).replace("\\", "/")


def validate_filename(path_filename: str, ) -> bool:
    filename_abspath = path2linux(os.path.abspath(path_filename))
    return bool(os.path.exists(filename_abspath))


def check_dir(input_dir: str) -> list:
    files_found = []
    files_not_found = []
    for file in gmns_elements:
        path_filename = os.path.join(input_dir, file)
        if validate_filename(path_filename):
            files_found.append(file)
        else:
            files_not_found.append(file)

    print(f"Files found in the folder:\n\t{files_found}")
    # print(f"The following file(s) was not found in the folder: \n \t {files_not_found}")

    return files_found


def get_file_names_from_folder_by_type(dir_name: str, file_type: str = "txt",
                                       isTraverseSubdirectory: bool = False) -> list:
    if isTraverseSubdirectory:
        files_list = []
        for root, dirs, files in os.walk(dir_name):
            files_list.extend([os.path.join(root, file) for file in files])
        return [path2linux(file) for file in files_list if file.split(".")[-1] == file_type]

    # files in the first layer of the folder
    return [path2linux(os.path.join(dir_name, file)) for file in os.listdir(dir_name) if file.split(".")[-1] == file_type]


def check_required_files_exist(required_files: list, dir_files: list) -> bool:
    # format the required file name to standard linux path
    required_files = [path2linux(os.path.abspath(filename)) for filename in required_files]

    required_files_short = [filename.split("/")[-1] for filename in required_files]
    dir_files_short = [filename.split("/")[-1] for filename in dir_files]

    # mask have the same length as required_files
    mask = [file in dir_files_short for file in required_files_short]
    if all(mask):
        return True

    print(f"Error: Required files are not satisfied, \
          missing files are: {[required_files_short[i] for i in range(len(required_files_short)) if not mask[i]]}")

    return False


def generate_absolute_path(file_name: str = "p4g_fig.png", folder_name: str = "p4g_fig_results"):
    # create folder if not exist
    if not os.path.isdir(os.path.join(Path(__file__).parent, folder_name)):
        os.mkdir(os.path.join(Path(__file__).parent, folder_name))
    return path2linux(os.path.join(Path(__file__).parent, folder_name, file_name))


def update_filename(path_filename: str, ) -> str:
    """if the file name exist in path,then create new file name with _1, _1_1, ..."""
    filename_abspath = path2linux(os.path.abspath(path_filename))

    file_suffix = filename_abspath.split(".")[-1]
    file_without_suffix = filename_abspath[:-len(file_suffix) - 1]

    if os.path.exists(filename_abspath):
        filename_update = f"{file_without_suffix}_1.{file_suffix}"
        return update_filename(filename_update)
    return filename_abspath