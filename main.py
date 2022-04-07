import ply.lex as lex

tokens = ('COMMAND', "LCBRACKET", "RCBRACKET", "PROPS", "TEXT")

#################################
############ TOKENS #############
# Tokeny mozna definiowac jako zmienna i jako metoda

t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
t_PROPS = r'\{(\w+)\}'


def t_COMMAND(token):
    r'\\(\w+)\s*'
    token.value = str (token.value).strip()
    return token


def t_TEXT(token):
    r'[A-Za-z,;\'"\s]+'
    return token


# def t_WHITECHARS(token):
#     r'\s+'
#     return token


# New line rule
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Comment rule
def t_COMMENT(t):
    r'%.*'
    pass


# Column finding rule
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

input = """
\\begin{enumerate}
    \\item sample text
"""

lexer.input(input)

nextToken = lexer.token()
while nextToken is not None:
    print(nextToken)
    nextToken = lexer.token()


