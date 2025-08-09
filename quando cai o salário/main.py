import calendar
import datetime
import holidays
import os
import sys

def calcular():
    
    os.system('cls' if os.name == 'nt' else 'clear')

   
    dias_semana_pt = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }

    meses_pt = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    print(f"{BOLD}{CYAN}{'=' * 50}")
    print(f"{'Calculadora do 5º Dia Útil':^50}")
    print(f"{'=' * 50}{RESET}")

    
    while True:
        try:
            mes = int(input(f"{YELLOW}Digite o mês (1 a 12): {RESET}"))
            if 1 <= mes <= 12:
                break
            else:
                print(f"{RED}Mês inválido. Tente novamente.{RESET}")
        except ValueError:
            print(f"{RED}Entrada inválida. Digite um número de 1 a 12.{RESET}")

    
    while True:
        try:
            ano = int(input(f"{YELLOW}Digite o ano (2000 a 2100): {RESET}"))
            if 2000 <= ano <= 2100:
                break
            else:
                print(f"{RED}Ano inválido. Tente novamente.{RESET}")
        except ValueError:
            print(f"{RED}Entrada inválida. Digite um número válido.{RESET}")

    print(f"\n{CYAN}Mês selecionado: {meses_pt[mes]} ({mes})")
    print(f"Ano selecionado: {ano}{RESET}\n")

    primeiro_dia = datetime.date(ano, mes, 1)
    feriados = holidays.Brazil(years=ano)
    data = primeiro_dia
    dias_uteis = 0

    while data.month == mes:
        if data.weekday() < 6 and data not in feriados:
            dias_uteis += 1
            if dias_uteis == 5:
                break
        data += datetime.timedelta(days=1)

    original_data = data
    if data.weekday() == 5:
        anterior = data - datetime.timedelta(days=1)
        while anterior.weekday() >= 5 or anterior in feriados:
            anterior -= datetime.timedelta(days=1)
        data = anterior

    print(f"{BOLD}{GREEN}Resultado:{RESET}")
    print(f"O {BOLD}5º dia útil{RESET} de {BOLD}{meses_pt[mes]} de {ano}{RESET} é:")
    print(f" → {BOLD}{dias_semana_pt[data.strftime('%A')]} - {data.strftime('%d/%m/%Y')}{RESET}")

    if original_data != data:
        print(f"{YELLOW}Obs: o 5º dia útil cairia no sábado {original_data.strftime('%d/%m/%Y')}, então foi ajustado para sexta-feira anterior.{RESET}")

    print(f"\n{CYAN}{'=' * 50}")
    print(f"{'Cálculo concluído com sucesso!':^50}")
    print(f"{'=' * 50}{RESET}")

while True:
    calcular()
    escolha = input("\nDeseja reiniciar (R) ou sair (S)? ").strip().lower()
    if escolha == "s":
        print("\n👋 Saindo...")
        sys.exit()
    elif escolha != "r":
        print("Opção inválida! Reiniciando...")
