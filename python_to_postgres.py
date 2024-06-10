import psycopg2

hostname = 'localhost'
database = 'project-1'
username = 'postgres'
pwd = 'postgres'
port_id = 5432
connectionToSql = None
cursor = None
try:
    connectionToSql = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)

    cursor = connectionToSql.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30))'''
    
    cursor.execute(create_script)

    connectionToSql.commit()
except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if connectionToSql is not None:
        connectionToSql.close()