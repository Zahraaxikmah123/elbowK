from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator

def find_best_k(X_scaled, max_k=10, save_plot=True):
    """
    Automatically detects the optimal number of clusters (k) using the Elbow method.
    Plots SSE vs k and optionally saves it as 'elbow_plot.png'.
    Returns the optimal k.
    """
    sse = []
    K_range = range(1, max_k + 1)

    for k in K_range:
        km = KMeans(n_clusters=k, n_init="auto", random_state=42)
        km.fit(X_scaled)
        sse.append(km.inertia_)

    kneedle = KneeLocator(K_range, sse, curve="convex", direction="decreasing")
    optimal_k = kneedle.knee or max_k

    plt.figure(figsize=(8, 5))
    plt.plot(K_range, sse, 'bo-', label='SSE')
    plt.vlines(optimal_k, plt.ylim()[0], plt.ylim()[1], linestyles='dashed',
               colors='red', label=f'Optimal k = {optimal_k}')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('SSE')
    plt.title('Elbow Method')
    plt.xticks(K_range)
    plt.legend()
    plt.grid(True)
    if save_plot:
        plt.savefig("elbow_plot.png")

    return optimal_k