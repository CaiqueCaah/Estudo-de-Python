# CORES
# STYLE         TEXT            BACK
# 0 NONE        30 BRANCO       40 BRANCO
# 1 BOLD        31 VERMELHO     41 VERMELHO
# 4 UNDERLINE   32 VERDE        42 VERDE
# 7 NEGATIVE    33 AMARELO      43 AMARELO
#               34 AZUL CLARO   44 AZUL CLARO
#               35 ROXO         45 ROXO
#               36 AZUL BB      46 AZUL BB
#               37 CINZA        47 CINZA
#
# \033[4;33;44mTEXTO A FICAR COLORIDO {SEQUENCIA PARA COLOCAR COR}
palavra = str('CAIQUE GONÇALVES DA SILVA')
print('\033[1;37;43m{}\033[m'.format(palavra))
print('\033[4;30;45mOlá, Mundo !!\033[m')
print('Olá, {}{}{} prazer em te conhecer !!!'.format('\033[4;31m', palavra, '\033[m'))

cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'amareloVerde': '\033[33;42m',
    'azulbb': '\033[36m'
}
print('Olá {}{}{}, tudo bem ? '.format(cores['vermelho'], palavra, cores['azulbb']))
