# Projetos
Pasta de projeto feito durante o curso técnico 2025
import random

def jogar_rpg():
    print("--- INÍCIO DO COMBATE ---")

    invasao_inicial = random.randint(2, 3)
    barreira_vida = 4
    vida_lenh = 4
    vida_mine = 10
    vida_ferro = 10
   
    print(f"Uma invasão inicial de {invasao_inicial} goblins se aproxima!")
    print(f"Sua barreira tem {barreira_vida} pontos de resistência.")

    for rodada in range(invasao_inicial):
        print(f"\n--- RODADA {rodada + 1} ---")

        num_goblins_na_rodada = random.randint(2, 5)
        print(f"Um grupo de {num_goblins_na_rodada} goblins aparece!")

        for goblin_ataque in range(num_goblins_na_rodada):
            if barreira_vida > 0:
                print(f"Goblin {goblin_ataque + 1} ataca a barreira (Estacas: {barreira_vida})")
                quebra_chance = random.randint(1, 100)
               
                if quebra_chance >= 70:
                    barreira_vida -= 1
                    print(f"A barreira foi danificada! Estacas restantes: {barreira_vida}")
                    escolha_jogador = input("\nGOBLIN AVANCA! VOCÊ O ENFRENTA OU NÃO? (sim/nao): \n").lower ()
                    if escolha_jogador == "sim":
                        print("\nVocê escolheu enfrentar! Iniciando dinâmica com o professor na vida real...")
                        print("Após a dinâmica, a batalha no programa continua para a próxima rodada/grupo de goblins.\n")
                    else:
                        print("\nVocê decide não enfrentar os goblins.\n")
                        print("Os goblins atacam os moradores!")
                       
                       
                        vida_lenh -= 1
                        vida_mine -= 1
                        vida_ferro -= 1
                       
                        print(f"Vida do lenhador: {vida_lenh}\n Vida do minerador: {vida_mine}\n Vida do ferreiro: {vida_ferro}")
                       
                        queima_plantacao_chance = random.randint(1, 100)
                        if queima_plantacao_chance <= 5:
                            print("VOCÊ PERDEU UMA PLANTAÇÃO! Goblins incendiaram a colheita.")
                        else:
                            print("Ufa! As plantações estão seguras por enquanto.")
                else:
                    print("O ataque do goblin falhou! A barreira resistiu.\n")
            else:
                break

       
        if rodada < invasao_inicial - 1:
            input("\nPressione Enter para ir para a próxima rodada...")

    print("\n--- FIM DO COMBATE (Rodadas da invasão inicial concluídas) ---")
    if barreira_vida > 0:
        print("Sua barreira resistiu à invasão inicial!")
    else:
        print("Sua barreira foi destruída na invasão inicial.")

jogar_rpg()
