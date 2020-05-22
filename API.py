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


#En esta ocasión lo que se busca, es mostrar los discos que se den en un año determinado
#Código viejo, que uso para comparar
#@app.route('/Discos/<string:product_anyo>')
#def getAnyo(product_anyo):
#
#   for anyo in Discos:
#        if anyo['año_publicacion'] == product_anyo.lower():
#            anyoFound=anyo
#    print(type(anyoFound))
#    if(len(anyoFound) > 0):
#        return jsonify({'anyo': anyoFound})
#    return jsonify({'message': 'Producto no encontrado'})

@app.route('/Discos/<string:genero_disk>')
def getDisco_genero(genero_disk):
    encontrado=False
    for Disco in Discos:
        print(Disco['genero'])
        if Disco['genero'].lower() == genero_disk.lower():
            DiscosFound=Disco
            encontrado=True
            
    if encontrado==True:  
    #print(type(DiscosFound))
        return jsonify({'Disco': DiscosFound})
    else:
        return jsonify({'message': 'Producto no encontrado'})

if __name__=='__main__':
    app.run(debug=True, port=5000)