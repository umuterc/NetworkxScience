import numpy as np
from matplotlib import pyplot as plt


NUM_NODES=100


arr=np.random.random_integers(0,1,(NUM_NODES,NUM_NODES))
arr=np.tril(arr,-1)+np.tril(arr,-1).T

node_con=np.zeros(NUM_NODES,dtype=np.int)

count=np.zeros(NUM_NODES,dtype=np.int)
count[0]=NUM_NODES

for i in range(0,NUM_NODES):
    for j in range(i+1,NUM_NODES):
        if arr[i][j]==1:
            node_con[i]+=1
            node_con[j]+=1

            count[node_con[i]]+=1
            count[node_con[i]-1]-=1

            count[node_con[j]]+=1
            count[node_con[j]-1]-=1

linkes=np.linspace(0,NUM_NODES-1,NUM_NODES,dtype=np.int)
print(arr)
print(count)

plt.figure(1)
plt.bar(linkes,count/NUM_NODES)
plt.figure(2)
plt.plot(linkes,count/NUM_NODES)
plt.show()
