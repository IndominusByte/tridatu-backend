from sqlalchemy import Table, Column, BigInteger, String, ForeignKey
from config import metadata

cart = Table('carts', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('note', String(100), nullable=True),
    Column('qty', BigInteger, nullable=False),
    Column('user_id', BigInteger, ForeignKey('users.id',onupdate='cascade',ondelete='cascade'), nullable=False),
    Column('variant_id',BigInteger,ForeignKey('variants.id',onupdate='cascade',ondelete='cascade'),nullable=False)
)
