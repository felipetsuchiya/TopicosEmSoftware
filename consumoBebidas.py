#  Trabalho de Topicos em Software - Felipe, Graziela, Gustavo, Yuri 
#  Analise de consumo de bebida alcoolica no mundo 
#  

# Importar bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
def main():
    df = pd.read_csv("drinks.csv")  # Lendo arquivo

    df = df.rename(columns={
        "country": "País",
        "total_litres_of_pure_alcohol": "Consumo de Álcool Puro",
        "spirit_servings": "Consumo de Bebida Destilada",
        "wine_servings": "Consumo de Vinho",
        "beer_servings": "Consumo de Cerveja"
    })

    turnOn = True

    while(turnOn):
        # Exibir opções para o usuário
        print("Escolha uma opção:")
        print("1. Países que mais consomem bebidas alcoólicas no mundo")
        print("2. Países onde o álcool é proibido")
        print("3. Países que consomem menos álcool")
        print("4. País que consome mais bebida destilada (espirituosa)")
        print("5. País que consome mais vinho")
        print("6. País que consome mais cerveja")

        # Receber a escolha do usuário
        opcao = input("Digite o número da opção desejada: ")

        # Converter a escolha do usuário para um número inteiro
        opcao = int(opcao)

        # Com base na escolha do usuário, exibir as informações relevantes
        if opcao == 1:
            top_countries_total_alcohol = df.sort_values(by="Consumo de Álcool Puro", ascending=False).head(5)
            
            print(top_countries_total_alcohol[["País", "Consumo de Álcool Puro"]])
        elif opcao == 2:
            prohibited_countries = df[df["Consumo de Álcool Puro"] == 0]
            print(prohibited_countries[["País", "Consumo de Álcool Puro"]])
        elif opcao == 3:
            lowest_consumption_countries = df.sort_values(by="Consumo de Álcool Puro").head(5)
            print(lowest_consumption_countries[["País", "Consumo de Álcool Puro"]])
        elif opcao == 4:
            top_spirit_consumption = df.sort_values(by="Consumo de Bebida Destilada", ascending=False).head(5)
            print(top_spirit_consumption[["País", "Consumo de Bebida Destilada"]])
        elif opcao == 5:
            top_wine_consumption = df.sort_values(by="Consumo de Vinho", ascending=False).head(5)
            print(top_wine_consumption[["País", "Consumo de Vinho"]])
        elif opcao == 6:
            top_beer_consumption = df.sort_values(by="Consumo de Cerveja", ascending=False).head(5)
            print(top_beer_consumption[["País", "Consumo de Cerveja"]])
        elif opcao == 7:
            turnOn = False
            print("Final da seção!")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1 a 7).")


def criar_graficos(data, opcao):
    if opcao not in data.columns:
        print("Opção inválida. A coluna especificada não existe no DataFrame.")
        return

    valores = data[opcao]

    # Gráfico de Barras
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 4, 1)
    plt.bar(data.index, valores)
    plt.xlabel("Índice")
    plt.ylabel(opcao)
    plt.title("Gráfico de Barras")

    # Gráfico de Linha
    plt.subplot(1, 4, 2)
    plt.plot(data.index, valores)
    plt.xlabel("Índice")
    plt.ylabel(opcao)
    plt.title("Gráfico de Linha")

    # Gráfico de Pizza
    plt.subplot(1, 4, 3)
    plt.pie(valores, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Gráfico de Pizza")

    # Gráfico de Dispersão
    plt.subplot(1, 4, 4)
    x = range(len(data))
    plt.scatter(x, valores)
    plt.xlabel("Índice")
    plt.ylabel(opcao)
    plt.title("Gráfico de Dispersão")

    plt.tight_layout()
    plt.show()


main()