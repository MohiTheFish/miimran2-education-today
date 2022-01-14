CREATE TABLE Affiliations (
    AffiliationId bigint PRIMARY KEY,
    AffiliationRank int,
    NormalizedName varchar(256),
    DisplayName varchar(256),
    WikiPage varchar(256),
    CreatedDate datetime
);

CREATE TABLE Authors (
    AuthorId bigint PRIMARY KEY,
    AuthorRank int,
    NormalizedName varchar(256),
    DisplayName varchar(256),
    LastKnownAffiliationId bigint DEFAULT NULL
);

CREATE TABLE Papers (
    PaperId bigint PRIMARY KEY,
    DocType varchar(32),
    OriginalTitle varchar(1024),
    PaperYear int DEFAULT NULL,
    PaperDate datetime DEFAULT NULL,
    Publisher varchar(1024),
    OriginalVenue varchar(1024)
);

CREATE TABLE PaperAuthorAffiliations (
    PaperId bigint,
    AuthorId bigint,
    AffiliationId bigint DEFAULT NULL,

    id bigint PRIMARY KEY NOT NULL AUTO_INCREMENT
);

CREATE TABLE PaperReferences (
    PaperId bigint,
    PaperReferenceId bigint,

    PRIMARY KEY (PaperId, PaperReferenceId)
);