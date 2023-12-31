from api import db, app
from ..models import conta_model


def listar_contas(usuario):
    contas = conta_model.Conta.query.filter_by(usuario_id=usuario)
    return contas


def listar_conta_id(id):
    return conta_model.Conta.query.filter_by(id=id).first()


def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(
        nome=conta.nome, resumo=conta.resumo, valor=conta.valor, usuario_id=conta.usuario
    )  # noqa
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


def altera_saldo_conta(conta_id, operacao, tipo_funcao, valor_antigo=None):
    app.logger.info("entrou aqui")
    # tipo_funcao -> 1 = Cadastro de operação
    # tipo_funcao -> 2 = Atualização de operação
    # tipo_funcao -> 3 = Exclusão de Operação
    conta = listar_conta_id(conta_id)
    if tipo_funcao == 1:
        if operacao.tipo == "entrada":
            conta.valor += operacao.custo
        else:
            conta.valor -= operacao.custo
    elif tipo_funcao == 2:
        if operacao.tipo == "entrada":
            conta.valor -= valor_antigo
            conta.valor += operacao.custo
        else:
            conta.valor += valor_antigo
            conta.valor -= operacao.custo
    elif tipo_funcao == 3:
        app.logger.info("entrou aqui também: " + str(operacao.tipo.value))
        if operacao.tipo.value == 1:
            conta.valor -= operacao.custo
        else:
            conta.valor += operacao.custo


    db.session.commit()
