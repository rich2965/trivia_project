import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://root:Tester2965@34.69.30.119:5432/triviapractice')
engine.connect()

# load the TSV file into a pandas DataFrame, data that was labeled as 'basics'
df = pd.read_csv('countries_data.csv')

# do something with the DataFrame (e.g. print the first 5 rows)
print(df.head())


print(pd.io.sql.get_schema(df,name='countries_data',con=engine))
df.to_sql(name='countries_data',con=engine,if_exists='append')