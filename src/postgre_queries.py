
shipping_table = '''CREATE table if NOT exists ship_mode(
    ship_mode_id SERIAL primary key NOT NULL,
    ship_mode VARCHAR(60) UNIQUE NOT NULL);'''
region_table = '''CREATE table if NOT exists regions(
    region_id SERIAL primary key NOT NULL,
    region VARCHAR(60) UNIQUE NOT NULL
);'''
segment_table = '''CREATE table if NOT exists segments(
    segment_id SERIAL primary key NOT NULL, 
    segment VARCHAR(60) UNIQUE NOT NULL
);
'''
city_table = '''CREATE table if NOT exists citys(
    city_id SERIAL primary key NOT NULL,
    city VARCHAR(100) UNIQUE NOT NULL
);'''
category_table = '''CREATE table if NOT exists category(
    category_id SERIAL primary key NOT NULL, 
    category VARCHAR(100) UNIQUE NOT NULL
);'''

sub_category_table = '''CREATE table if NOT exists sub_category(
    sub_category_id SERIAL primary key NOT NULL, 
    sub_category VARCHAR(100) UNIQUE NOT NULL
);'''
country_table = '''CREATE table if NOT exists country(
    country_id SERIAL primary key NOT NULL, 
    country VARCHAR(100) UNIQUE NOT NULL
);'''

state_table = '''CREATE table if NOT exists states(
    state_id SERIAL primary key NOT NULL, 
    state VARCHAR(100) UNIQUE NOT NULL
);'''

sales_fact = """CREATE TABLE IF NOT EXISTS sales_fact(
    sale_id SERIAL PRIMARY KEY NOT NULL,
    ship_mode_id INT NOT NULL,
    segment_id INT NOT NULL,
    country_id INT NOT NULL,
    city_id INT NOT NULL,
    state_id INT NOT NULL,
    region_id INT NOT NULL,
    category_id INT NOT NULL,
    sub_category_id INT NOT NULL,
    Sales MONEY NOT NULL,
    Profit MONEY NOT NULL,

    
    CONSTRAINT fk_shipmodes
        FOREIGN KEY(ship_mode_id)
            REFERENCES ship_mode(ship_mode_id),
    CONSTRAINT fk_segments
        FOREIGN KEY(segment_id)
            REFERENCES segments(segment_id),
    CONSTRAINT fk_country
        FOREIGN KEY(country_id)
            REFERENCES country(country_id),
    CONSTRAINT fk_cities
        FOREIGN KEY(city_id)
            REFERENCES citys(city_id), 
    CONSTRAINT fk_states
        FOREIGN KEY(state_id)
            REFERENCES states(state_id),
    CONSTRAINT fk_regions
        FOREIGN KEY(region_id)
            REFERENCES regions(region_id),            
    CONSTRAINT fk_category
        FOREIGN KEY(category_id)
            REFERENCES category(category_id),
    CONSTRAINT fk_sub_categorys
        FOREIGN KEY(sub_category_id)
            REFERENCES sub_category(sub_category_id)
    );"""

insert_fact_table    =  """
    INSERT INTO sales_fact(ship_mode_id, segment_id, country_id, city_id, state_id, region_id,category_id, sub_category_id,Sales,Profit) 
        VALUES (
            (SELECT ship_mode_id FROM ship_mode WHERE ship_mode = %s),
            (SELECT segment_id FROM segments WHERE segment = %s),
            (SELECT country_id FROM country WHERE country = %s),
            (SELECT city_id FROM citys WHERE city = %s),
            (SELECT state_id FROM states WHERE state = %s),
            (SELECT region_id FROM regions WHERE region = %s),
            (SELECT category_id FROM category WHERE category = %s),
            (SELECT sub_category_id FROM sub_category WHERE sub_category = %s),
            %s,
            %s
            );
            """
