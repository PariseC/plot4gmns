# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 18:47
# @Author  : CZY
# @File    : test_plot4gmns.py
# @Software: PyCharm
"""
For :
"""
import plot4gmns as pg
net=pg.readNetwork('../data/DC')
# net.get_valid_node_attr_list()
# net.get_valid_link_attr_list()
# net.get_valid_poi_attr_list()
# net.get_valid_zone_id_list()

# pg.get_node_attr_value_list(net,'activity_type')
# pg.get_link_attr_value_list(net,'link_type_name')# if the capacity value exists in the link.csv
# pg.get_poi_attr_value_list(net,'building')
# pg.get_zone_id_list(net)


# pg.showNetByAllMode(net)
# pg.showNetByAutoMode(net)
# pg.showNetByBikeMode(net)
# pg.showNetByWalkMode(net)
# pg.showNetByRailMode(net)

# pg.showNetByNodeAttr(net,{'activity_type':'primary'})
# pg.showNetByLinkAttr(net,{'link_type_name':'secondary'})

# pg.showNetByNodeProduction(net)
# pg.showNetByNodeAttraction(net)
# pg.showNetByLinkFreeSpeed(net)
# pg.showNetByLinkLaneNum(net)
# pg.showNetByLinkCapacity(net)

# pg.showNetByPOIAttr(net,{'activity_zone_id':(1,5)})
# pg.showNetByPOIAttractionHeat(net)
# pg.showNetByPOIProductionHeat(net)
# pg.showNetByPOIAttractionContour(net)
# pg.showNetByPOIProductionContour(net)
#
# pg.showNetByZoneDemandHeat(net,annot=False)# annot:bool,whether or not show zone-to-zone demand value
# pg.showNetByZoneDemandFlow(net)

pg.showNetByZoneAgent(net,[(1,15),(6,5)])