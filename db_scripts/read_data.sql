LOAD DATA INFILE 'C:/Users/mumui/Desktop/miimran2-education-today-init/data/Affiliations.txt' INTO TABLE Affiliations
(
    AffiliationId,
    AffiliationRank,
    NormalizedName,
    DisplayName,
    @iGridId,
    @iOfficialPage,
    WikiPage,
    @iPaperCount,
    @iPaperFamilyCount,
    @iCitationCount,
    @iIso3166Code,
    @iLatitude,
    @iLongitude,
    CreatedDate
);

LOAD DATA INFILE 'C:/Users/mumui/Desktop/miimran2-education-today-init/data/Authors.txt' INTO TABLE Authors
(
    AuthorId,
    AuthorRank,
    NormalizedName,
    DisplayName,
    @vLastKnownAffiliationId,
    @iPaperCount,
    @iPaperFamilyCount,
    @iCitationCount,
    @iCreatedDate
)
SET LastKnownAffiliationId = NULLIF(@vLastKnownAffiliationId, '');

LOAD DATA INFILE 'C:/Users/mumui/Desktop/miimran2-education-today-init/data/Papers.csv' IGNORE INTO TABLE Papers
CHARACTER SET UTF8
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
(
    PaperId,
    DocType,
    OriginalTitle,
    @vPaperYear,
    @vPaperDate,
    Publisher,
    OriginalVenue
)
SET
PaperYear = NULLIF(@vPaperYear, ''),
PaperDate = NULLIF(@vPaperDate, '')
;

LOAD DATA INFILE 'C:/Users/mumui/Desktop/miimran2-education-today-init/data/PaperAuthorAffiliations.txt' IGNORE INTO TABLE PaperAuthorAffiliations
(
    PaperId,
    AuthorId,
    @vAffiliationId,
    @iAuthorSequenceNumber,
    @iOriginalAuthor,
    @iOriginalAffiliation
)
SET AffiliationId = NULLIF(@vAffiliationId, '');

LOAD DATA INFILE 'C:/Users/mumui/Desktop/miimran2-education-today-init/data/PaperReferences.txt' INTO TABLE PaperReferences
(
    PaperId,
    PaperReferenceId
);

