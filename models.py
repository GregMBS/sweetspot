# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, MetaData, Table, Text, Time, text

metadata = MetaData()


t_business = Table(
    'business', metadata,
    Column('id', BigInteger, nullable=False, unique=True,
           server_default=text("nextval('business_id_seq'::regclass)")),
    Column('name', Text)
)


t_user = Table(
    'user', metadata,
    Column('id', BigInteger, nullable=False, unique=True,
           server_default=text("nextval('user_id_seq'::regclass)")),
    Column('admin', Boolean,
           server_default=text("false")),
    Column('business_id', BigInteger, nullable=False,
           server_default=text("nextval('user_business_id_seq'::regclass)")),
    Column('name', Text)
)


t_beacon = Table(
    'beacon', metadata,
    Column('id', BigInteger, nullable=False, unique=True,
           server_default=text("nextval('beacon_id_seq'::regclass)")),
    Column('business_id', ForeignKey('business.id'), nullable=False, index=True,
           server_default=text("nextval('beacon_business_id_seq'::regclass)")),
    Column('user_id', ForeignKey('user.id'), nullable=False, index=True,
           server_default=text("nextval('beacon_user_id_seq'::regclass)"))
)


t_data = Table(
    'data', metadata,
    Column('id', BigInteger, nullable=False, unique=True,
           server_default=text("nextval('data_id_seq'::regclass)")),
    Column('beacon_id', ForeignKey('beacon.id'), nullable=False, index=True,
           server_default=text("nextval('data_beacon_id_seq'::regclass)")),
    Column('timestamp', Time),
    Column('counter', BigInteger,
           server_default=text("0"))
)
