CREATE TABLE IF NOT EXISTS yourname.users (
	id serial,
	name text,
	address text
)
;

CREATE TABLE IF NOT EXISTS yourname.admins (
	id serial,
	username text,
	pass text,
	name text
)
;