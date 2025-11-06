query_create_index = """--sql
    CREATE UNIQUE INDEX IF NOT EXISTS idx_homicides_unique
    ON homicides_alagoas (death_date, city, neighborhood, hour);
"""