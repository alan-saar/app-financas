from api import marshmallow
from ..models import conta_model
from marshmallow import fields


class ContaSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = conta_model.Conta
        load_instance = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        valor = fields.Float(required=True)
