import sklearn.svm
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from category_encoders import OrdinalEncoder
import joblib
import datetime
import numpy as np
from sklearn.svm import LinearSVC

class Machine:

    def __init__(self, df):
        self.name = "Random Forest Classifier"

        target = "Rarity"
        x = df.drop(columns=target)
        y = df[target]

        self.model = make_pipeline(
            OrdinalEncoder(),
            RandomForestClassifier(random_state=42, n_jobs=-1, max_samples=0.4, n_estimators=240)
        ).fit(x, y)

        self.init_time = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S:%p")

    def __call__(self, feature_basis):
        prediction = self.model.predict(feature_basis)
        scores = self.model.predict_proba(feature_basis)
        confidence = np.array(scores)

        return prediction, confidence.max()

    def save(self, filepath):
        joblib.dump(self.model, 'model_jlib')

    @staticmethod
    def open(filepath):
        m_jlib = joblib.load('model_jlib')

    def info(self):
        return f"Timestamp: {self.init_time}"
