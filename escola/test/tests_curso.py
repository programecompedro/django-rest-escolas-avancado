from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso="Curso de Teste 1", descricao="Descrição de um curso de teste1", nivel = "B"
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso="Curso de Teste 2", descricao="Descrição de um curso de teste2", nivel = "B"
        )
        self.curso_3 = Curso.objects.create(
            codigo_curso="Curso de Teste 3", descricao="Descrição de um curso de teste3", nivel = "B"
        )
    def test_falhador(self):
        self.fail("Teste falhou de propósito")