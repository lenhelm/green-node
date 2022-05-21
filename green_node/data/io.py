from pathlib import Path


def get_root() -> Path:
    return Path(__file__).parent.parent.parent


def get_example(xml: str) -> Path:
    return Path(get_root() / "green_node/data/example" / xml)
