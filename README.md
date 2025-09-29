
# elbowK 🚀


This package provides tools for determining the optimal number of clusters in K-Means clustering using the **Elbow Method**. 🤖
It automatically calculates the sum of squared errors (SSE) for different values of *k*, detects the Best k, and visualizes the results with an elbow plot. 📈

---


## Installation 🛠️


### Install from requirements.txt 📦

```bash
pip install -r requirements.txt
```


### Install in development mode (local) 🧑‍💻

```bash
pip install -e .
```


### Install from PyPI 🌐

```bash
pip install elbowK
```

---


## Usage 🏃‍♂️


To use the package, import the main function and pass your scaled data:

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from elbowK.elbow import find_best_k

# Example dataset
data = pd.DataFrame({
    'Income_$': [15, 16, 17, 18, 19, 20],
    'SpendingScore': [39, 81, 6, 77, 40, 76]
})

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

# Find the best k and save the elbow plot
best_k = find_best_k(X_scaled, max_k=10, save_plot=True)
print(f"Optimal k: {best_k}")
# The elbow plot will be saved as 'elbow_plot.png' in your working directory. 🖼️
```

---


## Package Structure 📁

```
elbowK/
    __init__.py       # Initializes the package
    elbow.py          # Core functionality for determining optimal clusters
setup.py              # Package metadata and setup configuration
requirements.txt      # Dependencies required
tests/
    elbow_test.py     # Unit tests
```

---


## License 📄

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
