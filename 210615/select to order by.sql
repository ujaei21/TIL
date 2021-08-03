use tip;

select * from  tips limit 5;

select *, tip/total_bill as tip_rate from tips limit 5;

select * from tips where time = 'Dinner'
limit 5;

select * from tips where time = 'Dinner' and tip > 5 ;

select * from tips where size >= 5 or total_bill > 45;

select sex,count(*) count from tips group by sex;

select day,avg(tip), count(*) as count from tips 
group by day order by day;

select smoker,day, count(*) as count, avg(tip) as mean 
from tips group by smoker,day 
order by smoker;