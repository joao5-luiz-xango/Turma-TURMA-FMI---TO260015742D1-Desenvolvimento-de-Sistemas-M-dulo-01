from colorama import Fore, Style, init
# Inicializa o colorama para o funcionamento correto no terminal 
init(autoreset=True)
# Lista contendo os niveis, para o funcionamento correto para o reservatório[span_2](start_span)[span_2](end_span
niveis_reservatorio = [
    {"nivel": 1, "situacao": "MUITO BAIXO (critico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "BAIXO" , "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "MEDIO" , "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "ALTO" , "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "MUITO ALTO (ALERTA)", "cor": Fore.BLUE},

           
] 
def exibir_status_reservatorio(nivel_desejado):
    """
    Busca o nível na lista e exibe a situação
    com a cor correspondente no terminal.
    """
    encontrado = False

    for item in niveis_reservatorio:
        if item["nivel"] == nivel_desejado:
            print(
                f"{item['cor']}Status atual -> "
                f"Nível {item['nivel']}: "
                f"{item['situacao']}{Style.RESET_ALL}"
            )
            encontrado = True
            break

    if not encontrado:
        print(
            f"{Fore.RED}Erro: Nível {nivel_desejado} "
            f"não encontrado!{Style.RESET_ALL}"
        )




# Simulação de um ambiente real de monitoramento[span_5](start_span)[span_5](end_span)
if __name__ == "__main__":
  
  print("=== MONITORAMENTO DE RESERVATÓRIO DE ÁGUA ===")
  print("Iniciando simulação com valores predefinidos...\n")

  # Simulando a variação dos níveis do reservatório ao longo do tempo
  leituras_simuladas = [1, 3, 5, 2, 4]

  for leitura in leituras_simuladas:
    print(f"Lendo sensor... (Valor lido: Nível {leitura})")
    exibir_status_reservatorio(leitura)
    print("-" * 45)

