from api import db
from hashlib import md5
# from passlib.hash import pbkdf2_sha256


class Usuario(db.Model):
    __tablename__ = "usuario"
    __table_args__ = {"schema": "VOIP"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(90), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def cripto_senha(self):
        # self.senha = pbkdf2_sha256(self.senha)
        self.senha = md5(self.senha.encode('utf-8')).hexdigest()

    def decripto_senha(self, senha):
        return self.senha == md5(senha.encode('utf-8')).hexdigest()
