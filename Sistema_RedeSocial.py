import pymysql

class RedeSocial:
    def __init__(self):
        self.conexao = pymysql.connect(
            user='root',
            host='localhost',
            password='',
            database='redesocial'
        )
        self.gerenciador = self.conexao.cursor()

    def cadastrar(self, login, senha):
        sql = '''
            insert into usuario
            (nome, login, senha)
            values
            (%s, %s);
        '''
        self.gerenciador.execute(sql,(login, senha))
        self.conexao.commit()

#rs = RedeSocial()
#rs.cadastrar('pv', '123')

