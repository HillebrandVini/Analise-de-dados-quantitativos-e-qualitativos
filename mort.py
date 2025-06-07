import pandas as pd
from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt
import os

lt = os.get_terminal_size().columns

arquivo = ('m.csv')

df = pd.read_csv(arquivo, sep=';', encoding='latin1')

df['Branca'] = pd.to_numeric(df['Branca']).fillna(0)
df['Total'] = pd.to_numeric(df['Total']).fillna(0)

branca = df['Branca'].tolist()
total = df['Total'].tolist()

correlacao, _ = pearsonr(total, branca)

mediaBranca = np.mean(branca)
mediaTotal = np.mean(total)
# Media Branca
# Media Total

m = np.sum((total - mediaTotal) * (branca - mediaBranca)) / np.sum((total - mediaTotal)**2)
# Coeficiente Angular = m => 

b = mediaBranca - m * mediaTotal
# Coeficiente Linear = b =>

y = m * np.array(total) + b

print("")
print(("=" * lt))
print("")
print(f"Correlação = r => {correlacao:.4f}".center(lt))
print("")
print(("=" * lt))
print("")

print(f"Coeficiente de Determinação = r^2 => {correlacao**2:.4f}".center(lt))
print("")
print(("=" * lt))
print("")


print(f"Media Mortalidade Infantil de Crianças Brancas => {mediaBranca:.4f}".center(lt))
print(f"Media Mortalidade Infantil Total => {mediaTotal:.4f}".center(lt))
print("")
print(("=" * lt))
print("")


print(f"Coeficiente Angular = m => {m:.4f}".center(lt))
print("")
print(("=" * lt))
print("")


print((f"Coeficiente Linear = b => {b:.4f}").center(lt))
print("")
print(("=" * lt))
print("")


print((f"Modelo de Regressão Linear: y = {m:.4f} * x + {b:.4f}").center(lt))
print("")
print(("=" * lt))
print("")




plt.figure("Regressão Linear", figsize=(10, 8))
plt.scatter(total, branca, color = 'blue')
plt.plot(total, y, color = 'red', label = f'Modelo de Regressão Linear: y = {m:.2f}x + {b:.2f}')
plt.legend(loc='best', fontsize=17)
plt.title("Regressão Linear - Mortalidade infantil total x Mortalidade infantil de pessoas brancas")
plt.xlabel('Mortalidade infantil total')
plt.ylabel('Mortalidade infantil de crianças brancas')
plt.grid(True)
plt.tight_layout()
plt.show()