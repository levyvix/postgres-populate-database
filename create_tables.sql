create schema if not exists kaggle;


create table kaggle.machines (
	machineID smallint primary key,
	model varchar(10) not null,
	age int not null
);

create table kaggle.errors (
	error_id serial primary key,
	datetime timestamp not null,
	machineID int references kaggle.machines(machineID) not null,
	errorID varchar not null
);

create table kaggle.failures(
	failure_id serial primary key,
	datetime timestamp not null,
	machineID int references kaggle.machines(machineID) not null,
	failure varchar(10) not null
);

create table kaggle.maint(
	maint_id serial primary key,
	datetime timestamp not null,
	machineID int references kaggle.machines(machineID) not null,
	component varchar(10) not null
);

create table kaggle.telemetry(
	datetime timestamp,
	machineID int references kaggle.machines(machineID),
	volt float not null,
	rotate float not null,
	pressure float not null,
	vibration float not null,
	primary key (machineID, datetime)
);