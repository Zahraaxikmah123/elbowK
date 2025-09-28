import unittest
import pandas as pd
from sklearn.preprocessing import StandardScaler
from elbowK.elbow import find_best_k

class TestElbowMethod(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'Income_$': [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
            'SpendingScore': [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
        })
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.data)

    def test_optimal_k_range(self):
        optimal_k = find_best_k(self.X_scaled, max_k=5, save_plot=False)
        self.assertGreaterEqual(optimal_k, 1)
        self.assertLessEqual(optimal_k, 5)

    def test_optimal_k_with_large_range(self):
        optimal_k = find_best_k(self.X_scaled, max_k=10, save_plot=True)
        self.assertGreaterEqual(optimal_k, 1)
        self.assertLessEqual(optimal_k, 10)

if __name__ == '__main__':
    unittest.main()