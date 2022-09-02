from flask import Flask, render_template
app = Flask(__name__)

# 1. http://localhost:5000: deberíamostrarun tablero de ajedrez de 8 por 8
@app.route('/')
def html_inicio():
    return render_template('tablero1.html')

# 2. http://localhost:5000/4: debería mostrar un tablero de ajedrez de 8 por 4
@app.route('/<int:num>')
def num_tablero(num):
    num2 = int(num)/2
    print(num2)
    return render_template ('tablero2.html',numero=num, numero2=int(num2))

# 3• http://localhost:5000/(x)/(y): debería mostrar un tablero de ajedrez de x por
#ejemplo, http://localhost:5000/10/10 deberíamostrar un tablero de ajedrez de 10 por 10.
#Antes de pasar x y a Jinja, recuerdaprimero convertirlos a enteros (para que puedas
#usar x o y en un bucle for)
@app.route('/<int:num>/<int:count>')
def html_ten(num,count):
    num2 = int(num)/2
    count2 = int(count)/2
    print(num)
    print(count)
    return render_template('tablero3.html', num1 = int(num2), num2 = int(count2))


if __name__=="__main__":
    app.run(debug=True)