import create_psql as create

def query(queryOp: str, userName: str, passWord: str, hostAddr: str, dbName: str, portNo='5432'):
    import psycopg2

    try:
        conn = psycopg2.connect(
            user=userName,
            password=passWord,
            host=hostAddr,
            port=portNo,
            database=dbName
        )
        cursor = conn.cursor()

        try:
            cursor.execute(queryOp)
            conn.commit()
        except:
            print('Error executing SQL input', error)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
            print('Connection to PostgreSQL closed.')

        print('Connection to PostgreSQL established successfully!')

    except (Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL', error)
