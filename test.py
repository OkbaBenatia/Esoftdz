from unicodedata import name
from user import User
from Category import Category
from Author import Author
from Book import Book

# dhikra = User("dhikra","dhikra@gmail.com","1234hhghkiL","06596548","path")
# # moh = User("mohammed","moh@gmail.com","14589jilkh","0264935","pathpicture")
# #yassine = User("yssin","yassin@gmail.com","hfgk125","25634","picturepath",False)
# Science = Category("Science") #Test of category class
# author1 = Author('James M. McPherson', '0555 555 555','j.mcpherson@gmail.com','USA',
#         'His adress', 'https://www.goodreads.com/author/show/12144.James_M_McPherson','@jamesMc',1 )


# print(dhikra.create_at)  
# print(dhikra.status)
# print(Science.name)

# # using built-in vars to show all attributes
# print (vars(dhikra))
# print (dhikra.__doc__)
# print(author1.__doc__)
#book1 = Book("learn python","1.1","102","python easy to learn...","2020","20","english","path_pic","path_book","1","1")
#author1 = Author("yassin","06659632","yassin@gamil.com","Algeria","djelfa","www.yasin.co","twitter/yassin","1")
programming = Category("programming")
print(programming.create_at)