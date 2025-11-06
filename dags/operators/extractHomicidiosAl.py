import pandas as pd
import pprint

def extract_homicidios(**kwargs):
        df = pd.read_csv("/opt/airflow/volumes/homicidios_al.csv", sep = ";")
        
        pprint.pprint(df)

        return df