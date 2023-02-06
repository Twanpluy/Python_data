

create table if not exists Linkedin_job(
    id int primary key,
    job_id varchar(255),
    job_title varchar(255),
    company_name varchar(255),
    location varchar(255),
    job_description varchar,
    job_link varchar(255),
    job_posted_date varchar(255),
    create_date date default current_timestamp
    
);
