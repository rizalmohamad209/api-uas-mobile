from app import app
from flask import request, jsonify
from flask_marshmallow import Marshmallow
from app.models.beritaModel import db, Berita
import cloudinary.uploader

ma = Marshmallow(app)


class BeritaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'image',
                  'content', 'createdAt')


# init schema
beritaSchema = BeritaSchema()
beritaSchemas = BeritaSchema(many=True)


def getBerita():
    allBerita = Berita.query.all()
    result = beritaSchemas.dump(allBerita)
    return jsonify({"msg": "Success Get all Berita", "status": 200, "data": result})


def getBeritaById(id):
    berita = Berita.query.get(id)
    result = beritaSchema.dump(berita)
    return jsonify({"msg": "Success Get Berita By Id", "status": 200, "data": result})


def postBerita():
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    title = request.form['title']
    content = request.form['content']

    if 'image' not in request.files:
        resp = jsonify({"msg": "No body image attached in request"})
        resp.status_code = 501
        return resp
    fileImage = request.files['image']
    if fileImage.filename == '':
        resp = jsonify({'msg': "No file fileImage selected"})
        resp.status_code = 505
        return resp

    print(fileImage.filename)
    error = {}

    if fileImage and allowed_file(fileImage.filename):
        upload_result = cloudinary.uploader.upload(fileImage)
        image = upload_result["secure_url"]
    else:
        error[fileImage.filename] = 'File type is not allowed'

    newBerita = Berita(title, content, image)
    db.session.add(newBerita)
    db.session.commit()
    new = beritaSchema.dump(newBerita)
    return jsonify({"msg": "Success Post Berita", "status": 200, "data": new})


def updateBerita(id):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    berita = Berita.query.get(id)

    title = request.form['title']
    content = request.form['content']

    if 'image' not in request.files:
        resp = jsonify({"msg": "No body image attached in request"})
        resp.status_code = 501
        return resp
    fileImage = request.files['image']
    print(fileImage.filename)
    if fileImage.filename == '':
        resp = jsonify({'msg': "No file fileImage selected"})
        resp.status_code = 505
        return resp

    error = {}

    if fileImage and allowed_file(fileImage.filename):
        upload_result = cloudinary.uploader.upload(fileImage)
        print(upload_result["secure_url"])
        image = upload_result["secure_url"]
    else:
        error[fileImage.filename] = 'File type is not allowed'

    berita.title = title
    berita.content = content
    berita.image = image

    db.session.commit()
    BeritaUpdate = beritaSchema.dump(berita)
    return jsonify({"msg": "Success update berita", "status": 200, "data": BeritaUpdate})


def deleteBerita(id):
    berita = Berita.query.get(id)
    db.session.delete(berita)
    db.session.commit()
    BeritaDelete = beritaSchema.dump(berita)
    return jsonify({"msg": "Success Delete Berita", "status": 200, "data": BeritaDelete})
