import pandas as pd

populacao_cidades = pd.Series(['Itapevi', 'Rio de Janeiro','Belo Horizonte', \
    'Santo André', 'Itaquaquecetuba','Carapicuiba','Barueri','Itu', \
     'São Paulo'])

populacao = pd.Series([260000,6700000, 2700000, 375000,
                      400000, 276000, 175000, 12000000])

data_frame = pd.DataFrame({'Cidade': cidades, 'População': populacao})

print(data_frame)

populacao_cidades = dict(zio(cidades, populacao))

print(populacao_cidades)

print(type(populacao_cidades))

print(populacao_cidades['Itu'])

print('Belo Horizonte' in populacao_cidades)

data_frame.to_csv("C:\\treino\\projeto_pandas\\data_frame.csv")
data_frame.to_csv("data_frame.csv")

cidades_populacao = pd.read_csv("data_frame.csv", index_col = 0)

print(cidades_populacao)
print(cidades_populacao.info())
print(cidades_populacao.columns)
print(cidades_populacao.index)
print(cidades_populacao.head(3))
print(cidades_populacao.describe())
print(cidades_populacao.tail())
