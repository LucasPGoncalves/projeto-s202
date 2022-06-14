from neo4j import GraphDatabase

class Graph:
    def __init__(self):
        self.driver = GraphDatabase.driver('bolt://44.192.127.0:7687', auth=('neo4j', 'fives-capacitances-investment'))
    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data

def Divider():
    print("=========================================================")