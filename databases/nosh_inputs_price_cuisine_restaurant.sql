use nosh;
insert into price (price_values)
values ('£25 and under'), 
('£26 - £40'),
('£41 and over');

insert into cuisine(cuisine_name)
values ('Indian'),
('Chinese'),
('Italian'),
('Lebanese'),
('Japanese'),
('Mexican');

insert into restaurant(Restaurant_name, Address_Line_1, City, Postcode, Telephone, Opening_Hours, Cuisine_ID, Price_ID)
values ('The Famous Curry Bazaar', '77 Brick Lane', 'London', 'E1 6QL', '02073751986', 'Monday to Sunday, 12pm to 12am',1, 2),
('Orient London', '15 Wardour Street', 'London', 'W1D 6PH', '02079898880', 'Monday to Sunday, 11am to 11pm', 2, 2),
('Pizza Hut', '34 Colllege Raod', 'Harrow', 'H1 1AT', '02088632525', 'Monday to Sunday , 11am to 6pm',3, 1),
('Tarboush', '57 Market Street', 'Watford', 'WD18 0PR', '01923248898', 'Monday to Sunday, 11am to 12am', 4, 1),
('Umu Restaurant', '14 to 16 Bruton Place', 'London', 'W1 6LX', '02074998881', 'Monday to Sunday, 12pm to 2 pm, 6pm to 10pm', 5, 3),
('Ella Canta', '1 Hambleton Place', 'London', 'W1J 7QI', '02073188715', 'Monday to Sunday 12pm to 12am', 6,3)
;
 
