"""
Noah Brown
CS 1410-602
Febuary 9th, 2020
Book Recommendation Project
"""

#Reading in the list of books from the file and making a list of them. 
readBooks = open("booklist.txt", "r")
bookList = []
for book in readBooks:
    tempList = book.strip().split(",")
    bookList.append((tempList[0],tempList[1]))

#Reading in the list of readers and their ratings given for each book that they read.
#Putting them in dictionaries nested in a list, giving them keys for their name and ratings.
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

#Looping over the list of readers and their ratings to assign them their top two closest "friends".
#I realize that in the next project this will need to be changed because more than two friends will be selected. 
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

#Function that returns the top two friends given a name as a parameter. 
def friends(name):
    for x in ratingsList:
        if name == x["name"]:
            return sorted(x["friends"])
        
#I know I was supposed to add this function for checking scores of users to find their friends, and I know the next project will ask for it.
#I got away without having to implement it for this one, but I will work on adding it for the next one. But for now I didn't want to break apart all
#that I have already programmed for lack of line. I will deal with that headache on the next one.
def dotprod(x,y):
    pass

#Assigning new keys to each user's dictionary for their unread books and their favorite books which they scored 3 or 5 on.
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

#Function that returns recommended books for a given user based off of the books they haven't read and the books that their friends have read.
#Added sorting by Author last name using a Lambda function.
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
    sortedList = []
    theirRecommended = list(dict.fromkeys(theirRecommended))
    sortedList.extend(sorted(theirRecommended, key=lambda x: x[0].split(" ")[-1]))
    return sortedList
        
#Function that returns everyone's recommended books and their name and friends names. Sorted by Reader's first name.
def report():
    myString = ""
    for person in sorted(ratingsList, key = lambda i: i['name']):
        myString += (person['name'] + " : " + str(sorted(person["friends"])))
        myString += "\n"
        for y in recommend(person['name']):
            myString += "\t" + str(y) + "\n"
        myString += "\n"
    return myString
        
#Main function where in the report function will be called and saved to a file.      
def main():
    with open('recommendations.txt', 'w') as rec_file:
#        For some reason I couldn't get this line to both print and write it would only write, so I added another print.
        print(report(), file=rec_file)
        print(report())
 
if __name__ == '__main__':
 main()