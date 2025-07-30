from preprocessing.transformer import fusionner_profil, fusionner_offre
from sentence_transformers import util

def recommander_offre(profil, df, model):
    df["texte_complet"] = df.apply(fusionner_offre, axis=1)
    texte_utilisateur = fusionner_profil(profil)

    emb_user = model.encode(texte_utilisateur, convert_to_tensor=True)
    emb_offres = model.encode(df["texte_complet"].tolist(), convert_to_tensor=True)
    scores = util.cos_sim(emb_user, emb_offres)[0]
    df["score"] = scores.cpu().numpy()

    top = df.sort_values(by="score", ascending=False).head(1).iloc[0]

    return {
        "titre": top["titre"],
        "ville": top["city"],
        "resume": top["summary"],
        "score": float(top["score"])
    }
