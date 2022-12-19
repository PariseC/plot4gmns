import plot4gmns as p4g
mnet = p4g.generate_multi_network_from_csv(r'E:\CoderStudio\Py\2021-04-30-TestPackages\usingGrid2Demand\Berlin')

# cf = p4g.show_network_by_modes(mnet=mnet)
# cf.show()

# cf = p4g.show_network_by_modes(mnet=mnet,modes=['bike'])
# cf.show()

# cf = p4g.show_network_by_node_types(mnet=mnet,osm_highway=['traffic_signals','crossing'])
# cf.show()

# cf = p4g.show_network_by_link_types(mnet=mnet,link_types=['secondary','footway'])
# cf.show()

# cf = p4g.show_network_by_link_length(mnet=mnet,min_length=10,max_length=50)
# cf.show()

# cf = p4g.show_network_by_link_free_speed(mnet=mnet,min_free_speed=10,max_free_speed=40)
# cf.show()

# cf = p4g.show_network_by_link_lanes(mnet=mnet,min_lanes=2,max_lanes=4)
# cf.show()

# cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
# cf.show()

cf = p4g.show_network_by_link_capacity_distribution(mnet=mnet)
cf.show()

cf = p4g.show_network_by_link_free_speed_distribution(mnet=mnet)
cf.show()

# cf = p4g.show_network_by_poi_types(mnet=mnet,poi_type=['public','industrial'])
# cf.show()

# cf = p4g.show_network_by_poi_attraction_distribution(mnet=mnet)
# cf.show()

# cf = p4g.show_network_by_poi_production_distribution(mnet=mnet)
# cf.show()

# cf = p4g.show_network_demand_matrix_heatmap(mnet)
# cf.show()

# cf = p4g.show_network_by_demand_OD(mnet=mnet)
# cf.show()

# mnet.node_loaded = False
# cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
# cf.show()

# mnet.node_loaded = False
# mnet.POI_loaded = False
# cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
# mnet.link_loaded = False
# mnet.POI_loaded = True
# cf = p4g.show_network_by_poi_attraction_distribution(mnet,fig_obj=cf)
# cf.show()

# mnet.style.node_style.size = 3
# mnet.style.link_style.linecolor = 'green'
# mnet.style.poi_style.facecolor = 'gray'
# cf = p4g.show_network_by_modes(mnet=mnet)
# cf.show()