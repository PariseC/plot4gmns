# -*- coding: utf-8 -*-
# @Time    : 2022/11/29 10:48
# @Author  : Praise
# @File    : utility_lib.py
# obj:
import os
from pathlib import Path
from typing import Union

target_files = ['node.csv', 'link.csv', 'poi.csv']
required_files = ['node.csv', 'link.csv', 'poi.csv']
optional_files = ['demand.csv', 'zone.csv']

required_columns = {
    'node': ['x_coord', 'y_coord'],
    'link': ['geometry'],
    'poi': ['geometry'],
    'demand': ['geometry'],
    'zone': ['geometry']}

network_modes = ['all', 'bike', 'walk', 'auto', 'railway']


class NodeStyle:
    def __init__(self):
        self.size = 10
        self.edgecolors = 'none'
        self.markers = {
            'traffic_signals': 'd',
            'bus_stop': 's',
            'crossing': '+',
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


class Style:
    def __init__(self):
        self.figure_szie = (10, 8)
        self.dpi = 300
        self.node_style = NodeStyle()
        self.link_style = LinkStyle()
        self.poi_style = POIStyle()


def path2linux(path: Union[str, Path]) -> str:
    """Convert a path to a linux path, linux path can run in windows, linux and mac"""
    try:
        return path.replace("\\", "/")
    except Exception:
        return str(path).replace("\\", "/")


def validate_filename(path_filename: str, ) -> bool:
    filename_abspath = path2linux(os.path.abspath(path_filename))
    return bool(os.path.exists(filename_abspath))


def check_dir(input_dir: str,) -> list:
    files_found = []
    files_not_found = []
    for file in required_files + optional_files:
        path_filename = os.path.join(input_dir, file)
        if validate_filename(path_filename):
            files_found.append(file)
        else:
            files_not_found.append(file)
    print(f"The following file was found in the folder: \n \t {files_found}")
    print(f"The following file was not found in the folder: \n \t {files_not_found}")

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