require(igraph)
edges <- read.csv("/home/caroline/Documents/projects/probable-barnacle/finfish_freshwater_edges.csv")
vertices <- read.csv("/home/caroline/Documents/projects/probable-barnacle/finfish_freshwater_edges.csv")
g <- graph_from_data_frame(edges,directed=FALSE,vertices=NULL)
layout <- layout.kamada.kawai(g)
plot(g, layout=layout, vertex.color= V(g)$Group_Color)
         