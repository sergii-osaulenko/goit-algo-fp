items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# 1. Жадібний алгоритм (Greedy)
def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості
    item_list = []
    for name, data in items.items():
        ratio = data["calories"] / data["cost"]
        item_list.append((name, data["cost"], data["calories"], ratio))
    
    # Сортуємо за спаданням співвідношення
    item_list.sort(key=lambda x: x[3], reverse=True)
    
    total_calories = 0
    total_cost = 0
    chosen_items = []
    
    for name, cost, cal, ratio in item_list:
        if total_cost + cost <= budget:
            chosen_items.append(name)
            total_cost += cost
            total_calories += cal
            
    return chosen_items, total_calories, total_cost

# 2. Динамічне програмування (Dynamic Programming)
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]
    n = len(items)
    
    # Таблиця DP: рядки - страви, стовпці - бюджет від 0 до budget
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i-1] <= w:
                dp[i][w] = max(calories[i-1] + dp[i-1][w - costs[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Відновлення обраніх страв
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(item_names[i-1])
            w -= costs[i-1]
            
    return chosen_items, dp[n][budget]

# --- Тест ---
budget = 100
greedy_res = greedy_algorithm(items, budget)
dp_res = dynamic_programming(items, budget)

print(f"Жадібний алгоритм: {greedy_res[0]}, Калорії: {greedy_res[1]}")
print(f"Динамічне програмування: {dp_res[0]}, Калорії: {dp_res[1]}")

# Жадібний алгоритм: ['cola', 'potato', 'pepsi', 'hot-dog'], Калорії: 870
# Динамічне програмування: ['potato', 'cola', 'pepsi', 'pizza'], Калорії: 970