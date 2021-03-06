import pickle

from ..template import BaseTemplate
from ..exceptions import NotFoundError


class PickleTemplate(BaseTemplate):
    """
    Memory template using pickle storage
    """

    def save(self, data: dict, path):
        with path.open('wb') as f:
            pickle.dump(data, f)

    def load(self, path) -> dict:
        try:
            with path.open('rb') as f:
                return pickle.load(f)
        except FileNotFoundError as e:
            raise NotFoundError(e)
