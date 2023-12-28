from api import marshmallow
from ..models import operacao_model
from marshmallow import fields
from marshmallow_enum import EnumField


class OperacaoSchema(marshmallow.SQLAlchemyAutoSchema):
    tipo = EnumField(operacao_model.TipoOperacao, required=True)

    class Meta:
        model = operacao_model.Operacao
        load_instance = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        custo = fields.Float(required=True)
