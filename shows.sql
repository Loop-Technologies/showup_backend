 CREATE TABLE Show(
 show_id INT4 PRIMARY KEY,
  show_name VARCHAR(100) NOT NULL,
  show_date timestamp NOT NULL,
  venue_id INT4 not null,
  fan_id INT4 NOT NULL,
  artist_id INT4 NOT NULL
 
);
insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(1,'sing', '2023-01-03 12:30:00', 1, 1, 1);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(2,'Night of Fame', '2023-02-03 11:30:00', 2, 2, 2);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id,fan_id)
values(3,'sing', '2023-03-03 13:30:00', 3, 3, 3);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(4,'Night of Fame', '2023-04-03 14:30:00', 4, 4, 4);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(5,'sing', '2023-05-03 15:30:00', 5, 5, 5);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(6,'sing', '2023-07-03 17:30:00', 6, 6, 6);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(7,'Night of Fame', '2023-08-03 18:30:00', 7, 7, 7);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(8,'sing', '2023-08-03 19:30:00', 8, 8, 8);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(9,'Night of Fame', '2023-09-03 21:30:00', 9, 9, 9);

insert into Show(show_id ,show_name, show_date, venue_id, artist_id, fan_id)
values(10,'Night of Fame', '2023-09-03 22:30:00', 10, 10, 10);
