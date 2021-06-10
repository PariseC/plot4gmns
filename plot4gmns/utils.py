import chardet
import numpy as np
from shapely import geometry

def get_encoding(file):
    with open(file,'rb') as f:
        tmp = chardet.detect(f.read())
        return tmp['encoding']

def statNodeAttrValue(network,attr):
    attr_values={}
    try:
        if attr == 'ctrl_type':
            for k, node in network.node_dict.items():
                if isinstance(node.ctrl_type,int):
                    if node.ctrl_type not in attr_values.keys() and isinstance(node.ctrl_type,int):
                        attr_values[node.ctrl_type]=1
                    else:
                        attr_values[node.ctrl_type]+=1
        elif attr == 'activity_type':
            for k, node in network.node_dict.items():
                if node.activity_type:
                    if node.activity_type not in attr_values.keys() and node.activity_type:
                        attr_values[node.activity_type]=1
                    else:
                        attr_values[node.activity_type]+=1
        elif attr == 'production':
            min_v=float('inf')
            max_v=-float('inf')
            for k, node in network.node_dict.items():
                if isinstance(node.production,float):
                    if node.production<min_v:
                        min_v=node.production
                    if node.production>max_v:
                        max_v=node.production
            attr_values = {'min_v': min_v, 'max_v': max_v}
        elif attr == 'attraction':
            min_v=float('inf')
            max_v=-float('inf')
            for k, node in network.node_dict.items():
                if isinstance(node.attraction,float):
                    if node.attraction<min_v:
                        min_v=node.attraction
                    if node.attraction>max_v:
                        max_v=node.attraction
            attr_values={'min_v':min_v,'max_v':max_v}
    except Exception as e:
        print(e)
    return attr_values

def statLinkAttrValue(network,attr):
    attr_values={}
    try:
        if attr == 'length':
            min_v=float('inf')
            max_v=-float('inf')
            for k, link in network.link_dict.items():
                if isinstance(link.length,float):
                    if link.length>max_v:
                        max_v=link.length
                    if link.length<min_v:
                        min_v=link.length
            attr_values={'min_v':min_v,'max_v':max_v}
        elif attr == 'lanes':
            min_v = float('inf')
            max_v = -float('inf')
            for k, link in network.link_dict.items():
                if isinstance(link.lanes,int):
                    if link.lanes>max_v:
                        max_v=link.lanes
                    if link.lanes<min_v:
                        min_v=link.lanes
            attr_values = {'min_v': min_v, 'max_v': max_v}
        elif attr == 'free_speed':
            min_v = float('inf')
            max_v = -float('inf')
            for k, link in network.link_dict.items():
                if isinstance(link.free_speed,float):
                    if link.free_speed>max_v:
                        max_v=link.free_speed
                    if link.free_speed<min_v:
                        min_v=link.free_speed
            attr_values = {'min_v': min_v, 'max_v': max_v}
        elif attr == 'capacity':
            min_v = float('inf')
            max_v = -float('inf')
            for k, link in network.link_dict.items():
                if isinstance(link.capacity,float):
                    if link.capacity>max_v:
                        max_v=link.capacity
                    if link.capacity<min_v:
                        min_v=link.capacity
            attr_values = {'min_v': min_v, 'max_v': max_v}
        elif attr == 'link_type_name':
            for k, link in network.link_dict.items():
                if isinstance(link.link_type_name,str):
                    if link.link_type_name not in attr_values.keys() :
                        attr_values[link.link_type_name] = 1
                    else:
                        attr_values[link.link_type_name] += 1
        elif attr == 'allowed_uses':
            for k, link in network.link_dict.items():
                for allowed_uses in link.allowed_uses:
                    if allowed_uses not in attr_values:
                        attr_values[allowed_uses] = 1
                    else:
                        attr_values[allowed_uses] += 1
    except Exception as e:
        print(e)
    return attr_values

def statPoiAttrValue(network,attr):
    attr_values={}
    try:
        if attr == 'building':
            for k, poi in network.poi_dict.items():
                for building in poi.building:
                    if building not in attr_values.keys() and isinstance(building,str):
                        attr_values[building] = 1
                    else:
                        attr_values[building] += 1
        elif attr == 'activity_zone_id':
            for k, poi in network.poi_dict.items():
                if isinstance(poi.activity_zone_id,int):
                    if poi.activity_zone_id not in attr_values.keys() and isinstance(poi.activity_zone_id,int):
                        attr_values[poi.activity_zone_id] = 1
                    else:
                        attr_values[poi.activity_zone_id] += 1
    except Exception as e:
        print(e)
    return attr_values

def searchNetMode(network,net_type):
    node_x_coords=[]
    node_y_coords=[]
    link_coords=[]
    unique_links=[]
    for k,link in network.link_dict.items():
        if (link.from_node_id, link.to_node_id) not in unique_links and (link.to_node_id, link.from_node_id) not in unique_links:
            coords = list(link.geometry.coords)
            for allowed_uses in link.allowed_uses:
                if allowed_uses in net_type:
                    try:
                        from_node = network.node_dict[link.from_node_id]
                        to_node = network.node_dict[link.to_node_id]
                        node_x_coords.extend([from_node.x_coord,to_node.x_coord])
                        node_y_coords.extend([from_node.y_coord,to_node.y_coord])
                    except:
                        pass
                    link_coords.append(np.array(coords))
                    unique_links.append((link.from_node_id, link.to_node_id))
    node_coords=[node_x_coords,node_y_coords]
    return [node_coords,link_coords]

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
                    print('please input available ctrl_type range')
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
                    print('please input available node production range')
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
                    print('please input available node attraction range')
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
        if attr=='production' :
            for k,node in network.node_dict.items():
                if isinstance(node.production,float):
                    node_x_coords.append(node.x_coord)
                    node_y_coords.append(node.y_coord)
                    values.append(node.production)
        elif attr=='attraction':
            for k, node in network.node_dict.items():
                if isinstance(node.attraction,float):
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
                    if (link.from_node_id, link.to_node_id) not in unique_links and (
                            link.to_node_id, link.from_node_id) not in unique_links:
                        for allowed_uses in link.allowed_uses:
                            if allowed_uses == value:
                                coords = list(link.geometry.coords)
                                try:
                                    from_node = network.node_dict[link.from_node_id]
                                    to_node = network.node_dict[link.to_node_id]
                                    node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                                    node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                                except:
                                    pass
                                link_coords.append(np.array(coords))
                                unique_links.append((link.from_node_id, link.to_node_id))
            elif isinstance(value, list):
                for k, link in network.link_dict.items():

                    if (link.from_node_id, link.to_node_id) not in unique_links and (
                            link.to_node_id, link.from_node_id) not in unique_links:
                        for allowed_uses in link.allowed_uses:
                            if allowed_uses in value:
                                coords = list(link.geometry.coords)
                                try:
                                    from_node = network.node_dict[link.from_node_id]
                                    to_node = network.node_dict[link.to_node_id]
                                    node_x_coords.extend([from_node.x_coord, to_node.x_coord])
                                    node_y_coords.extend([from_node.y_coord, to_node.y_coord])
                                except:
                                    pass
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
                    for building in poi.building:
                        if building==value:
                            if isinstance(poi.geometry, geometry.MultiPolygon):
                                for geom in poi.geometry.geoms:
                                    coords = list(geom.exterior.coords)
                                    poi_coords.append(np.array(coords))
                            elif isinstance(poi.geometry, geometry.Polygon):
                                coords = list(poi.geometry.exterior.coords)
                                poi_coords.append(np.array(coords))
            elif isinstance(value,list):
                for k, poi in network.poi_dict.items():
                    for building in poi.building:
                        if building in value:
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

def statPoiAttrRangeforDensity(network,attr):
    poi_coords=[]
    values=[]
    try:
        if attr=='production_rate1':
            for k,poi in network.poi_dict.items():
                if isinstance(poi.geometry, geometry.MultiPolygon):
                    for geom in poi.geometry.geoms:
                        coords = list(geom.exterior.coords)
                        poi_coords.append(np.array(coords))
                        v=0
                        for building in poi.building:
                           v=v+ network.poi_trip_dict[building].production_rate1
                        values.append(v)
                elif isinstance(poi.geometry, geometry.Polygon):
                    coords = list(poi.geometry.exterior.coords)
                    poi_coords.append(np.array(coords))
                    v = 0
                    for building in poi.building:
                        v = v + network.poi_trip_dict[building].production_rate1
                    values.append(v)
        elif attr=='attraction_rate1':
            for k, poi in network.poi_dict.items():
                if isinstance(poi.geometry, geometry.MultiPolygon):
                    for geom in poi.geometry.geoms:
                        coords = list(geom.exterior.coords)
                        poi_coords.append(np.array(coords))
                        v = 0
                        for building in poi.building:
                            v = v + network.poi_trip_dict[building].attraction_rate1
                        values.append(v)
                elif isinstance(poi.geometry, geometry.Polygon):
                    coords = list(poi.geometry.exterior.coords)
                    poi_coords.append(np.array(coords))
                    v = 0
                    for building in poi.building:
                        v = v + network.poi_trip_dict[building].attraction_rate1
                    values.append(v)
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

def statAgentTracebyID(network,agent_id):
    agent_trace_route_coords = []
    node_x_coords=[]
    node_y_coords=[]
    agent=network.agent_dict[agent_id]
    if isinstance(agent.geometry, geometry.LineString):
        coords = list(agent.geometry.coords)
        agent_trace_route_coords.append(np.array(coords))
    for node_id in agent.node_sequence:
        try:
            node_x_coords.append(network.node_dict[node_id].x_coord)
            node_y_coords.append(network.node_dict[node_id].y_coord)
        except:
            pass
    agent_trace_node_coords=[node_x_coords,node_y_coords]
    return agent_trace_node_coords,agent_trace_route_coords
