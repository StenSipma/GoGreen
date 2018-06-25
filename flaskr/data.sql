INSERT INTO Users
(username, password, name, email, street_name, street_number, city, postcode, ean_energy, ean_gas, score)
VALUES (
       'GoGreen-Team',
       'password',
       'GoGreen Group',
       'group@gogreen.com',
       'Street',
       10,
       'Groningen',
       '1234AB',
       'aaaaaaaaaaaaaaaaaa',
       'bbbbbbbbbbbbbbbbbb',
       98.1
);

INSERT INTO Users
(username, password, name, email, street_name, street_number, city, postcode, ean_energy, ean_gas, score)
VALUES (
       'flintstones',
       'password',
       'The Flintstones',
       'example@email.com',
       'Street',
       10,
       'Groningen',
       '1234AB',
       'aaaaaaaaaaaaaaaaaa',
       'bbbbbbbbbbbbbbbbbb',
       30.8
);

INSERT INTO Users
(username, password, name, email, street_name, street_number, city, postcode, ean_energy, ean_gas, score)
VALUES (
       'janssen',
       'password',
       'Family Janssen',
       'example@email.com',
       'Street',
       10,
       'Groningen',
       '1234AB',
       'aaaaaaaaaaaaaaaaaa',
       'bbbbbbbbbbbbbbbbbb',
       55.0
);

INSERT INTO Users
(username, password, name, email, street_name, street_number, city, postcode, ean_energy, ean_gas, score)
VALUES (
       'franklins',
       'password',
       'Rosalind Franklin',
       'example@email.com',
       'Street',
       10,
       'Groningen',
       '1234AB',
       'aaaaaaaaaaaaaaaaaa',
       'bbbbbbbbbbbbbbbbbb',
       74.4
);

INSERT INTO Users
(username, password, name, email, street_name, street_number, city, postcode, ean_energy, ean_gas, score)
VALUES (
       'turing',
       'password',
       'Alan Turing',
       'example@email.com',
       'Street',
       10,
       'Groningen',
       '1234AB',
       'aaaaaaaaaaaaaaaaaa',
       'bbbbbbbbbbbbbbbbbb',
       13.0
);

INSERT INTO Friends (user_id, friend_id) VALUES (1, 2);
INSERT INTO Friends (user_id, friend_id) VALUES (1, 3);
INSERT INTO Friends (user_id, friend_id) VALUES (1, 4);

INSERT INTO Groups (user_id, group_name) VALUES (
       1,
       'Friends'
);

INSERT INTO GroupMembers (group_id, user_id) VALUES (1, 2);
INSERT INTO GroupMembers (group_id, user_id) VALUES (1, 3);

INSERT INTO Groups (user_id, group_name) VALUES (
       1,
       'Family'
);

INSERT INTO GroupMembers (group_id, user_id) VALUES (2, 4);
