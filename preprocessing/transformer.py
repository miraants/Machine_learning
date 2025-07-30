def fusionner_profil(profil):
    return f"{profil.fonction} - {profil.ville_voulue} - {profil.competences}"

def fusionner_offre(row):
    return f"{row['titre']} - {row['city']} - {row['summary']}"
