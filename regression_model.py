import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression

# Génération d'un graphe simple
def create_graph():
    G = nx.DiGraph()
    edges = [
        (1, 2, 5),
        (2, 3, 10),
        (1, 3, 15),
        (3, 4, 10),
        (2, 4, 5)
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    return G

# Simulation de données pour un modèle de régression
def simulate_regression_data(graph):
    np.random.seed(42)
    features = []
    targets = []
    for u, v, data in graph.edges(data=True):
        features.append([u, v])  # Utilisation des nœuds source et cible comme caractéristiques
        targets.append(data['weight'] + np.random.normal(0, 2))  # Ajout d'un bruit aux poids réels
    return np.array(features), np.array(targets)

# Ajustement d'un modèle de régression pour prédire les poids
def train_model(features, targets):
    model = LinearRegression()
    model.fit(features, targets)
    return model

# Mise à jour des poids des arêtes en fonction des prédictions du modèle
def update_graph_weights(graph, model):
    for u, v, data in graph.edges(data=True):
        prediction = model.predict([[u, v]])
        data['weight'] = max(1, prediction[0])  # Assurer des poids positifs
    return graph

# Recherche du chemin le plus court avec l'algorithme de Dijkstra
def find_shortest_path(graph, source, target):
    return nx.shortest_path(graph, source=source, target=target, weight='weight')

# Pipeline principal
def main():
    graph = create_graph()
    features, targets = simulate_regression_data(graph)
    model = train_model(features, targets)
    updated_graph = update_graph_weights(graph, model)
    shortest_path = find_shortest_path(updated_graph, source=1, target=4)
    print("Chemin le plus court :", shortest_path)

if __name__ == "__main__":
    main()





