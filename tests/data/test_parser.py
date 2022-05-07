from collections import OrderedDict

from green_node.data.io import get_example
from green_node.data.parser import xml_to_dict


def test_xml_to_dict():
    path = get_example("shortest-path.xml")
    assert type(xml_to_dict(path)) is OrderedDict
