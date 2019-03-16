"""
OBSERVATORIO DE SANEAMENTO E MEIO AMBIENTE DO RECIFE (OSAR)
Projeto DataSanear - sistematizacao de dados de saneamento na cidade do Recife

Claudio Alves Monteiro
claudioalvesmonteiro.github.io
"""

# importar pacotes
import pandas as pd
import unidecode

# unaccented_string contains 'Malaga'and is of type 'str
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

#
df=ibgeAgua2000
def numVarName(df)):
    str_ange = range(0, df.length())
    

#===========================#
# Padronizacao
#===========================#

# funcao para padronizar nomes das variaveis
def standVarName(frase):
    std_string = ""
    for caracter in frase:
        if caracter == " ":
            std_string += "_"
        else:
            std_string += unidecode.unidecode(caracter)
    return std_string.lower()

test = "Caçamba de serviço de limpeza"
print(standVarName(test))

#----------------------
# ibgeAgua2000

df = ibgeAgua2000 
def stdIBGEagua200(df):
    # capturar nomes das variaveis
    var_name = ["localidade"]
    var_name.append(df[])




pd.options.display.max_columns = 50
pd.options.display.max_rows = 50
print(ibgeAgua2000) 

#========================#
# Combinacao
#========================#
