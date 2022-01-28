

DROP TABLE dbo.[User]

CREATE TABLE dbo.[User] (
userID int NOT NULL IDENTITY ,
userName varchar(250),
userPassword varchar (250),
userEmail varchar (30),
userPhone varchar (20),
userPicturePath varchar (250),
userStatus bit ,
userType varchar (10),
create_At date,
update_At date,

PRIMARY KEY CLUSTERED 
   (
  userID 
   )
) ON [PRIMARY];

DROP TABLE dbo.Book

CREATE TABLE dbo.Book (
bookID int NOT NULL IDENTITY , --PK
bookName varchar(250),
bookVersion varchar (250),
bookNumberPage int,
bookAbstract varchar (500),
bookPicturePath varchar (250),
bookYearPub varchar (4)  ,
bookNumberViews int ,
bookLanguage varchar (30),
bookPath varchar (200),
authorID int , --FK
categoryID int , --FK
userID int , --FK
create_At date,
update_At date,

PRIMARY KEY CLUSTERED 
   (
  bookID 
   )
) ON [PRIMARY];


DROP TABLE dbo.Author 

CREATE TABLE dbo.Author (
authorID int NOT NULL IDENTITY,
authorNAme varchar (250),
authorEmail varchar (250),
authorPhone varchar (20),
authorCountry varchar (20),
authorAddress varchar (250),
authorWebsiteUrl varchar (250),
authorTwitterUrl varchar (250),
userID int , --FK
create_At date,
update_At date,

PRIMARY KEY CLUSTERED 
   (
  authorID 
   )
) ON [PRIMARY];

DROP TABLE dbo.category 

CREATE TABLE dbo.category (
categoryID int NOT NULL IDENTITY,
categoryName varchar(200),
userID int , --FK
create_At date,
update_At date,


PRIMARY KEY CLUSTERED 
   (
  categoryID 
   )
) ON [PRIMARY];

