# Run Docker container with PostgreSQL
# docker start postgres-test # Start the container

## Alternative:
# docker run --name postgres-test -e POSTGRES_USER=myuser \
#     -e POSTGRES_PASSWORD=mypassword \
#     -e POSTGRES_DB=mydatabase \
#     -p 5432:5432 \
#     --network my_network \
#     -d postgres

import pandas as pd
from user_models import Base, engine, SessionLocal, User

Base.metadata.create_all(engine)

df = pd.read_csv("daten/user_data.csv", sep=";")
user_data = df.to_dict(orient="records")
user_data = [User(**user) for user in user_data]

session = SessionLocal()
session.add_all(user_data)
session.commit()
print("Daten wurden erfolgreich eingefügt!")
session.close()


# Check if data is inserted
df = pd.read_sql('SELECT * FROM user_data', engine)
print(df)
