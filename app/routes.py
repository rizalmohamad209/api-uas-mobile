from app import app
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers import beritaController, usersController


@app.route('/signup', methods=['POST'])
def signUp():
    return usersController.signUp()


@app.route('/signin', methods=['POST'])
def signIn():
    return usersController.signIn()


@app.route('/user', methods=['PUT', 'GET'])
@jwt_required()
def userDetails():
    payload = get_jwt_identity()
    if(request.method == 'GET'):
        return usersController.getDetailUser(payload)
    elif(request.method == 'PUT'):
        return usersController.updateUser(payload)


@app.route('/berita', methods=["GET", "POST"])
@jwt_required()
def berita():
    if(request.method == 'GET'):
        return beritaController.getBerita()
    if(request.method == 'POST'):
        return beritaController.postBerita()


@app.route('/berita/<id>', methods=["GET", "PUT", "DELETE"])
@jwt_required()
def actionBerita(id):
    if(request.method == "GET"):
        return beritaController.getBeritaById(id)
    elif(request.method == "PUT"):
        return beritaController.updateBerita(id)
    elif(request.method == "DELETE"):
        return beritaController.deleteBerita(id)
