from sqlalchemy import Table, Column, BigInteger, Integer, ForeignKey
from config import metadata

promo_apply = Table('promo_applies', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('product_id', BigInteger,ForeignKey('products.id',onupdate='cascade',ondelete='cascade'),nullable=True),
    Column('brand_id', Integer, ForeignKey('brands.id',onupdate='cascade',ondelete='cascade'), nullable=True),
    Column('category_id', Integer,ForeignKey('categories.id',onupdate='cascade',ondelete='cascade'),nullable=True),
    Column('sub_category_id', Integer,ForeignKey('sub_categories.id',onupdate='cascade',ondelete='cascade'),nullable=True),
    Column(
        'item_sub_category_id', Integer,
        ForeignKey('item_sub_categories.id',onupdate='cascade',ondelete='cascade'),
        nullable=True
    ),
    Column('promo_code_id', BigInteger,ForeignKey('promo_codes.id',onupdate='cascade',ondelete='cascade'),nullable=False),
)
