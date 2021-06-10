from .readfiles import *
from .plot import *
from .utils import *
from .setting import *

def get_num_of_nodes_by_attr(network, attr):
    """
    :param network:
    :param attr: str
    :return:
    """
    if attr not in avl_node_attrs_for_num:
        print("ValueError: {} is expected".format(avl_node_attrs_for_num))
    else:
        attr_values = statNodeAttrValue(network, attr)
        if len(attr_values)==0:
            print("the '%s' value not found in node.csv"%attr)
        else:
            print('%-20s%-20s' % (attr, 'number'))
            for k, v in attr_values.items():
                print('%-20s%-20s' % (k, v))

def get_range_of_node_attr(network,attr):
    """
    :param network:
    :param attr: str
    :return:
    """
    if attr not in avl_node_attrs_for_range:
        print("ValueError: {} is expected".format( avl_node_attrs_for_range))
    else:
        attr_values = statNodeAttrValue(network, attr)
        if len(attr_values) == 0:
            print("the '%s' value not found in node.csv" % attr)
        else:
            print('%-20s%-20s%-20s' % ('attr', 'min value', 'max value'))
            print('%-20s%-20.4f%-20.4f' % (attr, attr_values['min_v'],attr_values['max_v']))

def get_num_of_links_by_attr(network, attr):
    """
    :param network:
    :param attr: str
    :return:
    """
    if attr not in avl_link_attrs_for_num:
        print("ValueError: {} is expected".format(avl_link_attrs_for_num))
    else:
        attr_values = statLinkAttrValue(network, attr)
        if len(attr_values)==0:
            print("the '%s' value not found in link.csv"%attr)
        else:
            print('%-20s%-20s' % (attr, 'number'))
            for k, v in attr_values.items():
                print('%-20s%-20s' % (k, v))

def get_range_of_link_attr(network,attr):
    """
    :param network:
    :param attr: str
    :return:
    """
    if attr not in avl_link_attrs_for_range:
        print("ValueError: {} is expected".format(avl_link_attrs_for_range))
    else:
        attr_values = statLinkAttrValue(network, attr)
        if len(attr_values) == 0:
            print("the '%s' value not found in link.csv" % attr)
        else:
            print('%-20s%-20s%-20s' % ('attr', 'min value', 'max value'))
            print('%-20s%-20.4f%-20.4f' % (attr,attr_values['min_v'], attr_values['max_v']))

def get_num_of_pois_by_attr(network, attr):
    """
    :param network:
    :param attr: str
    :return:
    """
    if attr not in avl_poi_attrs:
        print("ValueError: {} is expected".format(avl_poi_attrs))
    else:
        attr_values = statPoiAttrValue(network, attr)
        if len(attr_values)==0:
            print("the '%s' attribute value missing in poi.csv"%attr)
        else:
            print('%-30s%-20s' % (attr, 'number'))
            for k, v in attr_values.items():
                print('%-30s%-20s' % (k, v))

def get_info_of_zone_by_id(network,zone_id=None):
    """
    :param network:
    :param zone_id: int
    :return:
    """
    print('%-20s%-20s%-20s%-20s%-20s'%('zone_id','name','total_poi_count','total_production','total_attraction'))
    if isinstance(zone_id,int):
        for k, zone in network.zone_dict.items():
            if zone.activity_zone_id==zone_id:
                print('%-20s%-20s%-20s%-20.4f%-20.4f' % (zone.activity_zone_id, zone.name,zone.total_poi_count,
                                                     zone.total_production, zone.total_attraction))
    else:
        for k, zone in network.zone_dict.items():
            print('%-20s%-20s%-20s%-20.4f%-20.4f' % (zone.activity_zone_id, zone.name, zone.total_poi_count,
                                                 zone.total_production, zone.total_attraction))


def readNetwork(input_folder=None):
    """
    :param input_folder: str (the file directory)
    :return:
    """
    if input_folder:
        node_filepath = os.path.join(input_folder, 'node.csv')
        link_filepath = os.path.join(input_folder, 'link.csv')
        poi_filepath = os.path.join(input_folder, 'poi.csv')
        demand_filepath=os.path.join(input_folder,'demand.csv')
        agent_filepath=os.path.join(input_folder,'input_agent.csv')
        poi_trip_filepath = os.path.join(input_folder, 'poi_trip_rate.csv')
        zone_filepath = os.path.join(input_folder, 'zone.csv')
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

def showNetByAllMode(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    plotNetbySelectedObj(network.node_coords,network.link_coords,network.poi_coords,savefig)

def showNetByAutoMode(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    auto_net=searchNetMode(network,['auto','all'])
    if len(auto_net[0][0])>0:
        plotNetbySelectedObj(auto_net[0],auto_net[1],network.poi_coords,savefig)
    else:
        print('error!  auto mode not found in the link.csv')

def showNetByWalkMode(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    walk_net = searchNetMode(network, ['walk','all'])
    if len(walk_net[0][0]) > 0:
        plotNetbySelectedObj(walk_net[0],walk_net[1], network.poi_coords,savefig)
    else:
        print('error! walk mode not found in the link.csv')

def showNetByBikeMode(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    bike_net = searchNetMode(network, ['bike','all'])
    if len(bike_net[0][0]) > 0:
        plotNetbySelectedObj(bike_net[0],bike_net[1], network.poi_coords,savefig)
    else:
        print('error! bike mode not found in the link.csv')

def showNetByRailMode(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    rail_net = searchNetMode(network, ['railway'])
    if len(rail_net[0][0]) > 0:
        plotNetbySelectedObj(rail_net[0],rail_net[1], network.poi_coords,savefig)
    else:
        print('error! rail mode not found in the link.csv')

def showNetByNodeAttr(network,attr_dict,savefig=None):
    """
    :param network:
    :param attr_dict: dict,for example: {'ctrl_type':1}
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    attr,value=list(attr_dict.items())[0]
    if attr not in avl_node_attrs:
        print("ValueError: ‘{}’ is not available node attributes, {} is expected".format(attr,avl_node_attrs))
    else:
        node_coords, link_coords=searchNetbyNodeAttr(network,attr,value)
        if len(node_coords[0]):
            plotNetbySelectedObj(node_coords,link_coords,network.poi_coords,savefig)
        else:
            print(" '{}={}' values not found".format(attr,value))
def showNetByNodeProduction(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    node_coords,values=statNodeAttrRange(network,'production')
    if len(values)>0:
        plotNetbyNodeAttrRange(node_coords, network.link_coords,network.poi_coords,attr='production',
                               value=values,savefig=savefig)
    else:
        print("node production values not found")
def showNetByNodeAttraction(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    node_coords, values = statNodeAttrRange(network,'attraction')
    if len(values)>0:
        plotNetbyNodeAttrRange(node_coords, network.link_coords, network.poi_coords, attr='attraction',
                               value=values,savefig=savefig)
    else:
        print("node attraction values not found")


def showNetByLinkAttr(network,attr_dict,savefig=None):
    """
    :param network:
    :param attr_dict: dict, for example: {'link_type_name':'secondary'}
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    attr, value = list(attr_dict.items())[0]
    if attr not in avl_link_attrs:
        print("ValueError: ‘{}’ is not available link attributes, {} is expected".format(attr,avl_link_attrs))
    else:
        node_coords, link_coords=searchNetbyLinkAttr(network,attr,value)
        if len(node_coords[0]):
            plotNetbySelectedObj(node_coords,link_coords,network.poi_coords,savefig)
        else:
            print(" '{}={}' values not found".format(attr,value))

def showNetByLinkFreeSpeed(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    node_coords,link_coords, values=statLinkAttrRange(network,'free_speed')
    if len(values)>0:
        plotNetbyLinkAttrRange(node_coords,link_coords,network.poi_coords,'free_speed',values,savefig)
    else:
        print("link free speed values not found")

def showNetByLinkLaneNum(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    node_coords,link_coords, values = statLinkAttrRange(network, 'lanes')
    if len(values)>0:
        plotNetbyLinkAttrRange(node_coords, link_coords, network.poi_coords, 'lanes', values,savefig)
    else:
        print("link lanes values not found")
def showNetByLinkCapacity(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    node_coords,link_coords, values = statLinkAttrRange(network, 'capacity')
    if len(values)>0:
        plotNetbyLinkAttrRange(node_coords, link_coords, network.poi_coords, 'capacity', values,savefig)
    else:
        print("link capacity values not found")

def showNetByPOIAttr(network,attr_dict,savefig=None):
    """
    :param network:
    :param attr_dict: dict, for example: {'building':'parking'}
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    attr, value = list(attr_dict.items())[0]
    if attr not in avl_poi_attrs:
        print("ValueError: ‘{}’ is not available poi attributes, {} is expected".format(attr,avl_poi_attrs))
    else:
        poi_coords=searchNetbyPoiAttr(network,attr,value)
        if len(poi_coords)>0:
            plotNetbySelectedObj(network.node_coords,network.link_coords,poi_coords,savefig)
        else:
            print(" '{}={}' values not found".format(attr,value))

def showNetByZonePOIProductionDensity(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    poi_coords, values=statPoiAttrRangeforDensity(network,attr='production_rate1')
    if len(poi_coords)>0:
        plotNetbyZonePoiAttrDensity(poi_coords,values,savefig)
    else:
        print("poi production values not found")
def showNetByZonePOIAttractionDensity(network,savefig=None):
    """
    :param network:
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    poi_coords, values=statPoiAttrRangeforDensity(network,attr='attraction_rate1')
    if len(poi_coords)>0:
        plotNetbyZonePoiAttrDensity(poi_coords,values,savefig)
    else:
        print("poi attraction values not found")

def showNetByZoneDemandHeatMap(network,annot=False,savefig=None):
    """
    :param network:
    :param annot: bool, whether show demand volume values
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    if network.number_of_zone==0:
        print("zone demand volume information not found, please check demand.csv")
    else:
        demand=statZoneDemandforHeat(network)
        plotNetbyZoneDeamndHeat(network,demand,annot,savefig)
def showNetByZoneDemandFlow(network,annot=True,bg=True,savefig=None):
    """
    :param network:
    :param annot: bool, whether show zone id
    :param bg: bool, whether show network as background
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    if network.number_of_demand==0:
        print("zone demand volume information not found, please check demand.csv")
    else:
        demand_line, values, zone_grid, zone_labels=statZoneDemandforFlow(network)
        plotNetbyZoneDemandFlow(network,demand_line,values, zone_grid, zone_labels,annot,bg,savefig)

def showNetByAgentTrace(network,agent_id,savefig=None):
    """
    :param network:
    :param agent_id: int
    :param savefig: dict for exampel:{'filename':'a.png','dpi':300}
    :return:
    """
    if agent_id not in network.agent_dict.keys():
        print(" 'agent id={}' not found".format(agent_id))
    else:
        agent_trace_node_coords, agent_trace_route_coords=statAgentTracebyID(network,agent_id)
        if len(agent_trace_node_coords[0])==0 and len(agent_trace_route_coords)==0:
            print("the trace of 'agent id={}' not found".format(agent_id))
        else:
            plotNetByAgentTrace(network.node_coords,network.link_coords,network.poi_coords,
                                agent_trace_node_coords,agent_trace_route_coords,savefig)


