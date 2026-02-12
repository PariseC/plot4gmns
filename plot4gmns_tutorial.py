import plot4gmns as pg

mnet = pg.generate_multi_network_from_csv(r'./datasets/Berlin')

fig = pg.show_gmns_nodes(mnet)

fig = pg.show_gmns_links(mnet)

fig = pg.show_gmns_poi(mnet)

fig = pg.show_gmns_zones(mnet)

fig = pg.show_gmns_location(mnet)

fig = pg.show_gmns_lanes(mnet)

fig = pg.show_gmns_movements(mnet)

fig = pg.show_gmns_geometries(mnet)

fig = pg.show_network_by_modes(mnet=mnet, modes=['auto'])

fig = pg.show_network_by_modes(mnet=mnet, modes=['bike'])

cf = pg.show_network_by_node_types(mnet=mnet, ctrl_type=['signal'])
# cf.show()

fig = pg.show_network_by_link_types(mnet=mnet, link_types=['secondary', 'footway'])
fig.show()

fig = pg.show_network_by_link_length(mnet=mnet, min_length=10, max_length=50)
fig.show()

fig = pg.show_network_by_link_free_speed(mnet=mnet, min_free_speed=10, max_free_speed=40)
fig.show()

fig = pg.show_network_by_link_lanes(mnet=mnet, min_lanes=2, max_lanes=4)
fig.show()

fig = pg.show_network_by_link_lane_distribution(mnet=mnet)
# fig.show()
#
fig = pg.show_network_by_link_capacity_distribution(mnet=mnet)
# fig.show()
#
fig = pg.show_network_by_link_free_speed_distribution(mnet=mnet)
fig.show()

fig = pg.show_network_by_poi_types(mnet=mnet, poi_type=['apartments', 'industrial'])
fig.show()

fig = pg.show_network_by_poi_attraction_distribution(mnet=mnet)
fig.show()

fig = pg.show_network_by_poi_production_distribution(mnet=mnet)
fig.show()

fig = pg.show_network_demand_matrix_heatmap(mnet)
# fig.show()