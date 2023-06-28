import matplotlib.pyplot as plt
import networkx as nx
from random import sample


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        current = self.root
        while True:
            parent = current
            if key < current.key:
                current = current.left
                if current is None:
                    parent.left = Node(key)
                    return
            elif key >= current.key:
                current = current.right
                if current is None:
                    parent.right = Node(key)
                    return

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        if not node:
            print(f"klucza {key} nie ma w drzewie!")
        elif node.key == key:
            print(f"znaleziono klucz {key} w drzewie!")
        elif node.key > key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        self._delete(key, self.root)

    def _delete(self, key, node):
        if not node:
            return None
        elif key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                min_node = self.find_min(node.right)
                node.key = min_node.key
                node.right = self._delete(min_node.key, node.right)
        return node

    def height(self):
        if self.root is None:
            return 0
        queue = [self.root]
        height = 0
        while queue:
            node_count = len(queue)
            if node_count > 0:
                height += 1
            while node_count > 0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                node_count -= 1
        return height

    def clean(self):
        self.root = None

    def print(self):
        self._print(self.root)

    def _print(self, node, level=0):
        if node is not None:
            self._print(node.right, level + 1)
            print(" " * 6 * level + str(node.key) + " <")
            self._print(node.left, level + 1)

    def draw(self, filename, count=20):
        graph = nx.Graph()

        self._add_to_graph(graph, count)
        pos = self._calculate_node_positions(self.root, 0, 0, count * 100)

        fig_width = count * 2
        fig_height = count

        plt.figure(figsize=(fig_width, fig_height))
        nx.draw_networkx(
            graph, pos=pos, with_labels=True, node_color="#90EE90", font_size=18
        )

        plt.savefig(filename, bbox_inches="tight")
        # plt.show()
        plt.close("all")

    def _add_to_graph(self, graph, count):
        queue = [(self.root, 0)]

        curr_level = 0
        level_nodes = 0

        while queue and count > 0:
            node, level = queue.pop(0)

            if level != curr_level:
                curr_level = level
                level_nodes = 0

            level_nodes += 1

            graph.add_node(node.key)

            if node != self.root:
                graph.add_edge(node.key, node.parent.key)

            if node.left:
                node.left.parent = node
                queue.append((node.left, level + 1))

            if node.right:
                node.right.parent = node
                queue.append((node.right, level + 1))

            count -= 1

    def _calculate_node_positions(self, node, x, y, distance_x):
        if node is None:
            return {}

        pos = {node.key: (x, y)}

        if node.left is not None:
            pos.update(
                self._calculate_node_positions(
                    node.left, x - distance_x // 2, y - 1, distance_x // 2
                )
            )

        if node.right is not None:
            pos.update(
                self._calculate_node_positions(
                    node.right, x + distance_x // 2, y - 1, distance_x // 2
                )
            )

        return pos


with open("words.txt", "r") as f:
    words = [word.replace("\n", "") for word in f.readlines()]

tree = Tree()

for size in [500, 1000, 2000]:
    for word in sample(words, size):
        tree.insert(word)
    print(f"wysokość drzewa dla ilości słów {size} wynosi:", tree.height())
    # tree.print()
    tree.draw(f"drzewo-{size}.png")
    tree.clean()

for word in ["banana", "apple", "cherry", "chocolate", "orange", "strawberry", "bbb"]:
    tree.insert(word)
print(f"wysokość drzewa:", tree.height())
# tree.print()
tree.draw("drzewo-przed-usunieciem.png")
tree.delete("banana")
tree.draw(f"drzewo-po-usunieciem.png")

# wyniki mogą się różnić ze względu na losowość danych
# Wysokość drzewa dla ilości słów 500 wynosi: 19
# Wysokość drzewa dla ilości słów 1000 wynosi: 21
# Wysokość drzewa dla ilości słów 2000 wynosi: 30
