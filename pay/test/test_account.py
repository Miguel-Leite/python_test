import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import django
django.setup()
import unittest
from graphene_django.utils.testing import graphql_query

from pay.app.repository.accountrepository import AccountRepositoryDB

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.run = AccountRepositoryDB()

    def test_account(self):
        account = self.run.save({'account_status': 'teste_status', 'account_purpose': 'teste_purpose','account_description': 'teste_description'})
        print(account)
        self.assertTrue(account)
