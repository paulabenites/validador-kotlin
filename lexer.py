import ply.lex as lex




token = (
    'INT', 'DOUBLE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'TAB', 'newline',
    'EQUALS', 'DOSPUNTOS', 'COMA','STRING',
    'PUNTO','PUNTOS','CADENA_DE_CARACTERES', 'EQUAL', 'NOTEQ', 'LARGE', 'SMALL', 'LRGEQ', 'SMLEQ', 'ID', 'FALSO',
    'VERDAD', 'IPAR', 'DPAR', "INDENT","Int",'Double','Boolean','AND','NOT','OR','NEGATION','ILLAVE','DLLAVE',
    'VAL','VAR','LISTOF',"SETOF","MAPOF","STEP","IN"
)

reserveda= ('ELSE','IF','RETURN','PRINT','println','ISEMPTY' ,'WHILE','FOR','FUN',"values",'TO','READLINE')

tokens=token+reserveda
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_ILLAVE    = r'\{'
t_DLLAVE    = r'\}'
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

# t_VAR= r'var'
# t_VAL= r'val'



# Reglas de correspondencia

def t_values(token):
    r'values\s'
    token.value = str(token.value)
    return token

def t_VAR(token):
    r'var\s'
    token.value = str(token.value)
    return token

def t_VAL(token):
    r'val\s'
    token.value = str(token.value)
    return token

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_Int(token):
    r'Int'
    token.value = str(token.value)
    return token


def t_STRING(token):
    r'String=\String\s'
    token.value = str(token.value)
    return token




def t_Double(token):
    r'Double=|Double\s'
    token.value = str(token.value)
    return token


def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value[::])
    return t


def t_Boolean(token):
    r'Boolean=|Boolean\s'
    token.value = str(token.value)
    return token


def t_VERDAD(token):
    r'true\s'
    token.value = str(token.value)
    return token


def t_FALSO(token):
    r'false\s'
    token.value = str(token.value)
    return token


def t_SIZE(token):
    r'size\s'
    token.value = str(token.value)
    return token

def t_ISEMPTY(token):
    r'isEmpty'
    token.value = str(token.value)
    return token

def t_TO(token):
    r'to\s'
    token.value = str(token.value)
    return token

def t_READLINE(token):
    r'readLine'
    token.value = str(token.value)
    return token

def t_WHILE(token):
    r'while\s'
    token.value = str(token.value)
    return token


def t_LISTOF(token):
    r'listOf'
    token.value = str(token.value)
    return token

def t_SETOF(token):
    r'setOf'
    token.value = str(token.value)
    return token

def t_MAPOF(token):
    r'mapOf'
    token.value = str(token.value)
    return token


def t_println(token):
    r'println'
    token.value = str(token.value)
    return token

def t_PRINT(token):
    r'print'
    token.value = str(token.value)
    return token


def t_RETURN(token):
    r'return\s'
    token.value = str(token.value)
    return token

def t_FOR(token):
    r'for'
    token.value = str(token.value)
    return token

def t_FUN(token):
    r'fun'
    token.value = str(token.value)
    return token



def t_STEP(token):
    r'step\s'
    token.value = str(token.value)
    return token


def t_IN(token):
    r'in\s'
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











# Error handling rule
def t_error(token):
    print("Error caracter no definido en token:'%s'" % token.value[0])
    token.lexer.skip(1)
    return token


# Codigo para leer Archivo

file =open("EjemplosBenites.txt", "r")
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