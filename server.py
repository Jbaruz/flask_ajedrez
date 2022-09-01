from flask import Flask, render_template
app = Flask(__name__)

# 1. http://localhost:5000: deberíamostrarun tablero de ajedrez de 8 por 8
@app.route('/')
def html_inicio():
    return render_template('tablero1.html')

#2. http://localhost:5000/4: debería mostrar un tablero de ajedrez de 8 por 4
@app.route('/<int:num>')
def num_tablero(num):
    return render_template ('tablero2.html',numero=num)


if __name__=="__main__":
    app.run(debug=True)