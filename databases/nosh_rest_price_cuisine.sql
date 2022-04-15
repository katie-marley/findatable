use nosh;

create table restaurant
(
Restaurant_ID int not null primary key auto_increment,
Restaurant_Name varchar(50) not null,
Address_Line_1 varchar(50) not null,
City varchar(50) not null,
Postcode varchar(8) not null,
Telephone varchar(15) not null,
Opening_Hours varchar(50) not null,
Cuisine_ID int, 
foreign key (Cuisine_ID) references Cuisine(Cuisine_ID),
Price_ID int, 
foreign key (Price_ID) references Price(Price_ID)
);

create table cuisine
(
Cuisine_ID int not null primary key auto_increment,
Cuisine_Name varchar(50) not null
);

create table price
(
Price_ID int not null primary key auto_increment,
Price_Values varchar(50) not null
);


