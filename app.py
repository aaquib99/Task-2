import nltk
nltk.download('punkt')
from collections import Counter
from datetime import datetime
try:
    print("Hello")
    f = open("inputFile.txt","r", encoding="utf8")
    str = f.read()
    # print(str)
    #Data get stored in str variable from input file.
    text = nltk.word_tokenize(str)
    # print(text)
    #Created the list of all words to identify.
    ans = nltk.pos_tag(text)
    # print(ans)
    #Here with the help of pos tags eah word will get its tag
    counts = Counter(tag for word,tag in ans)
    #Here  we will count the which tag has how many values.
    # print("Counts",counts)
    res  = dict((word,count) for word,count in counts.items())
    #Just to remove tuple from outside of of counts and stored that in res
    # print(res)
    for i in res :
        if(i == "JJ"):
            adjective = res[i]
        elif(i == "NN"):
            noun = res[i]
        elif(i == "VB"):
            verb = res[i]
        elif(i == "NNP"):
            noun = noun + res[i]
    # print(noun,adjective,verb)
    #Counted all the requires details
    result = f'Number of Nouns is {noun} ,verb count is {verb} and adjective count is {adjective}'
    file = open("result.txt", "w")
    #result will be stored in result.txt
    file.write(result)

    
except Exception as error:
    #Here all type of exception will be handled and stored in error variable
    print(error)
    current_time = datetime.now()
    error = f'{current_time} : Error in file app.py {error}\n'
    file = open("logFile.txt", "a+")
    #here this error will be stored in logFile.txt
    file.write(error)