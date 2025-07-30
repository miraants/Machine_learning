from fastapi import FastAPI
from pydantic import BaseModel
from models.predictor import recommander_offre
from data.database import get_opportunities
import pickle

app = FastAPI()

# Charger le modèle NLP
with open("data/model.pkl", "rb") as f:
    model = pickle.load(f)

# Schéma de données attendu
class ProfilUtilisateur(BaseModel):
    fonction: str
    ville_actuelle: str
    ville_voulue: str
    competences: str

@app.post("/predict")
def predict(profil: ProfilUtilisateur):
    df = get_opportunities()
    return recommander_offre(profil, df, model)
