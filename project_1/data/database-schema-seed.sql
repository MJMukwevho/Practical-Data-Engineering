-- CREATE SCHEMAS
CREATE SCHEMA staging; 


CREATE TABLE staging."users"(
    id uuid not null,
    title text not null,
    gender text not null,
    name text not null,
    email text not null, 
    date_of_birth timestamptz,
    age numeric(3),
    phone text
)