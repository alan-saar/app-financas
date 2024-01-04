from api import marshmallow
from ..models import conta_model
from marshmallow import fields
from ..schemas import operacao_schema


class ContaSchema(marshmallow.SQLAlchemyAutoSchema):
    operacoes = marshmallow.Nested(operacao_schema.OperacaoSchema, many=True, only=('id', 'nome', 'resumo', 'tipo', 'custo', 'data'))
    class Meta:
        model = conta_model.Conta
        load_instance = True

        nome = fields.String(required=True)
        valor = fields.Float(required=True)
