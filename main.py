import plot4gmns as p4g

mnet = p4g.generate_multi_network_from_csv(r'E:\BaiduBackup\Github\osm2rail\convert_csv_to_geos_files')

# cf = p4g.show_network_by_modes(mnet=mnet,modes=['auto'])
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

# cf = p4g.show_network_by_link_capacity_distribution(mnet=mnet)
# cf.show()

# cf = p4g.show_network_by_link_free_speed_distribution(mnet=mnet)
# cf.show()
#
# cf = p4g.show_network_by_poi_types(mnet=mnet,poi_type=['apartments','industrial'])
# cf.show()

# cf = p4g.show_network_by_poi_attraction_distribution(mnet=mnet)
# cf.show()

# cf = p4g.show_network_by_poi_production_distribution(mnet=mnet)
# cf.show()

# cf = p4g.show_network_demand_matrix_heatmap(mnet)
# cf.show()