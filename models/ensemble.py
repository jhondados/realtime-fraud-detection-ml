"""Calibrated ensemble for fraud detection."""
import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.base import BaseEstimator

class FraudEnsemble(BaseEstimator):
    def __init__(self, models: list, weights: list = None):
        self.models = models
        self.weights = weights or [1/len(models)] * len(models)
        self.calibrators = []

    def fit(self, X, y):
        for model in self.models:
            cal = CalibratedClassifierCV(model, method="isotonic", cv=5)
            cal.fit(X, y)
            self.calibrators.append(cal)
        return self

    def predict_proba(self, X) -> np.ndarray:
        probas = np.array([cal.predict_proba(X)[:, 1] for cal in self.calibrators])
        weighted = np.average(probas, axis=0, weights=self.weights)
        return np.column_stack([1 - weighted, weighted])

    def predict(self, X, threshold: float = 0.5) -> np.ndarray:
        return (self.predict_proba(X)[:, 1] >= threshold).astype(int)
