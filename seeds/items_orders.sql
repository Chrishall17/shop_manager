-- DROP TABLE IF EXISTS items CASCADE;
-- DROP SEQUENCE IF EXISTS items_id_seq;
-- DROP TABLE IF EXISTS orders CASCADE;
-- DROP SEQUENCE IF EXISTS orders_id_seq;
-- DROP TABLE IF EXISTS items_orders CASCADE;

-- Create the first table.
-- CREATE SEQUENCE IF NOT EXISTS items_id_seq;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name text,
    unit_price int,
    quantity int
);

-- Create the second table.
-- CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer text,
    order_date date
);

-- Create the join table.
CREATE TABLE items_orders (
    item_id int,
    order_id int,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    PRIMARY KEY (item_id, order_id)
);

INSERT INTO items (name, unit_price, quantity) VALUES ('Vacuum', 99, 30);
INSERT INTO items (name, unit_price, quantity) VALUES ('Coffee Machine', 69, 15);
INSERT INTO items (name, unit_price, quantity) VALUES ('Monopoly', 18, 20);
INSERT INTO items (name, unit_price, quantity) VALUES ('Prime', 12, 1);

INSERT INTO orders (customer, order_date) VALUES ('Chris', '2023-3-24');

INSERT INTO items_orders (item_id, order_id) VALUES (1, 1);