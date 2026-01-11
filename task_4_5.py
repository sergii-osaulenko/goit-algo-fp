import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# --- Базовий код з умови ---
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Tree Visualization"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# --- ЗАВДАННЯ 4: Візуалізація бінарної купи ---

def build_heap_tree(heap_list, index=0):
    if index >= len(heap_list):
        return None
    
    node = Node(heap_list[index])
    
    # Лівий нащадок: 2*i + 1
    node.left = build_heap_tree(heap_list, 2 * index + 1)
    
    # Правий нащадок: 2*i + 2
    node.right = build_heap_tree(heap_list, 2 * index + 2)
    
    return node

# --- ЗАВДАННЯ 5: Візуалізація обходу (DFS/BFS) ---

def generate_color(step, total_steps):
    """Генерує колір від темного (#1296F0) до світлого"""
    base_color = [18, 150, 240] # RGB для #1296F0
    # Робимо колір світлішим з кожним кроком
    factor = step / total_steps
    r = int(base_color[0] + (255 - base_color[0]) * factor)
    g = int(base_color[1] + (255 - base_color[1]) * factor)
    b = int(base_color[2] + (255 - base_color[2]) * factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def visualize_dfs(root):
    if not root: return
    stack = [root]
    visited_order = []
    
    while stack:
        node = stack.pop()
        visited_order.append(node)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        
    # Призначаємо кольори
    total = len(visited_order)
    for i, node in enumerate(visited_order):
        node.color = generate_color(i, total)
    
    draw_tree(root, "DFS Traversal Visualization")

def visualize_bfs(root):
    if not root: return
    queue = [root]
    visited_order = []
    
    while queue:
        node = queue.pop(0)
        visited_order.append(node)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    
    # Призначаємо кольори
    total = len(visited_order)
    for i, node in enumerate(visited_order):
        node.color = generate_color(i, total)
        
    draw_tree(root, "BFS Traversal Visualization")

# --- Виконання ---
if __name__ == "__main__":
    # 1. Створення купи
    data = [10, 5, 3, 2, 4, 1, 0]
    heapq.heapify(data) # Перетворюємо в купу: [0, 2, 1, 5, 4, 3, 10]
    print(f"Heap array: {data}")
    
    heap_root = build_heap_tree(data)
    draw_tree(heap_root, "Binary Heap Visualization")

    # 2. Обходи дерева (скидаємо кольори перед кожним)
    visualize_dfs(heap_root)
    
    # Перебудовуємо дерево для чистоти експерименту (скидаємо кольори)
    heap_root = build_heap_tree(data) 
    visualize_bfs(heap_root)

    # Heap array: [0, 2, 1, 5, 4, 10, 3]