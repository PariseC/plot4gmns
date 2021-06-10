import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.collections import PolyCollection
from scipy.interpolate import griddata as gd
from matplotlib.lines import Line2D


def plotNetbySelectedObj(node_coords,link_coords,poi_coords,savefig):
    fig, ax = plt.subplots(figsize=(10,8))
    # plot network nodes
    ax.scatter(node_coords[0], node_coords[1], marker='o', c='red', s=10,zorder=1)
    # plot network links
    ax.add_collection(LineCollection(link_coords, colors='orange', linewidths=1,zorder=2))
    # plot network pois
    if len(poi_coords):
        coll = PolyCollection(poi_coords, alpha=0.7,zorder=0)
        ax.add_collection(coll)
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()
    #save fig
    if savefig:
        try:
            figname=savefig['filename'] if 'filename' in savefig.keys() else 'mode_network.png'
            dpi=savefig['dpi'] if 'dpi' in savefig else 300
            fig.savefig(figname,dpi=dpi,bbox_inches='tight')
        except Exception as e:
            print(e)
def plotNetbyNodeAttrRange(node_coords, link_coords,poi_coords,attr,value,savefig):
    fig, ax = plt.subplots(figsize=(10, 8))
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
    ax.legend(proxies, labels,loc='upper right')
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()
    # save fig
    if savefig:
        try:
            figname = savefig['filename'] if 'filename' in savefig.keys() else 'node_attr_range.png'
            dpi = savefig['dpi'] if 'dpi' in savefig else 300
            fig.savefig(figname, dpi=dpi, bbox_inches='tight')
        except Exception as e:
            print(e)
def plotNetbyLinkAttrRange(node_coords, link_coords,poi_coords,attr,value,savefig):
    fig, ax = plt.subplots(figsize=(10, 8))
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
    ax.legend(proxies, ['%s:%.4f'%(attr,min(value)), '%s:%.4f'%(attr,max(value))],loc='upper right')
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()
    # save fig
    if savefig:
        try:
            figname = savefig['filename'] if 'filename' in savefig.keys() else 'link_attr_range.png'
            dpi = savefig['dpi'] if 'dpi' in savefig else 300
            fig.savefig(figname, dpi=dpi, bbox_inches='tight')
        except Exception as e:
            print(e)
def plotNetbyZonePoiAttrDensity(poi_coords,value,savefig):
    fig, ax = plt.subplots(figsize=(10,8))
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
    # save fig
    if savefig:
        try:
            figname = savefig['filename'] if 'filename' in savefig.keys() else 'zone_poi_attr_density.png'
            dpi = savefig['dpi'] if 'dpi' in savefig else 300
            fig.savefig(figname, dpi=dpi, bbox_inches='tight')
        except Exception as e:
            print(e)

def plotNetbyZoneDeamndHeat(network,demand,annot,savefig):

    max_vol = np.max(demand.reshape(1, -1))
    min_vol = np.min(demand.reshape(1, -1))
    labels = [str(i + 1) for i in range(network.number_of_zone)]
    data = pd.DataFrame(demand, index=labels, columns=labels)
    fig=sns.heatmap(data=data, vmax=max_vol, vmin=min_vol, annot=annot, cmap='jet')
    # set axis
    plt.xlabel('to_zone_id')
    plt.ylabel('from_zone_id')
    plt.tight_layout()
    # show fig
    plt.show()
    # save fig
    if savefig:
        try:
            figname = savefig['filename'] if 'filename' in savefig.keys() else 'zone_demand_density.png'
            dpi = savefig['dpi'] if 'dpi' in savefig else 300
            scatter_fig = fig.get_figure()
            scatter_fig.savefig(figname, dpi=dpi, bbox_inches='tight')
        except Exception as e:
            print(e)
def plotNetbyZoneDemandFlow(network,demand_line,values, zone_grid, zone_labels,annot,bg,savefig):
    fig, ax = plt.subplots(figsize=(10, 8))
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
    # save fig
    if savefig:
        try:
            figname = savefig['filename'] if 'filename' in savefig.keys() else 'zone_demand_flow.png'
            dpi = savefig['dpi'] if 'dpi' in savefig else 300
            fig.savefig(figname, dpi=dpi, bbox_inches='tight')
        except Exception as e:
            print(e)

def plotNetByAgentTrace(node_coords,link_coords,poi_coords,trace_node_coords,trace_route_coords,savefig):
    fig, ax = plt.subplots(figsize=(10, 8))
    # plot network nodes
    ax.scatter(node_coords[0], node_coords[1], marker='o', c='red', s=10, zorder=1)
    # plot network links
    ax.add_collection(LineCollection(link_coords, colors='orange', linewidths=1, zorder=2))
    # plot network pois
    if len(poi_coords):
        coll = PolyCollection(poi_coords, alpha=0.7, zorder=0)
        ax.add_collection(coll)
    # plot trace node sequence
    ax.scatter(trace_node_coords[0],trace_node_coords[1], marker='o', c='black', s=15, zorder=2)
    # plot trace route
    ax.add_collection(LineCollection(trace_route_coords, colors='blue', linewidths=2, zorder=2))
    # set axis
    ax.autoscale_view()
    plt.xlabel('x_coord')
    plt.ylabel('y_coord')
    plt.tight_layout()
    # show fig
    plt.show()
    # save fig
    if savefig:
        try:
            figname = savefig['filename'] if 'filename' in savefig.keys() else 'agent_trace.png'
            dpi = savefig['dpi'] if 'dpi' in savefig else 300
            fig.savefig(figname, dpi=dpi, bbox_inches='tight')
        except Exception as e:
            print(e)