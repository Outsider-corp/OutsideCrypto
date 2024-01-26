CREATE SCHEMA IF NOT EXISTS crypto;

CREATE TABLE crypto.transaction
(
    id               integer PRIMARY KEY,
    user_id          integer          NOT NULL,
    from_exchange_id integer          NOT NULL,
    to_exchange_id   integer          NOT NULL,
    coin             varchar          NOT NULL,
    count            double precision NOT NULL,
    datetime         date             NOT NULL,
    commission_coin  varchar          NOT NULL,
    commission_count varchar          NOT NULL
);

CREATE TABLE crypto.spot
(
    id             integer PRIMARY KEY,
    user_id        integer          NOT NULL,
    exchange_id    integer          NOT NULL,
    wasted_coin    varchar          NOT NULL,
    wasted_count   double precision NOT NULL,
    received_coin  varchar          NOT NULL,
    received_count double precision NOT NULL,
    datetime       date             NOT NULL
);

CREATE TABLE crypto.p2p
(
    id          integer PRIMARY KEY,
    user_id     integer          NOT NULL,
    exchange_id integer          NOT NULL,
    currency    varchar          NOT NULL,
    price       double precision NOT NULL,
    coin        varchar          NOT NULL,
    count       double precision NOT NULL
);

CREATE TABLE crypto.user
(
    id       integer PRIMARY KEY,
    login    varchar NOT NULL,
    password varchar NOT NULL,
    email    varchar NOT NULL
);

CREATE TABLE crypto.api_key
(
    id          integer PRIMARY KEY,
    user_id     integer NOT NULL,
    exchange_id integer NOT NULL,
    key_role_id integer NOT NULL,
    public_api  text    NOT NULL,
    secret_api  text
);

CREATE TABLE crypto.key_role
(
    id      integer PRIMARY KEY,
    purpose varchar NOT NULL
);

CREATE TABLE crypto.exchange
(
    id            integer PRIMARY KEY,
    exchange_name varchar NOT NULL
);


ALTER TABLE crypto.transaction
    ADD FOREIGN KEY (user_id) REFERENCES crypto.user (id);
ALTER TABLE crypto.transaction
    ADD FOREIGN KEY (from_exchange_id) REFERENCES crypto.exchange (id);
ALTER TABLE crypto.transaction
    ADD FOREIGN KEY (to_exchange_id) REFERENCES crypto.exchange (id);

ALTER TABLE crypto.spot
    ADD FOREIGN KEY (user_id) REFERENCES crypto.user (id);
ALTER TABLE crypto.spot
    ADD FOREIGN KEY (exchange_id) REFERENCES crypto.exchange (id);

ALTER TABLE crypto.p2p
    ADD FOREIGN KEY (user_id) REFERENCES crypto.user (id);
ALTER TABLE crypto.p2p
    ADD FOREIGN KEY (exchange_id) REFERENCES crypto.exchange (id);

ALTER TABLE crypto.api_key
    ADD FOREIGN KEY (user_id) REFERENCES crypto.user (id);
ALTER TABLE crypto.api_key
    ADD FOREIGN KEY (exchange_id) REFERENCES crypto.exchange (id);
ALTER TABLE crypto.api_key
    ADD FOREIGN KEY (key_role_id) REFERENCES crypto.key_role (id);
