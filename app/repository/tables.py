from app.repository.database import db


class AccountModel(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), default="anonymous")
