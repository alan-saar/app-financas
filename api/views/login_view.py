from api import api
from flask_restful import Resource
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services import usuario_services


class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        errors = ls.validate(request.json)
        if errors:
            return make_response(jsonify(errors))
        else:
            email = request.json["email"]
            senha = request.json["senha"]

            usuario_bd = usuario_service.listar_usuario_email(email)
            if usuario_bd and usuario_bd.decripto_senha(senha):
                pass


api.add_resource(LoginList, "/login")
