from pay.app.repository.depositrepository import DepositRepositoryDB

class DepositUsecase:

    def __init__(self):

        self.obj = DepositRepositoryDB()

    def _save(self, **kwargs) -> DepositRepositoryDB:
        try:
            return self.obj._save(kwargs)
        except Exception as ex:
            return ex