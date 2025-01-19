import osmnx as ox
import networkx as nx
import openai

openai.api_key = "#"

def get_coordinates(city):
    return ox.geocode(city)

def generate_html_with_openai(start_city, end_city, path_coordinates):
    prompt = f"""
Crée une page HTML interactive utilisant Leaflet.js pour afficher le chemin entre {start_city} et {end_city}.
Le chemin doit être tracé avec les coordonnées suivantes : {path_coordinates}.
Ajoute des marqueurs pour le point de départ et d'arrivée et centre la carte pour englober tout le trajet.
"""
    r = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un assistant qui génère du code HTML pour des cartes interactives."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0
    )
    return r['choices'][0]['message']['content']

def get_shortest_path_and_generate_map(start_city, end_city, output_file="itineraire.html"):
    s = get_coordinates(start_city)
    e = get_coordinates(end_city)
    if not s or not e:
        return
    a = min(s[0], e[0])
    b = max(s[0], e[0])
    c = min(s[1], e[1])
    d = max(s[1], e[1])
    p = 0.2
    a -= p
    b += p
    c -= p
    d += p
    g = ox.graph_from_bbox(b, a, d, c, network_type='drive')
    sn = ox.distance.nearest_nodes(g, s[1], s[0])
    en = ox.distance.nearest_nodes(g, e[1], e[0])
    if not nx.has_path(g, sn, en):
        return
    sp = nx.shortest_path(g, source=sn, target=en, weight="length")
    pc = [(g.nodes[n]['y'], g.nodes[n]['x']) for n in sp]
    h = generate_html_with_openai(start_city, end_city, pc)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(h)

if __name__ == "__main__":
    s = input("Entrez le nom de la ville de départ : ")
    e = input("Entrez le nom de la ville d'arrivée : ")
    get_shortest_path_and_generate_map(s, e)
