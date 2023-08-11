CREATE TABLE fan ( 
 fan_id SERIAL4 PRIMARY KEY,
  admin_id INT4 NOT NULL,
  full_name VARCHAR(500) NOT NULL,
  email VARCHAR(150) NOT NULL,
  phone_number VARCHAR(150) NOT NULL,
  password VARCHAR NOT NULL
);
INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (1,'Zone Leslie','zonecoco0@gmail.com', '678098406', 'cocobaby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (2,'Zon Lesli','onecoco0@gmail.com', '678098400', 'ocobaby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (3,'one lie','izoneco0@gmail.com', '678098000', 'cbaby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (4,'jone Leslie','jonecoco0@gmail.com', '69780906', 'cocby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (1,'Zdone Lyt','bb0@gmail.com', '67780986', 'ttcobaby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (2,'Zone  bvlie','mccoco0@gmail.com', '67840637', 'nhobaby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (3,'Zovgc Leslie','lkbvco0@gmail.com', '67587406', 'fcfmocobaby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (4,'Zbg  Leskmlie','zonecnhvoco0@gmail.com', '67880986', 'ckklhocobaby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (1,'Zomgxe Leslie','zobolnecoco0@gmail.com', '67088406', 'conunzcobaby');

INSERT INTO fan(admin_id, full_name, email, phone_number, password)
VALUES (2,'Zongxe Leslie','zobllnecoco0@gmail.com', '67188406', 'conffzcobaby');




CREATE TABLE artist (
  artist_id SERIAL4 PRIMARY KEY,
   admin_id INT4 NOT NULL,
   full_name varchar(500), 
  username VARCHAR(200) NOT NULL,
  email VARCHAR(150) NOT NULL,
  phone_number VARCHAR(150) NOT NULL,
  password VARCHAR NOT NULL,
  image VARCHAR (500),
  seeking_venue VARCHAR CHECK (seeking_venue IN ('ON', 'OFF')),
  facebook_link varchar(200),
  instagram_link varchar(100),
  seeking_description VARCHAR(200) NOT NULL
);
insert into artist (admin_id, full_name, username, email, phone_number, password,  image, seeking_venue, facebook_link, instagram_link, seeking_description)
values(1, 'Nadege', 'cocobaby2612','zonecoco0@gmail.com', '678098406', 'cocobaby',  'eduijdmio', 'ON', 'www.facebook.com', 'www.instagram', 'sxhghiuj');

insert into artist (admin_id, full_name, username, email, phone_number, password,  Image,  seeking_venue,  facebook_link, instagram_link,seeking_description)
values(2,  'Naxdege', 'ella312','ella0@gmail.com', '678098903', 'ellie',   'uejwnfvc', 'OFF', 'www.facendook.com', 'www.instgdgram',  'fdrhxzg');

insert into artist (admin_id,  full_name,  username, email, phone_number, password,  Image, seeking_venue, facebook_link, instagram_link, seeking_description)
values(3,  'Naxfhge', 'cocobaby261','zoncoco0@gmail.com', '678098407', 'cocobaby1',  'mcjebg',  'ON', 'www.fausdfebook.com', 'www.insdhggram', 'ersxchj');

insert into artist (admin_id,  full_name, username, email, phone_number, password,  Image, seeking_venue, facebook_link, instagram_link, seeking_description)
values(4, 'Naxerjyge', 'ella312','ella0@gmail.com', '678098903', 'elliew', 'ftrsxergr', 'OFF','www.facebook.com', 'www.instagram', '');

insert into artist (admin_id,  full_name, username, email, phone_number, password,  Image,  seeking_venue, facebook_link, instagram_link, seeking_description)
values(1, 'Naxqwege', 'cochgbaby2612','zonehoco0@gmail.com', '678068406', 'coclbaby',  'riewjow', 'ON','www.faceeook.com', 'www.instigram', 'fcdt');

insert into artist (admin_id,  full_name, username, email, phone_number, password,  Image,  seeking_venue, facebook_link, instagram_link, seeking_description)
values(2, 'Naxqwele', 'cocogbaby2612','zonehoco0@gmail.com', '678068406', 'cocubaby',  'lprlrf', 'ON','www.faceeook.com', 'www.instigram', 'fcdt');


insert into artist (admin_id,  full_name, username, email, phone_number, password,  Image,  seeking_venue, facebook_link, instagram_link,  seeking_description)
values(3,  ' Nasege','elya312','elly0@gmail.com', '678098503', 'elie', 'thrbtvrf', 'OFF', 'www.facebnhgk.com', 'www.insxdngram', '');
select * FROM artist;

insert into artist (admin_id,  full_name, username, email, phone_number, password,  Image,  seeking_venue, facebook_link, instagram_link, seeking_description)
values(4, 'Naxqwege', 'cochibaby2612','zonemoco0@gmail.com', '678068406', 'cocibaby',  'rt4wrf4q', 'ON','www.faceeook.com', 'www.instigram', 'fcdt');

insert into artist ( admin_id,  full_name, username, email, phone_number, password,  Image, seeking_venue, facebook_link, instagram_link,  seeking_description)
values(1,  'Natuyge', 'cocaby2612','zoecoco0@gmail.com', '679098406', 'baby',   'egrefdwex', 'ON', 'www.faueyook.com', 'www.instenxram', '');

insert into artist (admin_id,  full_name, username, email, phone_number, password,  Image, seeking_venue, facebook_link, instagram_link,  seeking_description)
values(2,  'Naxyyge', 'elja312','la0@gmail.com', '675098903', 'elie',   'fwqdrqc', 'OFF', 'www.fahdyook.com', 'www.innyxedgram', '');



CREATE TABLE sysadmin (
  admin_id SERIAL4 PRIMARY KEY,
  first_name VARCHAR(200) NOT NULL,
  last_name VARCHAR(200) NOT NULL,
  email VARCHAR(150) NOT NULL,
  password VARCHAR NOT NULL
 
);


INSERT INTO sysadmin (first_name, last_name, email, password)
VALUES ('coco', 'baby', 'zonecoco0@gmail.com', 'cocobaby123');

INSERT INTO sysadmin (first_name, last_name, email, password)
VALUES ('baby', 'baby', 'coco0@gmail.com', 'cocobaby');

INSERT INTO sysadmin (first_name, last_name, email, password)
VALUES ('cocobaby2', 'baby', 'zonoco0@gmail.com', 'cocobaby1');

INSERT INTO sysadmin (first_name,last_name, email, password)
VALUES ('cocobaby26', 'baby', 'zoneco0@gmail.com', 'cocobaby12');




-- CREATE TABLE payment(
--   payment_id SERIAL4 PRIMARY KEY,
--   fan_id INT4 NOT NULL,
--   artist_id INT4 NOT NULL,
--   admin_id INT4 NOT NULL,
--   payment_method PAYMENTMETHOD,
--   payment_date Timestamp,
--   amount NUMERIC
-- );

-- insert into payment (fan_id, artist_id,admin_id, payment_method, payment_date, amount)
-- values(1, 1, 1, 'MOMO', '2023-02-03 11:30:00', 2000);

-- insert into payment(fan_id, artist_id, admin_id, payment_method, payment_date, amount)
-- values(2, 3, 2, 'OM', '2023-02-03 11:10:00', 22000);

-- insert into payment(fan_id, artist_id, admin_id,payment_method, payment_date, amount)
-- values(3, 3, 3, 'Card', '2023-02-03 11:20:00', 2000);

-- insert into payment(fan_id, artist_id, admin_id,payment_method, payment_date, amount)
-- values(4, 4, 4, 'OM', '2023-02-03 11:40:00', 12000);

-- insert into payment(fan_id, artist_id, admin_id,payment_method, payment_date, amount)
-- values(5, 5, 1, 'MOMO','2023-02-03 11:50:00', 2000);

-- insert into payment(fan_id, artist_id, admin_id,payment_method, payment_date, amount)
-- values(6, 6, 2, 'Card', '2023-02-03 11:59:00', 2000);

-- insert into payment(fan_id, artist_id, admin_id,payment_method, payment_date, amount)
-- values(7, 7, 3, 'MOMO', '2023-02-03 11:39:00', 2000);

-- insert into payment(fan_id, artist_id, admin_id,payment_method, payment_date, amount)
-- values(8, 8, 4, 'OM', '2023-02-03 13:30:00', 20000);

-- insert into payment(fan_id, artist_id, admin_id,payment_method, payment_date, amount)
-- values(9, 9, 1, 'Card', '2023-02-03 14:30:00', 20000);

-- insert into payment(fan_id, artist_id, admin_id,payment_method, payment_date, amount)
-- values(10, 10, 2, 'OM','2022-02-03 15:00:10', 25000);



CREATE TABLE venue(
venue_id SERIAL PRIMARY KEY,
admin_id INT4 NOT NULL,
artist_id INT4 not null,
  venue_name VARCHAR(200) NOT NULL,
  venue_capacity INT4 NOT NULL,
  venue_state varchar(100) check(venue_state in ('Available', 'Reserved')) NOT NULL,
  venue_location varchar(300) NOT NULL,
  venue_photo VARCHAR(500) not null
 
);

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(1, 1, 'memose', 200, 'Available', 'buea', '(E`\\xDEADBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(2, 2, 'omnisport', 200, 'Available', 'Limbe', '(E`\\aDEFDBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(3, 3, 'memose', 200, 'Available', 'buea', '(E`\\bDEADBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(4, 4, 'omnisport', 200, 'Available', 'Limbe', '(E`\\cDEFDBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(1, 5, 'mhtse', 200, 'Available', 'buea', '(E`\\dDEADBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(2, 6, 'omvgjsport', 200, 'Reserved', 'Limbe', '(E`\\eDEFDBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(3, 7, 'mftghose', 200, 'Reserved', 'buea', '(E`\\fDEADBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(4, 8, 'omnyyretport', 200, 'Reserved', 'Limbe', '(E`\\xAEFDBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(1, 9, 'mechnse', 200, 'Reserved', 'buea', '(E`\\xBEADBEEF`)');

insert into venue(admin_id, artist_id, venue_name, venue_capacity, venue_state, venue_location, venue_photo)
values(2, 10, 'omnictjort', 200, 'Reserved', 'Limbe', '(E`\\xCEFDBEEF`)');



 CREATE TABLE Show(
 show_id SERIAL PRIMARY KEY,
  show_name VARCHAR(100) NOT NULL,
  show_date timestamp NOT NULL,
  venue_id INT4 not null,
  fan_id INT4 NOT NULL,
  artist_id INT4 NOT NULL
 
);
insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('sing', '2023-01-03 12:30:00', 1, 1, 1);

insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('Night of Fame', '2023-02-03 11:30:00', 2, 2, 2);

insert into Show(show_name, show_date, venue_id, artist_id,fan_id)
values('sing', '2023-03-03 13:30:00', 3, 3, 3);

insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('Night of Fame', '2023-04-03 14:30:00', 4, 4, 4);

insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('sing', '2023-05-03 15:30:00', 5, 5, 5);

insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('sing', '2023-07-03 17:30:00', 6, 6, 6);

insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('Night of Fame', '2023-08-03 18:30:00', 7, 7, 7);

insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('sing', '2023-08-03 19:30:00', 8, 8, 8);

insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('Night of Fame', '2023-09-03 21:30:00', 9, 9, 9);

insert into Show(show_name, show_date, venue_id, artist_id, fan_id)
values('Night of Fame', '2023-09-03 22:30:00', 10, 10, 10);



CREATE TABLE ticket (
ticket_id SERIAL4 PRIMARY KEY,
  ticket_type TICKETTYPE NOT NULL,
  ticket_description VARCHAR(500) NOT NULL,
  show_id INT4 NOT NULL,
  fan_id INT4 NOT NULL,
  ticket_price NUMERIC NOT NULL CHECK (ticket_price > 0)
);


insert into ticket( ticket_type, ticket_description , show_id, fan_id, ticket_price)
values('VIP', 'this party is gonna be lite', 1, 1, 50000);

insert into ticket(ticket_type, ticket_description ,show_id, fan_id, ticket_price)
values('PLATINUM', 'dont miss this show', 2, 2, 70000);

insert into ticket( ticket_type, ticket_description , show_id, fan_id, ticket_price)
values('REGULAR', 'his party is gonna be lite', 3, 3, 50000);

insert into ticket( ticket_type, ticket_description , show_id, fan_id, ticket_price)
values('VIP', 'this party is gonna be lite', 4, 4, 50000);

insert into ticket(ticket_type, ticket_description ,show_id, fan_id, ticket_price)
values('PLATINUM', 'dont miss this show', 5, 5, 70000);

insert into ticket( ticket_type, ticket_description , show_id, fan_id, ticket_price)
values('REGULAR', 'this party is gonna be lite', 6, 6, 50000);

insert into ticket( ticket_type, ticket_description , show_id, fan_id, ticket_price)
values('VIP', 'this party is gonna be lite', 7, 7, 50000);

insert into ticket(ticket_type, ticket_description ,show_id, fan_id, ticket_price)
values('PLATINUM', 'dont miss this show', 8, 8, 70000);

insert into ticket( ticket_type, ticket_description , show_id, fan_id, ticket_price)
values('REGULAR', 'this party is gonna be lite', 9, 9, 50000);

insert into ticket( ticket_type, ticket_description , show_id, fan_id, ticket_price)
values('VIP', 'this party is gonna be lite', 10, 10, 50000);


