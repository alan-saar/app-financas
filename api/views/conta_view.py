from flask_restful import Resource
from ..schemas import conta_schema
from flask import jsonify, make_response, request
from ..entidades import conta
from ..services import conta_service
from api import api
from flask_jwt_extended import jwt_required


class ContaList(Resource):

    @jwt_required()
    def get(self):
        contas = conta_service.listar_contas()
        cs = conta_schema.ContaSchema(many=True)
        return make_response(cs.jsonify(contas), 201)

    @jwt_required()
    def post(self):
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome, resumo=resumo, valor=valor)
            resultado = conta_service.cadastrar_conta(conta_nova)
            return make_response(cs.jsonify(resultado), 201)


api.add_resource(ContaList, '/contas')


class ContaDetail(Resource):

    @jwt_required()
    def get(self, id):
        conta = conta_service.listar_conta_id(id)
        if conta is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        cs = conta_schema.ContaSchema()
        return make_response(cs.jsonify(conta), 200)

    @jwt_required()
    def put(self, id):
        conta_bd = conta_service.listar_conta_id(id)
        if conta_bd is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        cs = conta_schema.ContaSchema()
        errors = cs.validate(request.json)
        if errors:
            return make_response(jsonify(errors), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome, resumo=resumo, valor=valor)
            resultado = conta_service.atualizar_conta(conta_bd, conta_nova)
            return make_response(cs.jsonify(resultado), 201)

    @jwt_required()
    def delete(self, id):
        conta = conta_service.listar_conta_id(id)
        if conta is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        conta_service.exclui_conta(conta)
        return make_response(jsonify(""), 204)



api.add_resource(ContaDetail, '/contas/<int:id>')
