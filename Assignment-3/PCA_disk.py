import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set a seed for reproducibility
np.random.seed(42)

# Parameters for the disk shape
n_samples = 1000
theta = np.linspace(0, 2 * np.pi, n_samples)

# Create disk data
radii = np.sqrt(np.random.rand(n_samples))  # Radii
x = radii * np.cos(theta)  # X coordinates
y = radii * np.sin(theta)  # Y coordinates
z = 0.1 * np.random.randn(n_samples)  # Limited depth (Z coordinate)

#Q1
data = np.column_stack([x,y,z])

# Perform PCA
# De-mean the dataset by subtracting the mean from each dimension.
mean_centered_data = data - np.mean(data, axis=0)

# Compute the covariance matrix of the mean-centered data.
covariance_matrix = np.cov(mean_centered_data, rowvar=False)

# Calculate the eigenvalues and eigenvectors of the covariance matrix, then sort them in descending order.
eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

# Sort eigenvalues and corresponding eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Print results
print("Covariance Matrix:")
print(covariance_matrix)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)

#Q2
# Calculate the variance explained by each principal component
explained_variance_ratio = eigenvalues / np.sum(eigenvalues)

# Print results
print("\nExplained Variance Ratio")
for i, r in enumerate(explained_variance_ratio, start=1):
    print(f"  PC{i}: {r:.8f}\n")
#The first two components comprise approximately 98% of all the variance in the data. Which means most of the variance is in two directions, not three. This would make our data spread look more like a disk instead of a ball

#Q3
projected_data = np.dot(mean_centered_data, eigenvectors[:, :2])

# Create a DataFrame for the table
table_data = pd.DataFrame(data, columns=['Original X', 'Original Y','Original Z'])
table_data['Projected PC1'] = projected_data[:, 0]
table_data['Projected PC2'] = projected_data[:, 1]

# Display the table
print(table_data.head(5))

# Plot the data and principal components
plt.figure(figsize=(8, 8))
plt.scatter(projected_data[:, 0], projected_data[:, 1], alpha=0.5)
plt.title("Projection of Two Principal Components")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.tight_layout()
plt.show()

#Q4
# Plot the data and principal components
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(projected_data[:, 0], projected_data[:, 1], alpha=0.5, label='Projected Data Points')

# Plot principal components scaled by the square root of their eigenvalues
mean = np.zeros(2)

for i in range(2):
    eigenvalue_scaled_component = np.sqrt(eigenvalues[i]) * eigenvectors[:, i][:2]
    ax.quiver(mean[0], mean[1], eigenvalue_scaled_component[0], eigenvalue_scaled_component[1],
              color=f'C{i + 1}', angles='xy', scale_units='xy', scale=1, label=f'Principal Component {i + 1}')

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_title('PCA of 2D Random Data')
ax.legend()
plt.grid(True)
plt.tight_layout()
plt.show()