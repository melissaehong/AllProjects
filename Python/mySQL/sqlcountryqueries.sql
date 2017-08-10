select countries.name, languages.language, languages.percentage
from countries
left join languages on countries.id = languages.country_id
where languages.language = 'Slovene'
order by languages.percentage desc;

select countries.name, count(cities.id) as cities_num
from countries
left join cities on countries.id = cities.country_id
group by countries.id
order by cities_num desc;

select cities.population, cities.name
from countries
left join cities on countries.id = cities.country_id
where countries.name = 'Mexico' and cities.population > 500000
order by cities.population desc;

select languages.percentage, languages.language, countries.name
from countries
left join languages on countries.id = languages.country_id
where languages.percentage > 89.00
order by languages.percentage desc;

select countries.surface_area, countries.population, countries.name
from countries
where countries.surface_area < 501 and countries.population > 100000;

select countries.government_form, countries.capital, countries.life_expectancy, countries.name
from countries
where countries.government_form = 'Constitutional Monarchy' and countries.capital > 200 and countries.life_expectancy > 75;

select countries.name, cities.name, cities.district, cities.population
from countries
left join cities on countries.id = cities.country_id
where countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;

select count(countries.id) as num, countries.region
from countries
group by countries.region
order by num desc;







