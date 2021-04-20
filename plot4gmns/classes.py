from shapely.wkt import loads
class Node():
    def __init__(self,*args):
        self.name = args[0]
        self.node_id = int(float(args[1])) if args[1] else 0
        self.osm_node_id=args[2]
        self.osm_highway=args[3]
        self.zone_id=int(float(args[4])) if args[4] else ''
        self.ctrl_type = int(float(args[5])) if args[5] else ''
        self.node_type=args[6]
        self.activity_type = args[7] if args[7] else 'unclassified'
        self.is_boundary=args[8]
        self.x_coord=float(args[9]) if args[9] else ''
        self.y_coord=float(args[10]) if args[10] else ''
        self.main_node_id=args[11]
        self.poi_id=int(float(args[12])) if args[12] else ''
        self.notes=args[13]
        self.activity_zone_id=int(float(args[14])) if args[14] else ''
        self.production=float(args[15]) if args[15] else 0
        self.attraction=float(args[16]) if args[16] else 0
        self.activity_location_tab=args[17] if args[17] else 'unclassified'

        self.out_link_list=[]
        self.in_link_list=[]


class Link():
    def __init__(self,*args):
        self.name = args[0]
        self.link_id=int(float(args[1])) if args[1] else 0
        self.osm_way_id=args[2]
        self.from_node_id=int(float(args[3])) if args[3] else 0
        self.to_node_id=int(float(args[4])) if args[4] else 0
        self.dir_flag =int(float(args[5])) if args[5] else 1
        self.length =float(args[6]) if args[6] else ''
        self.lanes =int(float(args[7])) if args[7] else ''
        self.free_speed =float(args[8]) if args[8] else ''
        self.capacity = float(args[9]) if args[9] else ''
        self.link_type_name=args[10] if args[10] else 'unclassified'
        self.link_type = args[11]
        self.geometry = loads(args[12]) if args[12] else ''
        self.allowed_uses=args[13] if args[13] else 'unclassified'
        self.from_biway=args[14]



class Agent():
    def __init__(self,*args):
        self.agent_id=int(float(args[0])) if args[0] else 1
        self.agent_type=args[1]
        self.o_node_id=int(float(args[2])) if args[2] else ''
        self.d_node_id=int(float(args[3])) if args[3] else ''
        self.o_osm_node_id=args[4]
        self.d_osm_node_id=args[5]
        self.o_zone_id=int(float(args[6])) if args[6] else ''
        self.d_zone_id=int(float(args[7])) if args[7] else ''
        self.geometry=loads(args[8]) if args[8] else ''
        self.departure_time=float(args[9]) if args[9] else 0


class Demand():
    def __init__(self,*args):
        self.o_zone_id=int(float(args[0]))
        self.o_zone_name=args[1] if args[1] else 'unnamed'
        self.d_zone_id=int(float(args[2]))
        self.d_zone_name=args[3] if args[3] else 'unnamed'
        self.accessibility=float(args[4]) if args[4] else ''
        self.volume=float(args[5]) if args[5] else ''
        self.geometry=loads(args[6]) if args[6] else ''

class POI():
    def __init__(self,*args):
        self.name=args[0]
        self.poi_id=int(float(args[1])) if args[1] else ''
        self.osm_way_id=args[2]
        self.osm_relation_id=args[3]
        self.building=args[4] if args[4] else 'unclassified'
        self.amenity=args[5]
        self.way=args[6]
        self.geometry=loads(args[7]) if args[7] else ''
        self.centroid=loads(args[8]) if args[8] else ''
        self.area=float(args[9])
        self.area_ft2=args[10]
        self.activity_zone_id=int(float(args[11])) if args[11] else ''

class POITrip():
    def __init__(self,*args):
        self.poi_type_id=int(float(args[0])) if args[0] else 0
        self.building=args[1] if args[1] else 'unclassified'
        self.unit_of_measure=args[2]
        self.trip_purpose=args[3]
        self.production_rate1=float(args[4]) if args[4] else 0
        self.attraction_rate1=float(args[5]) if args[5] else 0
        self.production_notes=args[6]
        self.attraction_notes=args[7]

class Zone():
    def __init__(self,*args):
        self.activity_zone_id=int(float(args[0])) if args[0] else ''
        self.name=args[1] if args[1] else 'unclassified'
        self.centroid_x=float(args[2]) if args[2] else ''
        self.centroid_y=float(args[3]) if args[3] else ''
        self.geometry=loads(args[4]) if args[4] else ''
        self.centroid=loads(args[5]) if args[5] else ''
        self.total_poi_count=float(args[6]) if args[6] else 0
        self.residential_poi_count=float(args[7]) if args[7] else 0
        self.office_poi_count=float(args[8]) if args[8] else 0
        self.shopping_poi_count=float(args[9]) if args[9] else 0
        self.school_poi_count=float(args[10]) if args[10] else 0
        self.parking_poi_count=float(args[11]) if args[11] else 0
        self.boundary_node_count=float(args[12])if args[12] else 0
        self.total_production=float(args[13]) if args[13] else 0
        self.total_attraction=float(args[14]) if args[14] else 0

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
        self.demand_coords=[]

        self.node_id_list = []

        self.node_ctrl_type_list=[]
        self.node_type_list=[]
        self.node_activity_type_list=[]
        self.node_production_list=[]
        self.node_attraction_list=[]

        self.free_speed_range=[]
        self.lane_range=[]
        self.capacity_range=[]


        self.min_lat=-90
        self.max_lat=90
        self.min_lng=-180
        self.max_lng=180

    def get_valid_node_attr_list(self):
        self.node_attr_dict = {
            'ctrl_type': 'int',
            'activity_type': 'str',
            'production': 'float',
            'attraction': 'float',
        }
        print('%-30s%-20s' % ('attr', 'type'))
        for k, v in self.node_attr_dict.items():
            print('%-30s%-20s' % (k, v))

    def get_valid_link_attr_list(self):
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

    def get_valid_poi_attr_list(self):
        self.poi_attr_dict = {
            'building': 'str',
            'activity_zone_id': 'int'
        }
        print('%-30s%-20s' % ('attr', 'type'))
        for k, v in self.poi_attr_dict.items():
            print('%-30s%-20s' % (k, v))

    def get_valid_zone_id_list(self):
        if self.number_of_zone==0:
            print("zone.csv doesn't exist")
        else:
            print('%-20s%-20s' % ('min zone id', 'max zone id'))
            print('%-20s%-20s' % (1, self.number_of_zone))