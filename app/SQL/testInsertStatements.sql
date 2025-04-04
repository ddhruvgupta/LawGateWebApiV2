insert into Clients (client_name, client_email, client_phone) values ('Sahu Construction', 'example@sahu.com', '123456789');

insert into contracts (contract_name, client_id) values ('Contract 1', 1);

insert into claims (claim_name, claim_description, s3_folder_link, contract_id, client_id) values ('Claim 1', 'This is a claim', 'https://s3.amazonaws.com/claim1', 1, 1);

insert into letters (contract_id, client_id, letter_name, letter_description, s3_folder_link) values (1, 1, 'Letter 1', 'This is a letter', 'https://s3.amazonaws.com/letter1');