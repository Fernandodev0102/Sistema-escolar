-- 
# Autor: Fernando Pereira Alves
# GitHub: @Fernandodev0102
# Contato: 85976014779  





from flask import Flask, render_template, request, redirect, url_for



import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sistema_escolar"
)
cursor = db.cursor(dictionary=True)

# Página inicial: Cadastro de alunos (login ou registro)
@app.route("/", methods=["GET", "POST"])
def cadastro_aluno():
    if request.method == "POST":
        matricula = request.form["matricula"]
        nome = request.form["nome"]
        idade = request.form["idade"]
        curso = request.form["curso"]
        acesso = request.form["acesso"]
        
        # Inserir ou verificar se a matrícula já existe
        cursor.execute("SELECT * FROM alunos WHERE matricula = %s", (matricula,))
        aluno_existente = cursor.fetchone()
        if aluno_existente:
            return "Matrícula já cadastrada. Tente novamente."

        cursor.execute(
            "INSERT INTO alunos (matricula, nome, idade, curso, acesso) VALUES (%s, %s, %s, %s, %s)",
            (matricula, nome, idade, curso, acesso)
        )
        db.commit()
        return redirect(url_for("cadastro_notas"))
    return render_template("cadastro.html")

# Tela para cadastro de notas
@app.route("/cadastro_notas", methods=["GET", "POST"])
def cadastro_notas():
    if request.method == "POST":
        matricula = request.form["matricula"]
        nota = request.form["nota"]
        avaliacao = request.form["avaliacao"]

        # Inserir nota
        cursor.execute(
            "INSERT INTO notas (matricula_aluno, nota, avaliacao) VALUES (%s, %s, %s)",
            (matricula, nota, avaliacao)
        )
        db.commit()

        # Recalcular média
        cursor.execute("SELECT AVG(nota) AS media FROM notas WHERE matricula_aluno = %s", (matricula,))
        media = cursor.fetchone()["media"]
        cursor.execute("UPDATE alunos SET media = %s WHERE matricula = %s", (media, matricula))
        db.commit()

        return "Nota adicionada com sucesso!"
    return render_template("notas.html")

# Tela para listar todos os alunos com suas médias
@app.route("/listar_alunos")
def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    return render_template("listar.html", alunos=alunos)

if __name__ == "__main__":
    app.run(debug=True)
