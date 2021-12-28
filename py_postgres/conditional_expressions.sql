
-- CASE-WHEN

select cc.customer_id, 
case
	when (cc.customer_id <= 100) then 'First'
	when (cc.customer_id between 100 and 110 ) then 'Second'
	when (cc.customer_id between 110 and 150) then 'Third'
else 'Nada'
end as customer_class
from public.customer cc 


-- CASE-WHEN EXPRESSION

select cc.customer_id, 
case cc.customer_id
	when 2 then 'Winner'
	when 3 then 'Second'
else 'Nada'
end as customer_prise
from public.customer cc 


-- both above together

select cc.customer_id, 
case
	when (cc.customer_id <= 100) then 'First'
	when (cc.customer_id between 100 and 110 ) then 'Second'
	when (cc.customer_id between 110 and 150) then 'Third'
else 'Nada'
end as customer_class,
case cc.customer_id
	when 2 then 'Winner'
	when 3 then 'Second'
else 'Nada'
end as customer_prise
from public.customer cc 


-- CHALLENGE
select distinct (ff.rating) from  public.film ff

select 
sum(case 
when (ff.rating = 'R') then 1 else 0
end) as r,
sum(case
when (ff.rating = 'PG') then 1  else 0
end) as pg,
sum(case
when (ff.rating = 'PG-13') then 1  else 0
end) as pg13
from public.film ff


-- CAST

select cast (5 as integer)

select '5'::integer




