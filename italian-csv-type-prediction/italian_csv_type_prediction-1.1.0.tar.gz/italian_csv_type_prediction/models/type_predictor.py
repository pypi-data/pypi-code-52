from ..embedding import DataframeEmbedding
from ..dataframe_generators import SimpleDatasetGenerator
import compress_pickle
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier


class TypePredictor:

    def __init__(self, local_path: str = "type_predictor.pkl.gz"):
        self._embedder = DataframeEmbedding()
        self._local_path = "{pwd}/{local_path}".format(
            pwd=os.path.dirname(os.path.abspath(__file__)),
            local_path=local_path
        )
        self._forest = self._load_model()

    def fit(self, number: int = 1000):
        X, y = SimpleDatasetGenerator().build(number)
        self._forest = RandomForestClassifier(
            n_estimators=1000, max_depth=20, random_state=42, class_weight="balanced").fit(X, y)
        self._save_model()

    def _save_model(self):
        compress_pickle.dump(self._forest, self._local_path)

    def _load_model(self):
        if os.path.exists(self._local_path):
            return compress_pickle.load(self._local_path)
        return None

    def predict_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Return dataframe with given dataframe type predictions."""
        return self._embedder.reverse_label_embedding(
            self._forest.predict(self._embedder.transform(df)),
            df
        )
