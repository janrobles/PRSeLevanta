create table Applicants(apl_ID serial primary key, first_name varchar(10), last_name varchar(10));

create table Region(rid serial primary key, city varchar(25), region varchar(25));create table Suppliers(supp_ID serial primary key, first_name varchar(10), last_name varchar(10));

create table CreditCards(card_num integer primary key, apl_ID integer references Applicants(apl_ID), exp_date date, balance integer);

create table Accounts(acct_num integer primary key, supp_ID integer references Suppliers(supp_ID), balance integer);

create table ApplicantsAddress(aid serial primary key, apl_ID integer references Applicants(apl_ID), rid integer references Region(rid), street varchar(25), urb_conde varchar(25), num integer, city varchar(25), state varchar(25), zip integer,  gps_local varchar(25));

create table SuppliersAddress(aid serial primary key, supp_ID integer references Suppliers(supp_ID), rid integer references Region(rid), street varchar(25), urb_conde varchar(25), num integer, city varchar(25), state varchar(25), zip integer,  gps_local varchar(25));

﻿create table Transactions(trans_ID serial primary key, card_num integer references CreditCards(card_num), acct_num integer references Accounts(acct_num), trans_date date, status varchar(10), amount integer);

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

--Useful queries--

--select * from applicantsaddress;

--select first_name, region from applicants natural inner join applicantsaddress natural inner join region where region='Mayaguez-Aguadilla';

﻿--select apl_ID,first_name,last_name,street,urb_conde,num,city,state,zip,region,gps_local from applicants natural inner join applicantsaddress natural inner join region;

--insert into CreditCards(card_num,apl_ID,exp_date,balance) values (515224967, (select apl_ID from applicants where last_name='Barbosa'),to_date('2021-07','YYYY-MM') ,300);

select apl_ID,first_name, last_name, card_num, exp_date, balance from creditcards natural inner join applicants where apl_ID=3;

--select first_name, region from applicants natural inner join applicantsaddress natural inner join region where region='Mayaguez-Aguadilla';

--select * from applicantsaddress natural inner join applicants;












































































