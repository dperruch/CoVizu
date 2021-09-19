"""

DavidPerruchoud @ Aktiia SA (created on 17/09/2021)
"""
import json
from requests import get

OFSP_CONTEXT_API_URL = 'https://www.covid19.admin.ch/api/data/context'


class Context:
    def __init__(self):
        self.full_context = json.loads(get(OFSP_CONTEXT_API_URL).text)
        sources = self.full_context.get('sources')
        self.ofsp_readme = sources.get('readme')
        self.csv_context = sources.get('individual').get('csv')
        self.daily = self.csv_context.get('daily')
        self.weekly = self.csv_context.get('weekly')

    def get_csv_context(self, db_hierarchy: tuple) -> str:
        """Returns the URL of the target database, according to db_hierarchy.
        Raises a LookUpError if the given hierarchy is invalid."""
        pointer = self.csv_context
        for next_layer in db_hierarchy:
            if not isinstance(pointer, dict):
                raise LookupError(f"'{next_layer}' is not a recognized hierarchy in the database.")
            pointer = pointer.get(next_layer)
            if pointer is None:
                raise LookupError(f"'{next_layer}' is not a recognized hierarchy in the database.")

        return pointer



