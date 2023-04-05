import psycopg2

def db_cursor():
    
    conn = psycopg2.connect(
        database='postgres',
        host='127.0.0.1',
        password='ratestask',
    )

    return conn