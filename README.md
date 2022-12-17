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

## Simple Example

```python
>>>import plot4gmns as pg

"""Step 1: Reading network files"""
net=pg.readNetwork('./data')

"""Step 2: Visualizing network of different modes"""
# show all modes network
pg.showNetByAllMode(net)
# show auto mode network
pg.showNetByAutoMode(net)
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/all_mode.png?raw=true" width="800" height="600" alt="all modes network"/><br/>

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/auto_mode.png?raw=true" width="800" height="600" alt="auto mode network"/><br/>

```python
"""Step 3: Visualizing network by node attributes"""
# show network by node ‘ctrl_type’ for 1 as signalized intersection
pg.showNetByNodeAttr(net,{'ctrl_type':1})
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/node_ctrl_type_1.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
"""Step 4: Visualizing network by link attributes"""
# show network by given link type names
pg.showNetByLinkAttr(net,{'link_type_name':'secondary'})
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/link_type_secondary.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
"""Step 5: Visualizing network by POI attributes"""
# show network by given POI building types
pg.showNetByPOIAttr(net,{'building':'parking'})
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/poi_parking.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
"""Step 6: Visualizing network by zone attributes"""
# show network by zone demand traces
pg.showNetByZoneDemandFlow(net)
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/zone_demand_flow.png?raw=true" width="800" height="600" alt=" "/><br/>

```python
"""Step 7: Visualizing network by agent traces"""
pg.showNetByAgentTrace(net,agent_id=1)
```

<img src="https://github.com/PariseC/plot4gmns/blob/main/media/zone_trace.png?raw=true?raw=true" width="800" height="600" alt=" "/><br/>

## User guide

Users can check the [user guide](https://github.com/PariseC/plot4gmns/tree/main/doc) for detialed introduction of plot4gmns.
