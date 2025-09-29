# Projetos
Pasta de projeto feito durante o curso técnico 2025
import sqlite3

conn = sqlite3.connect("armazem.db")
cursor = conn.cursor()


cursor.execute ("""
CREATE TABLE IF NOT EXISTS armazem (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   nome TEXT NOT NULL,
   quantidade INTEGER NOT NULL,
   consumo INTEGER NOT NULL,
   producao INTEGER NOT NULL
)
""")
conn.commit()

dados = [
 ('Grao', 120, 24, 0),
 ('Madeira', 20, 5, 0),
 ('Erva',  30, 2, 2),
 ('Ferro', 70, 10, 30),
]


cursor.executemany("INSERT INTO armazem (nome, quantidade, consumo, producao) VALUES (?, ?, ?, ?)", dados)
conn.commit()

cursor.execute("SELECT nome, quantidade, consumo, producao FROM armazem")
resultados = cursor.fetchall()


print("Recursos da vila:")


recursos_resultado = []


for nome, quantidade, consumo, producao in resultados:
   saldo_diario = producao - consumo


   if saldo_diario == 0:
       duracao = 0
   else:
       duracao = round(quantidade / abs(saldo_diario), 2)


   recursos_resultado.append((nome, quantidade, consumo, producao, duracao))


for nome, quantidade, consumo, producao, duracao in recursos_resultado:
   print(f"{nome}: Quantidade {quantidade}, Consumo Diario {consumo}, Produção {producao}, Duração: {duracao} dias")



import random
import time


def combate():
    print("⚔️ COMBATE INICIADO! ⚔️")
    time.sleep(3)
   
    # Valores iniciais
    invasao = random.randint(2, 3)
    barreiras = 4  # 4 das 17 barreiras
    plantacoes = 7 # 5% dos goblins queimarem, mas não para sempre. Graças a Deus
    dano_moradores = 0


    print(f"\nQuantidade de invasões: {invasao}")
    print(f"Barreiras do grupo: {barreiras}")
    print(f"Plantações: {plantacoes}")
    time.sleep(3)
   
    for rodada in range(invasao):
        print(f"\n--- Rodada {rodada + 1} ---")
        goblins = random.randint(2, 5)
        print(f"{goblins} goblins apareceram!")
       
        for _ in range(goblins):
            if barreiras > 0:
                quebra = random.randint(1, 100)
                print(f"Goblin {_ +1}")
                if quebra <= 70:
                    print("⛔ Barreira resistiu! Goblin se ferrou.")
                    time.sleep(2)
                else:
                    barreiras -= 1  # Reduz o número de barreiras intactas
                    print(f"\n💥 Goblin quebrou uma barreira! \nBarreiras restantes: {barreiras}")
                    time.sleep(2)


                    enfrenta = input("Enfrentar o goblin? (sim/não): ").strip().lower() # O .strip vai tirar os espaços e outras coisas, obg pessoa que n lembro de falar sobre isso.
                    time.sleep(2)
                   
                    if enfrenta == "sim":
                        print("⚔️ Diâmica foi iniciada!")
                        # Lógica do combate direto aqui
                    else:
                        print(f"😱 Você fugiu! Moradores sofrem dano equivalente a 1")
                        dano_moradores += 1
                       
                        if random.randint(1, 100) <= 5:
                            plantacoes -= 1
                            print(f"🔥 Uma plantação foi queimada! Restantes: {plantacoes}")
            else:
                print("\n🚧 Todas as barreiras foram destruídas! \nGoblins avançam livremente!")
                enfrenta = input("Enfrentar os goblins? (sim/não): ").strip().lower()
                if enfrenta == "sim":
                    print("⚔️ Combate direto iniciado contra todos!")
                else:
                    dano_moradores += 1  # Dano por goblin que passa
                    print(f"😱 Você fugiu! Moradores sofrem dano equivalente a 1")


    vida_do_lenhador = 4
    vida_do_ferreiro = 10
    vida_do_mineiro = 10




    # Tudo que a gente precisa saber junto de time sleep
    print("\n=== FIM DO COMBATE ===")
    time.sleep(3)
    print("Resumo final:")
    time.sleep(1)
    print(f"- Barreiras intactas: {barreiras}")
    time.sleep(1)
    print(f"- Dano total aos moradores: {dano_moradores}")
    time.sleep(1)
    print(f"- Plantações restantes: {plantacoes}")
    time.sleep(1)
    print(f"- Vida dos moradores da vila do espantalho\nLenhador: {vida_do_lenhador - dano_moradores}\nFerreiro: {vida_do_ferreiro - dano_moradores}\nMineiro: {vida_do_mineiro - dano_moradores}")


combate()




#inicio
vida = 10
arvores = 0
# Loop das 3 horas
for hora in range(3):
    print(f"\nHora {hora + 1}: O lenhador cortou uma árvore.")
    print("O goblin apareceu!")
   
    # Entrada do usuário
    acao = input("Você escolheu que o lenhador iria correr ou lutar? ").lower()
   
    # Decisão com base na ação escolhida
    if acao == "correr":
        if random.random() < 0.5:
            print("O lenhador correu, mas não conseguiu levar a árvore!")
        else:
            arvores += 1
            print("O lenhador correu e conseguiu levar a árvore.")
    elif acao == "lutar":
        vida -= 2
        arvores += 1
        print(f"O lenhador lutou e levou 2 de dano. Vida restante: {vida}")
    else:
        vida = 0
        print("Ação inválida! Ele fica parado e o goblin o ataca, tirando toda a vida dele, resultando em morte imediata!!")
        print("O Lenhador morreu!")
        break
   
    # Verificação de vida
    if vida <= 0:
        print("O Lenhador morreu!")
        break

# Cálculo das estacas
estacas = 0
for
