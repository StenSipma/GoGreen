DROP TABLE IF EXISTS GroupMembers;
DROP TABLE IF EXISTS Groups;
DROP TABLE IF EXISTS Friends;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
       id		INTEGER	     PRIMARY KEY AUTOINCREMENT,
       username    	VARCHAR(255) NOT NULL UNIQUE,
       password    	VARCHAR(255) NOT NULL,
       name 	   	VARCHAR(255) NOT NULL,
       email 	   	VARCHAR(255) NOT NULL,
       street_name 	VARCHAR(255) NOT NULL,
       street_number 	INTEGER      NOT NULL,
       city 		VARCHAR(255) NOT NULL,
       postcode 	CHAR(6)      NOT NULL,
       ean_energy 	CHAR(18)     NOT NULL,
       ean_gas 		CHAR(18)     NOT NULL,
       score 		REAL 	     NOT NULL DEFAULT 0 CHECK (score BETWEEN 0 AND 100)
);


CREATE TABLE Friends (
       user_id	     INTEGER NOT NULL,
       friend_id     INTEGER NOT NULL,
       PRIMARY KEY (user_id, friend_id),
       FOREIGN KEY (user_id) REFERENCES Users(id),
       FOREIGN KEY (friend_id) REFERENCES Users(id)
);


CREATE TABLE Groups (
       id    	    INTEGER		PRIMARY KEY AUTOINCREMENT,
       user_id      INTEGER 		NOT NULL,
       group_name   VARCHAR(255) 	NOT NULL,
       UNIQUE (user_id, group_name),
       FOREIGN KEY (user_id) REFERENCES Users(id)
);


CREATE TABLE GroupMembers (
       group_id		  INTEGER NOT NULL,
       user_id		  INTEGER NOT NULL,
       PRIMARY KEY (group_id, user_id),
       FOREIGN KEY (group_id) REFERENCES Groups(id),
       FOREIGN KEY (user_id) REFERENCES Users(id)
);
