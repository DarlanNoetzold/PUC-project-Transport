import pandas as pd

# Leitura dos dados
dados = pd.read_csv("DNIT-Distancias.csv", sep=";")

# Formatação das Colunas
columns = dados.columns.to_series()
dados.set_index(columns, inplace=True)


# Inicializa o Menu do Programa e chama as funções de cada opção
def main():
    load_program = True
    custo_por_km = 0
    while load_program:
        print("=== MENU ===")
        print("1. Configurar custo por KM")
        print("2. Consultar trecho")
        print("3. Consultar rota")
        print("4. Terminar o programa")
        print("\nEscolha uma das opcoes: ")
        op = input()

        # Opção de Configurar custo por KM
        if op == "1":
            invalid_op = True
            while invalid_op:
                print("\nInforme o custo por KM: ")
                custo_por_km = float(input())
                if custo_por_km <= 0:
                    print("Opcao Invalida, por favor digite um valor maior que 0!")
                else:
                    invalid_op = False

        # Opção de Consultar Trecho
        elif op == "2":
            if custo_por_km > 0:
                print("\nDigite a cidade de origem: ")
                cidade_origem = input()
                cidade_origem = cidade_origem.upper()
                print("\nDigite a cidade de destino: ")
                cidade_destino = input()
                cidade_destino = cidade_destino.upper()
                consultar_trecho(cidade_origem, cidade_destino, custo_por_km)
            else:
                print("Voce deve informar o custo por KM antes de definir um trecho!")

        # Opção de Consultar Rota
        elif op == "3":
            if custo_por_km > 0:
                print("\nDigite o nome de duas ou mais cidades separadas por virgula:")
                string_cidades = input()
                string_cidades = string_cidades.upper()
                lista_cidades = string_cidades.split(", ")
                consultar_rota(lista_cidades, custo_por_km)
            else:
                print("Voce deve informar o custo por KM antes de definir uma rota!")

        # Opção de Término do Programa
        elif op == "4":
            print("\nFim do programa!")
            load_program = False
        else:
            print("\nOpcao Invalida!")


# Função que Consulta o Trecho que recebe a cidade de origem e
# de destino e o Custo por KM. E imprime a Distância e o custo
def consultar_trecho(cidade_origem, cidade_destino, custo_por_km):
    try:
        km = dados.loc[cidade_origem, cidade_destino]
        print("Distancia entre", cidade_origem, "e", cidade_destino, "e de", km, "km")
        print("Custo de R$", km * custo_por_km, "\n")
    except:
        print("Alguma cidade digitada esta incorreta ou não temos em nossos dados!")


# Função que Consulta uma rota que recebe uma lista das cidades e o custo por KM.
def consultar_rota(lista_cidades, custo_por_km):
    try:
        cont = 0
        total_km = 0
        while cont < len(lista_cidades) - 1:
            km = dados.loc[lista_cidades[cont], lista_cidades[cont+1]]
            total_km = km + total_km
            print(lista_cidades[cont], "->", lista_cidades[cont+1], "(", km, "KM )")
            cont = cont + 1
        print("\nDistância total: ", total_km, "km")
        print("Custo total: R$ %.2f" % (total_km*custo_por_km))
        print("O total de litros gastos foi de: %.3f" % (total_km*2.57))
        print("A viagem durou %d dias.\n" % (total_km/283))
    except:
        print("Alguma cidade digitada esta incorreta ou não temos em nossos dados!")

# Chama a função main


main()
