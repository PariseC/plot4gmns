from .readfiles import *
from .plot import *
from .utils import *
from .setting import *

def get_node_attr_value_list( network, attr):
    if attr not in valid_node_attr_for_Net:
        print("please inut vaild node attr:%s" % valid_node_attr_for_Net)
    else:
        attr_values = statNodeAttrValue(network, attr)
        if len(attr_values)==0:
            print("the '%s' attribute value missing"%attr)
        else:
            if attr=='production' or attr=='attraction':
                print('%-20s%-20s%-20s' % ('attr','min value','max value'))
                k=list(attr_values.keys())
                print('%-20s%-20s%-20s' % (attr, min(k), max(k)))
            else:
                print('%-20s%-20s' % (attr, 'number'))
                for k, v in attr_values.items():
                    print('%-20s%-20s' % (k, v))
def get_link_attr_value_list(network, attr):
    if attr not in valid_link_attr_for_Net:
        print("please inut vaild link attr:%s" % valid_link_attr_for_Net)
    else:
        attr_values = statLinkAttrValue(network, attr)
        if len(attr_values)==0:
            print("the '%s' attribute value missing"%attr)
        else:
            if attr=='link_type_name' or attr=='allowed_uses':
                print('%-20s%-20s' % (attr, 'number'))
                for k, v in attr_values.items():
                    print('%-20s%-20s' % (k, v))
            else:
                print('%-20s%-20s%-20s' % ('attr', 'min value', 'max value'))
                k = list(attr_values.keys())
                print('%-20s%-20s%-20s' % (attr, min(k), max(k)))
def get_poi_attr_value_list(network, attr):
    if attr not in valid_poi_attr_for_Net:
        print("please inut vaild node attr:%s" % valid_poi_attr_for_Net)
    else:
        attr_values = statPoiAttrValue(network, attr)
        if len(attr_values)==0:
            print("the '%s' attribute value missing"%attr)
        else:
            print('%-30s%-20s' % (attr, 'number'))
            for k, v in attr_values.items():
                print('%-30s%-20s' % (k, v))
def get_zone_id_list(network,zone_id=None):
    print('%-20s%-20s%-20s%-20s%-20s'%('zone_id','name','total_poi_count','total_production','total_attraction'))
    if isinstance(zone_id,int):
        for k, zone in network.zone_dict.items():
            if zone.activity_zone_id==zone_id:
                print('%-20s%-20s%-20s%-20s%-20s' % (zone.activity_zone_id, zone.name,zone.total_poi_count,
                                                     zone.total_production, zone.total_attraction))
    else:
        for k, zone in network.zone_dict.items():
            print('%-20s%-20s%-20s%-20s%-20s' % (zone.activity_zone_id, zone.name, zone.total_poi_count,
                                                 zone.total_production, zone.total_attraction))


def readNetwork(input_folder=None):
    global g_output_folder
    if input_folder:
        node_filepath = os.path.join(input_folder, 'node.csv')
        link_filepath = os.path.join(input_folder, 'link.csv')
        poi_filepath = os.path.join(input_folder, 'poi.csv')
        demand_filepath=os.path.join(input_folder,'demand.csv')
        agent_filepath=os.path.join(input_folder,'input_agent.csv')
        poi_trip_filepath = os.path.join(input_folder, 'poi_trip_rate.csv')
        zone_filepath = os.path.join(input_folder, 'zone.csv')
        g_output_folder = input_folder
    else:
        node_filepath = 'node.csv'
        link_filepath = 'link.csv'
        poi_filepath = 'poi.csv'
        demand_filepath = 'demand.csv'
        agent_filepath = 'input_agent.csv'
        poi_trip_filepath ='poi_trip_rate.csv'
        zone_filepath ='zone.csv'
    net=readNet(node_filepath,link_filepath,poi_filepath,zone_filepath,demand_filepath,poi_trip_filepath,agent_filepath)
    return net

def showNetByAllMode(network):
    plotNetbySelectedObj(network.node_coords,network.link_coords,network.poi_coords)
def showNetByAutoMode(network):
    auto_net=searchNetMode(network,'auto')
    if len(auto_net[0][0])>0:
        plotNetbySelectedObj(auto_net[0],auto_net[1],network.poi_coords)
    else:
        print('error! there is no auto mode in the input network')
def showNetByWalkMode(network):
    walk_net = searchNetMode(network, 'walk')
    if len(walk_net[0][0]) > 0:
        plotNetbySelectedObj(walk_net[0],walk_net[1], network.poi_coords)
    else:
        print('error! there is no walk mode in the input network')
def showNetByBikeMode(network):
    bike_net = searchNetMode(network, 'bike')
    if len(bike_net[0][0]) > 0:
        plotNetbySelectedObj(bike_net[0],bike_net[1], network.poi_coords)
    else:
        print('error! there is no bike mode in the input network')
def showNetByRailMode(network):
    rail_net = searchNetMode(network, 'railway')
    if len(rail_net[0][0]) > 0:
        plotNetbySelectedObj(rail_net[0],rail_net[1], network.poi_coords)
    else:
        print('error! there is no rail mode in the input network')

def showNetByNodeAttr(network,attr_dict):
    attr,value=list(attr_dict.items())[0]
    if attr not in valid_node_attr_for_Net:
        print("please inut vaild node attr:%s"%valid_node_attr_for_Net)
    else:
        node_coords, link_coords=searchNetbyNodeAttr(network,attr,value)
        if len(node_coords[0]):
            plotNetbySelectedObj(node_coords,link_coords,network.poi_coords)
        else:
            print('There is no node data that meets the requirements ')
def showNetByNodeProduction(network):
    node_coords,values=statNodeAttrRange(network,'production')
    plotNetbyNodeAttrRange(node_coords, network.link_coords,network.poi_coords,attr='production',value=values)
def showNetByNodeAttraction(network):
    node_coords, values = statNodeAttrRange(network,'attraction')
    plotNetbyNodeAttrRange(node_coords, network.link_coords, network.poi_coords, attr='attraction', value=values)


def showNetByLinkAttr(network,attr_dict):
    attr, value = list(attr_dict.items())[0]
    if attr not in valid_link_attr_for_Net:
        print("please input vaild link attr :%s"%valid_link_attr_for_Net)
    else:
        node_coords, link_coords=searchNetbyLinkAttr(network,attr,value)
        if len(node_coords[0]):
            plotNetbySelectedObj(node_coords,link_coords,network.poi_coords)
        else:
            print('There is no link data that meets the requirements ')
def showNetByLinkFreeSpeed(network):
    node_coords,link_coords, values=statLinkAttrRange(network,'free_speed')
    if len(values)>0:
        plotNetbyLinkAttrRange(node_coords,link_coords,network.poi_coords,'free_speed',values)
    else:
        print("the 'link free speed' attribute value missing")
def showNetByLinkLaneNum(network):
    node_coords,link_coords, values = statLinkAttrRange(network, 'lanes')
    if len(values)>0:
        plotNetbyLinkAttrRange(node_coords, link_coords, network.poi_coords, 'lanes', values)
    else:
        print("the 'link lanes' attribute value missing")
def showNetByLinkCapacity(network):
    node_coords,link_coords, values = statLinkAttrRange(network, 'capacity')
    if len(values)>0:
        plotNetbyLinkAttrRange(node_coords, link_coords, network.poi_coords, 'capacity', values)
    else:
        print("the 'link capacity' attribute value missing")

def showNetByPOIAttr(network,attr_dict):
    attr, value = list(attr_dict.items())[0]
    if attr not in valid_poi_attr_for_Net:
        print("please inut vaild POI attr :%s"%valid_poi_attr_for_Net)
    else:
        poi_coords=searchNetbyPoiAttr(network,attr,value)
        if len(poi_coords)>0:
            plotNetbySelectedObj(network.node_coords,network.link_coords,poi_coords)
        else:
            print('There is no link data that meets the requirements ')
def showNetByPOIProductionHeat(network):
    poi_coords, values=statPoiAttrRangeforHeat(network,attr='production_rate1')
    if len(poi_coords)>0:
        plotNetbyPoiAttrHeat(poi_coords,values)
    else:
        print('There is no poi data that meets the requirements ')
def showNetByPOIAttractionHeat(network):
    poi_coords, values=statPoiAttrRangeforHeat(network,attr='attraction_rate1')
    if len(poi_coords)>0:
        plotNetbyPoiAttrHeat(poi_coords,values)
    else:
        print('There is no poi data that meets the requirements ')
def showNetByPOIProductionContour(network):
    poi_coords, values = statPoiAttrRangeforContour(network, attr='production_rate1')
    if len(poi_coords) > 0:
        plotNetbyPoiAttrContour(network,poi_coords, values)
    else:
        print('There is no poi data that meets the requirements ')
def showNetByPOIAttractionContour(network):
    poi_coords, values = statPoiAttrRangeforContour(network, attr='attraction_rate1')
    if len(poi_coords) > 0:
        plotNetbyPoiAttrContour(network,poi_coords, values)
    else:
        print('There is no poi data that meets the requirements ')

def showNetByZoneDemandHeat(network,annot=False):
    if network.number_of_zone==0:
        print("there is no zone data")
    else:
        demand=statZoneDemandforHeat(network)
        plotNetbyZoneDeamndHeat(network,demand,annot)
def showNetByZoneDemandFlow(network,annot=True,bg=True):
    if network.number_of_demand==0:
        print("there is no demand data")
    else:
        demand_line, values, zone_grid, zone_labels=statZoneDemandforFlow(network)
        plotNetbyZoneDemandFlow(network,demand_line,values, zone_grid, zone_labels,annot,bg)
def showNetByZoneAgent(network,zone):
    if network.number_of_agent==0:
        print("there is no agent data")
    else:
        zone=zone if isinstance(zone,list) else [zone]
        agent_coords, agent_num, zone_grid, zone_labels=statZoneAgent(network,zone)
        plotNetbyZoneAgent(network,agent_coords, agent_num, zone_grid, zone_labels)
