create table Applicants(apl_ID serial primary key, first_name varchar(10), last_name varchar(10));

create table Suppliers(supp_ID serial primary key, first_name varchar(10), last_name varchar(10));

create table Region(rid serial primary key, city varchar(25), region varchar(25));create table Suppliers(supp_ID serial primary key, first_name varchar(10), last_name varchar(10));

create table CreditCards(card_num integer primary key, apl_ID integer references Applicants(apl_ID), exp_date date, balance integer);

create table Accounts(acct_num integer primary key, supp_ID integer references Suppliers(supp_ID), balance integer);

create table ApplicantsAddress(aid serial primary key, apl_ID integer references Applicants(apl_ID), rid integer references Region(rid), street varchar(25), urb_conde varchar(25), num integer, city varchar(25), state varchar(25), zip integer,  gps_local varchar(25));

create table SuppliersAddress(aid serial primary key, supp_ID integer references Suppliers(supp_ID), rid integer references Region(rid), street varchar(25), urb_conde varchar(25), num integer, city varchar(25), state varchar(25), zip integer,  gps_local varchar(25));

create table Transactions(trans_ID serial primary key, card_num integer references CreditCards(card_num), acct_num integer references Accounts(acct_num), trans_date date, status varchar(10), amount integer);

create table Resources(res_ID serial primary key, category varchar(10), price integer , qty integer);

create table PowerGenerator( pg_ID serial primary key, res_ID integer references Resources(res_ID), watts integer);

create table Batteries(bat_ID serial primary key, res_ID integer references Resources(res_ID), kind varchar(10));

create table Clothing(cloth_ID serial primary key, res_ID integer references Resources(res_ID), size varchar(5), gender varchar(5));

create table Ice(ice_ID serial primary key, res_ID integer references Resources(res_ID), size integer);

create table Food(food_ID serial primary key, res_ID integer references Resources(res_ID), kind varchar(20));

create table Fuel(fuel_ID serial primary key, res_ID integer references Resources(res_ID), kind varchar(20), size integer);

create table Medication(med_ID serial primary key, res_ID integer references Resources(res_ID), dosis integer);

create table Water(water_ID serial primary key,res_ID integer references Resources(res_ID), size integer);

create table Request(apl_ID integer references Applicants(apl_ID), res_ID integer references Resources(res_ID), primary key(apl_ID, res_ID));

create table Supplies(res_ID integer references Resources(res_ID),supp_ID integer references Suppliers(supp_ID), primary key(supp_ID,res_ID));

create table Purchase(res_ID integer references Resources(res_ID), trans_ID integer references Transactions(trans_ID), pprice integer, primary key (res_ID,trans_ID));

create table Fulfill(trans_ID integer references Transactions(trans_ID), supp_ID integer references Suppliers(supp_ID), primary key(trans_ID, supp_ID));

create table Owns(trans_ID integer references Transactions(trans_ID), apl_ID integer references Applicants(apl_ID), primary key(trans_ID, apl_ID));

insert into ApplicantsAddress(apl_ID, rid, street, urb_conde, num, city, state, zip, gps_local) values ((select apl_ID from applicants where first_name='Jan' and last_name='Robles'),(select rid from region where region.city = 'Mayaguez'), 'calle bosq', 'Bosque 61', 304, 'Mayaguez', 'PR', 00680, 'Austin');

insert into ApplicantsAddress(apl_ID, rid, street, urb_conde, num, city, state, zip, gps_local) values ((select apl_ID from applicants where first_name='Jan' and last_name='Toro'),(select rid from region where region.city = 'Mayaguez'), 'calle flor', 'las Dalias', 301, 'Mayaguez', 'PR', 00680, 'Austin');

insert into ApplicantsAddress(apl_ID, rid, street, urb_conde, num, city, state, zip, gps_local) values ((select apl_ID from applicants where first_name='Eric' and last_name='Barbosa'),(select rid from region where region.city = 'Mayaguez'), 'calle flor', 'Escorial 2', 506, 'Mayaguez', 'PR', 00680, 'Austin');

insert into Applicants(first_name,last_name) values('Jan','Toro');

--Inserting Regions--

insert into Region(city, region) values ('San Juan', 'San Juan');
insert into Region(city, region) values ('Aguas Buenas' , 'San Juan');
insert into Region(city, region) values ('sur de Guaynabo' , 'San Juan');
insert into Region(city, region) values ('Bayamon' , 'Bayamon');
insert into Region(city, region) values ('Catano' , 'Bayamon');
insert into Region(city, region) values ('norte de Guaynabo' , 'Bayamon');
insert into Region(city, region) values ('Toa Alta' , 'Bayamon');
insert into Region(city, region) values ('Toa Baja' , 'Bayamon');
insert into Region(city, region) values('Arecibo','Arecibo');
insert into Region(city, region) values ('Barceloneta' , 'Arecibo');
insert into Region(city, region) values ('Camuy' , 'Arecibo');
insert into Region(city, region) values ('Ciales' , 'Arecibo');
insert into Region(city, region) values ('Dorado' , 'Arecibo');
insert into Region(city, region) values ('Florida' , 'Arecibo');
insert into Region(city, region) values ('Hatillo' , 'Arecibo');
insert into Region(city, region) values ('Manati' , 'Arecibo');
insert into Region(city, region) values ('Morovis' , 'Arecibo');
insert into Region(city, region) values ('Quebradilla' , 'Arecibo');
insert into Region(city, region) values ('Vega Alta' , 'Arecibo');
insert into Region(city, region) values ('Vega Baja' , 'Arecibo');
insert into Region(city, region) values ('Aguada','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Aguadilla','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Anasco','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Cabo Rojo','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Hormigueros','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Isabela','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Las Marias','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Mayaguez','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Moca','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Rincon','Mayaguez-Aguadilla');
insert into Region(city, region) values ('San German','Mayaguez-Aguadilla');
insert into Region(city, region) values ('San Sebastian','Mayaguez-Aguadilla');
insert into Region(city, region) values ('Adjuntas','Ponce');
insert into Region(city, region) values ('Guanica','Ponce');
insert into Region(city, region) values ('Guayanilla','Ponce');
insert into Region(city, region) values ('Jayuya','Ponce');
insert into Region(city, region) values ('oeste de Juana Diaz','Ponce');
insert into Region(city, region) values ('Lajas','Ponce');
insert into Region(city, region) values ('Lares','Ponce');
insert into Region(city, region) values ('Maricao','Ponce');
insert into Region(city, region) values ('Penuelas','Ponce');
insert into Region(city, region) values ('Ponce','Ponce');
insert into Region(city, region) values ('Sabana Grande','Ponce');
insert into Region(city, region) values ('Utuado','Ponce');
insert into Region(city, region) values ('Yauco','Ponce');
insert into Region(city, region) values('Aibonito','Guayama');
insert into Region(city, region) values('Arroyo','Guayama');
insert into Region(city, region) values('Barranquitas','Guayama');
insert into Region(city, region) values('Cayey','Guayama');
insert into Region(city, region) values('Cidra','Guayama');
insert into Region(city, region) values('Coamo','Guayama');
insert into Region(city, region) values('Comerio','Guayama');
insert into Region(city, region) values('Corozal','Guayama');
insert into Region(city, region) values('Guayama','Guayama');
insert into Region(city, region) values('este de Juana Diaz','Guayama');
insert into Region(city, region) values('Naranjito','Guayama');
insert into Region(city, region) values('Orocovis','Guayama');
insert into Region(city, region) values('Salinas','Guayama');
insert into Region(city, region) values('Santa Isabel','Guayama');
insert into Region(city, region) values('Villalba','Guayama');
insert into Region(city, region) values ('Caguas','Humacao');
insert into Region(city, region) values ('Gurabo','Humacao');
insert into Region(city, region) values ('Humacao','Humacao');
insert into Region(city, region) values ('Juncos','Humacao');
insert into Region(city, region) values ('Las Piedras','Humacao');
insert into Region(city, region) values ('Maunabo','Humacao');
insert into Region(city, region) values ('Naguabo','Humacao');
insert into Region(city, region) values ('Patillas','Humacao');
insert into Region(city, region) values ('San Lorenzo','Humacao');
insert into Region(city, region) values ('Yabucoa','Humacao');
insert into Region(city, region) values ('Canovanas','Carolina');
insert into Region(city, region) values ('Carolina','Carolina');
insert into Region(city, region) values ('Ceiba','Carolina');
insert into Region(city, region) values ('Culebra','Carolina');
insert into Region(city, region) values ('Fajardo','Carolina');
insert into Region(city, region) values ('Loiza','Carolina');
insert into Region(city, region) values ('Luquillo','Carolina');
insert into Region(city, region) values ('Rio Grande','Carolina');
insert into Region(city, region) values ('Trujillo Alto','Carolina');
insert into Region(city, region) values ('Vieques','Carolina');

﻿insert into Suppliers(first_name,last_name) values('Juan','Colon');

insert into SuppliersAddress(supp_id, rid, street, urb_conde, num, city, state, zip, gps_local) values((select supp_ID from suppliers where first_name='Juan' and last_name='Colon'),(select rid from region where region.city = 'San Juan'), 'ave ashford', 'ashford palace', 1, 'San Juan', 'PR', 00907, 'Guaynabo');

insert into Accounts(acct_num,supp_ID,balance) values ( 4163279,(select supp_ID from suppliers where first_name='Juan' and last_name='Colon'),1000);

insert into Resources(category,price,qty) values('pgenerator',4000,5);

insert into PowerGenerator(res_ID,watts) values ((select res_ID from resources where category = 'pgenerator'), 7250);

insert into Supplies(res_ID,supp_ID) values ((select res_ID from resources where category = 'pgenerator'),(select supp_ID from suppliers where first_name='Juan' and last_name='Colon'));

insert into Request(res_ID,apl_ID) values((select res_ID from resources where category = 'pgenerator'),(select apl_ID from applicants where first_name='Jan' and last_name='Robles'));

insert into transactions(card_num,acct_num,trans_date,status,amount) values((select card_num from creditcards natural inner join applicants where apl_ID = (select apl_ID from applicants where first_name='Jan' and last_name='Robles')),(select acct_num from accounts natural inner join suppliers where supp_ID = (select supp_ID from suppliers where first_name='Juan' and last_name='Colon')),'2018-01-01', 'completed', 4000);

--insert into owns(trans_ID,apl_ID) values
--insert into fulfill(trnas_ID,supp_ID) values

insert into purchase(res_ID,trans_ID,pprice) values((select res_ID from resources where category = 'pgenerator'), (select trans_ID from transactions where card_num =(select card_num from creditcards natural inner join applicants where apl_ID = (select apl_ID from applicants where first_name='Jan' and last_name='Robles')) and acct_num = (select acct_num from accounts natural inner join suppliers where supp_ID = (select supp_ID from suppliers where first_name='Juan' and last_name='Colon'))), 4000);

--Useful queries--

--select * from applicantsaddress;

--select first_name, region from applicants natural inner join applicantsaddress natural inner join region where region='Mayaguez-Aguadilla';

﻿--select apl_ID,first_name,last_name,street,urb_conde,num,city,state,zip,region,gps_local from applicants natural inner join applicantsaddress natural inner join region;

--insert into CreditCards(card_num,apl_ID,exp_date,balance) values (515224967, (select apl_ID from applicants where last_name='Barbosa'),to_date('2021-07','YYYY-MM') ,300);

--select apl_ID,first_name, last_name, card_num, exp_date, balance from creditcards natural inner join applicants where apl_ID=3;

--select first_name, region from applicants natural inner join applicantsaddress natural inner join region where region='Mayaguez-Aguadilla';

--select * from applicantsaddress natural inner join applicants;

--inserts jan toro
insert into Applicants(first_name,last_name) values('Jeremy','Cardona');

insert into ApplicantsAddress(apl_ID, rid, street, urb_conde, num, city, state, zip, gps_local) values ((select apl_ID from applicants where first_name='Jeremy' and last_name='Cardona'),(select rid from region where region.city = 'Mayaguez-Aguadilla'), 'calle flore', 'Bosque51', 420, 'Mayaguez', 'PR', 00680, 'New York');

insert into Suppliers(first_name,last_name) values('Wilfredo','Gomez');

insert into SuppliersAddress(supp_id, rid, street, urb_conde, num, city, state, zip, gps_local) values((select supp_ID from suppliers where first_name='Wilfredo' and last_name='Gomez'),(select rid from region where region.city = 'Humacao'), 'Calle Flamboyan', 'Los Sauces', 400, 'Humacao', 'PR', 00791, 'Humacao');

insert into Resources(category,price,qty) values('ice',2.50,10);

insert into Ice(res_ID,size) values ((select res_ID from resources where category = 'ice'), 5);

insert into Supplies(res_ID,supp_ID) values ((select res_ID from resources where category = 'ice'),(select supp_ID from suppliers where first_name='Wilfredo' and last_name='Gomez'));


insert into Applicants(first_name,last_name) values('Josue','Rodriguez');

insert into ApplicantsAddress(apl_ID, rid, street, urb_conde, num, city, state, zip, gps_local) values ((select apl_ID from applicants where first_name='Josue' and last_name='Rodriguez'),(select rid from region where region.city = 'Humacao'), 'calle zeni', 'Veredas', 600, 'Gurabo', 'PR', 00793, 'Las Piedras');

insert into Suppliers(first_name,last_name) values('Armani','Caban');

insert into SuppliersAddress(supp_id, rid, street, urb_conde, num, city, state, zip, gps_local) values((select supp_ID from suppliers where first_name='Armani' and last_name='Caban'),(select rid from region where region.city = 'Humacao'), 'Calle Ceiba', 'Candelero', 150, 'Las Piedras', 'PR', 00792, 'Juncos');

insert into Resources(category,price,qty) values('food',0.00,200);

insert into Food(res_ID,kind) values ((select res_ID from resources where category = 'food'), MRE);

insert into Supplies(res_ID,supp_ID) values ((select res_ID from resources where category = 'food'),(select supp_ID from suppliers where first_name='Armani' and last_name='Caban'));


insert into Applicants(first_name,last_name) values('Cristiano ','Ronaldo');

insert into ApplicantsAddress(apl_ID, rid, street, urb_conde, num, city, state, zip, gps_local) values ((select apl_ID from applicants where first_name='Cristiano' and last_name='Ronaldo'),(select rid from region where region.city = 'San Juan'), 'calle San Sebastian', 'La Tortuga', 10, 'San Juan', 'PR', 00630, 'Guaynabo');

insert into Suppliers(first_name,last_name) values('Paul','Pogba');

insert into SuppliersAddress(supp_id, rid, street, urb_conde, num, city, state, zip, gps_local) values((select supp_ID from suppliers where first_name='Paul' and last_name='Pogba'),(select rid from region where region.city = 'San Juan'), 'Calle Palo', 'Viejo', 13, 'Cataño', 'PR', 00560, 'Condado');

insert into Resources(category,price,qty) values('medication',0.00,50);

insert into Medication(res_ID,dosis) values ((select res_ID from resources where category = 'medication'), 12);

insert into Supplies(res_ID,supp_ID) values ((select res_ID from resources where category = 'medication'),(select supp_ID from suppliers where first_name='Paul' and last_name='Pogba'));


insert into Applicants(first_name,last_name) values('Kobe ','Bryant');

insert into ApplicantsAddress(apl_ID, rid, street, urb_conde, num, city, state, zip, gps_local) values ((select apl_ID from applicants where first_name='Kobe' and last_name='Bryant'),(select rid from region where region.city = 'Carolina'), 'calle Gigante', 'Los Robles', 2, 'Luquillo', 'PR', 00630, 'Fajardo');

insert into Suppliers(first_name,last_name) values('Paul','Pogba');

insert into SuppliersAddress(supp_id, rid, street, urb_conde, num, city, state, zip, gps_local) values((select supp_ID from suppliers where first_name='Michael' and last_name='Jordan'),(select rid from region where region.city = 'Carolina'), 'Calle Air', 'Tiro Libre', 23, 'Canovanas', 'PR', 00240, 'Ceiba');

insert into Resources(category,price,qty) values('water',0.00,50);

insert into Water(res_ID,size) values ((select res_ID from resources where category = 'water'), 16);

insert into Supplies(res_ID,supp_ID) values ((select res_ID from resources where category = 'water'),(select supp_ID from suppliers where first_name='Michael' and last_name='Jordan'));


insert into Applicants(first_name,last_name) values('Carlos','Beltran');

insert into ApplicantsAddress(apl_ID, rid, street, urb_conde, num, city, state, zip, gps_local) values ((select apl_ID from applicants where first_name='Carlos' and last_name='Beltran'),(select rid from region where region.city = 'Guayama'), 'calle brujos', 'Los brujos', 2, 'Guayama', 'PR', 00630, 'Patillas');

insert into Suppliers(first_name,last_name) values('Paul','Pogba');

insert into SuppliersAddress(supp_id, rid, street, urb_conde, num, city, state, zip, gps_local) values((select supp_ID from suppliers where first_name='Yadier' and last_name='Molina'),(select rid from region where region.city = 'Guayama'), 'Calle Home', 'Home Plate', 4, 'Salinas', 'PR', 00240, 'Ponce');

insert into Resources(category,price,qty) values('batteries',5.00,300);

insert into Batteries(res_ID,kind) values ((select res_ID from resources where category = 'batteries'), AA);

insert into Supplies(res_ID,supp_ID) values ((select res_ID from resources where category = 'batteries'),(select supp_ID from suppliers where first_name='Yadier' and last_name='Molina'));












































































