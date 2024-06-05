import oracledb
import json

TABLE_ENDERECO = "T_GS_ENDERECO"
TABLE_CONTATO = "T_GS_CONTATO"
TABLE_NOME = "T_GS_CLIENTE"

class Cliente:
    def __init__(self, nome, endereco, contato) -> None:
        self.nome = nome
        self.endereco = endereco
        self.contato = contato

    
    

    def conexa_db():
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
            print("Conexão mal-sucedida {e}")


    def criar_cursor(connection):
        cursor = connection.cursor()

        return cursor


    def inserir_produto(id_produto, nome, descricao, area_atuacao, valor):

        connection = conexao_db()
    

        try:
            # Criar um cursor para executar comandos SQL
            cursor = criar_cursor(connection)

            # Comando SQL para inserir um novo produto na tabela
            sql = f"INSERT INTO {TABLE_NAME} (id_produto, nome, descricao, area_atuacao, valor) VALUES (:1, :2, :3, :4, :5)"

            # Executar o comando SQL com os parâmetros
            cursor.execute(sql, (id_produto, nome, descricao, area_atuacao, valor))

            # Confirmar a transação
            connection.commit()
            print("Produto inserido com sucesso!")

        except oracledb.Error as error:
            print(f"Erro ao inserir produto: {error}")

        finally:
            # Fechar o cursor e a conexão
            if cursor:
                cursor.close()
            if connection:
                connection.close()

