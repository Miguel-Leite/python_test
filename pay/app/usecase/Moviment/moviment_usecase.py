from pay.models import Moviment
from pay.app.repository.movimentrepository import MovimentRepositoryDB

class MovimentUsecase:

    def __init__(self):
        self.obj = MovimentRepositoryDB()

    def _save(self, **kwargs) -> MovimentRepositoryDB:
        try:
            return self.obj._save(kwargs)
        except Exception as ex:
            return ex