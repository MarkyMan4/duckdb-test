import duckdb

# create an in-memory database
con = duckdb.connect(':memory:')

with open('sql/create_schema.sql') as sql_file:
    sql = ''.join(sql_file.readlines())
    con.execute(sql)

con.execute('select * from t_test')
res = con.fetchall()
print(res)
