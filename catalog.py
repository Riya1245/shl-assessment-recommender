import json
import os

CATALOG_FILE = "data/catalog.json"


def load_catalog():

    if not os.path.exists(CATALOG_FILE):
        return []

    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)