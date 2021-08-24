import logging
from pay.models import Moviment

class MovimentRepositoryDB:

    def __init__(self):
        self.moviment = Moviment()

    # @classmethod
    def _save(self, **kwargs):
        try:
            self.moviment.code_movement = kwargs["code_movement"]
            self.moviment.debit_account_number = kwargs["code_account_number"]
            self.moviment.credit_account_number = kwargs["credit_account"]
            self.moviment.bank_debit_code = kwargs["bank_debit_code"]
            self.moviment.bank_credit_code = kwargs["bank_credit_code"]
            self.moviment.amount_movement = kwargs["amount_movement"]
            self.moviment.data_movement = kwargs["data_moviment"]
            self.moviment.data_validate_movement = kwargs["data_validate_movement"]
            self.moviment.description = kwargs["description"]
            self.moviment.n_cheque = kwargs["n_cheque"]
            self.moviment.rubric = kwargs["rubric"]
            self.moviment.responsible_movement = kwargs["responsible_movement"]
            self.moviment.save()


            return self.moviment

        except Exception as ex:
            logging.ERROR("ERRO AO CADASTRAR MOVIMENTO")
            return ex