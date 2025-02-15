import networkx as nx

class Executor:
    def __init__(self, ast):
        self.ast = ast
        self.structure_graph = nx.Graph()

    def add_motifs(self):
        """Add motifs as nodes in the graph."""
        for motif in self.ast["sections"].get("STRUCTURE", []):
            self.structure_graph.add_node(motif, type=motif[:3])  # Store type as first 3 chars
    
    def add_linkages(self):
        """Create edges between motifs based on linkages."""
        for linkage in self.ast["sections"].get("LINKAGES", []):
            if isinstance(linkage, dict):
                linkage_name, connected_motifs = list(linkage.items())[0]
                self.structure_graph.add_edge(*connected_motifs, type=linkage_name)

    def execute(self):
        """Run the execution pipeline."""
        self.add_motifs()
        self.add_linkages()
        return self.structure_graph  # Return the graph for visualization or further processing

# Example usage
executor = Executor(ast)
structure_graph = executor.execute()

# Print graph details
print("Nodes (Motifs):", structure_graph.nodes(data=True))
print("Edges (Linkages):", structure_graph.edges(data=True))
