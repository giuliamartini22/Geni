from database.DB_connect import DBConnect
from model.arco import Arco


class DAO():
    @staticmethod
    def getAllChromosome():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct chromosome
                    from genes g 
                    where chromosome >0"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["chromosome"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCorrelazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g1.Chromosome as c1, g2.Chromosome as c2, g1.GeneId as gen1, g2.GeneID as gen2, i.Expression_Corr as corr
                    from genes g1, genes g2, interactions i 
                    where g2.GeneID = i.GeneID2 
                    and g1.GeneID = i.GeneID1 
                    and g1.Chromosome != g2.Chromosome
                    and g1.Chromosome> 0 and  g2.Chromosome > 0
                    order by g1.Chromosome, g2.Chromosome"""

        cursor.execute(query)

        for row in cursor:
            result.append(Arco(**row))

        cursor.close()
        conn.close()
        return result

# andrea
    @staticmethod
    def getAllGenes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g.GeneID as gene
                    from genes g """

        cursor.execute(query)
        for row in cursor:
            result.append(row["gene"])

        cursor.close()
        conn.close()
        return result
        # return rows
    # fine andrea

    @staticmethod
    def getAllLocalizations():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.Localization as Loc
                    from classification c"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["Loc"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEssential():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g.Essential as ess
                    from genes g """

        cursor.execute(query)

        for row in cursor:
            result.append(row["ess"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getFunction():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g.`Function` as fun
                    from genes g """

        cursor.execute(query)

        for row in cursor:
            result.append(row["fun"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTypes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct i.`Type` as type
                    from interactions i """

        cursor.execute(query)

        for row in cursor:
            result.append(row["type"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getExprCorr():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct i.Expression_Corr as expr 
                    from interactions i
                    order by i.Expression_Corr desc """

        cursor.execute(query)

        for row in cursor:
            result.append(row["expr"])

        cursor.close()
        conn.close()
        return result