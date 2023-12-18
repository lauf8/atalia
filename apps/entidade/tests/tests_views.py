from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Membro, Entidade
from ..forms import MemberForm  # Assuming you have a form for creating members

class CreateMemberViewTest(TestCase):

    def setUp(self):
        # Create a sample Entidade
        self.entidade = Entidade.objects.create(nome='Sample Entidade')

        # Create a sample User
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_member_view_get(self):
        # Test that the view returns a 200 status code for a GET request
        url = reverse('create_member')  # Replace 'create_member' with the actual name or URL of your view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_member_view_post_valid_data(self):
        # Test that the view creates a member for valid POST data
        url = reverse('create_member')  # Replace 'create_member' with the actual name or URL of your view
        self.client.login(username='testuser', password='testpass')
        form_data = {
            'entidade': self.entidade.id,
            'nome': 'John Doe',
            'data_nascimento': '2000-01-01',
            'endereco': 'Sample Address',
            'celular': '+1234567890',  # Replace with an actual phone number
            'parentesco': 'FILHO',
        }
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful form submission
        created_member = Membro.objects.get(nome='John Doe')
        self.assertEqual(created_member.entidade, self.entidade)
        self.assertEqual(created_member.user, self.user)

    def test_create_member_view_post_invalid_data(self):
        # Test that the view handles invalid POST data
        url = reverse('create_member')  # Replace 'create_member' with the actual name or URL of your view
        self.client.login(username='testuser', password='testpass')
        invalid_form_data = {
            'entidade': self.entidade.id,
            'nome': '',  # Invalid: Name is required
            'data_nascimento': '2000-01-01',
            'endereco': 'Sample Address',
            'celular': '+1234567890',  # Replace with an actual phone number
            'parentesco': 'FILHO',
        }
        response = self.client.post(url, invalid_form_data)
        self.assertEqual(response.status_code, 200)  # Expecting a re-render of the form
        self.assertContains(response, 'This field is required.')  # Assuming the name field is required

# Add more test cases as needed...
