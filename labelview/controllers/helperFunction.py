import operator

def findAllLabels(database, budget, legal, produce, animals, governance):
    foundLabels = []
    matchedKeywords =	{}
    max_key =" "
    
    for i, label in enumerate(database):
        matchedKeywords[label[0]] = []
        for j, category in enumerate(label):
            x = category.split(", ")
            for word in x:
                if word in animals:
                    matchedKeywords[label[0]].append(word)
                    foundLabels.append(label[0])
                if word in produce:
                    matchedKeywords[label[0]].append(word)
                    foundLabels.append(label[0])
                if word in governance:
                    matchedKeywords[label[0]].append(word)
                    foundLabels.append(label[0])
                if word in budget:
                    matchedKeywords[label[0]].append(word)
                    foundLabels.append(label[0])
            if category == legal:
                matchedKeywords[label[0]].append(category)
                foundLabels.append(label[0])
        if label[1] == budget:
            if max_key is not findBestLabel(matchedKeywords):
                max_key = label[0]
    return foundLabels, max_key

def findBestLabel(matchedKeywords):
    length = {}

    for k in matchedKeywords:
        if isinstance(matchedKeywords[k], str):
            length[k] = 1
        else:
            length[k] = len(matchedKeywords[k])

    max_key = max(length.items(), key=operator.itemgetter(1))[0]
    return max_key  

