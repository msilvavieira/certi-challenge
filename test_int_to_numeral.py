from int_to_numeral import numerals



class TestNumeralsDict(object):
    def test_base_dict(self):
        assert numerals[0] == 'zero'
        assert numerals[1] == 'um'
        assert numerals[2] == 'dois'
        assert numerals[3] == 'três'
        assert numerals[4] == 'quatro'
        assert numerals[5] == 'cinco'
        assert numerals[6] == 'seis'
        assert numerals[7] == 'sete'
        assert numerals[8] == 'oito'
        assert numerals[9] == 'nove'

        assert numerals[10] == 'dez'
        assert numerals[11] == 'onze'
        assert numerals[12] == 'doze'
        assert numerals[13] == 'treze'
        assert numerals[14] == 'quatorze'
        assert numerals[15] == 'quinze'
        assert numerals[16] == 'dezesseis'
        assert numerals[17] == 'dezessete'
        assert numerals[18] == 'dezoito'
        assert numerals[19] == 'dezenove'

        assert numerals[20] == 'vinte'
        assert numerals[30] == 'trinta'
        assert numerals[40] == 'quarenta'
        assert numerals[50] == 'cinquenta'
        assert numerals[60] == 'sessenta'
        assert numerals[70] == 'setenta'
        assert numerals[80] == 'oitenta'
        assert numerals[90] == 'noventa'

        assert numerals[100] == 'cem'
        assert numerals[200] == 'duzentos'
        assert numerals[300] == 'trezentos'
        assert numerals[400] == 'quatrocentos'
        assert numerals[500] == 'quinhentos'
        assert numerals[600] == 'seiscentos'
        assert numerals[700] == 'setecentos'
        assert numerals[800] == 'oitocentos'
        assert numerals[900] == 'novecentos'

        assert numerals[1000] == 'mil'

