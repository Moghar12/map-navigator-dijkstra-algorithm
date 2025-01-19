import osmnx as ox
import networkx as nx
import folium


def find_and_plot_shortest_path_satellite(place, start_coords, end_coords, output_file="shortest_path.html"):
    """
    Trouve et trace le chemin le plus court entre deux points sur une carte satellite.

    :param place: zone à charger depuis OpenStreetMap
    :param start_coords: (latitude, longitude) du point de départ
    :param end_coords: (latitude, longitude) du point d'arrivée
    :param output_file: nom du fichier de sortie HTML
    """
    # Télécharger le graphe routier pour la zone spécifiée
    print("Téléchargement du graphe routier...")
    graph = ox.graph_from_place(place, network_type='drive')
    
    # Trouver les nœuds les plus proches pour les points de départ et d'arrivée
    print("Recherche des nœuds les plus proches...")
    start_node = ox.distance.nearest_nodes(graph, start_coords[1], start_coords[0])
    end_node = ox.distance.nearest_nodes(graph, end_coords[1], end_coords[0])
    
    # Calculer le chemin le plus court en termes de distance
    print("Calcul du chemin le plus court...")
    shortest_path = nx.shortest_path(graph, source=start_node, target=end_node, weight='length')
    
    # Extraire les coordonnées des nœuds du chemin
    route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in shortest_path]
    
    # Créer une carte centrée sur le point de départ
    print("Création de la carte...")
    route_map = folium.Map(location=start_coords, zoom_start=13, tiles="Stamen Terrain")
    
    # Ajouter le chemin sur la carte
    folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.7).add_to(route_map)
    
    # Ajouter un marqueur pour le point de départ
    folium.Marker(location=start_coords, popup="Point de départ", icon=folium.Icon(color="green")).add_to(route_map)
    
    # Ajouter un marqueur pour le point d'arrivée
    folium.Marker(location=end_coords, popup="Point d'arrivée", icon=folium.Icon(color="red")).add_to(route_map)
    
    # Sauvegarder la carte dans un fichier HTML
    print(f"Sauvegarde de la carte dans {output_file}...")
    route_map.save(output_file)
    print("Carte sauvegardée avec succès !")
    return route_map

# Zone à charger (Kénitra et Rabat)
place = "Kénitra, Morocco"

# Coordonnées des points (latitude, longitude)
start_coords = (34.24573, -6.58878)  # Université Ibn Tofail, Kénitra
end_coords = (33.99893, -6.84255)    # Université Mohammed V, Rabat

# Trouver et afficher le chemin sur une carte satellite
try:
    map_result = find_and_plot_shortest_path_satellite(place, start_coords, end_coords, "shortest_path.html")
    print("Ouvrez le fichier 'shortest_path.html' dans un navigateur pour voir la carte.")
except Exception as e:
    print("Erreur :", e)
