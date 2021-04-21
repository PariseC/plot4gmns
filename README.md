# Plot4GMNS: A visualization tool for visualizing and analyzing transportation network based on GMNS data format

**Authors :** Dr.Junhua Chen, Zanyang Cui

**Email :** cjh@bjtu.edu.cn, zanyangcui@outlook.com
## Introduction
As railroad management researchers, we hope to offer free tools for visualizing multimodal networks in broader areas of transportation system modeling and optimization. 
Plot4GMNS is an open-source transportation network data visualization and analysis tool based on GMNS data format. By taking advantage of OSM2GMNS and Grid2demand tools to obtain routable transportation network and demand, Plot4GMNS aims to visualize and analyze the node, link, POI, agent, and zone data of the network.


## Installation
```python
pip install plot4gmns
```

## Simple Example
```python
>>>import plot4gmns as pg

"""Step 1: build network from csv files"""
>>>net=pg.readNetwork('./data')

"""Step 2: check valid network  attributes"""
>>>net.get_valid_node_attr_list() #node attributes
attr                          type                
ctrl_type                     int                 
activity_type                 str                 
production                    float               
attraction                    float  
>>>net.get_valid_link_attr_list() #link attributes
attr                          type                
length                        float               
lanes                         int                 
free_speed                    float               
capacity                      float               
link_type_name                str                 
allowed_uses                  str   
>>>net.get_valid_poi_attr_list() #poi attributes
attr                          type                
building                      str                 
activity_zone_id              int    
>>>net.get_valid_zone_id_list() #zone attributes
min zone id         max zone id         
1                   45      

"""Step 3: get network attributes value list"""
>>>pg.get_node_attr_value_list(net,'activity_type')
activity_type       number              
primary             240                 
motorway            19                  
tertiary            104                 
secondary           160                 
residential         21                  
poi                 1282                
unclassified        36                  
centroid node       45
>>>pg.get_link_attr_value_list(net,'link_type_name')
link_type_name      number              
primary             482                 
tertiary            295                 
motorway            22                  
secondary           381                 
residential         43                  
connector           2564  
>>>pg.get_poi_attr_value_list(net,'building')
building                      number              
yes                           999                 
courthouse                    1                   
place_of_worship              9                   
house                         5                   
commercial                    13                  
arts_centre                   1                   
office                        35 
...                           ...
>>>pg.get_zone_id_list(net)
zone_id             name                total_poi_count     total_production    total_attraction    
1                   A1                  96.0                844.0478253270337   684.8038331279233   
2                   A2                  44.0                742.3576762712639   668.437867088064    
3                   A3                  54.0                729.8692152026176   703.8141044522879   
4                   A4                  49.0                596.3070090494338   654.1352135049601   
5                   A5                  56.0                452.5258671580673   388.14464787057284  
...
"""Step 4: show network of different modes"""
>>>pg.showNetByAllMode(net) #all modes
```
![ ](https://github.com/PariseC/plot4gmns/blob/main/media/allmode.png?raw=true)

```python
"""Step 5: show network by node attribute"""
>>>pg.showNetByNodeAttr(net,{'activity_type':'primary'})
```

![ ](https://github.com/PariseC/plot4gmns/blob/main/media/node_activity_type.png?raw=true)

```python
"""Step 6: show network by link attribute"""
>>>pg.showNetByLinkAttr(net,{'link_type_name':'secondary'})
```
![ ](https://github.com/PariseC/plot4gmns/blob/main/media/link_link_type_name.png?raw=true)

```python
>>>pg.showNetByLinkFreeSpeed(net)
```
![ ](https://github.com/PariseC/plot4gmns/blob/main/media/link_free_speed.png?raw=true)

```python
"""Step 7 : show network by poi attribute"""
>>>pg.showNetByPOIAttr(net,{'activity_zone_id':(1,5)})
```
![ ](https://github.com/PariseC/plot4gmns/blob/main/media/poi_activity_zone_id.png?raw=true)

```python
>>>pg.showNetByPOIAttractionHeat(net)
```
![ ](https://github.com/PariseC/plot4gmns/blob/main/media/poi_attraction_heat.png?raw=true)
```python
"""Step 8: show network by zone attribute"""
>>>pg.showNetByZoneDemandHeat(net,annot=False)
```
![ ](https://github.com/PariseC/plot4gmns/blob/main/media/zone_demand_heat.png?raw=true)
```python
>>>pg.showNetByZoneDemandFlow(net,annot=True,bg=True)
```
![ ](https://github.com/PariseC/plot4gmns/blob/main/media/demand_flow.png?raw=true)
```python
>>>pg.showNetByZoneAgent(net,[(1,15),(16,5)])
```
![ ](https://github.com/PariseC/plot4gmns/blob/main/media/zone_agent.png?raw=true)
## User guide
Users can check the [user guide](https://github.com/PariseC/plot4gmns/tree/main/doc) for detialed introduction of plot4gmns.