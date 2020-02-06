readBooks = open("booklist.txt", "r")
bookList = []
for book in readBooks:
    tempList = book.strip().split(",")
    bookList.append((tempList[0],tempList[1]))

readRatings = open("ratings.txt","r")
count = 1
name = "name"
ratingsList = []
for line in readRatings:
    if count % 2 != 0:
        name = line.strip().lower()
    else:
        numList = line.split()
        numberList = []
        for l in numList:
            l = int(l)
            numberList.append(l)
        newDic = {"name": name, "ratings": numberList}
        ratingsList.append(newDic)
    count += 1

for name in ratingsList:
    friendList = []
    for other in ratingsList:
        value = 0
        count = 0
        if other["name"] != name["name"]:
            for number in name["ratings"]:
                value += number * other["ratings"][count]
                count += 1
        friendList.append({"friend": other["name"], "score": value})
    large = 0
    largeName = "name"
    largest = 0
    largestName = "name"
    for friend in friendList:
        if friend["score"] > largest:
            largest = friend["score"]
            largestName = friend["friend"]
        elif friend["score"] > large:
            large = friend["score"]
            largeName = friend["friend"]        
    name["friends"] = [largestName,largeName]

def friends(name):
    for x in ratingsList:
        if name == x["name"]:
            print(x["friends"])

for user in ratingsList:
    goodBooks = []
    unreadBooks = []
    count = 0
    for num in user["ratings"]:
        if num >= 3:
            goodBooks.append(bookList[count])
        if num == 0:
            unreadBooks.append(bookList[count])
        count += 1    
    user["goodbooks"] = goodBooks
    user["unreadbooks"] = unreadBooks
            
def recommend(name):
    tempList = []
    theirRecommended = []
    for user in ratingsList:
        if user["name"] == name:
            for x in ratingsList:
                if x["name"] == user["friends"][0]:
                    tempList.extend(x["goodbooks"])
            for y in ratingsList:
                if y["name"] == user["friends"][1]:
                    tempList.extend(y["goodbooks"])
        if user["name"] == name:
            for book in tempList:
                if book in user["unreadbooks"]:
                    theirRecommended.append(book)
    
    theirRecommended = list(dict.fromkeys(theirRecommended))
    print(sorted(theirRecommended, key=lambda x: x[0].split(" ")[-1]))
            
    

def main():
    #friends("ben")
    recommend("albus dumbledore")
 #with open('recommendations.txt', 'w') as rec_file:
 #print(report(), file=rec_file)
 
 
if __name__ == '__main__':
 main()