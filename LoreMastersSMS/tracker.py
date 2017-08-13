import csv

hamWords = ['ok', 'go', 'say', 'goes', 'I', 'lives', 'he', 'she', 'talk', 'talked', 'k']
commonWords = ['the', 'and', 'this', 'is', 'you', 'a']
spamWords = ['entry', 'comp', 'text', 'apply', 'winner', 'rewards', 'claim', 'call', 'update', 'chance', 'chances', 'win', 'won', 'penis', 'viagra']
messageNum = 0

f = open('Documents.csv', 'r')
reader = csv.reader(f)
file = open('hamSpam.csv', 'w', newline='')
fieldnames = ['SMS_id', 'label']
writer = csv.writer(file, dialect = 'excel')
writer.writerow(fieldnames)

for row in reader:
    n=0
    spamCount = 0
    hamCount = 0
    number = row[0]
    message = row[1]
    word1 = "Spam"
    word2 = "Ham"
    #message = message.split()

    if number != "SMS_id":
        messageNum = messageNum + 1

    if message != "SMS":
        message = message.split()

        for word in message:
            word = word.lower()
            cTest = 0
            hTest = 0
            sTest = 0
            for spams in spamWords:
                if word == spams:
                    #print("This is spam")
                    spamCount = spamCount + 1
                    sTest = 1
            for ham in hamWords:
                if word == ham:
                    #print("This is ham")
                    hamCount = hamCount + 1
                    hTest = 1
            for common in commonWords:
                if word == common:
                    cTest = 1

            if cTest == 0:
                if hTest == 0:
                    hamWords.append(word)
                    #print("appended")

                if sTest == 0:
                    spamWords.append(word)
                    #print("appended")

        finalSpam = [messageNum, 0]
        finalHam = [messageNum, 1]

        if spamCount > hamCount:
            #print("Value of Spam: " + str(spamCount))
            writer.writerow(finalSpam)

        if hamCount > spamCount:
            #print ("Value of Ham: " + str(hamCount))
            writer.writerow(finalHam)

        if hamCount == spamCount:
            #print("Value of Spam: " + str(spamCount))
            #print ("Value of Ham: " + str(hamCount))
            writer.writerow(finalHam)

    #for word in message:
        #words[n] = hamWords.append(words[n])
        #n = n+1
        #print(word)
    #print (number)
    #print (message)
    #print ("-----------------")