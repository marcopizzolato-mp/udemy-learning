-- CHALLENGE CHAPTER 1

SELECT count(pp.amount) from public.payment pp where pp.amount > 5;
--3618 

select count(pp.first_name) from public.actor pp where pp.first_name LIKE 'P%';
-- 5

select count(distinct (aa.district)) from public.address aa
--378

select count(*) from public.film ff where rating = 'R' and replacement_cost between 5 and 15;
-- 52

select count(*) from public.film where title like ('%Truman%')
-- 5

-- CHALLENGE CHAPTER 2

select staff_id, count(*) from public.payment 
where staff_id in (1,2)
group by staff_id 


select rating, round(avg(replacement_cost),2) as average from public.film
group by rating 
order by average desc 


select customer_id, sum(amount) as sommatot from public.payment
group by customer_id 
order by sommatot desc 
limit 5 

-- CHALLENGE 3

select customer_id, count(amount) as transtot from public.payment
group by customer_id
having count(amount) >= 40
order by transtot desc 



select customer_id, sum(amount) as transtot from public.payment
where staff_id = 2
group by customer_id
having sum(amount) > 100
order by transtot desc 


-- ASSESSMENT TEST 1

-- 1. Return the customer IDs of customers who have spent at least $110 with the staff member who has an ID of 2.

select customer_id, sum(amount) as transtot from public.payment
where staff_id = 2
group by customer_id
having sum(amount) > 110
order by transtot desc

-- 2. How many films begin with the letter J?

select count(title) from public.film where title like 'J%'

-- 3. What customer has the highest customer ID number whose name starts with an 'E' and has an address ID lower than 500?

select first_name, last_name from public.customer
where first_name like 'E%' and address_id < 500
order by customer_id desc 
limit 1


-- CHALLENGE 4 Joins

-- What are the emails of the customers who live in Caifornia

select pc.first_name, pc.last_name, pc.email, pa.district from public.customer pc
left join public.address pa on pc.address_id = pa.address_id 
where pa.district = 'California'


select ff.title, aa.first_name, aa.last_name from public.film ff
left join public.film_actor fa on fa.film_id = ff.film_id 
left join public.actor aa on fa.actor_id = aa.actor_id 
where concat( aa.first_name, ' ', aa.last_name) = 'Nick Wahlberg'


-- CHALLENGE 5 Extract - to_char 

select distinct(to_char(pp.payment_date , 'month')) from public.payment pp

select count(*) from public.payment pp where extract(dow from pp.payment_date) = 1

