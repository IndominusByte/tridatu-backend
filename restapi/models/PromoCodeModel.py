from sqlalchemy import Table, Column, BigInteger, Integer, Float, String, ForeignKey
from config import metadata

promo_code = Table('promo_codes', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('code', String(20), nullable=False),
    Column('quota', Integer, nullable=False),
    Column('min_transaction', Integer, nullable=False),
    Column('nominal', Integer, nullable=True),
    Column('percent', Float, nullable=True),
    Column('max_discount', Integer, nullable=True),
    Column('kind', String(50), nullable=False),
    Column('applicable_product', String(50), nullable=False),
    Column('promo_id', BigInteger,ForeignKey('promos.id',onupdate='cascade',ondelete='cascade'),nullable=False),
)
