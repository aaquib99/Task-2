import nltk
nltk.download('punkt')
from collections import Counter
try:
    print("Hello")
    f = open("inputFile.txt","r", encoding="utf8")
    str = f.read()
    text = nltk.word_tokenize(str)
    ans = nltk.pos_tag(text)
    # print(ans)
    counts = Counter(tag for word,tag in ans)
    # print("Counts",counts)
    res  = dict((word,count) for word,count in counts.items())
    for i in res :
        if(i == "JJ"):
            adjective = res[i]
        elif(i == "NN"):
            noun = res[i]
        elif(i == "VB"):
            verb = res[i]

    # print(noun,adjective,verb)
    result = f'Number of Nouns is given file is {noun} ,verb count is {verb} and adjective count is {adjective}'
    file = open("result.txt", "w")
    file.write(result)

    
except Exception as e:
    print(e)
    error = f'Error in file app.py {e}\n'
    file = open("logFile.txt", "a+")
    file.write(error)