from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

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
    #def test_falhador(self):
        #self.fail("Teste falhou de propósito")

    def test_requisicao_get_listar_cursos(self):
        """Teste para verificar requisição GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post(self):
        """Teste para verificar requisição POST para criar cursos"""
        data = {
            'codigo_curso': 'CCV',
            'descricao': 'Curso Teste criado',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)