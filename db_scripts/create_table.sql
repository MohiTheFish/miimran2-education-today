CREATE TABLE Affiliations (
    AffiliationId bigint PRIMARY KEY,
    AffiliationRank int,
    NormalizedName varchar(256),
    DisplayName varchar(256),
    GridId varchar(256),
    OfficialPage varchar(256),
    WikiPage varchar(256),
    PaperCount bigint,
    PaperFamilyCount bigint,
    CitationCount bigint,
    Iso3166Code varchar(2),
    Latitude float,
    Longitude float,
    CreatedDate datetime
);

CREATE TABLE Authors (
    AuthorId bigint PRIMARY KEY,
    AuthorRank int,
    NormalizedName varchar(256),
    DisplayName varchar(256),
    LastKnownAffiliationId bigint,
    PaperCount bigint, 
    PaperFamilyCount bigint,
    CitationCount bigint,
    CreatedDate datetime
);

CREATE TABLE Papers (
    PaperId bigint PRIMARY KEY,
    PaperRank int,
    Doi varchar(256),
    DocType varchar(32),
    PaperTitle varchar(256),
    OriginalTitle varchar(256),
    BookTitle varchar(256),
    PaperYear int,
    PaperDate datetime,
    OnlineDate datetime,
    Publisher varchar(256),
    Volume varchar(256),
    Issue varchar(256),
    FirstPage text,
    LastPage text,
    ReferenceCount bigint,
    CitationCount bigint,
    EstimatedCitation bigint,
    OriginalVenue varchar(256),
    FamilyId bigint,
    FamilyRank int,
    DocSubTypes varchar(32),
    CreatedDate datetime
);

CREATE TABLE PaperAuthorAffiliations (
    PaperId bigint,
    AuthorId bigint,
    AffiliationId bigint,
    AuthorSequenceNumber int,
    OriginalAuthor varchar(256),
    OriginalAffiliation varchar(256),

    id bigint PRIMARY KEY NOT NULL AUTO_INCREMENT,
    FOREIGN KEY (PaperId) REFERENCES Papers(PaperId),
    FOREIGN KEY (AuthorId) REFERENCES Authors(AuthorId),
    FOREIGN KEY (AffiliationId) REFERENCES Affiliations(AffiliationId)
);

CREATE TABLE PaperReferences (
    PaperId bigint,
    PaperReferenceId bigint,

    PRIMARY KEY (PaperId, PaperReferenceId),
    FOREIGN KEY (PaperId) REFERENCES Papers(PaperId),
    FOREIGN KEY (PaperReferenceId) REFERENCES Papers(PaperId) 
);