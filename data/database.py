import pandas as pd
import pyodbc
from config.db_config import DB_CONN_STR

def get_opportunities():
    conn = pyodbc.connect(DB_CONN_STR)
    query = """
    SELECT o.ID, o.Titre, o.Summary, el.Contries AS city
    FROM Opportunity o
    LEFT JOIN ElementList el ON o.ID_Cities = el.ID_Element
    WHERE o.Status = 1;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    df.rename(columns={"Titre": "titre", "Summary": "summary"}, inplace=True)
    df.dropna(subset=["titre", "city", "summary"], inplace=True)
    return df
