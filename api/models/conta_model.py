from api import db


class Conta(db.Model):
    __tablename__ = "conta"
    __table_args__ = {"schema": "VOIP"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False) # noqa
    nome = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)
