from django.test import TestCase
from .models import Perro
# Create your tests here.

class TesPerro(TestCase):
    def test_perro_nombre(self):
        #Arrange
        Perro.objects.create(Nombre='DonPerro',Raza='kiltro',Caracteristicas='es negro y blanco pero no es transparente',estado='Rescatado')
        Perre = Perro.objects.get(Nombre='DonPerro')

        expected = 'DonPerro'

        #Act

        result = Perre.Nombre 

        #Assert

        self.assertEqual(expected, result)
        print('Resultado: ' + expected)
        print('Resultado correcto: ' + result)

""" ----------------------------------------------------------------------------------------------------------------------------------------- """
class TesPerroRaza(TestCase):
    def test_perro_razaEstado(self):
        #Arrange
        Perro.objects.create(Nombre='DonPerro',Raza='kiltro',Caracteristicas='es negro y blanco pero no es transparente',estado='Rescatado')
        Perre = Perro.objects.get(estado='Rescatado')

        expected = 'Rescatado'

        #Act

        result = Perre.estado

        #Assert

        self.assertEqual(expected, result)
        print('Resultado: ' + expected)
        print('Resultado correcto: ' + result)