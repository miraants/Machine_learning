from sentence_transformers import SentenceTransformer, util
import numpy as np

# Chargement du modèle NLP une seule fois
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

def calculer_similarite(texte_user, textes_offres):
    emb_user = model.encode(texte_user, convert_to_tensor=True)
    emb_offres = model.encode(textes_offres, convert_to_tensor=True)
    scores = util.cos_sim(emb_user, emb_offres)[0]
    return scores.cpu().numpy()
