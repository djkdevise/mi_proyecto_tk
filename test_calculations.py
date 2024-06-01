import unittest
from src.logic.calculations import add # Importa la función add directamente desde calculations.py

class TestCalculations(unittest.TestCase):
    def test_add(self):
        # Prueba la función add con valores conocidos
        self.assertEqual(add(1, 2), 3)  # Esperamos que 1 + 2 sea igual a 3

if __name__ == "__main__":
    unittest.main()