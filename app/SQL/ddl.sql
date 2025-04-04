CREATE DATABASE lawgateV2;

USE lawgateV2;

CREATE TABLE Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_email VARCHAR(255) NOT NULL,
    client_phone VARCHAR(255) NOT NULL,
    blob_storage_container_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE contracts (
    contract_id INT AUTO_INCREMENT PRIMARY KEY,
    contract_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    client_id INT FOREIGN KEY REFERENCES Clients(client_id),
    document_name VARCHAR(255), 
    document_link VARCHAR(255)
);


CREATE TABLE claims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY,
    claim_name VARCHAR(255),
    claim_description TEXT,
    s3_folder_link VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    contract_id INT,
    client_id INT,
    FOREIGN KEY (contract_id) REFERENCES contracts(contract_id),
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);


CREATE TABLE letters (
    letter_id INT AUTO_INCREMENT PRIMARY KEY,
    contract_id INT,
    client_id INT,
    letter_name VARCHAR(255),
    letter_description TEXT,
    s3_folder_link VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (contract_id) REFERENCES contracts(contract_id),
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);



CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

