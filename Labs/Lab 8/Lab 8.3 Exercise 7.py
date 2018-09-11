def create_books_2d_list(file_name):
    file = open(file_name).read().splitlines()
    lis=[]
    dates=[]

    for book in file:
        book=book.split("\t")
        name=book[0].strip()
        author=book[1].strip()
        publisher=book[2].strip()
        date=book[3].strip()

        date=date.split("/")
        day=date[0]
        month=date[1]
        year=date[2]
        findate=year+"-"+month+"-"+day
        date=findate
        genre=book[4].strip()
        
        lis.append([date, name, author, publisher, genre])
    return lis

def search_by_year(books,year1,year2):
    li=[]
    for j in range(year1,year2+1):
        for i in range(len(books)):
            year=books[i][0].split("-")
            if j==int(year[0]):
                li.append(books[i])
    print("\nAll titles between "+str(year1)+" and " +str(year2)+":\n")
    if len(li)==0:
        print("No books found in that range of years")
    else:
        for k in range(len(li)):
            print(li[k][1]+", by "+li[k][2]+" ("+li[k][0]+")")

#main
file_name = "NYT_short.txt"
file_name=file_name.strip()
books=create_books_2d_list(file_name)
print(books)
search_by_year(books,1945,1999)
