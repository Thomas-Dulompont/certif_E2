import pandas as pd

def filter_columns_with_missing(df, threshold=5):
    """
    Cette fonction prend un DataFrame en paramètre et renvoie un nouveau DataFrame
    contenant uniquement les colonnes qui ont plus de 'threshold' pourcentage de valeurs manquantes.
    
    :param df: DataFrame pandas - Le DataFrame d'entrée
    :param threshold: int - Le pourcentage de valeurs manquantes à partir duquel les colonnes sont filtrées (par défaut 5)
    :return: DataFrame pandas - Le DataFrame résultant avec les colonnes contenant des valeurs manquantes supérieures à 'threshold'
    """
    # Calculer la proportion de valeurs manquantes pour chaque colonne
    missing_percentages = df.isnull().mean() * 100

    # Filtrer les colonnes ayant plus de 'threshold' pourcentage de valeurs manquantes
    columns_with_missing = missing_percentages[missing_percentages > threshold].index

    # Isoler les colonnes avec plus de 'threshold' pourcentage de valeurs manquantes dans un nouveau DataFrame
    df_with_missing_values = df[columns_with_missing]

    return df_with_missing_values

def style_house(x):
    style = "Autre"

    if x == "BrkCmn" or x == "BrkFace":
        style = "Brique"
    elif x == "CBlock":
        style = "Parpaing"
    elif x == "Stone":
        style = "Pierre"

    return style