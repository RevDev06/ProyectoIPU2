import pytest
from main import Lavadora, mostrar_datos, InventarioVacio, inventario_global

# Fixture para limpiar la lista global antes de cada prueba automáticamente
@pytest.fixture(autouse=True)
def limpiar_inventario():
    inventario_global.clear()

def test_integracion_clase_herencia_gama():
    """Verifica que la clase Lavadora herede de Electrodomestico y calcule la Gama correctamente."""
    lavadora = Lavadora("L100", "Mabe", "AquaSaver", 8000.50, 12, 60, 4)
    
    # Verificamos la lógica de cálculo
    assert lavadora.tipo_gama() == "Gama Media"
    # Verificamos que el método __str__ integre los datos del padre y el hijo
    assert "Mabe" in str(lavadora)
    assert "Tipo Gama: Gama Media" in str(lavadora)

def test_integracion_mostrar_inventario_vacio():
    """Verifica que mostrar_datos lance la excepción personalizada si no hay aparatos."""
    with pytest.raises(InventarioVacio) as excinfo:
        mostrar_datos(inventario_global)
    
    assert "El inventario está vacío" in str(excinfo.value)