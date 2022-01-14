import mysql.connector
import sys, getopt

kBatchSize = 10
kDataDirectory='../data/'
kEncoding='utf-8'


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="education-today-miimran2"
)

def read_file(filename, sql_statement, nullable_fields=[], ignore_fields=[]):
    with open(kDataDirectory+filename, encoding=kEncoding) as f:
        cursor = db.cursor()
        i = 0
        val = []
        ignore_fields = set(ignore_fields)
        for line in f:
            cols = line.split('\t')
            
            if (len(cols) != 25):
                print(i, len(cols))
                for c in cols:
                    print('[',c,']')
                print('----------------------------------------------------')
            
            for idx in nullable_fields:
                if cols[idx] == '':
                    cols[idx] = None

            tmp = cols
            cols = []
            for idx in range(len(tmp)):
                if idx not in ignore_fields:
                    cols.append(tmp[idx])

            val.append(cols)
            i += 1

            if i % kBatchSize == 0:
                cursor.executemany(sql_statement,val)
                db.commit()
                i = 0
                val = []


def read_affiliations():
    print('reading affilitations')
    sql_statement = "INSERT INTO affiliations (AffiliationId, AffiliationRank, NormalizedName, DisplayName, GridId, OfficialPage, WikiPage, PaperCount, PaperFamilyCount, CitationCount, Iso3166Code, Latitude, Longitude, CreatedDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    read_file('Affiliations.txt', sql_statement, nullable_fields=[11, 12])

def read_authors():
    print('reading authors')
    sql_statement = "INSERT INTO authors (AuthorId, AuthorRank, NormalizedName, DisplayName, LastKnownAffiliationId, PaperCount, PaperFamilyCount, CitationCount, CreatedDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    read_file('Authors.txt', sql_statement, nullable_fields=[4])

def read_paperauthoraffiliations():
    # sql_statement = "INSERT INTO "
    pass

def read_paperreferences():
    pass

def read_papers():
    print('reading papers')
    sql_statement = """INSERT INTO papers (
        PaperId,
        PaperRank,
        Doi,
        DocType,
        PaperTitle,
        OriginalTitle,
        BookTitle,
        PaperYear,
        PaperDate,
        Publisher,
        Volume,
        Issue,
        CreatedDate
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"""
    read_file('Papers.txt', sql_statement, nullable_fields=[7,8], ignore_fields=[9, 11, 12, 13, 16,17,18,19,20,21,22,23])
    pass

def main():
    options = ["authors", "affiliations", "paperauthoraffiliations", "paperreferences", "papers"]
    table_reader = [read_authors, read_affiliations, read_paperauthoraffiliations, read_paperreferences, read_papers]
    should_read = [False for i in range(len(options))]
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["authors", "affiliations", "paperauthoraffiliations", "paperreferences", "papers"])
    except getopt.GetoptError:
      print('read_data.py [--authors] [--affiliations] [--paperauthoraffiliations] [--paperreferences] [--papers]')
      sys.exit(2)

    for (opt, arg) in opts:
        word = opt[2:]
        for i in range(len(options)):
            if word == options[i]:
                should_read[i] = True
                break

    for i in range(len(options)):
        if should_read[i]:
            table_reader[i]()

if __name__ == "__main__":
    main()