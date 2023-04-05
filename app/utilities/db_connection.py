import psycopg2

def db_cursor():
    
    # here i would take the env variables and place them somewhere else where they are secure and not commited
    conn = psycopg2.connect(
        database='postgres',
        host='127.0.0.1',
        password='ratestask',
    )

    return conn