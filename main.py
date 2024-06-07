from Classes import Ong, Design, DatabaseCsv
import time

o = Ong()
d = Design()
data = DatabaseCsv()



def main():
    while True:
        d.cabecalho()
        d.menu()

        op = int(input("\nInforme a opção escolhida: "))

        if op == 1:

            while True:
            
                id_ong = input("Informe o id da ONG: ")
                nome = input("Informe o nome da ONG: ")
                pais = input("Informe o pais: ")
                estado = input("Informe o estado: ")
                area_atuacao = input("Informe a area de atuação: ")
                material_coletado = input("Informe a quantidade de material coletado: ")
                imagem = input("\nInforme o nome da imagem (com a extenção .png): ")

                o.inserir_ong(id_ong, nome, pais, estado, area_atuacao, material_coletado, imagem)


                continuar = int(input("\nGostaria de inserir uma nova ONG?\n\n1- SIM\n2-NÃO\n"))

                if continuar == 2:
                    break

            

        elif op == 2:
            o.listar_ongs()
            time.sleep(10)
            

        elif op == 3:
            while True:
                d.cabecalho()
                o.listar_ongs()

                id_produto = int(input("Informe o id da ONG que deseja deletar: \n"))

                op = int(input("Você tem certeza que deseja concluir a ação?\n1- SIM\n2- NÃO\n"))

                if op == 1:
                    o.excluir_ong(id_produto)
                else:
                    print("Continuando...")
                    break

                opcao = int(input("\n\nDeseja excluir outro produto? \n1- SIM\n2- NÃO\n"))

                if opcao == 2:
                    break

        elif op == 4:
            while True:
                d.cabecalho()
                o.listar_ongs()
                
                id_ong = int(input("\n\nInforme o id do produto que você deseja alterar: \n"))


                novo_nome = input('Informe o novo nome da ONG: ')
                novo_pais = input('Informe o novo pais da ONG: ')
                novo_estado = input('Informe o novo estado da ONG: ')
                nova_area_atuacao = input('Informe a área de atuação da ONG: ')
                novo_material_coletado = int(input('Informe o valor do lixo coletado: '))
                
                nova_imagem = input('Informe o nome da imagem: ')

                o.alterar_ong(id_ong, novo_nome, novo_pais, novo_estado, nova_area_atuacao, novo_material_coletado, nova_imagem)


                continuar = int(input("\nGostaria de alterar outra ONG?\n\n1- SIM\n2-NÃO\n"))

                if continuar == 2:
                    break
        
        elif op == 5:
             while True:
                print("\n1- Csv de qualidade do ar e poluição da água")
                print("2- Csv de produção de plástico per-capita\n\n")

                opcao_csv = int(input("Informe sua opção: "))
                if opcao_csv == 1:
                    print("Inserindo dados...")
                    data.insert_qualidade_ar_agua("./data/5- poluicao-agua-cidades.csv")
                    time.sleep(5)

                    break

                elif opcao_csv == 2:
                    print("Inserindo dados...")
                    data.insert_plastico_produzido("./data/4- desperdicio-plastico-per-capita.csv")
                    time.sleep(5)
                    break

                else:
                    print("Opção inválida!")
                    time.sleep(2)
                    d.limpa_tela()
                    d.cabecalho()

        elif op == 6:
            d.saida()
            break


if __name__ == "__main__":
    main()