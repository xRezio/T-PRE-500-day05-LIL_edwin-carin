my_first_list = [4 , 5 , 6]
my_second_list = [1 , 2 , 3]
my_first_list.extend( my_second_list )
print(my_first_list) #" extend sert à ajouter une liste à une autre"

my_first_list1 = [7 , 8 , 9]
my_second_list1 = [4 , 5 , 6]
my_first_list1 = [* my_first_list1 , * my_second_list1 ]
print(my_first_list1) # pareil avec les étoiles

