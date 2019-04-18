numerals = (
    ("zero", "um", "dois", "três", "quatro", 
     "cinco", "seis", "sete", "oito", "nove",
     "dez", "onze", "doze", "treze", "quatorze", 
     "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",),

    ("", "", "vinte", "trinta", "quarenta", "cinquenta",
     "sessenta", "setenta", "oitenta", "noventa",),

    ("", "cento", "duzentos", "trezentos", "quatrocentos",
     "quinhentos", "seiscentos", "setecentos", "oitocentos",
     "novecentos",),

    #("mil",),
)




def int_to_numeral(integer):

    numeral = ''

    def parse_tens(integer):
        numeral = ''
        if integer < 20:
            numeral =  numerals[0][integer]
        else:
            div = divmod(integer, 10)
            numeral = numerals[1][div[0]]
            if div[1] != 0:
                numeral += ' e '
                numeral += numerals[0][div[1]]
        return numeral

    def parse_hundreds(integer):
        numeral = ''
        if integer == 0:
            pass
        elif integer < 100:
            numeral = parse_tens(integer)
        elif integer == 100:
            numeral = 'cem'
        elif integer % 100 == 0:
            numeral = numerals[1][integer / 100]
        else:
            div = divmod(integer, 100)
            numeral = numerals[2][div[0]]
            if numeral:
                numeral += ' e '
            numeral += parse_tens(div[1])
        return numeral

    def parse_thousands(integer):
        numeral = ''
        if integer == 1000:
            numeral = 'mil'
        else:
            div = divmod(integer, 1000)
            if div[0] == 1:
                numeral = 'mil '
            elif div[0] < 20:
                numeral = parse_tens(div[0])
                numeral += ' mil '
            else:
                numeral = parse_hundreds(div[0])
                numeral += ' mil '
            if div[1] < 100 and div[1] > 0:
                numeral += 'e '
            numeral += parse_hundreds(div[1])
        return numeral

    minus = False
    if integer < 0:
        integer = abs(integer)
        minus = True
    if integer < 100:
        numeral = parse_tens(integer)
    elif integer < 1000:
        numeral = parse_hundreds(integer)
    else:
        numeral = parse_thousands(integer)

    numeral = numeral.strip()
    if minus:
        numeral = 'menos ' + numeral
    return numeral

