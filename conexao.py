import oracledb
import json

class Conexao():

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
