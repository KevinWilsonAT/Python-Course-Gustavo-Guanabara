# Lists

#   syntax:
#       <list_name> = [<content1>, <content2>, ..., <contentN>]
#   To access, use:
#       print(<list_name>[<content_position>])

#   To add items in the LAST POSITION of the list, use:
#       <list_name>.append(<item>)

#   To add items in the FIRST POSITION of the list, use:
#       <list_name>.insert(0,<item>)

#   To add items in a POSITION in the range of the list, use:
#       <list_name>.insert(<index_inside_list_range>,<item>)

#   Doing the insert command affects the position number AFTER the item
#   inserted.

#   To deleter the LAST ITEM of the list, use:
#       <list_name>.pop()

#   To delete items of the lists by the POSITION NUMBER, use:
#       del <list_name>[<item_position>]    OR
#       <list_name>.pop(<item_position>)

#   To delete items of the lists by the CONTENT NAME, use:
#       <list_name>.remove(<item>)

#   To order alphabetically or numerically, use:
#       <list_name>.sort()

#   To order alphabetically or numerically in reverse order, use:
#       <list_name>.sort(reverse=True)

#   To show how many contents exists in the list, use:
#       len(<list_name>)


#   To insert values inside a list, use:
#       <list_name> = list()
#
#       for <iteration_variable_name> in range(<init_value, <final_value>):
#           <list_name>.append(<int/str/float>(input(<input_message>)))

#   To show those values and indexes from the list together, use:
#       for <index_variable_name>, <content_variable_name> in enumerate(<list_name>):
#           print({<index_variable_name>}{<content_variable_name>})

#   To show values and indexes from a list together, use:
#       <list_name> = (<content1>, <content2>, ..., <contentN>)
#
#       for <index_variable_name>, <content_variable_name> in enumerate(<list_name>):
#           print({<index_variable_name>}{<content_variable_name>})

#   To link two lists, use:
#       <list_1> = <list_2>

#   OBS.: That makes every change in <list_1 > appears in <list_2> and vice versa

#   To copy one list to another, use:

#       <list_1> = <list_2>[:]

#   OBS.: That ensures that <list_1 > values doesn't interfere in <list_2> values and vice versa
