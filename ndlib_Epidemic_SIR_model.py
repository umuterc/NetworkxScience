import ndlib.models.epidemics as ep
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
import ndlib.models.ModelConfig as mc
from bokeh.io import output_notebook, show
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
import matplotlib.animation as animation



num_of_iteration=30
num_of_nodes=100
infected_population=0.01


g=nx.barabasi_albert_graph(num_of_nodes,4)

model = ep.SIRModel(g)


config = mc.Configuration()
config.add_model_parameter('beta', 0.4)
config.add_model_parameter('gamma', 0.2)
config.add_model_parameter("fraction_infected", infected_population)
model.set_initial_status(config)


iterations = model.iteration_bunch(num_of_iteration)


trends = model.build_trends(iterations)
pos = nx.spring_layout(g)

viz=DiffusionTrend(model,trends)
p=viz.plot(width=400,height=400)
nx.draw(g,pos=pos)
show(p)

#colors
color_map=["green"]*num_of_nodes


#change colors
def change_color(i,iterations,color_map):
    plt.clf()
    plt.ion()
    temp_dict=iterations[i]["status"]
    for j in temp_dict:
        if(temp_dict[j]==1):
            color_map[j]="red"
        else:
            color_map[j]="green"
    
    nx.draw(g,node_color=color_map,pos=pos,with_labels=True)
    plt.show()
    

for i in range(num_of_iteration):
    change_color(i,iterations,color_map)






