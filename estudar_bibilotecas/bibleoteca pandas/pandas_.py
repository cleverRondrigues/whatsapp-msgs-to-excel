import pandas as pd

dados = {
    'nome': ['pedro', 'joão', 'paulo'],
    'idade': [20,30,12],
}
df = pd.DataFrame(dados)
print(df)