from Instrucciones.Funciones.Funcion import Funcion
from grammar import parse, crearNativas, errores
from TS.TablaSimbolos import TablaSimbolos
from flask import Flask, jsonify, request
from TS.Excepcion import Excepcion
from TS.Arbol import Arbol
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/compiler', methods=["POST"])
def noseque():
    entrada = request.json["codigo"]
    instrucciones = parse(entrada) #ARBOL AST
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos('global')
    ast.setTSGlobal(TSGlobal)
    crearNativas(ast)

    for error in errores: #Captura de errores lexicos y sintacticos 
        ast.getExcepciones().append(error)
        ast.updateConsolaln(error.toString())
    

    for instruccion in ast.getInstrucciones():
        if isinstance(instruccion, Funcion):
            ast.addFuncion(instruccion)
        else:
            valor = instruccion.interpretar(ast, TSGlobal)
            if isinstance(valor, Excepcion):
                ast.getExcepciones().append(valor)
                ast.updateConsolaln(valor.toString())
        
    return jsonify({'salida': ast.getConsola()})

if __name__ == '__main__':
    app.run(debug=True, port=4000)

    