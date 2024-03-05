# List inside another list

#   step by step:
#
#   1 - to create a list and use append to insert contents inside this list, use:
#       <list_name1> = list()
#       <list_name1>.append(<content1>)
#       <list_name1>.append(<content2>)

#       the list <list_name1> will have two contents inside it:
#       <list_name1>
#       [<content1>][<content2>]
#           0           1

#   2 - then, create a new list and use the first list to insert the entire list as a content of the second list. For this, use:
#       <list_name2> = list()
#       <list_name2>.append(<list_name1>[:])
#

#   3 - to access and display the contents of a specific location of the "superlist" <list_name2>, use:
#       print(<listname2>[<index_of_listname2_to_use>][<index_of_listname1_to_use>])

#   4 - to access and display the contents of an entire list inside the "superlist" <list_name2>, use:
#       print(<listname2>[<index_of_listname2_that_contains_listname1>])