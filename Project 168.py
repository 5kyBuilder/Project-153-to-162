year = 2024

class BookStore:
    def __init__(self, Name, Author, Year, Price):
        self.Name = Name
        self.Author = Author
        self.Year = Year
        self.Price = Price
        
    def details(self):
        print("------------------------------------------------")
        print("Book Name: " + self.Name)
        print("Book Author: " + self.Author)
        print("Book was published in " + str(self.Year))
        print("The book was published " + str(year - self.Year) + " years ago")
        print("Book Price: " + str(self.Price))
        print("book added!")
        print("------------------------------------------------")

Harry_Potter = BookStore("Harry Potter", "J.K Rowling", 1997, 40)
Harry_Potter.details()

DiaryOfAWimpyKid = BookStore("Diary of a Wimpy Kid", "Jeff Kinney", 2017, 60)
DiaryOfAWimpyKid.details()