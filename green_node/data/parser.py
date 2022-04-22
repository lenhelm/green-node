from copy import copy
from pathlib import Path
import xml.etree.ElementTree as ET

import xmltodict


def xml_to_dict(path: Path) -> dict:

    with open(str(path), "r") as file:
        xml_input = file.read()

    return xmltodict.parse(xml_input)
