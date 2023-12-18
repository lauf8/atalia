from django.test import TestCase

from ..models import Entidade, Membro, Patrimonio
from django.contrib.auth.models import User


class MembroModelTest(TestCase):


    def setUp(self):
        self.entidade = Entidade.objects.create(nome='Sample Entidade')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.membro = Membro.objects.create(
        nome = 'LAUF-8',
        data_nascimento ='2023-01-01',
        endereco ='Rua de Caculé',
        celular = '88 8965852',
        parentesco_maconico = 'SEM_PARENTESCO',
        user = self.user,
        entidade = self.entidade
        )

    def test_membro_has_name(self):
        self.assertEqual(self.membro.nome, 'LAUF-8')
    
    def test_membro_has_address(self):
        self.assertEqual(self.membro.endereco, 'Rua de Caculé')
    
    def test_membro_is_active(self):
        self.assertEqual(self.membro.ativo, True)

    def test_membro_has_phone(self):
        self.assertEqual(self.membro.celular, '88 8965852')
    
    def test_membro_has_kinship(self):
        self.assertEqual(self.membro.parentesco_maconico, 'SEM_PARENTESCO')

    def test_membro_has_user(self):
        self.assertEqual(self.membro.user, self.user)
    
    def test_membro_has_entidade(self):
        self.assertEqual(self.membro.entidade, self.entidade)
    
    def test_membro_has_birth(self):
        self.assertEqual(self.membro.data_nascimento, '2023-01-01')



class MembroModelTest(TestCase):

    def setUp(self):
        self.entidade = Entidade.objects.create(nome='Sample Entidade')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.patrimonio = Patrimonio.objects.create(
        nome = 'Capas',
        quantidade = 50,
        user = self.user,
        entidade = self.entidade
        )

    def test_patrimonio_has_name(self):
        self.assertEqual(self.patrimonio.nome, 'Capas')

    def test_patrimonio_has_amount(self):
        self.assertEqual(self.patrimonio.quantidade, 50)

    def test_patrimonio_has_user(self):
        self.assertEqual(self.patrimonio.user, self.user)
    
    def test_patrimonio_has_entidade(self):
        self.assertEqual(self.patrimonio.entidade, self.entidade)


