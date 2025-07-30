def fusionner_offres(df):
    df["texte_complet"] = (
        df["titre"].astype(str) + " - " +
        df["city"].astype(str) + " - " +
        df["summary"].astype(str)
    )
    return df

def fusionner_profil(profil):
    return (
        profil.fonction + " - " +
        profil.ville_voulue + " - " +
        profil.competences
    )
