import networkx as nx
import numpy as np
import collections
from matplotlib import pyplot as plt
from networkx.algorithms import community
import random


def colorization(communities):
    nodeList={}
    for i in communities:
        rgb=[random.random(),random.random(),random.random()]
        nodeList[i]=[rgb]

    return nodeList

def degreeDist(g,graph_name):
    d=g.degree()
    all_degrees=sorted([i[1] for i in d],reverse=True)
    degreeCounter=collections.Counter(all_degrees)
    deg,con=zip(*degreeCounter.items())
    plt.bar(deg,con,color='b')
    plt.title(str(graph_name)+" Degree Distrubution")
    plt.grid()
    plt.show()

#initilize numbers
num_of_nodes=100
g=nx.barabasi_albert_graph(num_of_nodes,1)


#call degreeDist function for network
degreeDist(g,graph_name="Main Network")


community_generator=community.greedy_modularity_communities(g)
c_seperate=[list(x) for x in community_generator]

#print number of communities
community_num=np.size(community_generator)
print("\nnumber of communities:\t"+str(len(c_seperate)))

#give name to communities in a dictionary
communities = {}
for j in range(community_num):
    communities['community'+str(j+1)]=c_seperate[j]
   

#print community chart
print("\ncommunity\t\t"+"community size\t\t"+"nodes in the community")
for key in communities:
    print(str(key)+"\t\t"+str(len(communities[key]))+"\t\t"+str(communities[key]))


#giving different colors to different communities
colors = colorization(communities)

#define positions of nodes
pos = nx.fruchterman_reingold_layout(g)
#define sizes of nodes by their degrees
sizes={}
d=g.degree()


for i in communities:
    # multiplying with 100 here to see nodes bigger if necesarry multiplier number can change
    sizes[i]=[d[s]*100 for s in communities[i]]

#drawing network
for i in communities:
    nx.draw_networkx_nodes(g,pos=pos,nodelist=communities[i],node_size=sizes[i] ,node_color=colors[i], label=str(i),edgecolors=(0.0,0.0,0.0))


nx.draw_networkx_edges(g,pos=pos)
nx.draw_networkx_labels(g,pos=pos)
plt.legend()
plt.title(label="Main Network")
plt.show()

#making subnetworks and drawing them with their degree distrubutions
subgraphs={}
for i in range(len(communities)):
    subgraphs["sub_network"+str(i+1)]=g.subgraph(communities["community"+str(i+1)])
    
    nx.draw(subgraphs["sub_network"+str(i+1)],pos=pos,node_size=sizes["community"+str(i+1)],node_color=colors["community"+str(i+1)],with_labels=True,edgecolors=(0.0,0.0,0.0))
    plt.title(label="Subnetwork "+str(i+1))
    plt.show()
    degreeDist(subgraphs["sub_network"+str(i+1)],graph_name="Subnetwork "+str(i+1))

