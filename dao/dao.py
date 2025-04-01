import mysql.connector

from dao.dbConnect import DBConnect
from voto.voto import Voto


class LibrettoDAO:
    # def __init__(self):
    #     self.dbConnect = DBConnect()

    # Qui mettiamo i metodi del DAO

    @staticmethod  # è un metodo che vede solo i parametri passati
    def getAllVoti():  # tolgo il self
        # cnx = mysql.connector.connect(  # creo la connessione
        #     user="root",
        #     password="AticniviR1121!",
        #     host="127.0.0.1",
        #     database="Libretto")
        #cnx = self.dbConnect

        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)  # creo cursore
        query = """select * from voti"""
        cursor.execute(query)
        res = []
        for row in cursor:
            # materia = row["materia"]  # str
            # punteggio = row("punteggio")  # int
            # lode = row("lode")  # str
            # data = row("data")  # datetime
            # v = Voto(materia, punteggio, data, lode)
            # res.append(v)
            # print(row)
            if row["lode"] == False:
                res.append(Voto(row["materia"], row["punteggio"], row["data"].date(), False))
            else:
                res.append(Voto(row["materia"], row["punteggio"], row["data"].date(), True))

        cnx.close()  # chiudere connessione
        return res

    @staticmethod
    def addVoto( voto:Voto):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query = ("insert into voti" 
                 "(materia, punteggio, data, lode)" 
                 "values (%s, %s, %s, %s)")
        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))
        cnx.commit()
        cnx.close()
        return

    @staticmethod
    def hasVoto(voto: Voto):
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor()
        query = """select * 
                    from voti v
                    where v.materia = %s"""  #%s è una stringa passata da fuori
        cursor.execute(query, (voto.materia,))
        res = cursor.fetchall()
        cnx.close()

        return len(res) > 0  # se la lunghezza è maggiore di 0 vuol dire che quel voto già esiste




if __name__ == "__main__":
    mydao = LibrettoDAO()
    mydao.getAllVoti()
