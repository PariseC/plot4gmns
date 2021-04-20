import numpy as np
from shapely import geometry


def statNodeAttrValue(network,attr):
    attr_values={}
    try:
        for k,node in network.node_dict.items():
            if attr == 'ctrl_type':
                if isinstance(node.ctrl_type,int):
                    if node.ctrl_type not in attr_values.keys() and isinstance(node.ctrl_type,int):
                        attr_values[node.ctrl_type]=1
                    else:
                        attr_values[node.ctrl_type]+=1
            elif attr == 'activity_type':
                if node.activity_type not in attr_values.keys() and node.activity_type:
                    attr_values[node.activity_type]=1
                else:
                    attr_values[node.activity_type]+=1
            elif attr == 'production':
                if node.production not in attr_values.keys() and isinstance(node.production,float):
                    attr_values[node.production]=1
                else:
                    attr_values[node.production]+=1
            elif attr == 'attraction':
                if node.attraction not in attr_values.keys() and isinstance(node.attraction,float):
                    attr_values[node.attraction]=1
                else:
                    attr_values[node.attraction]+=1
    except Exception as e:
        print(e)
    return attr_values
def statLinkAttrValue(network,attr):
    attr_values={}
    try:
        for k,link in network.link_dict.items():
            if attr == 'length':
                if isinstance(link.length,float):
                    if link.length not in attr_values.keys() and isinstance(link.length,float):
                        attr_values[link.length] = 1
                    else:
                        attr_values[link.length] += 1
            elif attr == 'lanes':
                if isinstance(link.lanes,int):
                    if link.lanes not in attr_values.keys() and isinstance(link.lanes,int):
                        attr_values[link.lanes] = 1
                    else:
                        attr_values[link.lanes] += 1
            elif attr == 'free_speed':
                if isinstance(link.free_speed,float):
                    if link.free_speed not in attr_values.keys() and isinstance(link.free_speed,float):
                        attr_values[link.free_speed] = 1
                    else:
                        attr_values[link.free_speed] += 1
            elif attr == 'capacity':
                if isinstance(link.capacity,float):
                    if link.capacity not in attr_values.keys() and isinstance(link.capacity,float):
                        attr_values[link.capacity] = 1
                    else:
                        attr_values[link.capacity] += 1
            elif attr == 'link_type_name':
                if isinstance(link.link_type_name,str):
                    if link.link_type_name not in attr_values.keys() and isinstance(link.link_type_name,str):
                        attr_values[link.link_type_name] = 1
                    else:
                        attr_values[link.link_type_name] += 1
            elif attr == 'allowed_uses':
                if isinstance(link.allowed_uses,str):
                    if link.allowed_uses not in attr_values.keys() and isinstance(link.allowed_uses,str):
                        attr_values[link.allowed_uses] = 1
                    else:
                        attr_values[link.allowed_uses] += 1
    except Exception as e:
        print(e)
    return attr_values
def statPoiAttrValue(network,attr):
    attr_values={}
    try:
        for k,poi in network.poi_dict.items():
            if attr == 'building':
                if poi.building not in attr_values.keys() and isinstance(poi.building,str):
                    attr_values[poi.building] = 1
                else:
                    attr_values[poi.building] += 1
            elif attr == 'activity_zone_id':
                if isinstance(poi.activity_zone_id,int):
                    if poi.activity_zone_id not in attr_values.keys() and isinstance(poi.activity_zone_id,int):
                        attr_values[poi.activity_zone_id] = 1
                    else:
                        attr_values[poi.activity_zone_id] += 1
    except Exception as e:
        print(e)
    return attr_values

def searchNetbyNodeAttr(network,attr,value):
    node_x_coords = []
    node_y_coords = []
    link_coords = []
    unique_links = []
    try:
        if attr == 'ctrl_type':
            if isinstance(value, int):
                for k, node in network.node_dict.items():
                    if node.ctrl_type ==value:
                        node_x_coords.append(node.x_coord)
                        node_y_coords.append(node.y_coord)
                        for out_link in node.out_link_list:
                            if (node.node_id, out_link.to_node_id) not in unique_links and (out_link.to_node_id, node.node_id) not in unique_links:
                                coords = list(out_link.geometry.coords)
                                link_coords.append(np.array(coords))
                                unique_links.append((node.node_id, out_link.to_node_id))
                        for in_link in node.in_link_list:
                            if (in_link.from_node_id, node.node_id) not in unique_links and \
                                    (node.node_id, in_link.from_node_id) not in unique_links:
                                coords = list(in_link.geometry.coords)
                                link_coords.append(np.array(coords))
                                unique_links.append((in_link.from_node_id, node.node_id))
            elif isinstance(value, tuple):
                if value[0]>value[1]:
                    print('please input vaild range')
                else:
                    for k, node in network.node_dict.items():
                        if isinstance(node.ctrl_type,int):
                            if node.ctrl_type <=value[1] and node.ctrl_type>=value[0]:
                                node_x_coords.append(node.x_coord)
                                node_y_coords.append(node.y_coord)
                                for out_link in node.out_link_list:
                                    if (node.node_id, out_link.to_node_id) not in unique_links and (
                                    out_link.to_node_id, node.node_id) not in unique_links:
                                        coords = list(out_link.geometry.coords)
                                        link_coords.append(np.array(coords))
                                    unique_links.append((node.node_id, out_link.to_node_id))
                                for in_link in node.in_link_list:
                                    if (in_link.from_node_id, node.node_id) not in unique_links and \
                                            (node.node_id, in_link.from_node_id) not in unique_links:
                                        coords = list(in_link.geometry.coords)
                                        link_coords.append(np.array(coords))
                                    unique_links.append((in_link.from_node_id, node.node_id))
        elif attr == 'activity_type':
            if isinstance(value,str):
                for k, node in network.node_dict.items():
                    if node.activity_type == value:
                        node_x_coords.append(node.x_coord)
                        node_y_coords.append(node.y_coord)
                        for out_link in node.out_link_list:
                            if (node.node_id, out_link.to_node_id) not in unique_links and (
                                    out_link.to_node_id, node.node_id) not in unique_links:
                                coords = list(out_link.geometry.coords)
                                link_coords.append(np.array(coords))
                                unique_links.append((node.node_id, out_link.to_node_id))
                        for in_link in node.in_link_list:
                            if (in_link.from_node_id, node.node_id) not in unique_links and \
                                    (node.node_id, in_link.from_node_id) not in unique_links:
                                coords = list(in_link.geometry.coords)
                                link_coords.append(np.array(coords))
                                unique_links.append((in_link.from_node_id, node.node_id))
            elif isinstance(value,list):
                for k, node in network.node_dict.items():
                    if node.activity_type in value:
                        node_x_coords.append(node.x_coord)
                        node_y_coords.append(node.y_coord)
                        for out_link in node.out_link_list:
                            if (node.node_id, out_link.to_node_id) not in unique_links and (
                                    out_link.to_node_id, node.node_id) not in unique_links:
                                coords = list(out_link.geometry.coords)
                                link_coords.append(np.array(coords))
                            unique_links.append((node.node_id, out_link.to_node_id))
                        for in_link in node.in_link_list:
                            if (in_link.from_node_id, node.node_id) not in unique_links and \
                                    (node.node_id, in_link.from_node_id) not in unique_links:
                                coords = list(in_link.geometry.coords)
                                link_coords.append(np.array(coords))
                            unique_links.append((in_link.from_node_id, node.node_id))
        elif attr=='production':
            if isinstance(value,tuple):
                if value[0] > value[1]:
                    print('please input vaild range')
                else:
                    for k, node in network.node_dict.items():
                        if isinstance(node.production,float):
                            if node.production <= value[1] and node.production >= value[0]:
                                node_x_coords.append(node.x_coord)
                                node_y_coords.append(node.y_coord)
                                for out_link in node.out_link_list:
                                    if (node.node_id, out_link.to_node_id) not in unique_links and (
                                            out_link.to_node_id, node.node_id) not in unique_links:
                                        coords = list(out_link.geometry.coords)
                                        link_coords.append(np.array(coords))
                                        unique_links.append((node.node_id, out_link.to_node_id))
                                for in_link in node.in_link_list:
                                    if (in_link.from_node_id, node.node_id) not in unique_links and \
                                            (node.node_id, in_link.from_node_id) not in unique_links:
                                        coords = list(in_link.geometry.coords)
                                        link_coords.append(np.array(coords))
                                        unique_links.append((in_link.from_node_id, node.node_id))
        elif attr=='attraction':
            if isinstance(value, tuple):
                if value[0] > value[1]:
                    print('please input vaild range')
                else:
                    for k, node in network.node_dict.items():
                        if isinstance(node.attraction,float):
                            if node.attraction <= value[1] and node.attraction >= value[0]:
                                node_x_coords.append(node.x_coord)
                                node_y_coords.append(node.y_coord)
                                for out_link in node.out_link_list:
                                    if (node.node_id, out_link.to_node_id) not in unique_links and (
                                            out_link.to_node_id, node.node_id) not in unique_links:
                                        coords = list(out_link.geometry.coords)
                                        link_coords.append(np.array(coords))
                                        unique_links.append((node.node_id, out_link.to_node_id))
                                for in_link in node.in_link_list:
                                    if (in_link.from_node_id, node.node_id) not in unique_links and \
                                            (node.node_id, in_link.from_node_id) not in unique_links:
                                        coords = list(in_link.geometry.coords)
                                        link_coords.append(np.array(coords))
                                        unique_links.append((in_link.from_node_id, node.node_id))
    except Exception as e:
        print(e)
    node_coords=[node_x_coords,node_y_coords]
    return [node_coords,link_coords]
def statNodeAttrRange(network,attr):
    node_x_coords = []
    node_y_coords = []
    values=[]
    try:
        if attr=='production':
            for k,node in network.node_dict.items():
                node_x_coords.append(node.x_coord)
                node_y_coords.append(node.y_coord)
                values.append(node.production)
        else:
            for k, node in network.node_dict.items():
                node_x_coords.append(node.x_coord)
                node_y_coords.append(node.y_coord)
                values.append(node.attraction)
    except Exception as e:
        print(e)
    node_coords=[node_x_coords,node_y_coords]
    return node_coords,values

def searchNetbyLinkAttr(network,attr,value):
    node_x_coords = []
    node_y_coords = []
    link_coords = []
    unique_links = []
    try:
        if attr=='length':
            if isinstance(value,tuple):
                for k, link in network.link_dict.items():
                    if isinstance(link.length, float):
                        from_node = network.node_dict[link.from_node_id]
                        to_node = network.node_dict[link.to_node_id]
                        if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
                            if link.length <= value[1] and link.length >= value[0]:
                                coords = list(link.geometry.coords)
                                node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                                node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                                link_coords.append(np.array(coords))
                                unique_links.append((link.from_node_id, link.to_node_id))
        elif attr=='lanes':
            if isinstance(value, tuple):
                for k, link in network.link_dict.items():
                    if isinstance(link.lanes, int):
                        from_node = network.node_dict[link.from_node_id]
                        to_node = network.node_dict[link.to_node_id]
                        if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
                            if link.lanes <= value[1] and link.lanes >= value[0]:
                                coords = list(link.geometry.coords)
                                node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                                node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                                link_coords.append(np.array(coords))
                                unique_links.append((link.from_node_id, link.to_node_id))
        elif attr=='free_speed':
            if isinstance(value, tuple):
                for k, link in network.link_dict.items():
                    if isinstance(link.free_speed,float):
                        from_node = network.node_dict[link.from_node_id]
                        to_node = network.node_dict[link.to_node_id]
                        if (link.from_node_id, link.to_node_id) not in unique_links and (
                                link.to_node_id, link.from_node_id) not in unique_links:
                            if link.free_speed <= value[1] and link.free_speed >= value[0]:
                                coords = list(link.geometry.coords)
                                node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                                node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                                link_coords.append(np.array(coords))
                                unique_links.append((link.from_node_id, link.to_node_id))
        elif attr=='capacity':
            if isinstance(value, tuple):
                for k, link in network.link_dict.items():
                    if isinstance(link.capacity,float):
                        from_node = network.node_dict[link.from_node_id]
                        to_node = network.node_dict[link.to_node_id]
                        if (link.from_node_id, link.to_node_id) not in unique_links and (
                                link.to_node_id, link.from_node_id) not in unique_links:
                            if link.capacity <= value[1] and link.capacity >= value[0]:
                                coords = list(link.geometry.coords)
                                node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                                node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                                link_coords.append(np.array(coords))
                                unique_links.append((link.from_node_id, link.to_node_id))
        elif attr=='link_type_name':
            if isinstance(value,str):
                for k, link in network.link_dict.items():
                    from_node = network.node_dict[link.from_node_id]
                    to_node = network.node_dict[link.to_node_id]
                    if (link.from_node_id, link.to_node_id) not in unique_links and (
                            link.to_node_id, link.from_node_id) not in unique_links:
                        if link.link_type_name==value:
                            coords = list(link.geometry.coords)
                            node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                            node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                            link_coords.append(np.array(coords))
                            unique_links.append((link.from_node_id, link.to_node_id))
            elif isinstance(value,list):
                for k, link in network.link_dict.items():
                    from_node = network.node_dict[link.from_node_id]
                    to_node = network.node_dict[link.to_node_id]
                    if (link.from_node_id, link.to_node_id) not in unique_links and (
                            link.to_node_id, link.from_node_id) not in unique_links:
                        if link.link_type_name in value:
                            coords = list(link.geometry.coords)
                            node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                            node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                            link_coords.append(np.array(coords))
                            unique_links.append((link.from_node_id, link.to_node_id))
        elif attr=='allowed_uses':
            if isinstance(value, str):
                for k, link in network.link_dict.items():
                    from_node = network.node_dict[link.from_node_id]
                    to_node = network.node_dict[link.to_node_id]
                    if (link.from_node_id, link.to_node_id) not in unique_links and (
                            link.to_node_id, link.from_node_id) not in unique_links:
                        if link.allowed_uses == value:
                            coords = list(link.geometry.coords)
                            node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                            node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                            link_coords.append(np.array(coords))
                            unique_links.append((link.from_node_id, link.to_node_id))
            elif isinstance(value, list):
                for k, link in network.link_dict.items():
                    from_node = network.node_dict[link.from_node_id]
                    to_node = network.node_dict[link.to_node_id]
                    if (link.from_node_id, link.to_node_id) not in unique_links and (
                            link.to_node_id, link.from_node_id) not in unique_links:
                        if link.allowed_uses in value:
                            coords = list(link.geometry.coords)
                            node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                            node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                            link_coords.append(np.array(coords))
                            unique_links.append((link.from_node_id, link.to_node_id))
    except Exception as e:
        print(e)
    node_coords = [node_x_coords, node_y_coords]
    return node_coords,link_coords
def statLinkAttrRange(network,attr):
    node_x_coords=[]
    node_y_coords=[]
    link_coords=[]
    unique_links = []
    values=[]
    try:
        if attr=='lanes':
            for k,link in network.link_dict.items():
                if isinstance(link.lanes, int):
                    if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
                        coords = list(link.geometry.coords)
                        link_coords.append(np.array(coords))
                        unique_links.append((link.from_node_id, link.to_node_id))
                        values.append(link.lanes)
                        from_node = network.node_dict[link.from_node_id]
                        to_node = network.node_dict[link.to_node_id]
                        node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                        node_y_coords.extend([from_node.y_coord, to_node.y_coord])
        elif attr=='free_speed':
            for k, link in network.link_dict.items():
                if isinstance(link.free_speed, float):
                    if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
                        coords = list(link.geometry.coords)
                        link_coords.append(np.array(coords))
                        unique_links.append((link.from_node_id, link.to_node_id))
                        values.append(link.free_speed)
                        from_node = network.node_dict[link.from_node_id]
                        to_node = network.node_dict[link.to_node_id]
                        node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                        node_y_coords.extend([from_node.y_coord, to_node.y_coord])
        else:
            for k, link in network.link_dict.items():
                if isinstance(link.capacity, float):
                    if (link.from_node_id, link.to_node_id) not in unique_links and (
                    link.to_node_id, link.from_node_id) not in unique_links:
                        coords = list(link.geometry.coords)
                        link_coords.append(np.array(coords))
                        unique_links.append((link.from_node_id, link.to_node_id))
                        values.append(link.capacity)
                        from_node = network.node_dict[link.from_node_id]
                        to_node = network.node_dict[link.to_node_id]
                        node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                        node_y_coords.extend([from_node.y_coord, to_node.y_coord])
    except Exception as e:
        print(e)
    node_coords=[node_x_coords,node_y_coords]
    return node_coords,link_coords,values

def searchNetbyPoiAttr(network,attr,value):
    poi_coords=[]
    try:
        if attr=='building':
            if isinstance(value,str):
                for k,poi in network.poi_dict.items():
                    if poi.building==value:
                        if isinstance(poi.geometry, geometry.MultiPolygon):
                            for geom in poi.geometry.geoms:
                                coords = list(geom.exterior.coords)
                                poi_coords.append(np.array(coords))
                        elif isinstance(poi.geometry, geometry.Polygon):
                            coords = list(poi.geometry.exterior.coords)
                            poi_coords.append(np.array(coords))
            elif isinstance(value,list):
                for k, poi in network.poi_dict.items():
                    if poi.building in value:
                        if isinstance(poi.geometry, geometry.MultiPolygon):
                            for geom in poi.geometry.geoms:
                                coords = list(geom.exterior.coords)
                                poi_coords.append(np.array(coords))
                        elif isinstance(poi.geometry, geometry.Polygon):
                            coords = list(poi.geometry.exterior.coords)
                            poi_coords.append(np.array(coords))
        elif attr=='activity_zone_id':
            if isinstance(value,tuple):
                for k, poi in network.poi_dict.items():
                    if poi.activity_zone_id <= value[1] and poi.activity_zone_id>=value[0]:
                        if isinstance(poi.geometry, geometry.MultiPolygon):
                            for geom in poi.geometry.geoms:
                                coords = list(geom.exterior.coords)
                                poi_coords.append(np.array(coords))
                        elif isinstance(poi.geometry, geometry.Polygon):
                            coords = list(poi.geometry.exterior.coords)
                            poi_coords.append(np.array(coords))
    except Exception as e:
        print(e)
    return poi_coords
def statPoiAttrRangeforHeat(network,attr):
    poi_coords=[]
    values=[]
    try:
        if attr=='production_rate1':
            for k,poi in network.poi_dict.items():
                if isinstance(poi.geometry, geometry.MultiPolygon):
                    for geom in poi.geometry.geoms:
                        coords = list(geom.exterior.coords)
                        poi_coords.append(np.array(coords))
                        values.append(network.poi_trip_dict[poi.building].production_rate1)
                elif isinstance(poi.geometry, geometry.Polygon):
                    coords = list(poi.geometry.exterior.coords)
                    poi_coords.append(np.array(coords))
                    values.append(network.poi_trip_dict[poi.building].production_rate1)
        else:
            for k, poi in network.poi_dict.items():
                if isinstance(poi.geometry, geometry.MultiPolygon):
                    for geom in poi.geometry.geoms:
                        coords = list(geom.exterior.coords)
                        poi_coords.append(np.array(coords))
                        values.append(network.poi_trip_dict[poi.building].attraction_rate1)
                elif isinstance(poi.geometry, geometry.Polygon):
                    coords = list(poi.geometry.exterior.coords)
                    poi_coords.append(np.array(coords))
                    values.append(network.poi_trip_dict[poi.building].attraction_rate1)
    except Exception as e:
        print(e)
    return poi_coords,values
def statPoiAttrRangeforContour(network,attr):
    poi_coords=[]
    values=[]
    try:
        if attr == 'production_rate1':
            for k, poi in network.poi_dict.items():
                if isinstance(poi.centroid, geometry.Point):
                    coords = list(poi.centroid.coords)
                    poi_coords.append(coords)
                    values.append(network.poi_trip_dict[poi.building].production_rate1)
        else:
            for k, poi in network.poi_dict.items():
                if isinstance(poi.centroid, geometry.Point):
                    coords = list(poi.centroid.coords)
                    poi_coords.append(coords)
                    values.append(network.poi_trip_dict[poi.building].attraction_rate1)
    except Exception as e:
        print(e)
    return poi_coords,values

def statZoneDemandforHeat(network):
    data=np.zeros((network.number_of_zone,network.number_of_zone))
    try:
        for k,demand in network.demand_dict.items():
            o=demand.o_zone_id
            d=demand.d_zone_id
            data[o-1,d-1]=demand.volume
    except Exception as e:
        print(e)
    return data
def statZoneDemandforFlow(network):
    demand_line=[]
    values=[]
    zone_grid=[]
    zone_labels=[]
    try:
        # statistics demand flow
        for k,demand in network.demand_dict.items():
            if isinstance(demand.geometry,geometry.LineString):
                if demand.volume>0:
                    coords = list(demand.geometry.coords)
                    demand_line.append(np.array(coords))
                    values.append(demand.volume)
        for k,zone in network.zone_dict.items():
            if isinstance(zone.geometry,geometry.Polygon):
                coords = list(zone.geometry.exterior.coords)
                zone_grid.append(np.array(coords))
            zone_labels.append([zone.activity_zone_id,zone.centroid_x,zone.centroid_y])
    except Exception as e:
        print(e)
    return demand_line,values,zone_grid,zone_labels
def statZoneAgent(network,zone_list):
    agent_coords=[]
    zone_grid=[]
    zone_labels=[]
    agent_num={}
    zone_id_list=[id for zone_od in zone_list for id in zone_od]
    try:
        if isinstance(zone_list,list):
            for k,agent in network.agent_dict.items():
                if (agent.o_zone_id,agent.d_zone_id) in zone_list:
                    if isinstance(agent.geometry, geometry.LineString):
                        coords = list(agent.geometry.coords)
                        agent_coords.append(np.array(coords))
                        if (agent.o_zone_id,agent.d_zone_id) in agent_num.keys():
                            agent_num[agent.o_zone_id,agent.d_zone_id]+=1
                        else:
                            agent_num[agent.o_zone_id, agent.d_zone_id]=1
            for k, zone in network.zone_dict.items():
                if zone.activity_zone_id in zone_id_list or zone.activity_zone_id in zone_id_list:
                    if isinstance(zone.geometry, geometry.Polygon):
                        coords = list(zone.geometry.exterior.coords)
                        zone_grid.append(np.array(coords))
                    zone_labels.append([zone.activity_zone_id, zone.centroid_x, zone.centroid_y])
    except Exception as e:
        print(e)
    return agent_coords,agent_num,zone_grid,zone_labels























def searchNetMode(network,net_type):
    node_x_coords=[]
    node_y_coords=[]
    # node_id=[]
    link_coords=[]
    unique_links=[]
    for k,link in network.link_dict.items():
        from_node = network.node_dict[link.from_node_id]
        to_node = network.node_dict[link.to_node_id]
        if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
            coords = list(link.geometry.coords)
            if link.allowed_uses==net_type:
                node_x_coords.extend([from_node.x_coord,to_node.x_coord])
                node_y_coords.extend([from_node.y_coord,to_node.y_coord])
                # node_id.extend([from_node.node_id,to_node.node_id])
                link_coords.append(np.array(coords))

            unique_links.append((link.from_node_id, link.to_node_id))
    node_coords=[node_x_coords,node_y_coords]
    return [node_coords,link_coords]

def searchPOIType(network,poi_type):
    poi_coords=[]
    for k, poi in network.poi_dict.items():
        if poi.building==poi_type:
            if isinstance(poi.geometry, geometry.MultiPolygon):
                for geom in poi.geometry.geoms:
                    coords = list(geom.exterior.coords)
                    poi_coords.append(np.array(coords))
            elif isinstance(poi.geometry, geometry.Polygon):
                coords = list(poi.geometry.exterior.coords)
                poi_coords.append(np.array(coords))
    return poi_coords

def searchNetSpeedRange(network,vmin,vmax):
    node_x_coords = []
    node_y_coords = []
    link_coords = []
    link_free_speed=[]
    unique_links = []
    for k, link in network.link_dict.items():
        from_node = network.node_dict[link.from_node_id]
        to_node = network.node_dict[link.to_node_id]
        if (link.from_node_id, link.to_node_id) not in unique_links and (
        link.to_node_id, link.from_node_id) not in unique_links:
            coords = list(link.geometry.coords)
            if link.free_speed <=vmax and link.free_speed>=vmin:
                node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                link_coords.append(np.array(coords))
                link_free_speed.append(link.free_speed)
            unique_links.append((link.from_node_id, link.to_node_id))
    node_coords = [node_x_coords, node_y_coords]
    link_free_speed=(np.array(link_free_speed)/vmax)*4.5+0.5
    return [node_coords, link_coords,link_free_speed]

def searchNetLaneNum(network,min_lanes,max_lanes):
    node_x_coords = []
    node_y_coords = []
    link_coords = []
    link_lanes=[]
    unique_links = []
    for k, link in network.link_dict.items():
        from_node = network.node_dict[link.from_node_id]
        to_node = network.node_dict[link.to_node_id]
        if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
            coords = list(link.geometry.coords)
            if link.lanes <=max_lanes and link.lanes>=min_lanes:
                node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                link_coords.append(np.array(coords))
                link_lanes.append(link.lanes)
            unique_links.append((link.from_node_id, link.to_node_id))
    node_coords = [node_x_coords, node_y_coords]
    link_lanes=(np.array(link_lanes)/max_lanes)*4.5+0.5
    return [node_coords, link_coords,link_lanes]

def searchNetCapRange(network,min_cap,max_cap):
    node_x_coords = []
    node_y_coords = []
    link_coords = []
    link_cap=[]
    unique_links = []
    for k, link in network.link_dict.items():
        from_node = network.node_dict[link.from_node_id]
        to_node = network.node_dict[link.to_node_id]
        if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
            coords = list(link.geometry.coords)
            if link.capacity <=max_cap and link.capacity>=min_cap:
                node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                link_coords.append(np.array(coords))
                link_cap.append(link.capacity)
            unique_links.append((link.from_node_id, link.to_node_id))
    node_coords = [node_x_coords, node_y_coords]
    link_cap=(np.array(link_cap)/max_cap)*4.5+0.5
    return [node_coords, link_coords,link_cap]


def searchNetLinkType(network,link_type):
    if link_type:
        node_x_coords = []
        node_y_coords = []
        link_coords = []
        unique_links = []
        for k,link in network.link_dict.items():
            from_node = network.node_dict[link.from_node_id]
            to_node = network.node_dict[link.to_node_id]
            if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
                coords = list(link.geometry.coords)
                if link.link_type_name==link_type:
                    node_x_coords.extend([from_node.x_coord,to_node.x_coord])
                    node_y_coords.extend([from_node.y_coord,to_node.y_coord])
                    link_coords.append(np.array(coords))

                unique_links.append((link.from_node_id, link.to_node_id))
        node_coords=[node_x_coords,node_y_coords]
        return [node_coords,link_coords]
    else:
        node_x_coords = []
        node_y_coords = []
        link_classifier_coords = {}
        link_classifier_coords_num={}
        unique_links = []
        for k, link in network.link_dict.items():
            from_node = network.node_dict[link.from_node_id]
            to_node = network.node_dict[link.to_node_id]
            if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
                node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                coords = list(link.geometry.coords)
                if link.link_type_name in link_classifier_coords.keys():
                    link_classifier_coords[link.link_type_name].append(np.array(coords))
                else:
                    link_classifier_coords[link.link_type_name]=[np.array(coords)]
                unique_links.append((link.from_node_id, link.to_node_id))
            if link.link_type_name in link_classifier_coords_num:
                link_classifier_coords_num[link.link_type_name]+=1
            else:
                link_classifier_coords_num[link.link_type_name]=1
        node_coords = [node_x_coords, node_y_coords]
        for k,v in link_classifier_coords_num.items():
            print('the number of {} is :{}'.format(k,v))
        return [node_coords, link_classifier_coords]

def searchNetNodeCtrl(network,ctrl_type):
    if isinstance(ctrl_type,int):
        node_x_coords = []
        node_y_coords = []
        link_coords = []
        unique_links=[]
        for k,node in network.node_dict.items():
            if node.ctrl_type==ctrl_type:
                node_x_coords.extend([node.x_coord,node.x_coord])
                node_y_coords.extend([node.y_coord,node.y_coord])
                for out_link in node.out_link_list:
                    if (node.node_id, out_link.to_node_id) not in unique_links and \
                            (out_link.to_node_id,node.node_id) not in unique_links:
                        coords = list(out_link.geometry.coords)
                        link_coords.append(np.array(coords))
                    unique_links.append((node.node_id, out_link.to_node_id))
                for in_link in node.in_link_list:
                    if (in_link.from_node_id,node.node_id) not in unique_links and \
                            (node.node_id, in_link.from_node_id) not in unique_links:
                        coords = list(in_link.geometry.coords)
                        link_coords.append(np.array(coords))
                    unique_links.append((in_link.from_node_id,node.node_id))
        node_selected_coords=[node_x_coords,node_y_coords]
        return [node_selected_coords,link_coords]
    else:
        node_classifier_coords={}
        node_classifier_coords_num={}
        for k, node in network.node_dict.items():
            if node.ctrl_type in node_classifier_coords.keys():
                node_classifier_coords[node.ctrl_type][0].append(node.x_coord)
                node_classifier_coords[node.ctrl_type][1].append(node.y_coord)
                node_classifier_coords_num[node.ctrl_type]+=1
            else:
                node_classifier_coords[node.ctrl_type]=[[node.x_coord,],[node.y_coord]]
                node_classifier_coords_num[node.ctrl_type]= 1

        for k, v in node_classifier_coords_num.items():
            print('the number of {} is :{}'.format(k, v))
        return [node_classifier_coords]