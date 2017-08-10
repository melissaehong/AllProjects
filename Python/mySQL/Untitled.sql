select * from users;
select first_name as first, last_name as last from users;
select * from users
where id = 1 or id = 2
order by birthday asc;
insert into tweets (tweet, user_id, created_at, updated_at)
values ('hello', 1, now(), now());
select * from tweets;
update users set first_name = 'kobe1' where id = 1;
select * from users;
delete from tweets 
where id = 21;
select * from tweets;