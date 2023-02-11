import duckdb

# create an in-memory database
con = duckdb.connect(':memory:')

with open('sql/create_schema.sql') as sql_file:
    sql = ''.join(sql_file.readlines())
    con.execute(sql)

con.execute('select * from article limit 10')
res = con.fetchall()
print(res)

con.execute('select avg(score) from article')
res = con.fetchall()
print(res)
