import numpy as np
import statsmodels.api as sm
from scipy import stats

# Step 1: Create the data (study hours and exam scores)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])  # Study hours
Y = np.array([45, 50, 55, 60, 62, 65, 68, 72, 75, 78, 80, 83, 86, 88, 90])  # Exam scores

# Step 2: Perform linear regression using statsmodels
# Add a constant (intercept) to the independent variable
X_with_const = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(Y, X_with_const)  # OLS (Ordinary Least Squares)
results = model.fit()

# Print the regression results summary
print(results.summary())

# Step 3: Hypothesis Testing for the Slope (Beta1)
# Get the estimated slope and standard error
beta_1 = results.params[1]
se_beta_1 = results.bse[1]

# Calculate t-statistic for the slope
t_statistic = beta_1 / se_beta_1

# Calculate degrees of freedom
df = len(X) - 2

# Calculate p-value for two-tailed test
p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), df))

# Print the t-statistic and p-value
print(f"\nt-statistic: {t_statistic}")
print(f"p-value: {p_value}")

# Step 4: Conclusion
# If p-value < 0.05, reject the null hypothesis (beta1 != 0)
if p_value < 0.05:
    print("\nWe reject the null hypothesis: There is a significant relationship between study hours and exam scores.")
else:
    print("\nWe fail to reject the null hypothesis: There is no significant relationship between study hours and exam scores.")
