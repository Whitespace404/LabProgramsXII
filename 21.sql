-- CREATE TABLE Books (
--     Book_ID VARCHAR(255) PRIMARY KEY,
--     Book_Name VARCHAR(255),
--     Author_Name VARCHAR(255),
--     Publishers VARCHAR(255),
--     Price INT,
--     Type VARCHAR(255),
--     Qty INT
-- );

-- INSERT INTO Books (Book_ID, Book_Name, Author_Name, Publishers, Price, Type, Qty)
-- VALUES
--     ('F0001', 'The Tears', 'William Hopkins', 'First Publ.', 750, 'Fiction', 10),
--     ('F0002', 'Thunderbolts', 'Anna Roberts', 'First Publ.', 700, 'Fiction', 5),
--     ('T0001', 'My First C++', 'Brian & Brooke', 'EPB', 250, 'Text', 10),
--     ('T0002', 'C++ Brainworks', 'A.W.Rossaine', 'TDH', 325, 'Text', 5),
--     ('C0001', 'Fast Cookery', 'Lata Kapoor', 'EPB', 350, 'Cookery', 8);

-- CREATE TABLE Issued (
--     Book_ID VARCHAR(255) PRIMARY KEY,
--     Quantity_Issued INT
-- );

-- INSERT INTO Issued (Book_ID, Quantity_Issued)
-- VALUES
--     ('F0001', 3),
--     ('T0001', 1),
--     ('C0001', 5);

-- a. To show Book name, Author name and Price of books of EPB publishers:

SELECT Book_Name, Author_Name, Price
FROM Books
WHERE Publishers = 'EPB';

-- b. To list the names of the books of Fiction Type:

SELECT Book_Name
FROM Books
WHERE Type = 'Fiction';

-- c. To display the names and price of the books in descending order of their price:

SELECT Book_Name, Price
FROM Books
ORDER BY Price DESC;

-- d. To increase the price of all books of first publisher by 50:

UPDATE Books
SET Price = Price + 50
WHERE Publishers = 'First Publ.';

-- e. To display the Book_Id, Book_Name and Quantity issued for all books which have been issued:

SELECT B.Book_ID, B.Book_Name, I.Quantity_Issued
FROM Books B
JOIN Issued I ON B.Book_ID = I.Book_ID;

-- f. To insert a new row in the table issued:

INSERT INTO Issued (Book_ID, Quantity_Issued)
VALUES ('F0002', 4);