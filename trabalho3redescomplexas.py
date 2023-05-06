import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

def plotaComunidades(comunidades,G,colors):
    pos = nx.spring_layout(G)  # Layout para posicionar os nós
    for i, comunidade in enumerate(comunidades):
        nx.draw_networkx_nodes(G, pos, nodelist=list(comunidade), node_color=colors[i]) #Cada comunidade será retratada por uma cor diferente, seguindo a ordem que as mesmas aparecem na lista comunidades.
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()

# Grafo das Famílias Florentinas
G = nx.florentine_families_graph()
# Cria uma lista de comunidades geradas através do algorítmo de louvain.
colors = ['g', 'b', 'r', 'y']  # Quatro cores diferentes para as comunidades
comunidades = list(nx.community.louvain_communities(G))
plotaComunidades(comunidades,G,colors)
#Utilizando o algorítmo de girvan_newman
comunidadesGN = nx.community.girvan_newman(G)
comunidades= sorted(next(comunidadesGN))
#Utilizando Asynchronous Fluid Communities algorithm
plotaComunidades(comunidades,G,colors)
comunidades= nx.community.asyn_fluidc(G, k=4)#O parametro k indica a quantidade de comunidades que queremos gerar
plotaComunidades(comunidades,G,colors)
