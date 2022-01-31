from unicodedata import name
from user import User
from Category import Category

dhikra = User("dhikra","dhikra@gmail.com","1234hhghkiL","06596548","path")
# moh = User("mohammed","moh@gmail.com","14589jilkh","0264935","pathpicture")
#yassine = User("yssin","yassin@gmail.com","hfgk125","25634","picturepath",False)
Science = Category("Science") #Test of category class


print(dhikra.create_at)
print(dhikra.status)
print(Science.name)

# using built-in vars to show all attributes
print (vars(dhikra))