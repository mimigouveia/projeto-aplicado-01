import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === CONFIGURAÇÃO ===
arquivo = "Sexo.csv"

# === LER O CSV ===
df = pd.read_csv(arquivo, sep=",", encoding="utf-8")

# === RENOMEAR COLUNAS (opcional, só para simplificar) ===
df = df.rename(columns={
    "Região": "Regiao",
    "Categoria 1": "Categoria",
    "Matrículas": "Matriculas"
})

# === LIMPEZA ===
df = df.dropna(subset=["Regiao", "Categoria", "Matriculas"])
df["Matriculas"] = pd.to_numeric(df["Matriculas"], errors="coerce")
df = df.dropna(subset=["Matriculas"])

# === ESTATÍSTICAS GERAIS ===
print("\n📊 Estatísticas gerais das matrículas por categoria:")
print(df.groupby("Categoria")["Matriculas"].describe())

print("\n📊 Estatísticas gerais das matrículas por região:")
print(df.groupby("Regiao")["Matriculas"].describe())

print("\n📊 Total de matrículas por região e categoria:")
print(df.groupby(["Regiao", "Categoria"])["Matriculas"].sum())

# === VISUALIZAÇÕES ===

# 1️⃣ Total de matrículas por categoria administrativa
plt.figure(figsize=(6,4))
sns.barplot(data=df, x="Categoria", y="Matriculas", estimator="sum", ci=None, palette="Set2")
plt.title("Total de Matrículas por Sexo")
plt.xlabel("Categoria")
plt.ylabel("Total de Matrículas")
plt.tight_layout()
plt.show()

# 2️⃣ Total de matrículas por região
plt.figure(figsize=(8,4))
sns.barplot(data=df, x="Regiao", y="Matriculas", estimator="sum", ci=None, palette="Set3")
plt.title("Total de Matrículas por Região")
plt.xlabel("Região")
plt.ylabel("Total de Matrículas")
plt.tight_layout()
plt.show()

# 3️⃣ Gráfico combinado: regiões x categoria administrativa
plt.figure(figsize=(10,5))
sns.barplot(data=df, x="Regiao", y="Matriculas", hue="Categoria", estimator="sum", ci=None, palette="coolwarm")
plt.title("Matrículas por Região e Sexo")
plt.xlabel("Região")
plt.ylabel("Total de Matrículas")
plt.legend(title="Categoria")
plt.tight_layout()
plt.show()