import pandas as pd
import random

# --- CARREGAMENTO DE DADOS ---
# Esta função já está implementada e é responsável por carregar os dados, não altere.
def carregar_dados(url):
    """
    Carrega os dados da planilha e retorna como uma lista de listas.
    A primeira linha (cabeçalho) é ignorada.
    """
    df = pd.read_csv(url)
    reservas = df.values.tolist()
    return reservas

# --- OPERAÇÕES ---

def listar_reservas(reservas):
    """
    Opção 1: Lista todas as reservas com suas informações detalhadas.
    """
    print("--- LISTAGEM DE RESERVAS ---")
    for r in reservas:
        print("\n")
        print(f"ID Reserva: {r[0]}")
        print(f"ID Solicitante: {r[1]}")
        print(f"Solicitante: {r[2]}")
        print(f"Categoria: {r[3]}")
        print(f"Data de Início: {r[4]}")
        print(f"Data de Fim: {r[8]}")
        print(f"Valor da Diária: R$ {float(r[12]):.2f}")
        print(f"Desconto: R$ {float(r[13]):.2f}")
        print(f"Valor Total: R$ {float(r[14]):.2f}")

def filtrar_por_categoria(reservas):
    """
    Opção 2: Solicita uma categoria e lista as reservas que pertencem a ela.
    """
    categoria = input('Digite a categoria desejada (Externo/USP): ')

    if categoria != 'Externo' and categoria != 'USP':
        print('Categoria inválida! Escolha "USP" ou "Externo"')
        return

    print(f"--- RESERVAS DA CATEGORIA {categoria.upper()} ---")
    for r in reservas:
        if r[3] == categoria:
            print("\n")
            print(f"ID Reserva: {r[0]}")
            print(f"Solicitante: {r[2]}")
            print(f"Data de Início: {r[4]}")
            print(f"Data de Fim: {r[8]}")

def calcular_total_arrecadado(reservas):
    """
    Opção 3: Calcula e exibe o valor total arrecadado por categoria.
    """
    total_usp = 0
    total_externo = 0

    # Loop simples para soma de todos os valores para cada categoria
    for r in reservas:
        valor = float(r[14]) 
        if r[3] == "USP":
            total_usp += valor
        elif r[3] == "Externo":
            total_externo += valor

    # Exibição dos totais
    print("--- VALOR ARRECADADO POR CATEGORIA ---")
    print(f"Categoria USP: R$ {total_usp:.2f}")
    print(f"Categoria Externo: R$ {total_externo:.2f}")

def exibir_estatisticas(reservas):
    """
    Opção 4: Calcula e exibe estatísticas gerais, como média de diárias e
    percentual de reservas com desconto. 
    """
    dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Dias por mês
    total_diarias = 0
    reservas_com_desconto = 0
    total_reservas = len(reservas)

    for r in reservas:
        dia_inicio = int(r[5])
        mes_inicio = int(r[6])
        ano_inicio = int(r[7])
        dia_fim = int(r[9])
        mes_fim = int(r[10])
        ano_fim = int(r[11])

        diarias = 0

        # Todas as reservas começam e terminam no mesmo ano
        if mes_inicio == mes_fim:
            # Reserva dentro do mesmo mês
            diarias = dia_fim - dia_inicio + 1  # Cada dia conta como uma diária
        else:
            # Primeiro mês: do dia de início até o final do mês
            diarias += dias_no_mes[mes_inicio - 1] - dia_inicio + 1
            # Meses intermediários completos
            for m in range(mes_inicio, mes_fim - 1):
                diarias += dias_no_mes[m]
            # Último mês: do início do mês até o dia final da reserva
            diarias += dia_fim

        total_diarias += diarias

        # Verifica se houve desconto aplicado
        if float(r[13]) > 0:
            reservas_com_desconto += 1

    # Cálculos finais
    media_diarias = total_diarias / total_reservas
    percentual_desconto = int(round((reservas_com_desconto / total_reservas) * 100))

    # Exibição
    print("\n--- ESTATÍSTICAS GERAIS ---")
    print(f"Média de diárias por reserva: {media_diarias:.2f} dias")
    print(f"Percentual de reservas com desconto: {percentual_desconto}%")
    
# --- FUNÇÃO PRINCIPAL ---

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    # Carrega os dados do CSV online
    reservas = carregar_dados('https://raw.githubusercontent.com/rmcesarjr/iccd/main/data/reservas.csv')

    opcao = 1  # Inicializa com 1 para entrar no loop

    while opcao != 0:
        # Menu de opções
        print("--- MENU DE OPERAÇÕES ---")
        print("1 - Listar todas as reservas")
        print("2 - Filtrar por categoria")
        print("3 - Calcular totais de arrecadação")
        print("4 - Exibir estatísticas gerais")
        print("0 - Sair")

        opcao = int(input("Digite o número da operação desejada: "))

        # Redireciona para a função correspondente
        if opcao == 1:
            listar_reservas(reservas)
            print("\n")
        elif opcao == 2:
            filtrar_por_categoria(reservas)
            print("\n")
        elif opcao == 3:
            calcular_total_arrecadado(reservas)
            print("\n")
        elif opcao == 4:
            exibir_estatisticas(reservas)
            print("\n")
        elif opcao == 0:
            print("\nEncerrando o programa.")
        else:
            print("\nOperação inválida. Tente novamente.\n")


# --- EXECUÇÃO DO PROGRAMA ---
# Esta parte garante que o programa comece
if __name__ == "__main__":
    main()
