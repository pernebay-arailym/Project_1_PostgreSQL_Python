import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'project-1'
username = 'postgres'
pwd = 'postgres'
port_id = 5432
connectionToSql = None
cursor = None
try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as connectionToSql:

        with connectionToSql.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:

            cursor.execute('DROP TABLE IF EXISTS employee')

            create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                                    id      int PRIMARY KEY,
                                    name    varchar(40) NOT NULL,
                                    salary  int,
                                    dept_id varchar(30))'''
            
            cursor.execute(create_script)

            insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'Arailym', 30000, 'D1'), (2, 'Dana', 33000, 'D1'), (3, 'Ais', 35000, 'D2')]
            for record in insert_values:   
                cursor.execute(insert_script, record)

            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cursor.execute(update_script)

            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('Arailym',)
            cursor.execute(delete_script, delete_record)

            cursor.execute ('SELECT * FROM EMPLOYEE')
            for record in cursor.fetchall():
                print(record['name'], record['salary'])
except Exception as error:
    print(error)
finally:
    if connectionToSql is not None:
        connectionToSql.close()
