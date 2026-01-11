import matplotlib.pyplot as plt
import numpy as np

def draw_pithagoras_tree(ax, x, y, length, angle, level):
    if level == 0:
        return

    # Обчислюємо нові координати кінця гілки
    # angle в радіанах
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малюємо лінію (гілку)
    # Колір залежить від рівня (для краси)
    color = plt.cm.viridis(level / 10) 
    ax.plot([x, x_end], [y, y_end], color='brown', lw=level * 0.5)

    # Нова довжина для наступних гілок
    new_length = length * 0.8 # Коефіцієнт зменшення

    # Рекурсивні виклики для лівої та правої гілки
    # Ліва гілка: кут + 45 градусів (pi/4)
    draw_pithagoras_tree(ax, x_end, y_end, new_length, angle + np.pi/4, level - 1)
    
    # Права гілка: кут - 45 градусів (pi/4)
    draw_pithagoras_tree(ax, x_end, y_end, new_length, angle - np.pi/4, level - 1)

def main():
    try:
        level = int(input("Введіть рівень рекурсії (рекомендовано 8-10): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    # Налаштування графіка
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect('equal')
    ax.axis('off') # Прибираємо осі
    ax.set_title(f"Дерево Піфагора (Рівень {level})")

    # Початкові параметри: x=0, y=0, довжина=100, кут=90 градусів (pi/2)
    draw_pithagoras_tree(ax, 0, 0, 100, np.pi/2, level)

    plt.show()

if __name__ == "__main__":
    main()