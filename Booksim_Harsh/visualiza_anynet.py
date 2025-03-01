import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

file_path = "/mnt/data/anynet_HAIMA"  # Path to the file

routers = []
connections = []

with open(file_path, "r") as file:
    lines = file.readlines()

    for line in lines[:100]:
        router, node = map(int, line.split()[1::2])
        routers.append((router, node))

    for line in lines[100:]:
        parts = line.split()
        parts = [p for p in parts if p.isdigit()]  # Only numeric entries
        if len(parts) >= 2:
            for i in range(0, len(parts)-1, 2):  # Create connections for pairs of routers
                router1, router2 = int(parts[i]), int(parts[i+1])
                connections.append((router1, router2))

G = nx.Graph()
G.add_edges_from(connections)

num_routers = len(set([router for connection in connections for router in connection]))
grid_size = int(np.sqrt(num_routers))  

positions = {}
routers_set = set([router for connection in connections for router in connection])
for i, router in enumerate(routers_set):
    row = i // grid_size
    col = i % grid_size
    positions[router] = (col, row)

#Draw 
plt.figure(figsize=(10, 10))
nx.draw(G, pos=positions, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Router Network Visualization")
plt.show()
