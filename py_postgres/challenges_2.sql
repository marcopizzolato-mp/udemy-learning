
-- ASSESSMENT TEST 2

-- How can you retrieve all the information from the cd.facilities table?
select * from cd.facilities ff


-- You want to print out a list of all of the facilities and their cost to members. 
-- How would you retrieve a list of only facility names and costs?

select ff."name" , sum(ff.membercost) from cd.facilities ff 
group by ff."name" 

-- How can you produce a list of facilities that charge a fee to members?

select ff."name" , sum(ff.membercost) from cd.facilities ff 
group by ff."name" 
having sum(ff.membercost) > 0 


-- How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost?
-- Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.

select ff."name", ff.facid, ff.membercost, ff.monthlymaintenance from cd.facilities ff 
where ff.membercost < (ff.monthlymaintenance/50) and ff.membercost > 0


-- How can you produce a list of all facilities with the word 'Tennis' in their name?

select ff."name" from cd.facilities ff 
where ff."name" ilike '%Tennis%'

-- How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.

select * from cd.facilities ff 
where ff.facid in (1,5)


-- How can you produce a list of members who joined after the start of September 2012? 
-- Return the memid, surname, firstname, and joindate of the members in question

select mm.memid , mm.surname , mm.firstname , extract (month from mm.joindate) as datetime from cd.members mm
where extract (month from mm.joindate) > 8



-- How can you produce an ordered list of the first 10 surnames in the members table?
-- The list must not contain duplicates.

select distinct(mm.surname) as surlimi from cd.members mm
order by surlimi asc limit 10

-- You'd like to get the signup date of your last member. How can you retrieve this information?

select mm.joindate from cd.members mm 
order by age(mm.joindate) asc limit 1

-- Produce a count of the number of facilities that have a cost to guests of 10 or more.

select count(*) from  cd.facilities ff
where guestcost > 10


-- Produce a list of the total number of slots booked per facility in the month of September 2012.
-- Produce an output table consisting of facility id and slots, sorted by the number of slots.

select cc."name" , sum(bb.slots) from cd.bookings bb 
join cd.facilities cc on cc.facid = bb.facid 
where extract (month from bb.starttime) = 9
group by cc."name"
order by sum(bb.slots) asc 


-- Produce a list of facilities with more than 1000 slots booked.
-- Produce an output table consisting of facility id and total slots, sorted by facility id.

select cc."name" , sum(bb.slots) from cd.bookings bb 
join cd.facilities cc on cc.facid = bb.facid 
group by cc."name"
having sum(bb.slots) > 1000
order by sum(cc.facid) desc


-- How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'?
-- Return a list of start time and facility name pairings, ordered by the time.


select cc."name", to_char(bb.starttime,'HH24-MM'), to_char(bb.starttime, 'YYYY-MM-DD')  from cd.bookings bb
join cd.facilities cc on cc.facid = bb.facid 
where to_char(bb.starttime, 'YYYY-MM-DD') = '2012-09-21' and 
cc."name" ilike ('%Tennis Co%')


-- How can you produce a list of the start times for bookings by members named 'David Farrell'?

select concat(mm.firstname, ' ', mm.surname), to_char(bb.starttime,'HH24-MM'), to_char(bb.starttime, 'YYYY-MM-DD')  from cd.bookings bb
join cd.members mm on mm.memid = bb.memid 
where concat(mm.firstname, ' ', mm.surname) ilike ('%David Farrell%')





