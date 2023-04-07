import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("generated_data.csv")
print(data)
# Calculate correlation matrix
corr = data.corr()

# Create heatmap of the correlation matrix
sns.set(style='white')
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', square=True, ax=ax)

# Show plot
plt.show()
