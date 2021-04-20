import os
import csv
import locale
import numpy as np
import pandas as pd
from .classes import *
from itertools import islice
from shapely import geometry

def readNet(node_filepath,link_filepath,poi_filepath,zone_filepath,demand_filepath,poi_trip_filepath,agent_filepath):
    network=Network()
    #get local encode
    local_encoding=locale.getdefaultlocale()
    #read network nodes
    if os.path.exists(node_filepath):
        try:
            num_node=0
            x_coords=[]
            y_coords=[]
            with open(node_filepath,'r',encoding=local_encoding[1]) as f:
                node_reader=csv.reader(f)
                for row in islice(node_reader,1,None):
                    node=Node(*row)
                    network.node_dict[node.node_id]=node
                    x_coords.append(node.x_coord)
                    y_coords.append(node.y_coord)
                    network.node_id_list.append(node.node_id)
                    num_node += 1
                    if node.ctrl_type not in network.node_ctrl_type_list:
                        network.node_ctrl_type_list.append(node.ctrl_type)
            network.number_of_node=num_node
            network.node_coords=[x_coords,y_coords]
            network.min_lng,network.max_lng=min(x_coords),max(x_coords)
            network.min_lat,network.max_lat=min(y_coords),max(y_coords)
        except Exception as e:
            print("something is wrong when reading {}:".format(node_filepath))
            print(e)
    else:
        print("error :node.csv doesn't exist")

    #read network links
    if os.path.exists(link_filepath):
        try:
            num_link=0
            unique_links=[]
            with open(link_filepath,'r',encoding=local_encoding[1]) as f:
                link_reader=csv.reader(f)
                for row in islice(link_reader,1,None):
                    link=Link(*row)
                    network.link_dict[link.link_id] = link
                    network.node_dict[link.from_node_id].out_link_list.append(link)
                    network.node_dict[link.to_node_id].in_link_list.append(link)
                    if not link.geometry:
                        from_node=network.node_dict[link.from_node_id]
                        to_node=network.node_dict[link.to_node_id]
                        link.geometry=LineString([(from_node.x_coord,from_node.y_coord),(to_node.x_coord,to_node.y_coord)])
                    if (link.from_node_id,link.to_node_id) not in unique_links and (link.to_node_id,link.from_node_id) not in unique_links:
                        coords = list(link.geometry.coords)
                        network.link_coords.append(np.array(coords))
                        unique_links.append((link.from_node_id, link.to_node_id))
                    num_link += 1
            network.number_of_link=num_link
        except Exception as e:
            print("something is wrong when reading {}:".format(link_filepath))
            print(e)
    else:
        print("error :link.csv doesn't exist")
    if os.path.exists(poi_filepath):
        try:
            with open(poi_filepath,'r',encoding=local_encoding[1]) as f:
                poi_reader=csv.reader(f)
                poi_id=0
                for row in islice(poi_reader, 1, None):
                    poi=POI(*row)
                    network.poi_dict[poi.poi_id]=poi
                    if isinstance(poi.geometry,geometry.MultiPolygon):
                        for geom in poi.geometry.geoms:
                            coords = list(geom.exterior.coords)
                            network.poi_coords.append(np.array(coords))
                            poi_id += 1
                    elif isinstance(poi.geometry,geometry.Polygon):
                        coords=list(poi.geometry.exterior.coords)
                        network.poi_coords.append(np.array(coords))
                        poi_id+=1
                network.number_of_poi=poi_id
        except Exception as e:
            print("something is wrong when reading {}:".format(poi_filepath))
            print(e)
    else:
        print("warning :poi.csv doesn't exist")

    # read zone
    if os.path.exists(zone_filepath):
        try:
            zone_id=0
            with open(zone_filepath, 'r',encoding=local_encoding[1]) as f:
                zone_reader = csv.reader(f)
                for row in islice(zone_reader, 1, None):
                    zone=Zone(*row)
                    network.zone_dict[zone.name]=zone
                    zone_id+=1
                network.number_of_zone=zone_id
        except Exception as e:
            print("something is wrong when reading {}:".format(zone_filepath))
            print(e)
    else:
        print("warning :zone.csv doesn't exist")
    # read demand
    if os.path.exists(demand_filepath):
        try:
            demand_id = 0
            with open(demand_filepath, 'r',encoding=local_encoding[1]) as f:
                demand_reader = csv.reader(f)
                for row in islice(demand_reader, 1, None):
                    demand = Demand(*row)
                    network.demand_dict[demand_id] = demand
                    demand_id += 1
            network.number_of_demand = demand_id
        except Exception as e:
            print("something is wrong when reading {}:".format(demand_filepath))
            print(e)
    else:
        print("warning :demand.csv doesn't exist")
    # read poi_trip
    if os.path.exists(poi_trip_filepath):
        try:
            poi_type_id=0
            with open(poi_trip_filepath,'r',encoding=local_encoding[1]) as f:
                poi_trip_reader=csv.reader(f)
                for row in islice(poi_trip_reader,1,None):
                    poi_trip=POITrip(*row)
                    network.poi_trip_dict[poi_trip.building]=poi_trip
                    poi_type_id+=1
            network.number_of_poi_type=poi_type_id
        except Exception as e:
            print("something is wrong when reading {}:".format(poi_trip_reader))
            print(e)
    else:
        print("warning :poi_trip_rate.csv doesn't exist")
    # read agent
    if os.path.exists(agent_filepath):
        try:
            agent_id=0
            with open(agent_filepath, 'r',encoding=local_encoding[1]) as f:
                agent_reader = csv.reader(f)
                for row in islice(agent_reader, 1, None):
                    agent=Agent(*row)
                    network.agent_dict[agent.agent_id] = agent
                    agent_id += 1
                network.number_of_agent = agent_id
        except Exception as e:
            print("something is wrong when reading {}:".format(agent_filepath))
            print(e)
    else:
        print("warning :input_agent.csv doesn't exist")
    return network
