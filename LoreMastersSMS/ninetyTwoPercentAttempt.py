import csv
import string
import re 

hamWords = ['going', 'well', 'skype', 'sir', 'school', 'hope', 'will', 'feel', 'bad', 'drugs', 'bless', 'brain', 'job', 'studying', 'we', 'better', 'happy', 'eh', 'outta', 'good', 'night' 'call', 'sorry','youre',
 'there', 'him', 'her', 'ha', 'haha','hopefully', 'stubborn', 'weak', 'telling', 'ill','ur','ok', 'go', 'say', 'goes', 'I', 'lives', 'he', 'she', 'talk', 'talked', 'k', 'my', 'brother', 'sister', 'me', 'myself',
  'im', 'ive', 'thanks', 'leaving', 'wait', 'the', 'and', 'this', 'is', 'a', 'here', 'to', 'of', 'all', 'when', 'tomorrow', 'compliments', 'happiness', 'safe', 'common', 'what', 'ur', 'dear', 'angry','busy', 
  'pub', 'step', 'outta', 'slow', 'men', 'sweet', 'wishing', 'stuff', 'excellent', 'father', 'gorgeous', 'film', 'wants', 'regards', 'fine', 'nap', 'driving', 'buying', 'also', 'talk', 'loneliness', 'bus',
  'missed', 'way', 'understanding', 'differences', 'husband', 'liked', 'awesome', 'bank', 'family', 'spoiled', 'dreams', 'kfc', 'meals', 'want', 'skye', 'work', 'animation', 'lover', 'slippers', 'late', 'situation',
   'finished', 'class', 'network', 'performed', 'signing', 'tired', 'mate', 'prof', 'papers', 'daddy', 'deposit', 'great', 'sleeping', 'fffff', 'connect', 'goal', 'years', 'lol', 'perfume', 'mood', 'manage', 'oil',
   'couple', 'room', 'unnecessarily', 'teach', 'staying', 'resizing', 'oh', 'office', 'ring', 'money', 'outside', 'parents', 'christmas', 'tea', 'meeting', 'shopping', 'cool', 'waiting', 'project', 'next', 'print',
   'budget', 'uncle', 'college']
  #buying, also

commonWords = ['the', 'and', 'this', 'is', 'a', 'here', 'to', 'of', 'all', 'when']

spamWords = ['private', '...', '$', '£', 'winner', 'reply', 'prize', 'valid', 'code','dating', 'service', 'join', 'laid', 'congrats', 'correct','msg','entry', 'comp', 'text', 'sexy', 'passion', 'ref', 'tone',
 'apply', 'winner', 'rewards', 'claim', 'update', 'chance', 'chances', 'win', 'won', 'penis', 'viagra', 'urgent', 'free', 'membership', 'competition','awarded', 'chance', 'www', 'x', 'vodafone', 'beware',
 'tones', 'subscription', 'credit', 'shagged', 'xxx', 'cum', 'com', 'babe', '2nite', 'rental', 'price', 'erotic', 'ecstacy', 'darlin', 'call', 'co', 'uk', 'mailbox', 'alert', 'matches', 'yours', 'etc', 'supply',
  'weekly', 'quiz', 'unsub', 'auction', 'congratulations', 'minute', 'attempt']

messageNum = 1

f = open('Documents.csv', 'r')
reader = csv.reader(f)
file = open('hamSpam.csv', 'w', newline='')
fieldnames = ['SMS_id', 'label']
writer = csv.writer(file, dialect = 'excel')
writer.writerow(fieldnames)
totalHam = 0
totalSpam = 0
#totalSpamWords = 26
#totalHamWords = 20
totalHamWords = 0
totalSpamWords = 0

for row in reader:
    n=0
    spamCount = 0
    hamCount = 0
    number = row[0]
    message = row[1]
    test = row[1]
    word1 = "Spam"
    word2 = "Ham"
    #message = message.split()
    finalSpam = [messageNum, 0]
    finalHam = [messageNum, 1]

    if number != "SMS_id":
        messageNum = messageNum + 1

    if message != "SMS":
        message = re.sub(r'[^\w\s]','',message)
        #print (message)
        #message = message.translate(string.punctuation)
        #message = message.translate(".")
        message = message.split()

        for word in message:
            word = word.lower()
            #word = word.translate(".")
            #word = word.translate(string.punctuation)
            #word = word.translate(string.punctuation)
            #cTest = 0
            #hTest = 0
            #sTest = 0
            for spams in spamWords:
                if word == spams:
                    #print("This is spam")
                    spamCount = spamCount + 1
            for ham in hamWords:
                if word == ham:
                    #print("This is ham")
                    hamCount = hamCount + 1


        if spamCount > hamCount:
            for word in message:
                word = word.lower()
                if totalSpamWords < 110: #40, 45 might be more accurate
                    sTest = 0
                    cTest = 0
                    sTest = 0
                    for common in commonWords:
                        if word == common:
                            cTest = 1
                    for spams in spamWords:
                        if word == spams:
                            sTest = 1
                    for ham in hamWords:
                        if word != ham:
                            hTest = 1
                    if sTest == 0:
                        #print ("WORD ADDED: " + word)
                        spamWords.append(word)
                        totalSpamWords = totalSpamWords + 1

            
            #print("Value of Spam: " + str(spamCount))
            totalSpam = totalSpam + 1
            writer.writerow(finalSpam)
            print("FOUND SPAM!" + str(totalSpam) + " --- " + str(spamCount) + " vs " + str(hamCount) + " Number: " + str(totalSpam) + "/" + str(totalHam))
            print(test.encode('utf-8'))
            print("-------------------------------------------------------------------------------")
            #print(row[1])

        if hamCount > spamCount:
            for word in message:
                word = word.lower()
                if totalHamWords < 100:
                    hTest = 0
                    cTest = 0
                    sTest = 0
                    
                    for ham in hamWords:
                        if word == ham:
                            hTest = 1

                    for common in commonWords:
                        if word == common:
                            cTest = 1

                    for spams in spamWords:
                        if word == spams:
                            sTest = 1
                    
                    if hTest == 0:
                        #print("word added: " + word)
                        hamWords.append(word)
                        totalHamWords = totalHamWords + 1

            #print("FOUND HAM! " + str(totalHam))

            #print ("Value of Ham: " + str(hamCount))
            #print("FOUND HAM! --- " + str(spamCount) + " vs " + str(hamCount))
            #print(row[1])
            writer.writerow(finalHam)
            totalHam = totalHam + 1

        if hamCount == spamCount:
            for word in message:
                word = word.lower()
                if totalHamWords < 100:
                    hTest = 0
                    cTest = 0
                    sTest = 0
                    for common in commonWords:
                        if word == common:
                            cTest = 1
                    for ham in hamWords:
                        if word == ham:
                            hTest = 1
                    for spams in spamWords:
                        if word == spams:
                            sTest = 1
                    if hTest == 0:
                        hamWords.append(word)
                        totalHamWords = totalHamWords + 1

            #print("FOUND HAM! " + str(totalHam))
            #print("Value of Spam: " + str(spamCount))
            #print ("Value of Ham: " + str(hamCount))
            #print("FOUND EQUAL HAM!" + str(totalHam) + " --- " + str(spamCount) + " vs " + str(hamCount))
            #print(row[1])
            writer.writerow(finalHam)
            totalHam = totalHam + 1
    spamCount = 0
    hamCount = 0

print("Total Ham: " + str(totalHam))
print("Total Spam: " + str(totalSpam))

    #for word in message:
        #words[n] = hamWords.append(words[n])
        #n = n+1
        #print(word)
    #print (number)
    #print (message)
    #print ("-----------------")