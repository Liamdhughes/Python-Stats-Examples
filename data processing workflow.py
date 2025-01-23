import matplotlib.pyplot as plt
import networkx as nx

# Define the steps
steps = [
    "Input Data (Raw Dataset)",
    "Step 1: Handle Missing Values",
    "Step 2: Normalise Features",
    "Step 3: Address Class Imbalance",
    "Output Data (Preprocessed Dataset)"
]

# Create a directed graph
workflow = nx.DiGraph()
for i in range(len(steps) - 1):
    workflow.add_edge(steps[i], steps[i + 1])

# Draw the diagram
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(workflow, seed=42)
nx.draw(workflow, pos, with_labels=True, node_size=3000, node_color="lightblue",
        font_size=10, font_weight="bold", edge_color="gray", arrowsize=20)
plt.title("Data Preprocessing Workflow")
plt.show()
