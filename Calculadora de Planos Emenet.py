def calcular_valor_proporcional(dias_sem_conexao, valor_plano):
    """Calcula desconto proporcional por dias sem conexão"""
    dias_no_mes = 30  
    desconto = (dias_sem_conexao / dias_no_mes) * valor_plano
    valor_final = valor_plano - desconto
    return desconto, valor_final

def main():
    """Função principal do programa"""
    planos = {
        "200MEGAS": 69.90,
        "300MEGAS": 79.90,
        "400MEGAS": 89.90,
        "600MEGAS": 99.90
    }

    try:
        print("=== CALCULADORA DE DESCONTO - PLANOS EMENET ===")
        dias_sem_conexao = int(input("\n🚀 DIGITE O NÚMERO DE DIAS SEM CONEXÃO: "))

        if dias_sem_conexao < 0 or dias_sem_conexao > 30:
            print("\n⚠️ POR FAVOR, INSIRA UM NÚMERO VÁLIDO DE DIAS ENTRE 0 E 30.")
            return

        print("\n📌 Planos disponíveis:")
        for i, (plano, valor) in enumerate(planos.items(), 1):
            print(f"{i}. {plano} - 💰 R$ {valor:.2f}")

        escolha_num = int(input("\n🔎 Digite o número do plano desejado: "))

        if 1 <= escolha_num <= len(planos):
            escolha_plano = list(planos.keys())[escolha_num - 1]
            valor_plano = planos[escolha_plano]
        else:
            print("\n❌ Opção inválida. Tente novamente.")
            return

        desconto, valor_final = calcular_valor_proporcional(dias_sem_conexao, valor_plano)

        print("\n" + "="*50)
        print("📢 === CÁLCULO DO DESCONTO ===")
        print("="*50)
        print(f"📝 Plano selecionado: {escolha_plano}")
        print(f"💵 Valor original do plano: R$ {valor_plano:.2f}")
        print(f"📅 Dias sem conexão: {dias_sem_conexao} dias")
        print(f"🔻 Desconto aplicado: R$ {desconto:.2f}")
        print(f"✅ Valor final da mensalidade: R$ {valor_final:.2f}")
        print("="*50)

    except ValueError:
        print("\n🚨 Erro: Insira um número válido.")

if __name__ == "__main__":
    main()