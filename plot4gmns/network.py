# -*- coding:utf-8 -*-
##############################################################
# Created Date: Monday, December 5th 2022
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################

from .utility_lib import Style
from shapely.wkt import loads
from shapely.geometry import MultiPolygon, Polygon
import numpy as np


class Node:
    def __init__(self):
        self.value = None  # dataframe
        self.x_coords = None
        self.y_coords = None

    def update_coords(self, column: str = '', values: list = []) -> None:
        """extract node coordinates from node dataset

        Args:
            column (str): node ID set to be extracted
            values (list): Need to be specified
        """

        if values:
            res = self.value[self.value[column].isin(values)]
            self.x_coords = res['x_coord'].tolist()
            self.y_coords = res['y_coord'].tolist()
        else:
            self.x_coords = self.value['x_coord'].tolist()
            self.y_coords = self.value['y_coord'].tolist()


class Link:
    def __init__(self):
        self.value = None  # dataframe
        self.link_coords = []
        self.node_id_list = []
        self.attr_distribution = []

    def convert_str_to_geometry(self) -> None:
        # load a link geometry from a WKT string.
        self.value['geometry'] = self.value['geometry'].map(lambda x: loads(x))

    def extract_link_modes(self) -> None:
        # create link modes information from link dataset
        self.value['auto'] = self.value['allowed_uses'].map(lambda x: "auto" in x.split(';'))
        self.value['bike'] = self.value['allowed_uses'].map(lambda x: "bike" in x.split(';'))
        self.value['walk'] = self.value['allowed_uses'].map(lambda x: "walk" in x.split(';'))
        self.value['railway'] = self.value['allowed_uses'].map(lambda x: "railway" in x.split(';'))
        self.value.drop(columns=['allowed_uses'], inplace=True)

    def update_coords_by_link_modes(self, modes: list) -> None:
        # extract link coordinates of specified network mode from link dataset
        if 'all' in modes:
            self.link_coords = self.value['geometry'].map(lambda x: np.array(list(x.coords))).tolist()
            self.ID = []
        else:
            self.link_coords = []
            self.node_id_list = []
            for mode in modes:
                res = self.value[self.value[mode] == True]
                self.link_coords.extend(res['geometry'].map(lambda x: np.array(list(x.coords))).tolist())
                self.node_id_list.extend(res['from_node_id'].tolist() + res['to_node_id'].tolist())
            self.node_id_list = list(set(self.node_id_list))

    def update_coords_by_link_types(self, link_types: list) -> None:
        # extract link coordinates of specified link types from link dataset
        node_id_list = []
        res = self.value[self.value['link_type_name'].isin(link_types)]
        self.link_coords.extend(res['geometry'].map(lambda x: np.array(list(x.coords))).tolist())
        node_id_list.extend(res['from_node_id'].tolist() + res['to_node_id'].tolist())
        self.node_id_list = list(set(self.node_id_list))

    def update_coords_by_float_attr(self, column: str, min_v: int, max_v: int) -> None:
        # extract link coordinates of specified network link attributes range from link dataset
        res = self.value[(self.value[column] >= min_v) & (self.value[column] <= max_v)]
        self.link_coords = res['geometry'].map(lambda x: np.array(list(x.coords))).tolist()
        f_n = res['from_node_id'].tolist()
        t_n = res['to_node_id'].tolist()
        self.node_id_list = list(set(f_n + t_n))

    def update_coords_by_attr_distribution(self, column: str) -> None:
        self.link_coords = self.value['geometry'].map(lambda x: np.array(list(x.coords))).tolist()
        self.attr_distribution = self.value[column].tolist()


class POI:
    def __init__(self):
        self.value = None  # dataframe
        self.poi_coords = None

    def convert_str_to_geometry(self) -> None:
        # load a POI geometry from a WKT string.

        self.value['geometry'] = self.value['geometry'].map(lambda x: loads(x))

    def update_coords_by_poi_type(self, poi_type: list = []) -> None:
        # extract POI boundary coordinates from POI dataset

        def convert_geometry_to_list(geometry):
            coords = []
            if isinstance(geometry, MultiPolygon):
                for geom in geometry.geoms:
                    coords.extend(geom.exterior.coords[:-1])
            elif isinstance(geometry, Polygon):
                coords = list(geometry.exterior.coords)
            return coords
        if len(poi_type):
            res = self.value[(self.value['building'].isin(poi_type)) |
                             (self.value['amenity'].isin(poi_type)) |
                             (self.value['leisure'].isin(poi_type))]
            self.poi_coords = res['geometry'].map(convert_geometry_to_list).tolist()
        else:
            self.poi_coords = self.value['geometry'].map(convert_geometry_to_list).tolist()

    def update_coords_by_attr_distribution(self, column: str, rate: float = 1.0) -> None:
        def convert_geometry_to_list(geometry):
            coords = []
            if isinstance(geometry, MultiPolygon):
                for geom in geometry.geoms:
                    coords.extend(geom.exterior.coords[:-1])
            elif isinstance(geometry, Polygon):
                coords = list(geometry.exterior.coords)
            return coords
        poi_coords_ = self.value['geometry'].map(convert_geometry_to_list).tolist()
        attr_distribution_ = self.value[column].tolist()
        sorted_index_ = sorted(range(self.value.shape[0]), key=lambda id: attr_distribution_[id], reverse=True)
        selected_number = int(round(rate * self.value.shape[0], 0))
        sorted_index = sorted_index_[:selected_number]
        self.poi_coords = [poi_coords_[id] for id in sorted_index]
        self.attr_distribution = [attr_distribution_[id] for id in sorted_index]


class Demand:
    def __init__(self):
        self.value = None  # dataframe
        self.demand_matrix = None
        self.demand_OD_coords = None
        self.demand_OD_vol = None

    def convert_str_to_geometry(self) -> None:
        # load a POI geometry from a WKT string.
        self.value['geometry'] = self.value['geometry'].map(lambda x: loads(x))

    def update_demand_matrix(self, number_of_zone):

        demand_matrix = np.zeros((number_of_zone, number_of_zone))
        for row in range(self.value.shape[0]):
            o_zone_id = self.value['o_zone_id'][row]
            d_zone_id = self.value['d_zone_id'][row]
            vol = self.value['volume'][row]
            demand_matrix[o_zone_id - 1, d_zone_id - 1] = vol
        self.demand_matrix = demand_matrix

    def update_coords(self):
        res = self.value[self.value['volume'] > 0]
        self.demand_OD_coords = res['geometry'].map(lambda x: np.array(list(x.coords))).tolist()
        self.demand_OD_vol = res['volume'].tolist()


class Zone:
    def __init__(self):
        self.value = None  # dataframe
        self.zone_coords = None
        self.zone_names = None

    def convert_str_to_geometry(self) -> None:
        # load a POI geometry from a WKT string.
        self.value['geometry'] = self.value['geometry'].map(lambda x: loads(x))

    def update_coords(self):
        self.zone_coords = self.value['geometry'].map(lambda x: np.array(list(x.exterior.coords))).tolist()
        self.zone_names = self.value[['name', 'centroid_x', 'centroid_y']].values.tolist()


class MultiNet:
    def __init__(self):
        self.style = Style()
        self.node = Node()  # Node
        self.link = Link()  # Link
        self.POI = POI()  # POI
        self.demand = Demand()  # Demand
        self.zone = Zone()  # zone
        self.node_loaded = False
        self.link_loaded = False
        self.POI_loaded = False
        self.demand_loaded = False
        self.zone_loaded = False
