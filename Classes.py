import oracledb
import json
import os
import csv

class Conexao:

    def conexao_db(self):
        try:
            with open("credenciais.json") as f:
                credenciais = json.load(f)

            USER = credenciais["user"]
            PASS = credenciais["pass"]
        
            # Conecta ao servidor
            dsnStr = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")
            # Efetua a conexão com o Usuário
            connection = oracledb.connect(user=USER, password=PASS, dsn=dsnStr)

            return connection

        except FileNotFoundError:
            print("Arquivo não encontrado")    
        except Exception as e:
            print(f"Conexão mal-sucedida: {e}")

class Ong(Conexao):

    def __init__(self):
        pass

    

    def inserir_ong(self, id_ong, nome, pais, estado, area_atuacao, material_coletado, imagem):
        connection = self.conexao_db()

        try:
            cursor = connection.cursor()
            sql = "INSERT INTO T_GS_ONG (idOng, nome, pais, estado, areaAtuacao, materialColetado, imagem) VALUES (:1, :2, :3, :4, :5, :6, :7)"
            cursor.execute(sql, (id_ong, nome, pais, estado, area_atuacao, material_coletado, imagem))
            connection.commit()
            print("\nONG inserida com sucesso!")

        except oracledb.Error as error:
            print(f"Erro ao inserir ONG: {error}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def listar_ongs(self):
        connection = self.conexao_db()

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM T_GS_ONG")
            ongs = cursor.fetchall()

            print("Lista de Produtos:")
            print("=================")
            for ong in ongs:
                print(f"ID: {ong[0]}")
                print(f"Nome: {ong[1]}")
                print(f"Pais: {ong[2]}")
                print(f"Estado: {ong[3]}")
                print(f"Área de Atuação: {ong[4]}")
                print(f"Material Coletado: {ong[5]} toneladas")
                print("-----------------")

        except oracledb.Error as error:
            print(f"Erro ao listar ONGs: {error}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def excluir_ong(self, id_ong):
        connection = self.conexao_db()

        try:
            cursor = connection.cursor()
            sql = "DELETE FROM T_GS_ONG WHERE idOng = :1"
            cursor.execute(sql, (id_ong,))
            connection.commit()
            print("\nONG excluída com sucesso!")

        except oracledb.Error as error:
            print(f"Erro ao excluir ONG: {error}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def alterar_ong(self, idOng, novo_nome, novo_pais, novo_estado, nova_area_atuacao, novo_material_coletado, nova_imagem):
        connection = self.conexao_db()

        try:
            cursor = connection.cursor()
            sql = "UPDATE T_GS_ONG SET nome = :1, pais = :2, estado = :3, areaAtuacao = :4, materialColetado = :5, imagem = :6 WHERE idOng = :7"
            cursor.execute(sql, (novo_nome, novo_pais, novo_estado, nova_area_atuacao, novo_material_coletado, nova_imagem, idOng))
            connection.commit()
            print("\nONG alterada com sucesso!")

        except oracledb.Error as error:
            print(f"Erro ao alterar ONG: {error}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

class DatabaseCsv(Conexao):

    def __init__(self):
        pass

    def insert_qualidade_ar_agua(self, filepath):
        connection = self.conexao_db()
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Pula o cabeçalho

                cursor = connection.cursor()
                id_counter = 1  # Inicia o contador de ID
                
                for row in reader:
                    cidade, regiao, entidade, qualidade_do_ar, poluicao_agua = row
                    cursor.execute('''
                        INSERT INTO T_GS_QUALIDADE_AR_AGUA_CIDADE (id_cidade, cidade, regiao, entidade, qualidade_do_ar, poluicao_agua)
                        VALUES (:1, :2, :3, :4, :5, :6)
                    ''', (str(id_counter), cidade, regiao, entidade, qualidade_do_ar, poluicao_agua))
                    id_counter += 1  # Incrementa o contador de ID
                connection.commit()
                print("Dados inseridos com sucesso na tabela T_GS_QUALIDADE_AR_AGUA_CIDADE.")

        except Exception as e:
            print(f"Erro ao inserir dados: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def insert_plastico_produzido(self, filepath):
        connection = self.conexao_db()
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Pula o cabeçalho

                cursor = connection.cursor()
                id_counter = 1  # Inicia o contador de ID
                for row in reader:
                    entidade, codigo, ano, producao_anual = row
                    cursor.execute('''
                        INSERT INTO T_GS_PLASTICO_PRODUZIDO (id_ano, ano, producao_anual)
                        VALUES (:1, :2, :3)
                    ''', (str(id_counter), int(ano), float(producao_anual)))
                    id_counter += 1  # Incrementa o contador de ID
                connection.commit()
                print("Dados inseridos com sucesso na tabela T_GS_PLASTICO_PRODUZIDO.")

        except Exception as e:
            print(f"Erro ao inserir dados: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

class Design:

    def __init__(self):
        pass

    def limpa_tela(self):
        # Verifica o sistema operacional
        if os.name == 'posix':  # Para Linux e macOS
            _ = os.system('clear')
        elif os.name == 'nt':  # Para Windows
            _ = os.system('cls')
        else:
            # Se não estiver em nenhum dos sistemas acima, limpa usando caracteres de nova linha
            print('\n' * 100)  # Imprime 100 novas linhas para "limpar" a tela

    def cabecalho(self):
        self.limpa_tela()
        print("")
        print("""     _         _       _           _ 
                     | |       | |     | |         | |
   ___ _ __ _   _  __| |   __ _| | ___ | |__   __ _| |
  / __| '__| | | |/ _` |  / _` | |/ _ \| '_ \ / _` | |
 | (__| |  | |_| | (_| | | (_| | | (_) | |_) | (_| | |
  \___|_|   \__,_|\__,_|  \__, |_|\___/|_.__/ \__,_|_|
                           __/ |                      
                          |___/ """)

    def saida(self):
        self.limpa_tela()
        print(""" 
        _          _                 _       
       | |        (_)               | |      
   ___ | |__  _ __ _  __ _  __ _  __| | ___  
  / _ \| '_ \| '__| |/ _` |/ _` |/ _` |/ _ \ 
 | (_) | |_) | |  | | (_| | (_| | (_| | (_) |
  \___/|_.__/|_|  |_|\__, |\__,_|\__,_|\___/ 
                      __/ |                  
                     |___/ """)
        

    @staticmethod
    def menu():
        print("1- Inserir ONG")
        print("2- Listar ONG's")
        print("3- Excluir ONG")
        print("4- Alterar dados da ONG")
        print("5- Inserir Csv")
        print("6- SAIR")

# Exemplo de uso
if __name__ == "__main__":
    db_csv = DatabaseCsv()
    db_csv.insert_qualidade_ar_agua('./data/qualidade_ar_agua.csv')
    db_csv.insert_plastico_produzido('./data/plastico_produzido.csv')
