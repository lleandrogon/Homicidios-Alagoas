query = """
    CREATE TABLE IF NOT EXISTS homicides_alagoas(
        id SERIAL PRIMARY KEY,
        skin_color VARCHAR(100),
        sex VARCHAR(100),
        complement VARCHAR(100),
        death_type VARCHAR(100),
        city VARCHAR(100),
        neighborhood VARCHAR(100),
        death_date DATE,
        hour INTEGER
    );
"""