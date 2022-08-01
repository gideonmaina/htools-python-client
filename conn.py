import psycopg2
from config import config
def connect():
    """Connect to htools Postgres DB server"""
    
    print("connecting")
    conn=None
    try:
        params=config()
        print(params)
        conn=psycopg2.connect(**params)

        cur=conn.cursor()
        print('Postgres DB version: ')
        cur.execute('SELECT version()')

        db_version=cur.fetchone()
        print(db_version)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
            print('Closing DB connection')



if __name__=='___main__':
    connect()