import pytest
from unittest.mock import patch
from faturamento import faturamento, main

class TestFaturamento(unittest.TestCase):

    def test_faturamento(self):
        
        faturamento_diario = [1000, 1500, 2000, 0, 2500, 3000, 100, 500, 0, 4500, 1200, 800, 1800, 0, 4000]
        menor, maior, dias_acima_media = faturamento(faturamento_diario)

        self.assertEqual(menor, 100)
        self.assertEqual(maior, 4500)
        self.assertEqual(dias_acima_media, 6)

    @patch('builtins.input', side_effect=["1000 1500 2000 0 2500 3000 100 500 0 4500 1200 800 1800 0 4000"])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        main()
        
        # Checa se os valores corretos foram impressos
        mock_print.assert_any_call("Menor faturamento: 100.0")
        mock_print.assert_any_call("Maior faturamento: 4500.0")
        mock_print.assert_any_call("Número de dias com faturamento acima da média: 6")

if __name__ == "__main__":
    unittest.main()
