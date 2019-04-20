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
)




def int_to_numeral(integer):
    """
        The heart of the algorithm is python's native 'divmod' function,
        which given inputs x and y returns a tuple containing two elements,
        the quocient and remainder of the division of x/y (both integers):
            divmod(x, y) == (x // y, x % y).

        The function divmods the input by its closest numerical place value,
        repeating until we reach the ones place; each resulting quocient
        corresponds to the index of a given numeral in the numerals tuple.

        The main recursive loop goes like this:

        input = 9999:
          divmod(9999, 1000) = (9, 999)  # 'nove mil'   |  place value == 1000
          divmod(999,  100)  = (9,  99)  # 'novecentos' |  place value == 100
          divmod(99,   10)   = (9,   9)  # 'noventa'    |  place value == 10
          divmod(9,    1)    = (9,   0)  # 'nove'       |  place value == 1


        input = 10000:
          divmod(10000, 10) = (10, 0)    # pass         |  place value == 1000 *

            * stopped here, since values smaller than 20 return
              in one step
    """

    numeral = ''

    if integer < 0:
        integer = abs(integer)
        numeral = 'menos '

    if integer < 20:
        numeral += numerals[0][integer]
    elif integer <= 100:
        if integer == 100:
            numeral += 'cem'
            return numeral
        div = divmod(integer, 10)
        numeral += numerals[1][div[0]]
        if div[1]:
            numeral = numeral + ' e ' + int_to_numeral(div[1])
        return numeral
    elif integer <= 1000:
        if integer == 1000:
            numeral += 'mil'
            return numeral
        div = divmod(integer, 100)
        numeral += numerals[2][div[0]]
        if div[1]:
            numeral = numeral + ' e ' + int_to_numeral(div[1])
        return numeral
    else:
        div = divmod(integer, 1000)
        if div[0] == 1:
            numeral += 'mil'
        else:
            numeral += int_to_numeral(div[0])
            numeral += ' mil'
        if div[1]:
            numeral = numeral + ' e ' + int_to_numeral(div[1])
        return numeral

    return numeral

