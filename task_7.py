import random
import matplotlib.pyplot as plt

def monte_carlo_dice(num_simulations=100000):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_simulations):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        total = d1 + d2
        sums_count[total] += 1
        
    probabilities = {k: (v / num_simulations) * 100 for k, v in sums_count.items()}
    return probabilities

# Теоретичні ймовірності (у відсотках)
theoretical_probs = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

num_sims = 1000000
mc_probs = monte_carlo_dice(num_sims)

print(f"{'Сума':<5} | {'Монте-Карло (%)':<15} | {'Теорія (%)':<15} | {'Різниця':<10}")
print("-" * 50)
for s in range(2, 13):
    print(f"{s:<5} | {mc_probs[s]:<15.2f} | {theoretical_probs[s]:<15.2f} | {abs(mc_probs[s] - theoretical_probs[s]):<10.2f}")

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(mc_probs.keys(), mc_probs.values(), alpha=0.6, label='Монте-Карло', color='blue')
plt.plot(list(theoretical_probs.keys()), list(theoretical_probs.values()), color='red', marker='o', label='Теорія')
plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title(f'Ймовірності суми двох кубиків (Simulation: {num_sims})')
plt.legend()
plt.grid(True)
plt.show()