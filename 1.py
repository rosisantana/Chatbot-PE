
# utilizado para sair do while loop quando retornar uma String ao
# inves de um node da arvore
def is_obj(obj):
    return False if type(obj).__name__ == "str" else True

counter_tickets = 0
while True: # laco inicial com a criacao do objeto da arvore
    arvore = rec_build_tree(1)
    count_erros=0

    while True: # laco para validacao das respostas e retorno da classificacao
        if count_erros == 2:
            print("ERROS SUCESSIVOS\nVERIFIQUE AS OPÇÕES ANTES DE TENTAR NOVAMENTE\n")
            print("\nMuitas informações! :/ \nPor favor me reinicie.")
            break

        opcoes = {1:arvore.answerTrue,2:arvore.answerFalse}
        print("\nEscolha uma das opções abaixo:"+"\n0 para sair"+"\n1 para "+opcoes[1]+"\n2 para "+opcoes[2]+"\n")
        response = input(arvore.ask_question())

        while not response.isnumeric():
            if count_erros == 2:
                print("\nMuitas informações! :/ \nPor favor me reinicie.")
                sys.exit()

            print("\nMe desculpe, não conheço essa opção, vamos tentar novamente? :)\n")
            print("Escolha uma das opções abaixo:"+"\n0 para sair"+"\n1 para "+opcoes[1]+"\n2 para "+opcoes[2])
            response = input(arvore.ask_question())
            count_erros+=1
            
        if int(response) == 0:
            print("\nFim.\n")
            sys.exit()
            
        question = opcoes[int(response)]
        answer = arvore.check_answer(question)

        if answer == False:
            print("\nMe desculpe, não conheço essa opção, vamos tentar novamente? :)")
            count_erros+=1
        elif not is_obj(answer):
            break
        else:
            arvore = answer 
            
    print(answer)
                
    print("-------------------------------------")