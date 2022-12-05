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

    def update_coords(self, index: str, values: list) -> None:
        """extract node coordinates from node dataset

        Args:
            index (str): node ID set to be extracted
            values (list): Need to be specified
        """

        if values:
            res = self.value[self.value[index].isin(values)]
            self.x_coords = res['x_coord'].tolist()
            self.y_coords = res['y_coord'].tolist()
        else:
            self.x_coords = self.value['x_coord'].tolist()
            self.y_coords = self.value['y_coord'].tolist()


class Link:
    def __init__(self):
        self.value = None  # dataframe
        self.link_coords = None

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

    def get_coords_by_str_attr(self, mode: str) -> tuple:
        # extract link coordinates of specified network mode from link dataset

        value = self.value if mode == "all" else self.value[self.value[mode] == True]
        link_coords = value['geometry'].map(lambda x: np.array(list(x.coords))).tolist()

        ID = [] if mode == "all" else value['from_node_id'].tolist() + value['to_node_id'].tolist()

        return (link_coords, ID)

    def get_coords_by_float_attr(self, column: str, min_v: int, max_v: int) -> tuple:
        # extract link coordinates of specified network mode from link dataset

        value = self.value[(self.value[column] >= min_v) &
                           (self.value[column] <= max_v)]
        link_coords = value['geometry'].map(lambda x: np.array(list(x.coords))).tolist()
        f_n = value['from_node_id'].tolist()
        t_n = value['to_node_id'].tolist()
        ID = f_n + t_n

        return (link_coords, ID)


class POI:
    def __init__(self):
        self.value = None  # dataframe
        self.poi_coords = None

    def convert_str_to_geometry(self) -> None:
        # load a POI geometry from a WKT string.

        self.value['geometry'] = self.value['geometry'].map(lambda x: loads(x))

    def update_poi_coords(self) -> None:
        # extract POI boundary coordinates from POI dataset

        def convert_geometry_to_list(geometry):
            coords = []
            if isinstance(geometry, MultiPolygon):
                for geom in geometry.geoms:
                    coords.extend(geom.exterior.coords[:-1])
            elif isinstance(geometry, Polygon):
                coords = list(geometry.exterior.coords)
            return coords

        self.poi_coords = self.value['geometry'].map(
            convert_geometry_to_list).tolist()


class Demand:
    def __init__(self):
        self.value = None  # dataframe


class Zone:
    def __init__(self):
        self.value = None  # dataframe


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
