import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней: нескінченність для всіх, 0 для стартової
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Пріоритетна черга: (відстань, вершина)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо поточна відстань більша за вже знайдену, пропускаємо
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Граф у вигляді словника
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))