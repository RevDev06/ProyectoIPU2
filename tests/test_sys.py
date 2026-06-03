import sys
import os

import pytest

# Esto le dice a Python que suba un nivel en las carpetas para buscar módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import cargar_datos, inventario_global

@pytest.fixture(autouse=True)
def limpiar_inventario():
    """Limpia la lista global antes de cada prueba automáticamente."""
    inventario_global.clear()

def test_sistema_flujo_carga_exitosa(monkeypatch, capsys):
    """Simula a un usuario registrando un Refrigerador completo y regresando al menú."""
    # Secuencia de teclas que presionaría el usuario:
    # 2 (Refri) -> ID -> Marca -> Modelo -> Precio -> Puertas -> Metros -> Pies -> Enter -> 4 (Volver)
    entradas_usuario = iter([
        "2", "R01", "LG", "Inverter", "15000", "2", "12", "18", "", "4"
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(entradas_usuario))
    
    # Ejecutamos la función que controla el submenú
    cargar_datos()
    
    # Verificamos el impacto en el sistema global
    assert len(inventario_global) == 1
    assert inventario_global[0].id == "R01"
    assert inventario_global[0].tipo_gama() == "Gama Media"
    
    # Verificamos la respuesta visual de la consola
    consola = capsys.readouterr()
    assert "Objeto creado correctamente" in consola.out

def test_sistema_validacion_errores(monkeypatch, capsys):
    """Simula a un usuario cometiendo errores al teclear para validar que el sistema no falle."""
    # Intentos: 1 (Lavadora) -> ID vacío -> ID válido -> Letras en precio -> Precio válido ...
    entradas_usuario = iter([
        "1", "", "L02", "Whirlpool", "X1", "abc", "5000", "10", "50", "3", "", "4"
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(entradas_usuario))
    
    cargar_datos()
    consola = capsys.readouterr()
    
    # Verificamos que el sistema detectó los errores, avisó al usuario y no se cerró
    assert "Error: El campo no puede estar vacío" in consola.out
    assert "Error: Entrada inválida. Debe ingresar un número decimal" in consola.out
    # Verificamos que eventualmente el registro fue exitoso
    assert len(inventario_global) == 1