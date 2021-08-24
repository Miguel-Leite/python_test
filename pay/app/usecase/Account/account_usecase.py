from pay.app.repository.accountrepository import AccountRepositoryDB

class AccountUsecase:
    
    def __init__(self):
        self.account_repository = AccountRepositoryDB()

    def _save(self, *args):

        try:
            results = self.account_repository._save(args[0], args[1], args[2], args[3], args[4])
            return results
        except Exception as ex:
            return ex

    