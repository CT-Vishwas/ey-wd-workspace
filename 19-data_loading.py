#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com

import pandas as pd
from sqlalchemy import create_engine

DB_HOST='localhost'
DB_USER='root'
DB_PASS = 'root'
DB_NAME = 'devdb'
DRIVER = 'mysql+mysqldb'

TABLE_NAME = 'house_rents_data'

connection_string = f'{DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}?charset=utf8mb4'
df = pd.read_csv('house_rent.csv')

try:
    engine = create_engine(connection_string)
except Exception as e:
    print(f"Error while connecting with error:{e}")

try:
    df.to_sql(
        name=TABLE_NAME,
        con=engine,
        if_exists='replace',
        index=False
    )

    print('data loaded successfully')
except Exception as e:
    print(f"Error:{e}")