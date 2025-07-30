from fastapi import FastAPI
from pydantic import BaseModel
from data.database import get_opportunities
from preprocessing.transformer import fusionner_offres, fusionner_profil
from models.predictor import calculer_similarite

app = FastAPI()

class ProfilUtilisateur(BaseModel):
    fonction: str
    ville_actuelle: str
    ville_voulue: str
    competences: str

@app.post("/predict")
def recommander(profil: ProfilUtilisateur):
    df = get_opportunities()
    df = fusionner_offres(df)
    texte_utilisateur = fusionner_profil(profil)
    scores = calculer_similarite(texte_utilisateur, df["texte_complet"].tolist())
    df["score"] = scores
    top = df.sort_values(by="score", ascending=False).iloc[0]

    return {
        "titre": top["titre"],
        "ville": top["city"],
        "resume": top["summary"],
        "score": float(top["score"])
    }
