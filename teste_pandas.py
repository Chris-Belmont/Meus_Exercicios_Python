import pandas as pd
dados = {'Nome': ['Ana', 'Bruno', 'Clara'], 'Idade': [20, 25, 30], 'Cidade': ['São Paulo', 'Rio', 'Salvador']}
df = pd.DataFrame(dados)
print(df)
print("\nMédia das idades:", df['Idade'].mean())