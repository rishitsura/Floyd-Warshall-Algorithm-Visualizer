import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class FloydWarshallVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Floyd-Warshall Algorithm Visualizer")

        self.graph_label = tk.Label(root, text="Enter the graph matrix (use 'inf' for unreachable nodes):")
        self.graph_label.pack()

        self.graph_entry = tk.Text(root, height=5, width=30)
        self.graph_entry.pack()

        self.visualize_button = tk.Button(root, text="Visualize Floyd-Warshall Algorithm", command=self.visualize)
        self.visualize_button.pack()

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack()

    def visualize(self):
        try:
            graph_text = self.graph_entry.get("1.0", tk.END)
            graph_lines = graph_text.strip().split('\n')
            graph = [[float('inf') if x == 'inf' else float(x) for x in line.split()] for line in graph_lines]

            self.validate_graph(graph)

            self.show_result(self.floyd_warshall(graph))

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid matrix.")

    def floyd_warshall(self, graph):
        n = len(graph)
        g = nx.DiGraph()

        for i in range(n):
            for j in range(n):
                if graph[i][j] != float('inf'):
                    g.add_edge(i + 1, j + 1, weight=graph[i][j])

        fig, axes = plt.subplots(1, n + 1, figsize=(n * 5, 5))
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        pos = nx.circular_layout(g)

        # Draw initial graph with labels
        nx.draw(g, pos, with_labels=True, font_weight='bold', ax=axes[0])
        labels = {i + 1: str(i + 1) for i in range(n)}
        nx.draw_networkx_labels(g, pos, labels=labels, font_size=8, font_color='black', ax=axes[0])
        axes[0].set_title("Initial Graph")

        canvas.draw()
        self.root.update()
        plt.pause(2)  # Adjust the pause duration as needed

        for k in range(n):
            g_step = nx.DiGraph()

            for i in range(n):
                for j in range(n):
                    if graph[i][k] + graph[k][j] < graph[i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
                        g_step.add_edge(i + 1, j + 1, weight=graph[i][j])

            # Display nodes sequentially
            for node in range(1, n + 1):
                nx.draw_networkx_nodes(g_step, pos, nodelist=[node], node_color='r', node_size=800, ax=axes[k + 1])
                nx.draw_networkx_labels(g_step, pos, labels={node: str(node)}, font_size=8, font_color='black', ax=axes[k + 1])
                canvas.draw()
                self.root.update()
                plt.pause(1)  # Pause for 1 second between nodes

            # Highlight connectivity
            for edge in g_step.edges():
                nx.draw_networkx_edges(g_step, pos, edgelist=[edge], edge_color='b', width=2, ax=axes[k + 1])
                canvas.draw()
                self.root.update()
                plt.pause(1)  # Pause for 1 second between edges

            axes[k + 1].set_title(f"After Iteration k={k + 1}")

            canvas.draw()
            self.root.update()
            plt.pause(5)  # Pause for 5 seconds between iterations

        return graph

    def validate_graph(self, graph):
        n = len(graph)
        for i in range(n):
            if len(graph[i]) != n:
                raise ValueError("Invalid input. Matrix should be square.")

    def show_result(self, result):
        result_str = "\n".join([" ".join([str(int(val)) if val != float('inf') else 'inf' for val in row]) for row in result])
        messagebox.showinfo("Result", f"Floyd-Warshall Result:\n{result_str}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FloydWarshallVisualizer(root)
    root.mainloop()
