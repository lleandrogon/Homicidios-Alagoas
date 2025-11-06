from airflow.providers.postgres.hooks.postgres import PostgresHook

def load_homicidios(**kwargs):
    df = kwargs["ti"].xcom_pull(task_ids = "transform_homicidios")

    hook = PostgresHook(postgres_conn_id = "homicides", schema = "homicides")

    query = """
        INSERT INTO homicides_alagoas (
            skin_color,
            sex,
            complement,
            death_type,
            city,
            neighborhood,
            death_date,
            hour
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (death_date, city, neighborhood, hour) DO UPDATE SET
            skin_color = EXCLUDED.skin_color,
            sex = EXCLUDED.sex,
            complement = EXCLUDED.complement,
            death_type = EXCLUDED.death_type;
    """

    for row in df[["skin_color", "sex", "complement", "death_type",
    "city", "neighborhood", "death_date", "hour"]].itertuples(index = False, name = None):
        hook.run(query, parameters = row)