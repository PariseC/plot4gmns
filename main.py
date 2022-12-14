# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 18:47
# @Author  : CZY
# @File    : test_plot4gmns.py
# @Software: PyCharm
"""
For :
"""
import plot4gmns as p4g
input_dir = r'E:\CoderStudio\Py\2021-04-30-TestPackages\usingGrid2Demand\Berlin'

mnet = p4g.generate_multi_network_from_csv(input_dir)
# p4g.show_network_by_mode(mnet)
# p4g.show_network_by_node_type(mnet,osm_highway=['pitch'])
# p4g.show_network_by_link_free_speed(mnet,min_free_speed=10,max_free_speed=40)
# p4g.show_network_by_link_lane(mnet,min_lanes=1,max_lanes=4)

# p4g.show_network_by_link_length(mnet,min_length=10,max_length=100)
# p4g.show_network_by_link_lane_distribution(mnet)

# p4g.show_network_by_poi_type(mnet,poi_type=['park','parking'])
# p4g.show_network_by_poi_production_distribution(mnet)
# p4g.show_network_by_poi_attraction_distribution(mnet)

p4g.show_network_demand_matrix(mnet)
p4g.show_network_by_demand_OD(mnet)