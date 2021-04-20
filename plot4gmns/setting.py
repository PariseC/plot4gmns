

link_type_color_dict = {'motorway': 'aqua',
                        'trunk': 'blue',
                        'primary': 'darkcyan',
                        'secondary': 'darkmagenta',
                        'tertiary': 'darkred',
                        'residential': 'darkviolet',
                        'service': 'fuchsia',
                        'cycleway':'lime',
                        'footway': 'magenta',
                        'track': 'orangered',
                        'unclassified': 'maroon',
                        'connector':'black',
                        'railway':'brown',
                        'aeroway':'navy'}

node_attr_int_color_dict={0: 'darkred',
                      1: 'blue',
                      2: 'darkcyan',
                      3: 'darkmagenta',
                      4: 'aqua',
                      5: 'darkviolet',
                      6: 'fuchsia',
                      7:'lime',
                      8: 'magenta',
                      9: 'orangered',
                      10: 'maroon',
                      11:'black',
                      12:'brown',
                      13:'navy'}

node_activity_type_color_dict={'motorway': 'aqua',
                               'trunk': 'blue',
                               'primary': 'darkcyan',
                               'secondary': 'darkmagenta',
                               'tertiary': 'darkred',
                               'residential': 'darkviolet',
                               'service': 'fuchsia',
                               'cycleway':'lime',
                               'footway': 'magenta',
                               'track': 'orangered',
                               'unclassified': 'maroon',
                               'connector':'black',
                               'railway':'brown',
                               'aeroway':'navy',
                               'poi':'darkgreen',
                               'centroid node':'darkslategray'}

valid_node_attr_for_Net=['ctrl_type','activity_type','production','attraction']
valid_link_attr_for_Net=['link_type_name','allowed_uses','free_speed','lanes','capacity','length']
valid_poi_attr_for_Net=['building','activity_zone_id']