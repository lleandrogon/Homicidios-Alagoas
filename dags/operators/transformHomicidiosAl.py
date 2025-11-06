import pandas as pd
import pprint

def transform_homicidios(**kwargs):
    df = kwargs["ti"].xcom_pull(task_ids = "extract_homicidios")

    df["skin_color"] = df["skin_color"].replace("NI", "Não Informado")

    df["age"] = df["age"].replace("-", None)
    df["age"] = pd.to_numeric(df["age"], errors = "coerce")

    df["sex"] = df["sex"].replace("-", "Sexo Desconhecido")

    df["death_type"] = df["death_type"].str.title()
    df["death_type"] = df["death_type"].replace({
        "Paf": "PAF",
        "Paf/B": "PAF/B",
        "Ni": "Não Identificado"
    })

    df["city"] = df["city"].replace({
        "Olho d Água do Casado": "Olho d'Água do Casado",
        "Olho d Água Grande": "Olho d'Água Grande",
        "Olho d Água das Flores": "Olho d'Água das Flores"
    })

    df["neighborhood"] = df["neighborhood"].replace({
        "Olho d Água dos Cazuzinhos": "Olho d'Água dos Cazuzinhos",
        "Sítio Pau d Arco": "Sítio Pau d'Arco",
        "Sítio Gruta d Água": "Sítio Gruta d'Água"
    })

    df["neighborhood"] = df["neighborhood"].replace("Bairro não Informado", "Bairro Desconhecido")

    df = df.rename(columns = {"date": "death_date"})
    df["death_date"] = pd.to_datetime(df["death_date"], format = "%d/%m/%Y", errors = "coerce")

    return df