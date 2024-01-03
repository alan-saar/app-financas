from api import db


class Conta(db.Model):
    __tablename__ = "conta"
    __table_args__ = {"schema": "VOIP"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False) # noqa
    nome = db.Column(db.String(50), nullable=False)
    resumo = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("VOIP.usuario.id"))
