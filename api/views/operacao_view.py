from flask_restful import Resource
from ..schemas import operacao_schema
from flask import jsonify, make_response, request
from ..entidades import operacao
from ..services import operacao_service, conta_service
from api import api


class OperacaoList(Resource):
    def get(self):
        operacoes = operacao_service.listar_operacoes()
        os = operacao_schema.OperacaoSchema(many=True)
        return make_response(os.jsonify(operacoes), 201)

    def post(self):
        os = operacao_schema.OperacaoSchema()
        errors = os.validate(request.json)
        if errors:
            return make_response(jsonify(errors), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]
            if conta_service.listar_conta_id(conta) is None:
                return make_response(jsonify("Conta não existe"), 404)

            nova_operacao = operacao.Operacao(
                nome=nome, resumo=resumo, custo=custo, tipo=tipo, conta=conta
            )
            resultado = operacao_service.cadastrar_operacao(nova_operacao)
            return make_response(os.jsonify(resultado), 201)


class OperacaoDetail(Resource):
    def get(self, id):
        operacao = operacao_service.listar_operacao_id(id)
        if operacao is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        os = operacao_schema.OperacaoSchema()
        return make_response(os.jsonify(operacao), 200)

    def put(self, id):
        operacao_bd = operacao_service.listar_operacao_id(id)
        if operacao_bd is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        os = operacao_schema.OperacaoSchema()
        errors = os.validate(request.json)
        if errors:
            return make_response(jsonify(errors), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]

            if conta_service.listar_conta_id(conta) is None:
                return make_response(jsonify("Conta não existe"), 404)
            operacao_nova = operacao.Operacao(
                nome=nome, resumo=resumo, custo=custo, tipo=tipo, conta=conta
            )
            resultado = operacao_service.atualizar_operacao(operacao_bd, operacao_nova) # noqa
            return make_response(os.jsonify(resultado), 201)

    def delete(self, id):
        operacao = operacao_service.listar_operacao_id(id)
        if operacao is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        operacao_service.exclui_operacao(operacao)
        return make_response(jsonify(""), 204)


api.add_resource(OperacaoList, "/operacoes")
api.add_resource(OperacaoDetail, "/operacoes/<int:id>")
