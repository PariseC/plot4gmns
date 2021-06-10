import os
import csv
import copy
import numpy as np
from .classes import *
from .utils import get_encoding
from shapely import geometry

def readNet(node_filepath,link_filepath,poi_filepath,zone_filepath,demand_filepath,poi_trip_filepath,agent_filepath):
    network=Network()

    #read network nodes
    if os.path.exists(node_filepath):
        try:
            num_node=0
            x_coords=[]
            y_coords=[]

            encode=get_encoding(node_filepath)
            node_reader=csv.DictReader(open(node_filepath,'r',encoding=encode,errors='ignore'))
            for row_id,row in enumerate(node_reader):
                node=Node(row,row_id)
                network.node_dict[node.node_id]=node
                x_coords.append(node.x_coord)
                y_coords.append(node.y_coord)
                num_node += 1

            network.number_of_node=num_node
            network.node_coords=[x_coords,y_coords]
            network.min_lng,network.max_lng=min(x_coords),max(x_coords)
            network.min_lat,network.max_lat=min(y_coords),max(y_coords)
        except Exception as e:
            print("something is wrong when reading {}:".format(node_filepath))
            print(e)
    else:
        print("error: node.csv doesn't exist")
        sys.exit(0)

    #read network links
    if os.path.exists(link_filepath):
        try:
            num_link=0
            unique_links=[]
            encode=get_encoding(link_filepath)
            link_reader = csv.DictReader(open(link_filepath,'r',encoding=encode,errors='ignore'))
            for row_id,row in enumerate(link_reader):
                link=Link(row,row_id)
                if link.link_id==None:
                    link.link_id=num_link
                network.link_dict[link.link_id] = link
                try:
                    network.node_dict[link.from_node_id].out_link_list.append(link)
                    network.node_dict[link.to_node_id].in_link_list.append(link)
                except:
                    pass
                if not link.geometry:
                    from_node=network.node_dict[link.from_node_id]
                    to_node=network.node_dict[link.to_node_id]
                    link.geometry=geometry.LineString([(from_node.x_coord,from_node.y_coord),(to_node.x_coord,to_node.y_coord)])
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
        print("error: link.csv doesn't exist")
        sys.exit(0)

    if os.path.exists(poi_filepath):
        try:
            encode=get_encoding(poi_filepath)
            poi_reader = csv.DictReader(open(poi_filepath,'r',encoding=encode,errors='ignore'))
            poi_id=0
            for row_id,row in enumerate(poi_reader):
                poi=POI(row,row_id)
                if poi.poi_id==None:
                    poi.poi_id=poi_id
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
        print("warning: poi.csv doesn't exist")

    # read zone
    if os.path.exists(zone_filepath):
        try:
            zone_id=0
            min_zone_id=float('inf')
            max_zone_id=-float('inf')
            encode=get_encoding(zone_filepath)
            zone_reader = csv.DictReader(open(zone_filepath, 'r',encoding=encode,errors='ignore'))
            for row_id,row in enumerate(zone_reader):
                zone=Zone(row,row_id)
                network.zone_dict[zone.activity_zone_id]=zone
                zone_id+=1
                if zone.activity_zone_id>max_zone_id:
                    max_zone_id=zone.activity_zone_id
                if zone.activity_zone_id<min_zone_id:
                    min_zone_id=zone.activity_zone_id
            network.number_of_zone=zone_id
            network.range_of_zone_ids=[min_zone_id,max_zone_id]
        except Exception as e:
            print("something is wrong when reading {}:".format(zone_filepath))
            print(e)
    else:
        print("warning: zone.csv doesn't exist")
    # read demand
    if os.path.exists(demand_filepath):
        try:
            demand_id = 0
            encode=get_encoding(demand_filepath)
            demand_reader = csv.DictReader(open(demand_filepath, 'r',encoding=encode,errors='ignore'))
            for row_id,row in enumerate(demand_reader):
                demand = Demand(row,row_id)
                network.demand_dict[demand_id] = demand
                demand_id += 1
            network.number_of_demand = demand_id
        except Exception as e:
            print("something is wrong when reading {}:".format(demand_filepath))
            print(e)
    else:
        print("warning: demand.csv doesn't exist")
    # read poi_trip
    if os.path.exists(poi_trip_filepath):
        try:
            poi_type_id=0
            encode=get_encoding(poi_trip_filepath)
            poi_trip_reader = csv.DictReader(open(poi_trip_filepath,'r',encoding=encode,errors='ignore'))
            for row_id,row in enumerate(poi_trip_reader):
                poi_trip_=POITrip(row,row_id)
                for building in poi_trip_.building:
                    poi_trip=copy.deepcopy(poi_trip_)
                    poi_trip.building=building
                    network.poi_trip_dict[building]=poi_trip
                    poi_type_id+=1
            network.number_of_poi_type=poi_type_id
        except Exception as e:
            print("something is wrong when reading {}:".format(poi_trip_filepath))
            print(e)
    else:
        print("warning: poi_trip_rate.csv doesn't exist")
    # read agent
    if os.path.exists(agent_filepath):
        try:
            agent_id=0
            encode=get_encoding(agent_filepath)
            agent_reader = csv.DictReader(open(agent_filepath, 'r',encoding=encode,errors='ignore'))
            for row_id,row in enumerate(agent_reader):
                agent=Agent(row,row_id)
                if agent.agent_id:
                    network.agent_dict[agent.agent_id] = agent
                    agent_id += 1
            network.number_of_agent = agent_id
        except Exception as e:
            print("something is wrong when reading {}:".format(agent_filepath))
            print(e)
    else:
        print("warning: input_agent.csv doesn't exist")
    return network
