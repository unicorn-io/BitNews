from app import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())
    

class Contracts(Base):
    __tablename__ = 'contracts'
    upvotes = db.Column(db.BigInteger, nullable=False)
    downvotes = db.Column(db.BigInteger, nullable=False)