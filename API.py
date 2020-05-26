from flask import Flask, jsonify, request

app = Flask(__name__)

from Discos import Discos

#Voy a comprobar que el puerto funciona y que se ha activado de manera correcta
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


#ahora empiezo con la creación de la API de Discos
#en primer lugar hago que se muestren todos los discos que se han registrado
@app.route('/Discos')
def getDiscos():
    return jsonify({'Discos': Discos})

#Ahora lo que quiero es que muestre los datos de un disco, según su titulo
#@app.route('/Discos/<string:product_name>')
#def getDisco(product_name):
#   for Disco in Discos:
#        if Disco['titulo'] == product_name.lower():
#            DiscosFound=Disco
#    print(type(DiscosFound))
#   if (len(DiscosFound) > 0):
#        return jsonify({'Disco': DiscosFound})
#     return jsonify({'message': 'Producto no encontrado'})

@app.route('/Discos/<string:name_disk>')
def getDisco(name_disk):
    encontrado=False
    for Disco in Discos:
        print(Disco['titulo'])
        if Disco['titulo'].lower() == name_disk.lower():
            DiscosFound=Disco
            encontrado=True
            
    if encontrado==True:  
    #print(type(DiscosFound))
        return jsonify({'Disco': DiscosFound})
    else:
        return jsonify({'message': 'Producto no encontrado'})

#@app.route('/Discos/<string:genero_disk>')
#def getDisco_genero(genero_disk):
#    encontrado=False
#    for Disc in Discos:
#        print(Disc['genero'])
#        if Disc['genero'].lower() == genero_disk.lower():
#            DiscosFound=Disc
#            encontrado=True
#            
#    if encontrado==True:  
#    #print(type(DiscosFound))
#        return jsonify({'Disc': DiscosFound})
#    else:
#        return jsonify({'message': 'Producto no encontrado'})


#Ahora intento crear una aplicación que me permita añadir datos a mi API, en este caso Discos
#A la hora de intentar agregar el disco, se produce un error, y me sale el el mensaje de que no se pudo agregar
#de manera correcta el disco
@app.route("/Discos", methods=['POST'])
def addDisco():
    disco_nuevo = {
            'titulo': request.json['titulo'],
            'artista': request.json['artista'],
            'pais': request.json['pais'],
            'genero': request.json['genero'],
            'anyo_publicacion': request.json['anyo_publicacion']
    }

    Discos.append(disco_nuevo)
    return jsonify({'menssage': 'Producto no agregado correctamente'})

#Ahora lo que se va a intenar es actualizar un dato, para ello recibo un dato especifico, como puede ser el titulo
#Igual que antes, me vuelve ha salir un error
@app.route('/Discos/<string:name_disk>', methods=['PUT'])
def editDisk(name_disk):
    encontrado=False
    for Disco in Discos:
        print(Disco['titulo'])
        if Disco['titulo'].lower() == name_disk.lower():
            DiscosFound=Disco
            encontrado=True

    if encontrado==True:
        DiscosFound[0]['titulo'] = request.json['titulo']
        DiscosFound[0]['artista'] = request.json['artista']
        DiscosFound[0]['pais'] = request.json['pais']
        DiscosFound[0]['genero'] = request.json['genero']
        DiscosFound[0]['anyo_publicacion'] = request.json['anyo_publicacion']
        return jsonify({
            'message': 'Producto actualizado de manera correcta',
            'Disco': DiscosFound[0]
        })
    else:
        return jsonify({'message': 'Producto no encontrado'})

#Ahora diseño una forma para borrar datos de la API

@app.route('/Discos/<string:name_disk>', methods=['DELETE'])
def borrarDisco(name_disk):
    encontrado=False
    for Disco in Discos:
        print(Disco['titulo'])
        if Disco['titulo'].lower() == name_disk.lower():
            DiscosFound=Disco
            encontrado=True
    if encontrado==True:
        Discos.remove(DiscosFound[0])
        return jsonify({
            'message': 'Producto borrado correctamente',
            'Disco': Discos
        })

if __name__=='__main__':
    app.run(debug=True, port=5000)

#He intendado hacerlo como lo hicistes cuando lo explicaste y como lo hace
#el videotutorial, pero no me ha salido