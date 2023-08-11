from datetime import date
from app import db, showevn
db.drop_all()
db.create_all()

sh1=Show(
    show_name='sing',
    show_date='2023-01-03 12:30:00',
    venue_id=1,
    fan_id=1,
    artist_id=1
)
sh2=Show(
    show_name='sing all night',
    show_date='2023-03-03 12:30:00' ,
    venue_id=2,
    fan_id=2,
    artist_id=2
)
sh3= Show(show_name='sing',
    show_date='2023-02-03 12:30:00',
    venue_id=3,
    fan_id=3,
    artist_id=3
)
sh4=Show(
    show_name='night of fame',
    show_date='2023-04-03 12:30:00',
    venue_id=4,
    fan_id=4,
    artist_id=4
)
sh5=Show(
    show_name='sing',
    show_date='2023-05-03 12:30:00',
    venue_id=5,
    fan_id=5,
    artist_id=5
)
sh6=Show(
    show_name='sing',
    show_date='2023-06-03 12:30:00',
    venue_id=6,
    fan_id=6,
    artist_id=6
)
sh7=Show(
    show_name='sing',
    show_date='2023-07-03 12:30:00',
    venue_id=7,
    fan_id=7,
    artist_id=7
)
sh8=Show(
    show_name='sing',
    show_date='2023-08-03 12:30:00',
    venue_id=8,
    fan_id=8,
    artist_id=8
)
sh9=Show(
    show_name='sing',
    show_date='2023-09-03 12:30:00',
    venue_id=9,
    fan_id=9,
    artist_id=9
)
sh10=Show(
    show_name='sing',
    show_date='2023-10-03 12:30:00',
    venue_id=10,
    fan_id=10,
    artist_id=10
)
sh11=Show(
    show_name='sing',
    show_date='2023-11-03 12:30:00',
    venue_id=11,
    fan_id=11,
    artist_id=11
)
sh12=Show(
    show_name='sing',
    show_date='2024-01-03 12:30:00',
    venue_id=12,
    fan_id=12,
    artist_id=12
)
sh13=Show(
    show_name='sing',
    show_date='2024-11-03 12:30:00',
    venue_id=13,
    fan_id=13,
    artist_id=13
)
db.session.add_all([sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8, sh9, sh10 , sh11 , sh12 , sh13])

db.session.commit()