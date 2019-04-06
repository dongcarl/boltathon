from datetime import datetime
from boltathon.extensions import ma, db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class User(db.Model):
  __tablename__ = 'connection'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  date_created = db.Column(db.DateTime)
  email = db.Column(db.String(255), nullable=True)
  macaroon = db.Column(db.String(1023), nullable=True)
  cert = db.Column(db.String(2047), nullable=True)
  node_url = db.Column(db.String(255), nullable=True)
  pubkey = db.Colun(db.String(255), nullable=True)

  def __init__(self):
    self.id = uuid4()
    self.date_created = datetime.now()
  
  def update_config(
    self,
    email: str,
    macaroon: str,
    cert: str,
    node_url: str,
    pubkey: str,
  ):
    self.email = email
    self.macaroon = macaroon
    self.cert = cert
    self.node_url = node_url
    self.pubkey = pubkey
    db.session.add(self)
    db.session.flush()
