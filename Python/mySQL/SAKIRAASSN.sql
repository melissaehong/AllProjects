select * from city;
select * from customer;
select * from address;
select * from film; 

#1
select address.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address 
from customer
left join address on customer.customer_id = address.address_id
left join city on address.city_id = city.city_id
where city.city_id = '312';

#2
select film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
from film_category
left join film on film_category.film_id = film.film_id
left join category on film_category.category_id = category.category_id
where category.name = 'comedy';

#3
select actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title, film.description, film.release_year
from film_actor
left join film on film_actor.film_id = film.film_id
left join actor on film_actor.actor_id = actor.actor_id
where film_actor.actor_id = 5;

#4
select customer.first_name, customer.last_name, customer.email, address.address
from customer
left join address on customer.address_id = address.address_id
where customer.store_id = 1
and address.city_id in (1, 42, 312, 459);

#5
select film.title, film.description, film.release_year, film.rating, film.special_features
from film
left join film_actor on film_actor.film_id = film.film_id
where film.rating = "G"
and film.special_features
like "%Behind the scenes%"
and actor_id = 15; 

#6
select actor.first_name, actor.last_name, actor.last_update
from actor
left join film_actor on actor.actor_id = film_actor.actor_id
where film_actor.film_id = 369;

#7
select film.title, film.description, film.release_year, film.rating, film.special_features, category.name
from film
left join film_category on film.film_id = film_category.film_id
left join category on film_category.category_id = category.category_id
where category.name = "drama" and film.rental_rate = 2.99;

#8
select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre, actor.first_name, actor.last_name
from film
left join film_actor on film_actor.film_id = film.film_id
left join actor on actor.actor_id = film_actor.actor_id
left join film_category on film_category.film_id = film.film_id
left join category on category.category_id = film_category.category_id
where actor.first_name = "SANDRA"
and actor.last_name = "KILMER"
and category.name = "Action";
