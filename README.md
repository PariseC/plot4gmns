# Plot4GMNS: An open-source academic research tool for visualizing multimodal networks for transportation system modeling and optimization

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fa4f13889fb546afb83b1a174210e9cc)](https://app.codacy.com/gh/xyluo25/plot4gmns/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) [![Downloads](https://static.pepy.tech/badge/plot4gmns)](https://pepy.tech/project/plot4gmns) [![PyPI version](https://badge.fury.io/py/plot4gmns.svg)](https://badge.fury.io/py/plot4gmns) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)

**Authors:** Dr. Junhua Chen, Zanyang Cui, Xiangyong Luo

**Email:** cjh@bjtu.edu.cn, zanyangcui@outlook.com, luoxiangyong01@gmail.com

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Install](#install)
- [Features](#features)
- [Usage](#usage)
  - [Quickstart](#quickstart)
  - [Advance](#advance)
- [Contributing](#contributing)

## Introduction

To enable rapid transportation modeling and optimization, as traffic management researchers, we provide this free open-source tool for visualizing multimodal networks. Based on GMNS data format by [Zepha foundation](https://zephyrtransport.org/), plot4gmns is designed for reading and plotting multimodal data sets including transportation network files, demand and agent trace files.

## Requirements

- pandas
- shapely
- matplotlib
- numpy
- seaborn
- scipy
- chardet
- keplergl==0.3.2

## Install

```python
pip install plot4gmns
```

> Note
>
> - For Windows users, the _pip_ method might fail to install some dependencies. If errors occur when you try to install any of those dependencies, try instead to pip install their .whl files, which can be downloaded from the Unoffical Windows Binaries for [Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

## Features

* [X] **web-based network visualization**
* [X] **show networks in different modes**
* [X] **show network with given node types**
* [X] **show network by given link types**
* [X] **show network by given link attributes range**
* [X] **show network by link attributes distribution**
* [X] **show network with given POI types**
* [X] **show network by poi attributes distribution**
* [X] **show network demand matrix heatmap**
* [X] **show network demand OD**
* [X] ***Show only network elements of interest***
* [X] ***Show different networks on one diagram***
* [X] ***Set the drawing style***

## Usage

Before starting, you must have prepared network files, including node.csv, link.csv, poi.csv, demand.csv, and zone.csv. The [osm2gmns](https://github.com/asu-trans-ai-lab/OSM2GMNS) package will help you quickly obtain node, link, and poi data, and the[ grid2demand](https://github.com/asu-trans-ai-lab/grid2demand) package will help you obtain network demand and zone information.

### Quickstart

**Step 1: generate multimodal network**

```python
import plot4gmns as p4g
mnet=p4g.generate_multi_network_from_csv(r'./datasets')
```

> After executing the above command, you will get an Html file, as shown below. More visual operations are supported on the web site..

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/1674358532007.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 2: show networks in different modes**

```python
# draw 'all' modes network and save to png file
cf = p4g.show_network_by_modes(mnet=mnet)
# show the figure on the current window
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_mode.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
# show 'bike' mode network
cf = p4g.show_network_by_modes(mnet=mnet,modes=['bike'])
cf.show() # show the figure on the current window
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_bike_mode.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 3: show network with given node types**

```python
cf = p4g.show_network_by_node_types(mnet=mnet,ctrl_type=['traffic_signals','crossing'])
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_node_type.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 4: show network by given link types**

```python
# show network by given link types
cf = p4g.show_network_by_link_types(mnet=mnet,link_types=['secondary','footway'])
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_link_type.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 5: show network by given link attributes range**

```python
# show network by given link length range
cf = p4g.show_network_by_link_length(mnet=mnet,min_length=10,max_length=50)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_link_length.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
# show network by given link lane range
cf = p4g.show_network_by_link_lanes(mnet=mnet,min_lanes=1,max_lanes=3)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_link_lane.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
# show network by given link free speed range
cf = p4g.show_network_by_link_free_speed(mnet=mnet,min_free_speed=10,max_free_speed=40)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_link_free_speed.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 6: show network by link attributes distribution**

```python
# show network by link lane distribution
cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_link_lane_distribution.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
# show network by link capacity distribution
cf = p4g.show_network_by_link_capacity_distribution(mnet=mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_link_capacity_distribution.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
# show network by link free speed distribution
cf = p4g.show_network_by_link_free_speed_distribution(mnet=mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_link_free_speed_distribution.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 7: show network with given POI types**

```python
cf = p4g.show_network_by_poi_types(mnet=mnet,poi_type=['public','industrial'])
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_poi_type.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 8: show network by poi attributes distribution**

```python
# show network by poi attraction distribution
cf = p4g.show_network_by_poi_attraction_distribution(mnet=mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_poi_attraction_distribution.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
# show network by poi production distribution
cf = p4g.show_network_by_poi_production_distribution(mnet=mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_poi_production_distribution.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 9: show network demand matrix heatmap**

```python
cf = p4g.show_network_demand_matrix_heatmap(mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_demand_matrix_heatmap.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 10: show network demand OD**

```python
cf = p4g.show_network_by_demand_OD(mnet=mnet,load_network=True)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_demand_od.png?raw=true" width="800" height="600" alt=" "/><br/>

### Advance Usage

**Step 1: Show only network elements of interest**

The tool displays all elements by default, such as nodes, links, and POIs. If you want to display only the elements of interest, you can refer to the following example to modify the state of other elements before invoking the drawing command.

```python
# not show nodes
mnet.node_loaded = False
cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_link_lane_distribution2.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 2: Show different networks on one diagram**

By default, this tool will clear the original contents before drawing. If you want to draw different content on a graph, you can refer to the following example

```python
mnet.node_loaded = False
mnet.POI_loaded = False
cf = p4g.show_network_by_link_lane_distribution(mnet=mnet)
mnet.link_loaded = False
mnet.POI_loaded = True
cf = p4g.show_network_by_poi_attraction_distribution(mnet,fig_obj=cf)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_poi_attraction_distribution_2.png?raw=true" width="800" height="600" alt=" "/><br/>

**Step 3: Set the drawing style**

Users can refer to the following examples to adjust the color, size and other attributes of the image before drawing.

| parameter                             | Value                   | Description                      |
| ------------------------------------- | ----------------------- | -------------------------------- |
| mnet.style.figure_size                | tuple,(width,height)    | Image size                       |
| mnet.style.dpi                        | int                     | the resolution in dots per inch. |
| mnet.style.node_style.size            | int                     | node marker size                 |
| mnet.style.node_style.colors          | dict,{node_type:color}  | node color in different types    |
| mnet.style.node_style.markers         | dict,{node_type:marker} | node marker in different types   |
| mnet.style.link_style.linecolor       | str                     | link color                       |
| mnet.style.link_style.linewidth       | float                   | link width                       |
| mnet.style.poi_style.facecolor        | str                     | POI facecolor                    |
| mnet.style.poi_style.edgecolor        | str                     | POI edgecolor                    |
| mnet.style.demand_style.linecolor     | str                     | demand flow line color           |
| mnet.style.demand_style.linelinewidth | float                   | demand flow line width           |
| mnet.style.zone_style.linewidth       | float                   | zone grid line width             |
| mnet.style.zone_style.edgecolors      | str                     | zone grid edgecolors             |
| mnet.style.zone_style.fontsize        | int                     | zone label font size             |
| mnet.style.zone_style.fontcolor       | str                     | zone label font color            |

```python
mnet.style.node_style.size = 3
mnet.style.link_style.linecolor = 'green'
mnet.style.poi_style.facecolor = 'gray'
cf = p4g.show_network_by_modes(mnet=mnet)
cf.show()
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/docs/media/network_by_mode2.png?raw=true" width="800" height="600" alt=" "/><br/>

## Contributing

Feel free to dive in! [Open an issue](https://github.com/RichardLitt/standard-readme/issues).

## Contributors

[@PraiseC](https://github.com/PariseC)

[@xyluo25](https://github.com/xyluo25)

## Changelog

2023-01-25 -- v0.1.1:

Support web-based network visualization([Kepler.gl](https://github.com/keplergl/kepler.gl))

### TODO LIST

1. [ ] Add OD 3D visualization
