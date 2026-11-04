"""Vérifie le contenu et l'empreinte du CSV téléchargé."""

import hashlib
from pathlib import Path

import pandas as pd

path = Path("data/breast_cancer.csv")
df = pd.read_csv(path)
md5 = hashlib.md5(path.read_bytes()).hexdigest()

print(
    f"lignes : {len(df)} | colonnes : {df.shape[1]} | "
    f"B={(df['diagnosis'] == 'B').sum()} "
    f"M={(df['diagnosis'] == 'M').sum()}"
)
print(f"manquantes : {df.isna().sum().sum()} | MD5 : {md5}")
print(
    "OK : CSV conforme."
    if md5 == "f4aecff5892354dc4c7879d8ee2b3c09"
    else "ATTENTION : CSV modifié !"
)