import unittest
from unittest.mock import patch
from main import (
    limpiar_pantalla, leer_cadena, leer_medidas, leer_float, leer_entero,
    mostrar_datos, cargar_datos, InventarioVacio, Electrodomestico,
    Lavadora, Refrigerador, Microondas, inventario_global
)

class TestFuncionesClases(unittest.TestCase):

    """
      Pruebas unitarias para funciones de entrada
    """

    @patch('os.system')
    def test_limpiar_pantalla(self, mock_os):
        #Evalua que se llama a os.system con el comando correcto 
        limpiar_pantalla()
        mock_os.assert_called_once()

    @patch('builtins.input', side_effect=['', 'M@rca Invalida!', 'Marca_Valida-123'])
    def test_leer_cadena(self, mock_input):
        #Evalua caso nulo (''), caso con simbolos invalidos y caso de exito.
        resultado = leer_cadena("Ingrese dato: ")
        self.assertEqual(resultado, 'Marca_Valida-123')
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['', '80x90', '80x90x80.5'])
    def test_leer_medidas(self, mock_input):
        #Evalua caso vacio, caso con formato incorrecto y caso de exito.
        resultado = leer_medidas("Medidas: ")
        self.assertEqual(resultado, '80x90x80.5')
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['', 'abc', '-50.5', '0', '1500.50'])
    def test_leer_float(self, mock_input):
        #Evalua caso vacio, caso con texto, caso con negativo, caso con cero y caso de exito
        resultado = leer_float("Precio: ")
        self.assertEqual(resultado, 1500.50)
        self.assertEqual(mock_input.call_count, 5)

    @patch('builtins.input', side_effect=['', 'abc', '-5', '0', '10'])
    def test_leer_entero(self, mock_input):
        resultado = leer_entero("Cantidad: ")
        self.assertEqual(resultado, 10)
        

    """
    PRUEBAS UNITARIAS PARA CLASES ELECTRODOMESTICOS
    """

    def test_Electrodomestico(self):
        #Evalua la correcta creacion del objeto padre y su representacion en texto
        elec = Electrodomestico("A01", "LG", "X100", 5000.0)
        self.assertEqual(elec.id, "A01")
        self.assertIn("ID: A01, Marca: LG", str(elec))

    def test_Lavadora_tipo_gama(self):
        #Evalua los limites para Gama Baja, Media y Alta
        lav_baja = Lavadora("L1", "Mabe", "A", 3000, 10, 50, 3)
        self.assertEqual(lav_baja.tipo_gama(), "Gama Baja")

        lav_media = Lavadora("L2", "Whirlpool", "B", 6000, 15, 60, 5)
        self.assertEqual(lav_media.tipo_gama(), "Gama Media")

        lav_alta = Lavadora("L3", "Samsung", "C", 12000, 20, 70, 10)
        self.assertEqual(lav_alta.tipo_gama(), "Gama Alta")

    def test_Refrigerador_tipo_gama(self):
        #Evalua las condiciones combinadas de puertas y tamaño para las distintas gamas
        refri_baja = Refrigerador("R1", "Hisense", "X", 4000, 1, 10, 9)
        self.assertEqual(refri_baja.tipo_gama(), "Gama Baja")

        refri_media = Refrigerador("R2", "LG", "Y", 8000, 2, 13, 14)
        self.assertEqual(refri_media.tipo_gama(), "Gama Media")

        refri_alta = Refrigerador("R3", "Samsung", "Z", 15000, 3, 20, 25)
        self.assertEqual(refri_alta.tipo_gama(), "Gama Alta")

    def test_Microondas_tipo_gama(self):
        #Evalua los rangos de potencia segun los topes definidos
        micro_baja = Microondas("M1", "Daewoo", "W", 1000, 800, 10, "30x20x30")
        self.assertEqual(micro_baja.tipo_gama(), "Gama Baja")

        micro_media = Microondas("M2", "LG", "X", 2000, 1500, 15, "40x30x40")
        self.assertEqual(micro_media.tipo_gama(), "Gama Media")

        micro_alta = Microondas("M3", "Panasonic", "Y", 3500, 1600, 20, "50x40x50")
        self.assertEqual(micro_alta.tipo_gama(), "Gama Alta")


    """
    PRUEBAS UNITARIAS PARA MENU Y LISTA DE INVENTARIO
    """

    @patch('builtins.print')
    def test_mostrar_datos(self, mock_print):
        #Evalua caso de error (se arroja el error cuando la lista esta vacia)
        with self.assertRaises(InventarioVacio):
            mostrar_datos([])
        
        #Evalua el caso de exito (se arroja el inventario sin el error)
        micro = Microondas("M1", "M", "Mod", 100, 800, 10, "1x1x1")
        mostrar_datos([micro])
        self.assertGreaterEqual(mock_print.call_count, 2)

    @patch('builtins.input', side_effect=['4'])
    def test_cargar_datos(self, mock_input):
        #Evalua que la opcion de salida rompa el ciclo
        cargar_datos()
        mock_input.assert_called_with("Seleccione: ")

if __name__ == '__main__':
    unittest.main()