from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

class Graph:

    def __init__(self, uri: str, user: str, pw: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, pw))

    def setup_graph(tx, supplier1_name, supplier2_name):

        query = (
            "CREATE (s1:Person { name: $supplier1_name }) "
            "CREATE (s2:Person { name: $supplier2_name }) "
            "CREATE (s1)-[:KNOWS]->(s2) "
            "RETURN s1, s2"
        )
        result = tx.run(query, supplier1_name=supplier1_name, supplier2_name=supplier2_name)
        try:
            return [{"s1": record["s1"]["name"], "s2": record["s2"]["name"]}
                    for record in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

