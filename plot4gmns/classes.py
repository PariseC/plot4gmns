import sys
from shapely.wkt import loads
from shapely import geometry
class Node():
    def __init__(self,kwargs,row):
        keys=kwargs.keys()

        node_id=kwargs['node_id'] if 'node_id' in keys else ''
        if node_id:
            try:
                self.node_id=int(float(node_id))
            except Exception as e:
                print("broken at row{},".format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("node_id is not defined in node.csv, please check it!")
            sys.exit(0)

        ctrl_type=kwargs['ctrl_type'] if 'ctrl_type' in keys else ''
        try:
            self.ctrl_type=int(float(ctrl_type))
        except:
            self.ctrl_type=0
        self.activity_type = kwargs['activity_type'] if 'activity_type' in keys else 'unclassified'

        x_coord=kwargs['x_coord'] if 'x_coord' in keys else ''
        if x_coord:
            try:
                self.x_coord=float(x_coord)
            except Exception as e:
                print('broken at row {},'.format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("x_coord not found in node.csv, please check it!")
            sys.exit(0)
        y_coord=kwargs['y_coord'] if 'y_coord' in keys else ''
        if y_coord:
            try:
                self.y_coord=float(y_coord)
            except Exception as e:
                print('broken at row {},'.format(row), end=' ')
                print(e)
                sys.exit(0)
        else:
            print("y_coord not found in node.csv, please check it!")
            sys.exit(0)

        self.geometry=geometry.Point(self.x_coord,self.y_coord)
        production=kwargs['production'] if 'production' in keys else ''
        try:
            self.production=float(production)
        except:
            self.production=''
        attraction=kwargs['attraction'] if 'attraction' in keys else ''
        try:
            self.attraction=float(attraction)
        except:
            self.attraction=''

        self.out_link_list=[]
        self.in_link_list=[]


class Link():
    def __init__(self,kwargs,row):
        keys=kwargs.keys()

        link_id=kwargs['link_id'] if 'link_id' in keys else ''
        if link_id:
            try:
                self.link_id=int(float(link_id))
            except Exception as e:
                print('broken at row {},'.format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            self.link_id=None
        from_node_id=kwargs['from_node_id'] if 'from_node_id' in keys else ''
        if from_node_id:
            try:
                self.from_node_id=int(float(from_node_id))
            except Exception as e:
                print('broken at row {},'.format(row), end=' ')
                print(e)
                sys.exit(0)
        else:
            print("from_node_id not found in link.csv, please check it!")
            sys.exit(0)
        to_node_id=kwargs['to_node_id'] if 'to_node_id' in keys else ''
        if to_node_id:
            try:
                self.to_node_id=int(float(to_node_id))
            except Exception as e:
                print('broken at row {},'.format(row), end=' ')
                print(e)
                sys.exit(0)
        else:
            print("to_node_id not found in link.csv, please check it!")
            sys.exit(0)
        length=kwargs['length'] if 'length' in keys else ''
        try:
            self.length =float(length)
        except:
            self.length=''
        lanes=kwargs['lanes'] if 'lanes' in keys else ''
        try:
            self.lanes =int(float(lanes))
        except:
            self.lanes=''

        free_speed=kwargs['free_speed'] if 'free_speed' in keys else ''
        try:
            self.free_speed =float(free_speed)
        except:
            self.free_speed=''
        capacity=kwargs['capacity'] if 'capacity' in keys else ''
        try:
            self.capacity = float(capacity)
        except:
            self.capacity=''
        link_type_name=kwargs['link_type_name'] if 'link_type_name' in keys else ''
        if link_type_name:
            self.link_type_name=link_type_name
        else:
            self.link_type_name='unclassified'
        link_geo=kwargs['geometry'] if 'geometry' in keys else ''
        try:
            self.geometry = loads(link_geo)
        except:
            self.geometry=''
        if 'allowed_uses' in keys:
            allowed_uses=kwargs['allowed_uses']
            if allowed_uses:
                if ',' in allowed_uses:
                    self.allowed_uses=[allowed_use_.lstrip() for allowed_use_ in allowed_uses.split(',')]
                elif ';' in allowed_uses:
                    self.allowed_uses = [allowed_use_.lstrip() for allowed_use_ in allowed_uses.split(';')]
                else:
                    self.allowed_uses = [allowed_uses]
            else:
                self.allowed_uses = ['unclassified']
        else:
            self.allowed_uses=['unclassified']



class Agent():
    def __init__(self,kwargs,row):
        keys=kwargs.keys()
        agent_id=kwargs['agent_id'] if 'agent_id' in keys else ''
        if agent_id:
            self.agent_id=int(float(agent_id))
        else:
            self.agent_id=None
        node_sequence=kwargs['node_sequence'] if 'node_sequence' in keys else ''
        try:
            self.node_sequence=[int(float(id)) for id in node_sequence.split(';')[:-1]]
        except:
            self.node_sequence=''
        agent_geo=kwargs['geometry'] if 'geometry' in keys else ''
        if ',)' in agent_geo:
            agent_geo=agent_geo.replace(',)',')')
        try:
            self.geometry=loads(agent_geo)
        except:
            self.geometry=''
            print("warning: can't load geometry at row{}".format(row))


class Demand():
    def __init__(self,kwargs,row):
        keys=kwargs.keys()
        o_zone_id=kwargs['o_zone_id'] if 'o_zone_id' in keys else ''
        if o_zone_id:
            try:
                self.o_zone_id=int(float(o_zone_id))
            except Exception as e:
                print('broken at row {},'.format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("o_zone_id is not defined in demand.csv, please check it!")
            sys.exit(0)
        d_zone_id=kwargs['d_zone_id'] if 'd_zone_id' in keys else ''
        if d_zone_id:
            try:
                self.d_zone_id=int(float(d_zone_id))
            except Exception as e:
                print('broken at row {},'.format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("d_zone_id is not defined in demand.csv, please check it!")
            sys.exit(0)
        vol=kwargs['volume'] if 'volume' in keys else ''
        if vol:
            try:
                self.volume=float(vol)
            except Exception as e:
                print('broken at row {},'.format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("volume is not defined in demand.csv, please check it!")
            sys.exit(0)
        demand_geo=kwargs['geometry'] if 'geometry' in keys else ''
        if demand_geo:
            try:
                self.geometry=loads(demand_geo)
            except Exception as e:
                print('broken at row {},'.format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("geometry is not defined in demand.csv, please check it!")
            sys.exit(0)

class POI():
    def __init__(self,kwargs,row):
        keys=kwargs.keys()
        poi_id=kwargs['poi_id'] if 'poi_id' in keys else ''
        try:
            self.poi_id=int(float(poi_id))
        except :
            self.poi_id=None
        self.name=kwargs['name'] if 'name' in keys else ''
        building=kwargs['building'] if 'building' in keys else ''
        if building:
            self.building=building.split(';')
        else:
            self.building = ['unclassified']
        poi_geo=kwargs['geometry'] if 'geometry' in keys else ''
        if poi_geo:
            try:
                self.geometry=loads(poi_geo)
            except Exception as e:
                print('broken at row {}'.format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("geometry is not defined in poi.csv, please check it!")
            sys.exit(0)
        centroid=kwargs['centroid'] if 'centroid' in keys else ''
        if centroid:
            try:
                self.centroid=loads(centroid)
            except:
                self.centroid = self.geometry.centroid
        else:
            self.centroid=self.geometry.centroid

        activity_zone_id=kwargs['activity_zone_id'] if 'activity_zone_id' in keys else ''
        try:
            self.activity_zone_id=int(float(activity_zone_id))
        except:
            self.activity_zone_id=''

class POITrip():
    def __init__(self,kwargs,row):
        keys=kwargs.keys()
        building = kwargs['building'] if 'building' in keys else ''
        if building:
            self.building = building.split(';')
        else:
            self.building =['unclassified']
        production_rate1=kwargs['production_rate1'] if 'production_rate1' in keys else ''
        if production_rate1:
            try:
                self.production_rate1=float(production_rate1)
            except:
                self.production_rate1=0
        else:
            print("production_rate1 is not defined in poi_trip_rate.csv, please check it!")
            sys.exit(0)
        attraction_rate1=kwargs['attraction_rate1'] if 'attraction_rate1' in keys else ''
        if attraction_rate1:
            try:
                self.attraction_rate1=float(attraction_rate1)
            except:
                self.attraction_rate1=0
        else:
            print("attraction_rate1 is not defined in poi_trip_rate.csv, please check it!")
            sys.exit(0)


class Zone():
    def __init__(self,kwargs,row):
        keys=kwargs.keys()
        self.name=kwargs['name'] if 'name' in keys else ' '
        activity_zone_id=kwargs['activity_zone_id'] if 'activity_zone_id' in keys else ''
        if activity_zone_id:
            try:
                self.activity_zone_id=int(float(activity_zone_id))
            except Exception as e:
                print("broken at row{}".format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("activity_zone_id is not defined in zone.csv, please check it!")
            sys.exit(0)
        centroid_x=kwargs['centroid_x'] if 'centroid_x' in keys else ''
        if centroid_x:
            try:
                self.centroid_x=float(centroid_x)
            except Exception as e:
                print("broken at row{}".format(row),end=' ')
                print(e)
                sys.exit(0)
        else:
            print("centroid_x is not defined in zone.csv, please check it!")
            sys.exit(0)
        centroid_y=kwargs['centroid_y'] if 'centroid_y' in keys else ''
        if centroid_y:
            try:
                self.centroid_y=float(centroid_y)
            except Exception as e:
                print("broken at row{}".format(row), end=' ')
                print(e)
                sys.exit(0)
        else:
            print("centroid_y is not defined in zone.csv, please check it!")
            sys.exit(0)
        zone_geo=kwargs['geometry'] if 'geometry' in keys else ''
        if zone_geo:
            try:
                self.geometry=loads(zone_geo)
            except Exception as e:
                print("broken at row{}".format(row), end=' ')
                print(e)
                sys.exit(0)
        else:
            self.geometry=''
        centroid=kwargs['centroid'] if 'centroid' in keys else ''
        if centroid:
            try:
                self.centroid=loads(centroid)
            except Exception as e:
                print("broken at row{}".format(row), end=' ')
                print(e)
                sys.exit(0)
        else:
            print("centroid is not defined in zone.csv, please check it!")
            sys.exit(0)
        total_poi_count=kwargs['total_poi_count'] if 'total_poi_count' in keys else ''
        try:
            self.total_poi_count=float(total_poi_count)
        except:
            self.total_poi_count=0
        residential_poi_count=kwargs['residential_poi_count'] if 'residential_poi_count' in keys else ''
        try:
            self.residential_poi_count=float(residential_poi_count)
        except:
            self.residential_poi_count=0
        office_poi_count=kwargs['office_poi_count'] if 'office_poi_count' in keys else ''
        try:
            self.office_poi_count=float(office_poi_count)
        except:
            self.office_poi_count=0
        shopping_poi_count=kwargs['shopping_poi_count'] if 'shopping_poi_count' in keys else ''
        try:
            self.shopping_poi_count=float(shopping_poi_count)
        except:
            self.shopping_poi_count=0
        school_poi_count=kwargs['school_poi_count'] if 'school_poi_count' in keys else ''
        try:
            self.school_poi_count=float(school_poi_count)
        except:
            self.school_poi_count=0
        parking_poi_count=kwargs['parking_poi_count'] if 'parking_poi_count' in keys else ''
        try:
            self.parking_poi_count=float(parking_poi_count)
        except:
            self.parking_poi_count=0
        boundary_node_count=kwargs['boundary_node_count'] if 'boundary_node_count' in keys else ''
        try:
            self.boundary_node_count=float(boundary_node_count)
        except:
            self.boundary_node_count=0
        total_production=kwargs['total_production'] if 'total_production' in keys else ''
        try:
            self.total_production=float(total_production)
        except:
            self.total_production=0
        total_attraction=kwargs['total_attraction'] if 'total_attraction' in keys else ''
        try:
            self.total_attraction=float(total_attraction)
        except:
            self.total_attraction=0

class Network():
    def __init__(self):
        self.node_dict={}

        self.link_dict={}
        self.agent_dict={}
        self.demand_dict={}
        self.poi_dict={}
        self.poi_trip_dict={}
        self.zone_dict={}


        self.number_of_node=0
        self.number_of_link=0
        self.number_of_agent=0
        self.number_of_demand=0
        self.number_of_poi=0
        self.number_of_zone=0
        self.number_of_poi_type=0

        self.node_coords=[]
        self.link_coords=[]
        self.poi_coords=[]

        self.range_of_zone_ids=[]



        self.min_lat=-90
        self.max_lat=90
        self.min_lng=-180
        self.max_lng=180

    def get_avl_node_attrs(self):
        self.node_attr_dict = {
            'ctrl_type': 'int',
            'activity_type': 'str',
            'production': 'float',
            'attraction': 'float',
        }
        print('%-30s%-20s' % ('attr', 'type'))
        for k, v in self.node_attr_dict.items():
            print('%-30s%-20s' % (k, v))

    def get_avl_link_attrs(self):
        self.link_attr_dict = {
            'length': 'float',
            'lanes': 'int',
            'free_speed': 'float',
            'capacity': 'float',
            'link_type_name': 'str',
            'allowed_uses': 'str',
        }
        print('%-30s%-20s' % ('attr', 'type'))
        for k, v in self.link_attr_dict.items():
            print('%-30s%-20s' % (k, v))

    def get_avl_poi_attrs(self):
        self.poi_attr_dict = {
            'building': 'str',
            'activity_zone_id': 'int'
        }
        print('%-30s%-20s' % ('attr', 'type'))
        for k, v in self.poi_attr_dict.items():
            print('%-30s%-20s' % (k, v))

    def get_avl_range_of_zone_ids(self):
        if self.number_of_zone==0:
            print("zone.csv doesn't exist")
        else:
            print('%-20s%-20s' % ('min zone id', 'max zone id'))
            print('%-20s%-20s' % (self.range_of_zone_ids[0],self.range_of_zone_ids[1]))