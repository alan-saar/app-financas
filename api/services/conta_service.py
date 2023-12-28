from api import db
from ..models import conta_model


def listar_contas():
    contas = conta_model.Conta.query.all()
    return contas


def listar_conta_id(id):
    return conta_model.Conta.query.filter_by(id=id).first()


def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(nome=conta.nome, resumo=conta.resumo, valor=conta.valor)  # noqa
    db.session.add(conta_bd)
    db.session.commit()
    return conta_bd


def atualizar_conta(conta, conta_nova):
    conta.nome = conta_nova.nome
    conta.resumo = conta_nova.resumo
    conta.valor = conta_nova.valor
    db.session.commit()
    return conta


def exclui_conta(conta):
    db.session.delete(conta)
    db.session.commit()
