

def findLabel(database, budget, legal, produce, animals, governance):
    foundLabels = []
        
    for i, label in enumerate(database):
        for j, category in enumerate(label):
            x = category.split(", ")
            for word in x:
                if word in animals:
                    foundLabels.append(label[0])
                if word in produce:
                    foundLabels.append(label[0])
                if word in governance:
                    foundLabels.append(label[0])

    for label in database:
        for keywords in label:
            if budget == keywords:
                foundLabels.append(label[0])
            if legal == keywords:
                foundLabels.append(label[0])

    return foundLabels
