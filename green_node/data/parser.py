from pathlib import Path

import xmltodict


def xml_to_dict(path: Path) -> dict:

    with open(str(path), "r") as file:
        xml_input = file.read()

    return xmltodict.parse(xml_input)
