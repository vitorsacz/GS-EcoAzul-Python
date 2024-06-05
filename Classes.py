import oracledb
import json

class Conexao:

    def conexao_db(self):
        try:
            with open("credenciais.json") as f:
                credenciais = json.load(f)

            USER = credenciais["user"]
            PASS = credenciais["pass"]
        
            # Conecta o servidor
            dsnStr = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")
            # Efetua a conexão com o Usuário
            connection = oracledb.connect(user=USER, password=PASS, dsn=dsnStr)

            return connection

        except FileNotFoundError:
            print("Arquivo não encontrado")    
        except Exception as e:
            print(f"Conexão mal-sucedida: {e}")

class Ong(Conexao):
    def __init__(self, nome, pais, estado, area_atuacao):
        self.nome = nome
        self.pais = pais
        self.estado = estado
        self.area_atuacao = area_atuacao

    @staticmethod
    def menu_ong():
        print("1- Inserir ONG")
        print("2- Alterar dados da ONG")
        print("3- Excluir ONG")
        print("4- Listar ONG's")
        print("5- SAIR")

    def inserir_ong(self, id_produto, nome, descricao, area_atuacao, valor):
        connection = self.conexao_db()

        try:
            cursor = connection.cursor()
            sql = "INSERT INTO T_GS_ONG (id_produto, nome, descricao, area_atuacao, valor) VALUES (:1, :2, :3, :4, :5)"
            cursor.execute(sql, (id_produto, nome, descricao, area_atuacao, valor))
            connection.commit()
            print("Produto inserido com sucesso!")

        except oracledb.Error as error:
            print(f"Erro ao inserir produto: {error}")

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

            for ong in ongs:
                print(ong)

        except oracledb.Error as error:
            print(f"Erro ao listar ONGs: {error}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def alterar_ong(self, id_produto, nome, descricao, area_atuacao, valor):
        connection = self.conexao_db()

        try:
            cursor = connection.cursor()
            sql = "UPDATE T_GS_ONG SET nome = :1, descricao = :2, area_atuacao = :3, valor = :4 WHERE id_produto = :5"
            cursor.execute(sql, (nome, descricao, area_atuacao, valor, id_produto))
            connection.commit()
            print("ONG alterada com sucesso!")

        except oracledb.Error as error:
            print(f"Erro ao alterar ONG: {error}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

