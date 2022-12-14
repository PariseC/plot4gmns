import os
import pandas as pd
from .utility_lib import (required_files,
                          required_columns,
                          check_dir,
                          get_file_names_from_folder_by_type,
                          check_required_files_exist)
from .network import MultiNet


def read_single_csv_file(file_name: str, geo_type: str) -> tuple:
    df = pd.read_csv(os.path.join(file_name))

    # check if the required columns exist
    for column in required_columns[geo_type]:
        if column not in df.columns:
            print(f"{file_name} does not contain required column {column}!")
            return (None, False)
    return (df, True)

def generate_multi_network_from_csv(input_dir: str = './',) -> MultiNet:
    """read Multi-mode network from CSV file in the format of GMNS

    Args:
        input_dir (str, optional): a file path. Defaults to './'.

    Returns:
        MNet: MultiNet object
    """
    # Tell the user the input files format
    print(f"Please note, required input files are {required_files}")
    print(f"Reading network from CSV files in {input_dir}...")

    # Check if the input directory exists
    if not os.path.exists(input_dir):
        raise Exception(f"Input directory {input_dir} does not exist!")

    # check if the input directory contains all required files
    all_csv_files = get_file_names_from_folder_by_type(input_dir, 'csv')
    isRequired = check_required_files_exist(required_files, all_csv_files)

    if not isRequired:
        raise Exception(f"Input directory {input_dir} does not contain all required files!")

    # initialize a MultiNet object
    mnet = MultiNet()

    def read_single_csv_file(file_name: str, geo_type: str) -> tuple:
        df = pd.read_csv(os.path.join(file_name))

        # check if the required columns exist
        for column in required_columns[geo_type]:
            if column not in df.columns:
                print(f"{file_name} does not contain required column {column}!")
                return (None, False)
        return (df, True)

    # add required files and / or  optional files to the MultiNet object
    files_found = check_dir(input_dir)
    for filename in files_found:
        path_filename = os.path.join(input_dir, filename)
        element = filename.split(".")[0]
        if element == 'node':
            mnet.node.value, mnet.node_loaded = read_single_csv_file(path_filename, element)
        elif element == 'link':
            mnet.link.value, mnet.link_loaded = read_single_csv_file(path_filename, element)
            mnet.link.convert_str_to_geometry()
            mnet.link.extract_link_modes()
        elif element == 'poi':
            mnet.POI.value, mnet.POI_loaded = read_single_csv_file(path_filename, element)
            mnet.POI.convert_str_to_geometry()
        elif element == 'demand':
            mnet.demand.value, mnet.demand_loaded = read_single_csv_file(path_filename, element)
            mnet.demand.convert_str_to_geometry()
        elif element == 'zone':
            mnet.zone.value, mnet.zone_loaded = read_single_csv_file(path_filename, element)
            mnet.zone.convert_str_to_geometry()
    print("Complete file loading")
    return mnet

def extract_coordinates_by_network_mode(mnet: MultiNet, modes: tuple) -> None:
    # extract node,link, and poi coordinates of the specified network mode
    mnet.link.update_coords_by_str_attr(modes)
    mnet.node.update_coords(column='node_id',values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        raise Exception("please try other modes")

def extract_coordinates_by_node_type(mnet: MultiNet, osm_highway: list) -> None:
    # extract node,link, and poi coordinates of the specified node type

    x_coords = []
    y_coords = []
    for highway_type in osm_highway:
        mnet.node.update_coords(column='osm_highway', values=[highway_type])
        x_coords.append(mnet.node.x_coords)
        y_coords.append(mnet.node.y_coords)
        if len(mnet.node.x_coords) == 0:
            print(f"ValueError: '{highway_type}' osm_highway not found")

    mnet.node.x_coords = x_coords
    mnet.node.y_coords = y_coords
    mnet.link.update_coords_by_str_attr(modes=('all'))
    mnet.POI.update_coords_by_poi_type()
    if not x_coords:
        raise Exception("please try other keys")

def extract_coordinates_by_link_lane(mnet: MultiNet, lanes: tuple) -> None:
    # extract node,link, and poi coordinates of the specified network link lanes

    mnet.link.update_coords_by_float_attr(column='lanes', min_v=lanes[0], max_v=lanes[1])
    mnet.node.update_coords(column='node_id', values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        raise Exception("no results found, please try other keys")

def extract_coordinates_by_link_free_speed(mnet: MultiNet, free_speed: tuple) -> None:
    # extract node,link, and poi coordinates of the specified network link free speed

    mnet.link.update_coords_by_float_attr(column='free_speed', min_v=free_speed[0], max_v=free_speed[1])
    mnet.node.update_coords(column='node_id', values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        raise Exception("no results found, please try other keys")

def extract_coordinates_by_link_length(mnet: MultiNet, length: tuple) -> None:
    # extract node,link, and poi coordinates of the specified network link length

    mnet.link.update_coords_by_float_attr(column='length', min_v=length[0], max_v=length[1])
    mnet.node.update_coords(column='node_id', values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        raise Exception("no results found, please try other keys")

def extract_coordinates_by_link_lane_distribution(mnet: MultiNet, column: str) -> None:
    # extract node,link, and poi coordinates of the network link lane distribution

    if mnet.link.value[column].isnull().any():
        raise Exception(f"ValueError: nan found in {column}")
    mnet.link.update_coords_by_attr_distribution(column)
    mnet.node.update_coords(column='node_id')
    mnet.POI.update_coords_by_poi_type()

def extract_coordinates_by_link_capacity_distribution(mnet: MultiNet, column: str) -> None:
    # extract node,link, and poi coordinates of the network link capacity distribution

    if mnet.link.value[column].isnull().any():
        raise Exception(f"ValueError: nan found in {column}")
    mnet.link.update_coords_by_attr_distribution(column)
    mnet.node.update_coords(column='node_id')
    mnet.POI.update_coords_by_poi_type()

def extract_coordinates_by_poi_type(mnet: MultiNet, poi_type: list) -> None:
    # extract node,link, and poi coordinates of the specified network POI type

    mnet.node.update_coords(column='node_id')
    mnet.link.update_coords_by_str_attr(modes=('all'))
    mnet.POI.update_coords_by_poi_type(poi_type=poi_type)
    if len(mnet.POI.poi_coords) == 0:
        raise Exception("no results found, please try other keys")

def extract_coordinates_by_poi_attr_distribution(mnet: MultiNet, column: str) -> None:
    # extract node,link, and poi coordinates of the network POI attraction or production distribution

    if mnet.POI.value[column].isnull().any():
        raise Exception(f"ValueError: nan found in {column}")
    mnet.node.update_coords(column='node_id')
    mnet.link.update_coords_by_str_attr(modes=('all'))
    mnet.POI.update_coords_by_attr_distribution(column=column)

def count_demand_matrix(mnet: MultiNet) -> None:
    # count demand matrix of zones

    mnet.demand.update_demand_matrix(mnet.zone.value.shape[0])

def extract_coordinates_by_demand_OD(mnet: MultiNet, load_zone: bool, load_network: bool) -> None:
    # extract coordinates of the network demand OD

    mnet.demand.update_coords()
    if load_zone:
        mnet.zone.update_coords()
    if load_network:
        mnet.node.update_coords()
        mnet.link.update_coords_by_str_attr(modes=('all'))
        mnet.POI.update_coords_by_poi_type()