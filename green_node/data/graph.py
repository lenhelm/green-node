from neo4j import GraphDatabase


class Graph:
    def __init__(self, uri: str, user: str, pw: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, pw))

    def close(self):
        self.driver.close()
