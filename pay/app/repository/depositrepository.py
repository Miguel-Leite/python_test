import logging
from pay.models import Deposit
from pay.app.usecase.Moviment.moviment_usecase import MovimentUsecase


class DepositRepositoryDB:

    def __init__(self):

        self.obj = Deposit()

        self.obj_m = MovimentUsecase()

    def _save(self, **kwargs):
        try:
            self.obj.amount_numeric = kwargs["amount_numeric"]
            self.obj.applied_fee = kwargs["applied_fee"]
            self.obj.deposit_limit = kwargs["deposit_limit"]
            self.obj.created_at = kwargs["created_at"]
            self.obj.updated_at = kwargs["updated_at"]

            self.obj_m.code_movement = self.obj.objects.last()
            self.obj_m.debit_account_amount = kwargs["amount_numeric"]

            self.obj.save()
            self.obj_m.save()
            
            return self.obj

        except Exception as ex:
            logging.ERROR("ERRO AO EFECTUAR DEPOSITO!")
            return ex
