import pathlib

import mysql.connector


class DBConnect:
    # @classmethod
    # def getConnection(cls): # è un metodo di classe
    #     try:
    #         cnx = mysql.connector.connect(user="root",
    #                                       password="AticniviR1121!",
    #                                       host="127.0.0.1",
    #                                       database="Libretto")
    #         return cnx
    #     except mysql.connector.Error as err:
    #         print("Non riesco a collegarmi al database")
    #         print(err)
    #         return None

    def __init__(self):
        RuntimeError("Non creare una istanza di questa classe per favore!")
        # impediamo all'utente di creare istanza di questa classe

    _myPool = None

    @classmethod
    def getConnection(cls):  # è un metodo di classe
        if cls._myPool is None:
            # creo una connessione e restituisco il metodo get_connection
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(#user="root",
                                                                          #password="AticniviR1121!",
                                                                          #host="127.0.0.1",
                                                                          #database="Libretto",
                                                                          pool_size=3,
                                                                          pool_name="myPool",
                                                                          option_files =f"{pathlib.Path(__file__).resolve().parent}/connection.cfg")
            except mysql.connector.Error as err:
                print("Something is wrong in dbconnect")
                print(err)
                return None

            return cls._myPool.get_connection()
        else:
            # se il Pool già esiste restituisco direttamente la connessione
            return cls._myPool.get_connection()
