import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.collections import PolyCollection
from scipy.interpolate import griddata as gd
from matplotlib.lines import Line2D
from .setting import *

def plotNetbySelectedObj(node_coords,link_coords,poi_coords):
    fig, ax = plt.subplots(figsize=(13,10))
    # plot network nodes
    ax.scatter(node_coords[0], node_coords[1], marker='o', c='red', s=10,zorder=1)
    # plot network links
    ax.add_collection(LineCollection(link_coords, colors='orange', linewidths=1,zorder=2))
    # plot network pois
    coll = PolyCollection(poi_coords, alpha=0.7,zorder=0)
    ax.add_collection(coll)
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()
def plotNetbyNodeAttrRange(node_coords, link_coords,poi_coords,attr,value):
    fig, ax = plt.subplots(figsize=(13, 10))
    # plot network nodes
    max_v,min_v=max(value),min(value)
    s=np.array(value)/max_v*95+5
    ax.scatter(node_coords[0], node_coords[1], marker='o', c='red', s=s,zorder=2)
    # plot network links
    ax.add_collection(LineCollection(link_coords, colors='orange', linewidths=1, zorder=1))
    # plot network pois
    coll = PolyCollection(poi_coords, alpha=0.5, zorder=0)
    ax.add_collection(coll)
    # add legend
    proxies = []
    labels = []
    min_index = value.index(min_v)
    ax2 = ax.scatter(node_coords[0][min_index], node_coords[1][min_index], marker='o', c='red', s=5, zorder=2)
    proxies.append(ax2)
    labels.append('%s:%.4f' %(attr,min_v))
    max_index = value.index(max_v)
    ax1 = ax.scatter(node_coords[0][max_index], node_coords[1][max_index], marker='o', c='red', s=100, zorder=2)
    proxies.append(ax1)
    labels.append('%s:%.4f' % (attr, max_v))
    ax.legend(proxies, labels)
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()
def plotNetbyLinkAttrRange(node_coords, link_coords,poi_coords,attr,value):
    fig, ax = plt.subplots(figsize=(13, 10))
    # plot network nodes
    ax.scatter(node_coords[0], node_coords[1], marker='o', c='red', s=10, zorder=2)
    # plot network links
    max_v, min_v = max(value), min(value)
    w= np.array(value) / max_v *4.5 + 0.5
    ax.add_collection(LineCollection(link_coords, colors='orange', linewidths=w, zorder=1))
    # plot network pois
    coll = PolyCollection(poi_coords, alpha=0.5, zorder=0)
    ax.add_collection(coll)
    # add legend
    proxies = [Line2D([0, 1], [0, 1], color='orange', linewidth=0.5),
               Line2D([0, 1], [0, 1], color='orange', linewidth=5)]
    ax.legend(proxies, ['%s:%.4f'%(attr,min(value)), '%s:%.4f'%(attr,max(value))])
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()
def plotNetbyPoiAttrHeat(poi_coords,value):
    fig, ax = plt.subplots(figsize=(13,10))
    # plot network pois
    coll = PolyCollection(poi_coords, array=np.array(value), cmap='jet', edgecolors='none')
    ax.add_collection(coll)
    fig.colorbar(coll, ax=ax)
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()
def plotNetbyPoiAttrContour(network,poi_coords,value):
    fig, ax = plt.subplots(figsize=(13, 10))
    # plot network pois
    coll = PolyCollection(network.poi_coords, alpha=0.5, zorder=0)
    ax.add_collection(coll)
    # interpolate unstructured D-D data
    poi_coords = np.array(poi_coords).reshape(-1, 2)
    xi_coords = np.linspace(network.min_lng, network.max_lng, 200)
    yi_coords = np.linspace(network.min_lat, network.max_lat, 200)
    xi_coords, yi_coords = np.meshgrid(xi_coords, yi_coords)
    zi = gd((poi_coords), value, (xi_coords, yi_coords), method='linear')

    # plot contour with col value
    contour = ax.contour(xi_coords, yi_coords, zi, alpha=0.8, levels=15, cmap='jet',zorder=1)
    # show line label
    plt.clabel(contour, fontsize=8, colors=('k', 'r'), fmt='%.2f')
    # show bar
    plt.colorbar(contour, ax=ax, shrink=0.8)
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    plt.show()
def plotNetbyZoneDeamndHeat(network,demand,annot):

    max_vol = np.max(demand.reshape(1, -1))
    min_vol = np.min(demand.reshape(1, -1))
    labels = [str(i + 1) for i in range(network.number_of_zone)]
    data = pd.DataFrame(demand, index=labels, columns=labels)
    sns.heatmap(data=data, vmax=max_vol, vmin=min_vol, annot=annot, cmap='jet')
    # set axis
    plt.xlabel('to_zone_id')
    plt.ylabel('from_zone_id')
    plt.tight_layout()
    # show fig
    plt.show()
def plotNetbyZoneDemandFlow(network,demand_line,values, zone_grid, zone_labels,annot,bg):
    fig, ax = plt.subplots(figsize=(13, 10))
    if bg:
        # plot network links
        ax.add_collection(LineCollection(network.link_coords, colors='black', linewidths=1, zorder=1))
        # plot network pois
        coll = PolyCollection(network.poi_coords, alpha=0.5, zorder=0)
        ax.add_collection(coll)
    # plot network demand flow
    w=np.array(values)/max(values)*4.5+0.5
    ax.add_collection(LineCollection(demand_line, colors='orange', linewidths=w, zorder=2))

    # plot network zone
    coll = PolyCollection(zone_grid,facecolors='none',linewidths=5,edgecolors='olive', zorder=0)
    ax.add_collection(coll)
    if annot:
        for label in zone_labels:
            plt.annotate(str(label[0]), xy=(label[1],label[2]),xytext=(label[1],label[2]), weight='bold',
                         color='b', fontsize=14)
    # add legend
    proxies = [Line2D([0, 1], [0, 1], color='orange', linewidth=0.5),
               Line2D([0, 1], [0, 1], color='orange', linewidth=5)]
    ax.legend(proxies, ['%s:%.4f' % ('volume', min(values)), '%s:%.4f' % ('volume', max(values))])
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    plt.show()
def plotNetbyZoneAgent(network,agent_coords,agent_num,zone_grid,zone_labels):
    fig, ax = plt.subplots(figsize=(13, 10))
    # plot network links
    ax.add_collection(LineCollection(network.link_coords, colors='orange', linewidths=1, zorder=1))
    # plot network pois
    coll = PolyCollection(network.poi_coords, alpha=0.5, zorder=0)
    ax.add_collection(coll)
    # plot zone agent
    ax.add_collection(LineCollection(agent_coords, colors='brown', linewidths=1.5, zorder=1))
    # plot zone grid
    coll = PolyCollection(zone_grid, facecolors='none', linewidths=5, edgecolors='olive', zorder=0)
    ax.add_collection(coll)
    # label zone grid name
    for label in zone_labels:
        plt.annotate(str(label[0]), xy=(label[1], label[2]), xytext=(label[1], label[2]), weight='bold',
                     color='b', fontsize=14)
    # add legend
    proxies=[]
    labels=[]
    for k,v in agent_num.items():
        proxies.append(Line2D([0, 1], [0, 1], color='brown', linewidth=1.5))
        labels.append(str(k)+'agents:%d'%v)
    ax.legend(proxies, labels)
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    plt.show()








def plotNetBySelectedAttributeRange(node_coords,link_coords,poi_coords,value,ranges):
    fig, ax = plt.subplots(figsize=(13,10))
    # plot network nodes
    ax.scatter(node_coords[0], node_coords[1], marker='o', c='red', s=10,zorder=1)
    # plot network links
    # ax.add_collection(LineCollection(link_coords,array=link_free_speed,linewidths=1.5, cmap='jet',zorder=0))
    ax.add_collection(LineCollection(link_coords, colors='orange', linewidths=value, zorder=2))
    # plot network pois
    coll = PolyCollection(poi_coords, alpha=0.5,zorder=0)
    ax.add_collection(coll)
    # set legend
    proxies = [Line2D([0, 1], [0, 1],color='orange', linewidth=min(value)),
               Line2D([0, 1], [0, 1],color='orange',linewidth=max(value))]
    ax.legend(proxies, ['%.2f'%ranges[0],'%.2f'%ranges[1]])
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()

def plotNetByLinkTypes(node_coords,link_classifier_coords,poi_coords):
    fig, ax = plt.subplots(figsize=(13,10))
    # plot network nodes
    ax.scatter(node_coords[0], node_coords[1], marker='o', c='red', s=10,zorder=1)
    # plot network links
    proxies=[]
    labels=[]
    for classifier,link_coords in link_classifier_coords.items():
        link_ax=ax.add_collection(LineCollection(link_coords, colors=link_type_color_dict[classifier], linewidths=1.5,
                                                 zorder=2))
        proxies.append(link_ax)
        labels.append(classifier)
    # plot network pois
    coll = PolyCollection(poi_coords, alpha=0.5,zorder=0)
    ax.add_collection(coll)
    # set legend
    ax.legend(proxies,labels)
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()

def plotNetByNodeCtrlTypes(node_classifier_coords,link_coords,poi_coords):
    fig, ax = plt.subplots(figsize=(13,10))
    # plot network nodes
    proxies = []
    labels = []
    for classifier,node_coord in node_classifier_coords.items():
        node_ax=ax.scatter(node_coord[0], node_coord[1], marker='o', c=node_ctrl_color_dict[classifier], s=10,zorder=2)
        proxies.append(node_ax)
        labels.append('ctrl-'+str(classifier))

    # plot network links
    ax.add_collection(LineCollection(link_coords, colors='orange', linewidths=1.5, zorder=1))
    # plot network pois
    coll = PolyCollection(poi_coords, alpha=0.5,zorder=0)
    ax.add_collection(coll)
    # set legend
    ax.legend(proxies, labels)
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()