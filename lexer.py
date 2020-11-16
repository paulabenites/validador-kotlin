import ply.lex as lex




token = (
    'INT', 'DOUBLE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'TAB', 'newline',
    'EQUALS', 'DOSPUNTOS', 'COMA',
    'PUNTO','PUNTOS','CADENA_DE_CARACTERES', 'EQUAL', 'NOTEQ', 'LARGE', 'SMALL', 'LRGEQ', 'SMLEQ', 'ID', 'FALSO',
    'VERDAD', 'IPAR', 'DPAR', "INDENT","Int",'Double','Boolean','AND','NOT','OR','NEGATION','ILLAVE','DLLAVE',
    'VAL','VAR'
)


















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