import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given values for the Z-test
mu_0 = 150  # Null hypothesis mean
sigma = 50  # Population standard deviation
n = 30      # Sample size
alpha = 0.05 # Significance level

# Calculate the critical Z-value for a one-tailed test at alpha = 0.05
z_critical = norm.ppf(1 - alpha)

# Create a range of values for the x-axis (normal distribution)
# Focus heavily around the peak, eliminating the lower density regions entirely
x = np.linspace(mu_0 - 40, mu_0 + 50, 1000)  # Very narrow focus around the peak

# Get the corresponding y-values from the normal distribution
y = norm.pdf(x, mu_0, sigma / np.sqrt(n))  # This defines the shape of the curve

# Create the plot
plt.figure(figsize=(16, 8))  # Large plot for better clarity

# Plot the normal distribution (blue curve)
plt.plot(x, y, label="Normal Distribution (Null Hypothesis)", color='blue')

# Shade the rejection region (right of the critical Z-value)
plt.fill_between(x, y, where=(x >= mu_0 + z_critical * sigma / np.sqrt(n)), color='red', alpha=0.5, label="Rejection Region")

# Mark the critical Z-value with an orange dashed line
plt.axvline(mu_0 + z_critical * sigma / np.sqrt(n), color='orange', linestyle='--', label=f'Critical Z = {z_critical:.2f}')

# Set custom limits for the x-axis to focus more tightly on the peak area of the distribution
plt.xlim(mu_0 - 40, mu_0 + 50)  # Strongly focused range, even closer to the peak

# Labels and title
plt.title("Z-Test: One-Tailed Test (H₀: μ <= 150, H₁: μ > 150)")
plt.xlabel("Z-Statistic")
plt.ylabel("Density")
plt.legend(loc="upper left")
plt.grid(True)

# Show the plot
plt.show()

# Output the critical Z-value for clarity
print(f"Critical Z-Value (for alpha = 0.05): {z_critical:.2f}")
