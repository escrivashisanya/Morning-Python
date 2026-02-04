age =19  #integer
weight =45.78  #float
greeting = "hello there"  #string
ismammal =True  #Boolean

#Data Structures - Multiple elements in one variable
fruits = ["banana" ,"mango" ,"appple"]  #List - Ordered and Changeable
cars  = ("Ford" ,"G-Wagon" "Mazda" ,"BMW")  #Tuple - Ordered and Unchangeable
countries = {"Tanzania" ,"India" ,"Italy"}  #Set - unordered and unchangeable
student  = {
     "firstname" :"jeff",
     "course" : "MIT",
     "age" :17,
     "nationality" :"kenyan"
}  #Dictionary - Key Value Pair
courses = ["MIT" , "Cybersecurity","Datascience"] #Array -Similar Datatypes





print("Student is" ,age,"years old")
print(weight)
print("Is animal a mammal ? :" ,ismammal)
print(fruits)
print(countries)


#Typecasting - Converting one datatype to another
print(float(age))
print(int(weight))