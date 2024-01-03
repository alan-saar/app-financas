from sqlalchemy.orm import identity
from api import api
from flask_restful import Resource
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services import usuario_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


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
                access_token = create_access_token(
                    identity=usuario_bd.id, expires_delta=timedelta(minutes=15)
                )
                refresh_token = create_refresh_token(identity=usuario_bd.id)
                return make_response(
                    jsonify(
                        {
                            "access_token": access_token,
                            "refresh_token": refresh_token,
                            "mensagem": "Login realizado com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return make_response(jsonify({ "mensagem": 'Credenciais Inválidas'}))


api.add_resource(LoginList, "/login")
