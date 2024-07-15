# Floyd-Warshall Algorithm Visualizer

This project is a graphical user interface (GUI) application for visualizing the Floyd-Warshall algorithm, implemented in Python using the Tkinter library. The Floyd-Warshall algorithm is used to find the shortest paths between all pairs of nodes in a weighted graph.

## Features

- Input a graph as an adjacency matrix.
- Visualize the step-by-step execution of the Floyd-Warshall algorithm.
- Interactive and user-friendly interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- The following Python libraries:
  - `tkinter`
  - `networkx`
  - `matplotlib`

## Installation

1. Install the required libraries:
    ```sh
    pip install networkx matplotlib
    ```

## Usage

1. Run the script:
    ```sh
    python FloydWarshallVisualizer.py
    ```

2. Enter the graph matrix in the provided text box. Use `inf` for unreachable nodes. Example:
    ```
    0 3 inf
    2 0 inf
    inf 7 0
    ```

3. Click on the "Visualize Floyd-Warshall Algorithm" button to start the visualization.

## Example

Below is an example of how the interface looks and functions:

1. Enter your graph matrix:

    ```
    0 3 inf
    2 0 inf
    inf 7 0
    ```

2. Click the "Visualize Floyd-Warshall Algorithm" button to see the visualization.

![image](https://github.com/user-attachments/assets/8c75e495-5436-49a1-95ac-47eaef435ade)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
