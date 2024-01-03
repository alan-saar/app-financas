from api import db
from ..models import operacao_model, conta_model
from ..services import conta_service


def listar_operacoes(usuario):
    return operacao_model.Operacao.query.join(conta_model.Conta).filter_by(usuario_id=usuario).all()


def listar_operacao_id(id):
    return operacao_model.Operacao.query.filter_by(id=id).first()


def cadastrar_operacao(operacao):
    operacao_bd = operacao_model.Operacao(
        nome=operacao.nome,
        resumo=operacao.resumo,
        custo=operacao.custo,
        tipo=operacao.tipo,
        conta_id=operacao.conta
    )
    db.session.add(operacao_bd)
    db.session.commit()
    conta_service.altera_saldo_conta(operacao.conta, operacao, 1)
    return operacao_bd


def atualizar_operacao(operacao, operacao_nova):
    valor_antigo = operacao.custo
    operacao.nome = operacao_nova.nome
    operacao.resumo = operacao_nova.resumo
    operacao.custo = operacao_nova.custo
    operacao.tipo = operacao_nova.tipo
    operacao.conta_id = operacao_nova.conta
    db.session.commit()
    conta_service.altera_saldo_conta(operacao.conta_id, operacao, 2, valor_antigo)
    return operacao


def exclui_operacao(operacao):
    db.session.delete(operacao)
    db.session.commit()
    conta_service.altera_saldo_conta(operacao.conta_id, operacao, 3)
