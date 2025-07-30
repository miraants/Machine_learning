import pickle
from sentence_transformers import SentenceTransformer

def train_and_save_model():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    with open("data/model.pkl", "wb") as f:
        pickle.dump(model, f)
