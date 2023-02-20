import os
import pandas as pd
from .utility_lib import (required_files,
                          required_columns,
                          check_dir,
                          get_file_names_from_folder_by_type,
                          check_required_files_exist,
                          update_filename,
                          generate_absolute_path,
                          path2linux)
from .network import MultiNet
from keplergl import KeplerGl


def read_single_csv_file(file_name: str, geo_type: str) -> tuple:
    df = pd.read_csv(os.path.join(file_name))

    # check if the required columns exists
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
    print(f"Please note that required input files are {required_files}")
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

    # generate keplergl map, currently only support node, link, poi
    # The reason to load data again but not from mnet is to avoid errors after further operations for nodes, links and poi in mnet.
    map_layer_data = {}
    if mnet.node_loaded:
        map_layer_data["node"] = pd.read_csv(path2linux(f"{input_dir}/node.csv")).fillna("None_")
        print("Test path: ", f"{input_dir}/node.csv")
    if mnet.link_loaded:
        map_layer_data["link"] = pd.read_csv(f"{input_dir}/link.csv").fillna("None_")
    if mnet.POI_loaded:
        map_layer_data["poi"] = pd.read_csv(f"{input_dir}/poi.csv").fillna("None_")
    if mnet.demand_loaded:
        map_layer_data["demand"] = pd.read_csv(f"{input_dir}/demand.csv").fillna("None_")
    if mnet.zone_loaded:
        map_layer_data["zone"] = pd.read_csv(f"{input_dir}/zone.csv").fillna("None_")

    vis_map = generate_visualization_map_using_keplergl(map_layer_data)
    path_vis_map = update_filename(generate_absolute_path(file_name="plot4gmns_vis_map.html",
                                                          folder_name=path2linux(os.path.join(os.getcwd(), "p4g_fig_results"))))
    vis_map.save_to_html(file_name=path_vis_map)
    # print(f"Successfully generate interactive map visualization to {path_vis_map}")

    return mnet


def generate_visualization_map_using_keplergl(map_layer_data: dict, map_config: dict = None) -> None:

    # use default map config if map_config is not provided
    map_config_default = {'version': 'v1',
                          'config': {
                              'visState': {'filters': [],
                                           'layers': [{'id': 'wthskia',
                                                       'type': 'geojson',
                                                       'config': {'dataId': 'link',
                                                                  'label': 'link',
                                                                  'color': [18, 147, 154],
                                                                  'highlightColor': [252, 242, 26, 255],
                                                                  'columns': {'geojson': 'geometry'},
                                                                  'isVisible': True,
                                                                  'visConfig': {'opacity': 0.8,
                                                                                'strokeOpacity': 0.8,
                                                                                'thickness': 0.5,
                                                                                'strokeColor': None,
                                                                                'colorRange': {'name': 'Global Warming',
                                                                                               'type': 'sequential',
                                                                                               'category': 'Uber',
                                                                                               'colors': ['#5A1846',
                                                                                                          '#900C3F',
                                                                                                          '#C70039',
                                                                                                          '#E3611C',
                                                                                                          '#F1920E',
                                                                                                          '#FFC300']},
                                                                                'strokeColorRange': {'name': 'Global Warming',
                                                                                                     'type': 'sequential',
                                                                                                     'category': 'Uber',
                                                                                                     'colors': ['#5A1846',
                                                                                                                '#900C3F',
                                                                                                                '#C70039',
                                                                                                                '#E3611C',
                                                                                                                '#F1920E',
                                                                                                                '#FFC300']},
                                                                                'radius': 10,
                                                                                'sizeRange': [0, 10],
                                                                                'radiusRange': [0, 50],
                                                                                'heightRange': [0, 500],
                                                                                'elevationScale': 5,
                                                                                'enableElevationZoomFactor': True,
                                                                                'stroked': True,
                                                                                'filled': False,
                                                                                'enable3d': False,
                                                                                'wireframe': False},
                                                                  'hidden': False,
                                                                  'textLabel': [{'field': None,
                                                                                 'color': [255, 255, 255],
                                                                                 'size': 18,
                                                                                 'offset': [0, 0],
                                                                                 'anchor': 'start',
                                                                                 'alignment': 'center'}]},
                                                       'visualChannels': {'colorField': None,
                                                                          'colorScale': 'quantile',
                                                                          'strokeColorField': None,
                                                                          'strokeColorScale': 'quantile',
                                                                          'sizeField': None,
                                                                          'sizeScale': 'linear',
                                                                          'heightField': None,
                                                                          'heightScale': 'linear',
                                                                          'radiusField': None,
                                                                          'radiusScale': 'linear'}},
                                                      {'id': 'p7iq8',
                                                       'type': 'geojson',
                                                       'config': {'dataId': 'poi',
                                                                  'label': 'poi',
                                                                  'color': [221, 178, 124],
                                                                  'highlightColor': [252, 242, 26, 255],
                                                                  'columns': {'geojson': 'geometry'},
                                                                  'isVisible': True,
                                                                  'visConfig': {'opacity': 0.8,
                                                                                'strokeOpacity': 0.8,
                                                                                'thickness': 0.5,
                                                                                'strokeColor': [136, 87, 44],
                                                                                'colorRange': {'name': 'Global Warming',
                                                                                               'type': 'sequential',
                                                                                               'category': 'Uber',
                                                                                               'colors': ['#5A1846',
                                                                                                          '#900C3F',
                                                                                                          '#C70039',
                                                                                                          '#E3611C',
                                                                                                          '#F1920E',
                                                                                                          '#FFC300']},
                                                                                'strokeColorRange': {'name': 'Global Warming',
                                                                                                     'type': 'sequential',
                                                                                                     'category': 'Uber',
                                                                                                     'colors': ['#5A1846',
                                                                                                                '#900C3F',
                                                                                                                '#C70039',
                                                                                                                '#E3611C',
                                                                                                                '#F1920E',
                                                                                                                '#FFC300']},
                                                                                'radius': 10,
                                                                                'sizeRange': [0, 10],
                                                                                'radiusRange': [0, 50],
                                                                                'heightRange': [0, 500],
                                                                                'elevationScale': 5,
                                                                                'enableElevationZoomFactor': True,
                                                                                'stroked': True,
                                                                                'filled': True,
                                                                                'enable3d': False,
                                                                                'wireframe': False},
                                                                  'hidden': False,
                                                                  'textLabel': [{'field': None,
                                                                                 'color': [255, 255, 255],
                                                                                 'size': 18,
                                                                                 'offset': [0, 0],
                                                                                 'anchor': 'start',
                                                                                 'alignment': 'center'}]},
                                                       'visualChannels': {'colorField': None,
                                                                          'colorScale': 'quantile',
                                                                          'strokeColorField': None,
                                                                          'strokeColorScale': 'quantile',
                                                                          'sizeField': None,
                                                                          'sizeScale': 'linear',
                                                                          'heightField': None,
                                                                          'heightScale': 'linear',
                                                                          'radiusField': None,
                                                                          'radiusScale': 'linear'}},
                                                      {'id': '1ayio4d',
                                                       'type': 'point',
                                                       'config': {'dataId': 'node',
                                                                  'label': 'node',
                                                                  'color': [34, 63, 154],
                                                                  'highlightColor': [252, 242, 26, 255],
                                                                  'columns': {'lat': 'y_coord', 'lng': 'x_coord', 'altitude': None},
                                                                  'isVisible': True,
                                                                  'visConfig': {'radius': 10,
                                                                                'fixedRadius': False,
                                                                                'opacity': 0.8,
                                                                                'outline': False,
                                                                                'thickness': 2,
                                                                                'strokeColor': None,
                                                                                'colorRange': {'name': 'Global Warming',
                                                                                               'type': 'sequential',
                                                                                               'category': 'Uber',
                                                                                               'colors': ['#5A1846',
                                                                                                          '#900C3F',
                                                                                                          '#C70039',
                                                                                                          '#E3611C',
                                                                                                          '#F1920E',
                                                                                                          '#FFC300']},
                                                                                'strokeColorRange': {'name': 'Global Warming',
                                                                                                     'type': 'sequential',
                                                                                                     'category': 'Uber',
                                                                                                     'colors': ['#5A1846',
                                                                                                                '#900C3F',
                                                                                                                '#C70039',
                                                                                                                '#E3611C',
                                                                                                                '#F1920E',
                                                                                                                '#FFC300']},
                                                                                'radiusRange': [0, 50],
                                                                                'filled': True},
                                                                  'hidden': False,
                                                                  'textLabel': [{'field': None,
                                                                                 'color': [255, 255, 255],
                                                                                 'size': 18,
                                                                                 'offset': [0, 0],
                                                                                 'anchor': 'start',
                                                                                 'alignment': 'center'}]},
                                                       'visualChannels': {'colorField': None,
                                                                          'colorScale': 'quantile',
                                                                          'strokeColorField': None,
                                                                          'strokeColorScale': 'quantile',
                                                                          'sizeField': None,
                                                                          'sizeScale': 'linear'}}],
                                           'interactionConfig': {'tooltip': {'fieldsToShow': {'node': [{'name': 'name',
                                                                                                        'format': None},
                                                                                              {'name': 'node_id',
                                                                                               'format': None},
                                                                                              {'name': 'osm_node_id', 'format': None},
                                                                                              {'name': 'osm_highway',
                                                                                               'format': None},
                                                                                              {'name': 'zone_id', 'format': None}],
                                                                                              'link': [{'name': 'name', 'format': None},
                                                                                                       {'name': 'link_id',
                                                                                                        'format': None},
                                                                                                       {'name': 'osm_way_id',
                                                                                                        'format': None},
                                                                                                       {'name': 'from_node_id',
                                                                                                        'format': None},
                                                                                                       {'name': 'to_node_id', 'format': None}],
                                                                                              'poi': [{'name': 'name', 'format': None},
                                                                                                      {'name': 'poi_id',
                                                                                                       'format': None},
                                                                                                      {'name': 'osm_way_id',
                                                                                                       'format': None},
                                                                                                      {'name': 'osm_relation_id',
                                                                                                       'format': None},
                                                                                                      {'name': 'building', 'format': None}]},
                                                                             'compareMode': False,
                                                                             'compareType': 'absolute',
                                                                             'enabled': True},
                                                                 'brush': {'size': 0.5, 'enabled': False},
                                                                 'geocoder': {'enabled': False},
                                                                 'coordinate': {'enabled': False}},
                                           'layerBlending': 'normal',
                                           'splitMaps': [],
                                           'animationConfig': {'currentTime': None, 'speed': 1}},
                              'mapState': {'bearing': 0,
                                           'dragRotate': False,
                                           'latitude': 52.550856103943644,
                                           'longitude': 13.192007534858833,
                                           'pitch': 0,
                                           'zoom': 13,
                                           'isSplit': False},
                              'mapStyle': {'styleType': 'dark',
                                           'topLayerGroups': {},
                                           'visibleLayerGroups': {'label': True,
                                                                  'road': True,
                                                                  'border': False,
                                                                  'building': True,
                                                                  'water': True,
                                                                  'land': True,
                                                                  '3d building': False},
                                           'threeDBuildingColor': [9.665468314072013,
                                                                   17.18305478057247,
                                                                   31.1442867897876],
                                           'mapStyles': {}}
                          }}

    # auto zoom to the input data
    x_coord_mean, y_coord_mean = map_layer_data["node"]["x_coord"].mean(), map_layer_data["node"]["y_coord"].mean()
    map_config_default["config"]["mapState"]["latitude"] = y_coord_mean
    map_config_default["config"]["mapState"]["longitude"] = x_coord_mean

    try:
        # initialize the map with default height
        vis_map = KeplerGl(height=600)

        # add data according to input layer data
        for key in map_layer_data:
            vis_map.add_data(data=map_layer_data[key], name=key)

        # update map configuration if specified
        vis_map.config = map_config or map_config_default

    except Exception as e:
        print(f"Created an empty KeplerGl map for the reason: {e}")
        vis_map = KeplerGl(height=600)
    return vis_map


def extract_coordinates_by_network_mode(mnet: MultiNet, modes: list) -> None:
    # extract node,link, and poi coordinates of the specified network mode
    mnet.link.update_coords_by_link_modes(modes)
    mnet.node.update_coords(column='node_id',values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        raise Exception("please try other modes")


def extract_coordinates_by_node_types(mnet: MultiNet, osm_highway: list) -> None:
    # extract node,link, and poi coordinates of the specified node type

    x_coords = []
    y_coords = []
    isValid = False
    for highway_type in osm_highway:
        mnet.node.update_coords(column='osm_highway', values=[highway_type])
        x_coords.append(mnet.node.x_coords)
        y_coords.append(mnet.node.y_coords)
        if len(mnet.node.x_coords) == 0:
            print(f"ValueError: '{highway_type}' osm_highway not found")
        else:
            isValid = True

    mnet.node.x_coords = x_coords
    mnet.node.y_coords = y_coords
    mnet.link.update_coords_by_link_modes(modes=('all'))
    mnet.POI.update_coords_by_poi_type()
    if not isValid:
        valid_values = mnet.node.value['osm_highway'].unique()
        raise Exception(f"No results found, please try the following keywords:\n{valid_values}")


def extract_coordinates_by_link_types(mnet: MultiNet, link_types: list) -> None:
    # extract node,link, and poi coordinates of the specified node type

    mnet.link.update_coords_by_link_types(link_types)
    mnet.node.update_coords(column='node_id', values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        valid_values = mnet.link.value['link_type_name'].unique()
        raise Exception(f"no results found, please try the following keywords:\n{valid_values}")


def extract_coordinates_by_link_lane(mnet: MultiNet, lanes: tuple) -> None:
    # extract node,link, and poi coordinates of the specified network link lanes

    mnet.link.update_coords_by_float_attr(column='lanes', min_v=lanes[0], max_v=lanes[1])
    mnet.node.update_coords(column='node_id', values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        valid_values = mnet.link.value['lanes'].unique()
        raise Exception(f"no results found, the number of lanes should be between {min(valid_values)} and {max(valid_values)}")


def extract_coordinates_by_link_free_speed(mnet: MultiNet, free_speed: tuple) -> None:
    # extract node,link, and poi coordinates of the specified network link free speed

    mnet.link.update_coords_by_float_attr(column='free_speed', min_v=free_speed[0], max_v=free_speed[1])
    mnet.node.update_coords(column='node_id', values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        valid_values = mnet.link.value['free_speed'].unique()
        raise Exception(f"no results found, the link free speed should be between {min(valid_values)} and {max(valid_values)}")


def extract_coordinates_by_link_length(mnet: MultiNet, length: tuple) -> None:
    # extract node,link, and poi coordinates of the specified network link length

    mnet.link.update_coords_by_float_attr(column='length', min_v=length[0], max_v=length[1])
    mnet.node.update_coords(column='node_id', values=mnet.link.node_id_list)
    mnet.POI.update_coords_by_poi_type()
    if len(mnet.link.link_coords) == 0:
        valid_values = mnet.link.value['length'].unique()
        raise Exception(f"no results found, the link length should be between {max(valid_values)} and {min(valid_values)}")


def extract_coordinates_by_link_attr_distribution(mnet: MultiNet, column: str) -> None:
    # extract node,link, and poi coordinates of the network link lane distribution

    if mnet.link.value[column].isnull().any():
        raise Exception(f"ValueError: nan found in {column}")
    mnet.link.update_coords_by_attr_distribution(column)
    mnet.node.update_coords(column='node_id')
    mnet.POI.update_coords_by_poi_type()


def extract_coordinates_by_poi_type(mnet: MultiNet, poi_type: list) -> None:
    # extract node,link, and poi coordinates of the specified network POI type

    mnet.node.update_coords(column='node_id')
    mnet.link.update_coords_by_link_modes(modes=('all'))
    mnet.POI.update_coords_by_poi_type(poi_type=poi_type)
    if len(mnet.POI.poi_coords) == 0:
        valid_values_1 = mnet.POI.value['building'].unique().tolist()
        valid_values_2 = mnet.POI.value['amenity'].unique().tolist()
        valid_values_3 = mnet.POI.value['leisure'].unique().tolist()
        valid_values = valid_values_1 + valid_values_2 + valid_values_3
        raise Exception(f"no results found, please try the following keywords:\n{valid_values}")


def extract_coordinates_by_poi_attr_distribution(mnet: MultiNet, column: str) -> None:
    # extract node,link, and poi coordinates of the network POI attraction or production distribution

    if mnet.POI.value[column].isnull().any():
        raise Exception(f"ValueError: nan found in {column}")
    mnet.node.update_coords(column='node_id')
    mnet.link.update_coords_by_link_modes(modes=('all'))
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
        mnet.link.update_coords_by_link_modes(modes=('all'))
        mnet.POI.update_coords_by_poi_type()
