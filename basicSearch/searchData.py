import pandas as pd
from collections import Counter

def countNumberofOccurance(listofDocId):

    dictCount = {}

    for eachId in listofDocId:
        if eachId not in dictCount:
            dictCount[eachId] =1
        else:
            dictCount[eachId] +=1

    return dictCount

def accessTable(tableName,searchKeywords):
    df =pd.read_csv(tableName)
    lower_case_searchKeywords = [eachKeyword.lower() for eachKeyword in searchKeywords]
    options =lower_case_searchKeywords
    rslt_df =df[df['keywords'].isin(options)]

    docId= rslt_df['docId'].tolist()

    docIdCount =countNumberofOccurance(docId)

    orderedDoc = Counter(docIdCount)

    orderedDoc.most_common()

    return dict(orderedDoc)





# search query
result= accessTable("index.csv",['spark','python'])

print(result)