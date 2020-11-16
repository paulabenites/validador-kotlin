import ply.lex as lex




token = (
    'INT', 'DOUBLE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'TAB', 'newline',
    'EQUALS', 'DOSPUNTOS', 'COMA',
    'PUNTO','PUNTOS','CADENA_DE_CARACTERES', 'EQUAL', 'NOTEQ', 'LARGE', 'SMALL', 'LRGEQ', 'SMLEQ', 'ID', 'FALSO',
    'VERDAD', 'IPAR', 'DPAR', "INDENT","Int",'Double','Boolean','AND','NOT','OR','NEGATION','ILLAVE','DLLAVE',
    'VAL','VAR'
)

reserveda= ('ELSE','IF','RETURN','PRINT', 'WHILE','DEF')

tokens=token+reserveda
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_IPAR  = r'\('
t_DPAR  = r'\)'
t_EQUALS  = r'='
t_DOSPUNTOS = r':'
t_PUNTO     =r'\.'
t_COMA      =r'\,'
t_CADENA_DE_CARACTERES = r'(\".*\"|[a-zA-Z]+\s*)'
t_TAB       =r'\t'
t_ignore_COMMENT = r'\/\/.*'
t_EQUAL   = r'\=\='
t_NOTEQ   = r'\!\='
t_LARGE   = r'\>'
t_SMALL   = r'\<'
t_LRGEQ   = r'\>\='
t_SMLEQ   = r'\<\='
t_AND = r'\&\&'
t_OR  = r'\|\|'
t_NEGATION=r'\!'


# Reglas de correspondencia

def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value[::])
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_Int(token):
    r'Int'
    token.value = str(token.value)
    return token


def t_Double(token):
    r'Double'
    token.value = str(token.value)
    return token


def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value[::])
    return t


def t_Boolean(token):
    r'Boolean'
    token.value = str(token.value)
    return token


def t_VERDAD(token):
    r'true'
    token.value = str(token.value)
    return token


def t_FALSO(token):
    r'false'
    token.value = str(token.value)
    return token

def t_VAL(token):
    r'val'
    token.value = str(token.value)
    return token


def t_VAR(token):
    r'var'
    token.value = str(token.value)
    return token


def t_PRINT(token):
    r'print$'
    token.value = str(token.value)
    return token


def t_println(token):
    r'println'
    token.value = str(token.value)
    return token


def t_RETURN(token):
    r'return'
    token.value = str(token.value)
    return token


def t_ID(token):
    '([a-zA-Z_][a-zA-Z0-9_]*)'
    token.value = str(token.value)
    return token


def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

def t_whitespace(token):
    r'\s+'
    pass

def t_FUN(token):
    r'fun'
    token.value = str(token.value)
    return token

def t_FOR(token):
    r'for'
    token.value = str(token.value)
    return token
def t_STEP(token):
    r'step'
    token.value = str(token.value)
    return token

def t_IN(token):
    r'in'
    token.value = str(token.value)
    return token



# Codigo para leer Archivo

file =open("codigo.txt", "r")
if file.mode=="r":
    datos=file.read()


lexer = lex.lex()


def leerLexer1():
    lexer.input(datos)
    while True:
        tk = lexer.token()
        if not tk:
            break
        print(str(tk))
leerLexer1()