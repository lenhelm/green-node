from copy import copy

from neo4j import GraphDatabase


def dictify(r, root=True):
    if root:
        return {r.tag: dictify(r, False)}
    d = copy(r.attrib)
    if r.text:
        d["_text"] = r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag] = []
        d[x.tag].append(dictify(x, False))
    return d


class Graph:
    def __init__(self, uri: str, user: str, pw: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, pw))

    def close(self):
        self.driver.close()

    def setup_graph(self, path: str):

        with open(path, "r") as file:
            data = file.read()

        xml_dict = dictify(data)

        return xml_dict
