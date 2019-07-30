import textract
import re ,os
import ast
from nltk.tokenize import word_tokenize
import pandas as pd

def removeSmallWords(listofWords):
    newList =[]
    for eachWord in listofWords:
        if len(eachWord) > 3:
            newList.append(eachWord.lower())
    return newList

def readingStopwords():

    text =textract.process('stopwords.txt')

    # decoding in utf-8
    my_json1 = text.decode('utf8').replace("'", '"')

    #converting str to dict
    dict_stopwords=ast.literal_eval(my_json1)

    return dict_stopwords

def readFile(rootDirPath):

    # accessing all file from the given directory
    fileList = [item for item in os.listdir(rootDirPath) if os.path.isfile(os.path.join(rootDirPath, item))]

    for fileName in fileList:

        filePath =rootDirPath + '/' + fileName
        # Reading the doc file using textract library
        text = textract.process(filePath)

        temp = (str(text)).replace('\n', ' ').replace('\t', ' ')

        fileText = re.sub(r"[^a-zA-Z0-9]", " ", temp)


        tokenize_words = word_tokenize(fileText)

        # remove  small words
        tokenize_filtered_words =removeSmallWords(tokenize_words)

        textList = []
        dict_stopwords = readingStopwords()
        for eachWord in tokenize_filtered_words:
            if eachWord not in dict_stopwords:
                textList.append(eachWord)
        df = pd.DataFrame(textList, columns=["keywords"], index=None)

        df.insert(1, 'docId', fileName)
        print("====================",fileName)
        # df.to_csv("mainTable.csv", index=False)
        with open('index.csv', 'a') as f:
            df.to_csv(f, index=False)

        # return fileText
        # break





readFile('/home/vishal/Desktop/HUDOC/projectsDev/LUCENE/dataset')


