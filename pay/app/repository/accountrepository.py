import logging
from pay.models import Account

class AccountRepositoryDB:

    def __init__(self) -> Account:
    
        self.obj = Account()

    def _save(self, **kwargs):
        try: 
            self.account_status = kwargs['account_status']
            self.account_purpose = kwargs['account_purpose']
            self.account_description = kwargs['account_description']
            self.creation_date = kwargs['creation_date']
            self.update_date = kwargs['update_date']


            self.obj.save()

            return self.obj

        except Exception as ex:
            logging.ERROR("ERRO AO CRIAR CONTA!")
            return ex
