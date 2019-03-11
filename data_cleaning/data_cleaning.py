"""
OBSERVATORIO DE SANEAMENTO E MEIO AMBIENTE DO RECIFE (OSAR)
Projeto DataSanear - sistematizacao de dados de saneamento na cidade do Recife

Claudio Alves Monteiro
claudioalvesmonteiro.github.io
"""

# importar pacotes
import pandas as pd

#===== importar dados =====#

# SNIS
dataSNIS = pd.ExcelFile('original_data/SNIS_serie_Recife.xlsx')
dataSNIS = dataSNIS.parse(0)

# Plantas Agamenom
dataArbAga = pd.ExcelFile('original_data/plantas_agamenom.xls')
dataArbAga = dataArbAga.parse(0)

# IBGE Censos 2000 e 2010
ibgeAgua2000 = pd.ExcelFile('original_data/IBGE/abastecimento_agua-CENSO2000.xls')
ibgeAgua2000 = ibgeAgua2000.parse(0)

ibgeLixo2000 = pd.ExcelFile('original_data/IBGE/destino_lixo-CENSO2000.xls')
ibgeLixo2000 = ibgeLixo2000.parse(0)

ibgeAguaLixo2010 = pd.ExcelFile('original_data/IBGE/abastecimento_agua-destino_lixo-CENSO2010.xls')
ibgeAguaLixo2010 = ibgeAguaLixo2010.parse(0)

ibgeEsgoto2000 = pd.ExcelFile('original_data/IBGE/esgotamento-CENSO2000.xls')
ibgeEsgoto2000 = ibgeEsgoto2000.parse(0)

ibgeEsgoto2010 = pd.ExcelFile('original_data/IBGE/esgotamento-CENSO2010.xls')
ibgeEsgoto2010 = ibgeEsgoto2010.parse(0)