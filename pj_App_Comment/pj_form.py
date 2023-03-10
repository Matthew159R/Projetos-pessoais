from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Conexão com o MySQL
cnx = mysql.connector.connect(host='localhost', database='pj_form', user='root', password='159159')
if cnx.is_connected():
    print('Conectado com sucesso!')
cursor = cnx.cursor()

# Rota para receber os dados do formulário
@app.route('/submit', methods=['POST'])
def submit():
    # Receba os dados do formulário
    nome = request.form['nome']
    email = request.form['email']

    # Insira os dados no banco de dados MySQL
    add_user = ("INSERT INTO usuarios "
                "(nome, email) "
                "VALUES (%s, %s)")
    data_user = (nome, email)
    cursor.execute(add_user, data_user)
    cnx.commit()

    return 'Dados inseridos com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
cnx.close()
cursor.close()
