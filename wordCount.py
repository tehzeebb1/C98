def countWord():
    fileName=input("Enter the File name")
    numberOfWords=0
    #r refers to read
    file=open(fileName, 'r')

    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print(numberOfWords)
countWord()

