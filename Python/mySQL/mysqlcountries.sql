SELECT * FROM languages;
select * FROM cities;
select * from countries;

#1
select countries.name, languages.language, languages.percentage
from countries
left join languages ON countries.id = languages.country_id
where languages.language = 'Slovene'
order by languages.percentage desc;

#2
select countries.name, count(cities.id) as cities_num
from countries
join cities on countries.id = cities.country_id
group by countries.id
order by cities_num desc;

#3
select countries.name, cities.name, cities.population
from countries
left join cities on countries.id = cities.country_id
where countries.name = 'Mexico' and cities.population > 500000
order by cities.population desc;

#4
select countries.name, languages.language, languages.percentage
from countries
left join languages on countries.id = languages.country_id
where languages.percentage > 89.00
order by languages.percentage desc;

#5
select countries.name, countries.surface_area, countries.population
from countries
where countries.surface_area < 501 and countries.population > 100000;

#6
select countries.name, countries.government_form, countries.capital, countries.life_expectancy
from countries
where countries.government_form = "Constitutional Monarchy" and countries.capital > 200 and countries.life_expectancy > 75;

#7
select countries.name, cities.name, cities.district, cities.population
from countries
left join cities on countries.id = cities.country_id
where countries.name = "Argentina" and cities.population > 500000 and district = "Buenos Aires";

#8
select countries.region, count(countries.id) as country_num
from countries
group by countries.region
order by country_num desc;
