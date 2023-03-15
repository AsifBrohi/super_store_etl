'''Create tables'''


'''creating dimension tables '''
shipping_table = '''Create table if not exists ship_mode(
    ship_mode_id serial primary key not null,
    ship_mode VARCHAR(60) not null);'''
region_table = '''Create table if not exists regions(
    region_id serial primary key not null,
    region VARCHAR(60) not null
);'''
