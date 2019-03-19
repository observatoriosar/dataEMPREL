"""
OBSERVATORIO DE SANEAMENTO E MEIO AMBIENTE DO RECIFE (OSAR)
Projeto DataSanear - sistematizacao de dados de saneamento na cidade do Recife

Claudio Alves Monteiro
claudioalvesmonteiro.github.io
"""

# importar pacotes
import pandas as pd
import unidecode

#===== importar dados =====#

# SNIS
#dataSNIS = pd.ExcelFile('original_data/SNIS_serie_Recife.xlsx').parse(0)

# Plantas Agamenom
#dataArbAga = pd.ExcelFile('original_data/plantas_agamenom.xls').parse(0)

# IBGE Censos 2000 e 2010
ibgeAgua2000 = pd.ExcelFile('original_data/IBGE/abastecimento_agua-CENSO2000.xls').parse(0)
ibgeLixo2000 = pd.ExcelFile('original_data/IBGE/destino_lixo-CENSO2000.xls').parse(0)
ibgeAguaLixo2010 = pd.ExcelFile('original_data/IBGE/abastecimento_agua-destino_lixo-CENSO2010.xls').parse(0)
ibgeEsgoto2000 = pd.ExcelFile('original_data/IBGE/esgotamento-CENSO2000.xls').parse(0)
ibgeEsgoto2010 = pd.ExcelFile('original_data/IBGE/esgotamento-CENSO2010.xls').parse(0)


#===========================#
# Padronizacao
#===========================#

#----- funcao para padronizar nomes das variaveis -----#
def standVarName(frase):
    """ transforma \n ou " " em _
        nao incorpora " " seguidos
        retira caracteres latinos (acentos)
        caixa baixa
    """
    std_string = ""
    prev_chr = ""
    if isinstance(frase, str):
        for caracter in frase:
            if caracter == "\n" or caracter == " " and prev_chr != " ":
                std_string += "_"
            elif caracter != " " and caracter != "\n":
                std_string += unidecode.unidecode(caracter) # tratar " " seguindo de caracter
            # verifica se ultimos dois caracteres sao "__" e retorna string
            elif (std_string[len(std_string)-2:len(std_string)]) == "__":
                    return std_string[0:len(std_string)-1].lower()
            prev_chr = caracter
    return std_string[0:len(std_string)-1].lower()

test = "Caçamba de serviço de limpeza"
print(standVarName(test))

x = df.loc[[4]].values.flatten().tolist()
for i in x: print(standVarName(i))


#----------------------
# ibgeAgua2000

df=ibgeAgua2000

def stdData0(df):
    """ Padronizar banco de dados ibgeAgua200
    """
    # lista com os codigos das colunas
    str_ange = list( range(0, (df.shape[1])))
    # renomear colunas
    df.columns = [str(i) for i in str_ange]

    # capturar nomes
    NomesColunas = dataCVM.loc[[0]].values.flatten().tolist()

    return ""
    """ IF TOTAL: PEGAR NOME CELULA ACIMA
    """

df = ibgeAgua2000
def stdIBGEagua200(df):
    # capturar nomes das variaveis
    var_name = ["localidade"]
    var_name.append(df[])


#========================#
# Combinacao
#========================#
