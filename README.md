# Plot4GMNS: An open-source academic research tool for visualizing multimodal networks for transportation system modeling and optimization

**Authors:** Dr. Junhua Chen, Zanyang Cui, Xiangyong Luo

**Email:** cjh@bjtu.edu.cn, zanyangcui@outlook.com, luoxiangyong01@gmail.com

## Introduction

To enable rapid transportation modeling and optimization, as traffic management researchers, we provide this free open-source tool for visualizing multimodal networks. Based on GMNS data format by [Zepha foundation](https://zephyrtransport.org/), plot4gmns is designed for reading and plotting multimodal data sets including transportation network files, demand and agent trace files.

## Requirements

- pandas
- shapely
- matplotlib<=3.3.0
- numpy
- seaborn
- scipy
- chardet

## Installation

```python
pip install plot4gmns
```

> Note
>
> - For Windows users, the _pip_ method might fail to install some dependencies. If errors occur when you try to install any of those dependencies, try instead to pip install their .whl files, which can be downloaded from the Unoffical Windows Binaries for [Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

## Quick Start
Before starting, you must have prepared network files, including node.csv, link.csv, poi.csv, demand.csv, and zone.csv. The osm2gmns package will help you quickly obtain node, link, and poi data, and the grid2demand package will help you obtain network demand and zone information.


**Step 1: generate multimodal network**
```python
>>>import plot4gmns as p4g
mnet=p4g.generate_multi_network_from_csv(r'./datasets')
```

**Step 2: show networks in different modes**
```python
# draw 'all' modes network and save to png file
cf = p4g.show_network_by_modes(mnet=mnet)
# show the figure on the current window
cf.show()
# show 'bike' mode network
cf = p4g.show_network_by_modes(mnet=mnet,modes=['bike'])
cf.show() # show the figure on the current window
```
<img src="https://github.com/PariseC/plot4gmns/blob/main/media/node_ctrl_type_1.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 3: show network with given node types**
```python
cf = p4g.show_network_by_node_types(mnet=mnet,osm_highway=['traffic_signals','crossing'])
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/node_ctrl_type_1.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 4: show network by given link types**
```python
# show network by given link length range
cf = p4g.show_network_by_link_types(mnet=mnet,link_types=['secondary','footway'])
cf.show()
```

**Step 5: show network by given link attributes range**
```python
# show network by given link length range
cf = p4g.show_network_by_link_length(mnet=mnet,min_length=10,max_length=50)
cf.show()

# show network by given link lane range
cf = p4g.show_network_by_link_lanes(mnet=mnet,min_lanes=1,max_lanes=3)
cf.show()

# show network by given link free speed range
cf = p4g.show_network_by_link_free_speed(mnet=mnet,min_free_speed=10,max_free_speed=40)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/link_type_secondary.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 6: show network by link attributes distribution**
```python
# show network by link lane distribution
cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
cf.show()

# show network by link capacity distribution
cf = p4g.show_network_by_link_capacity_distribution(mnet=mnet)
cf.show()

# show network by link free speed distribution
cf = p4g.show_network_by_link_free_speed_distribution(mnet=mnet)
cf.show()
```

**Step 7: show network with given POI types**
```python
cf = p4g.show_network_by_poi_types(mnet=mnet,poi_type=['public','industrial'])
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/poi_parking.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 8: show network by poi attributes  distribution**
```python
# show network by poi attraction distribution
cf = p4g.show_network_by_poi_attraction_distribution(mnet=mnet)
cf.show()
# show network by poi production distribution
cf = p4g.show_network_by_poi_production_distribution(mnet=mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/zone_demand_flow.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 9: show network demand matrix heatmap**
```python
p4g.show_network_demand_matrix_heatmap(mnet)
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/zone_trace.png?raw=true?raw=true" width="800" height="600" alt=" "/><br/>

**Step 10: show network demand OD**
```python
cf = p4g.show_network_by_demand_OD(mnet=mnet,load_network=True)
cf.show()
```

## Advance

**Step 1: Show only network elements of interest**

The tool displays all elements by default, such as nodes, links, and POIs. If you want to display only the elements of interest, you can refer to the following example to modify the state of other elements before invoking the drawing command.
```python
# not show nodes
mnet.node_loaded = False
cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
cf.show()
```

**Step 2: Show different networks on one diagram**

By default, this tool will clear the original contents before drawing. If you want to draw different content on a graph, you can refer to the following example

```python
# not show nodes
mnet.node_loaded = False
cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
cf.show()
```

**Step 3: Set the drawing style**

Users can refer to the following examples to adjust the color, size and other attributes of the image before drawing.

| parameter                             | Value                   | Description                    |
|---------------------------------------|-------------------------|--------------------------------|
| mnet.style.figure_size                | tuple,(width,height)    | Image size                     |
| mnet.style.node_style.size            | int                     | node marker size               |
| mnet.style.node_style.colors          | dict,{node_type:color}  | node color in different types  |
| mnet.style.node_style.markers         | dict,{node_type:marker} | node marker in different types |
| mnet.style.link_style.linecolor       | str                     | link color                     |
| mnet.style.link_style.linewidth       | str                     | link width                     |
| mnet.style.poi_style.facecolor        | str                     | POI facecolor                  |
| mnet.style.poi_style.edgecolor        | str                     | POI edgecolor                  |
| mnet.style.demand_style.linecolor     | str                     | demand flow line color         |
| mnet.style.demand_style.linelinewidth | str                     | demand flow line width         |
| mnet.style.zone_style.linewidth       | str                     | zone grid line width           |
| mnet.style.zone_style.edgecolors      | str                     | zone grid edgecolors           |
| mnet.style.zone_style.fontsize        | str                     | zone label font size           |
| mnet.style.zone_style.fontcolor       | str                     | zone label font color          |

```python
# not show nodes
mnet.node_loaded = False
cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
cf.show()
```
## Logs