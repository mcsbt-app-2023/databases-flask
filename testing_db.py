# %%
from sqlalchemy import create_engine

engine = create_engine("sqlite:///paymepal.db")

with engine.connect() as connection:
    query = "SELECT * FROM users LIMIT 100"

    users = connection.execute(query)

    for user in users:
        print(user)
