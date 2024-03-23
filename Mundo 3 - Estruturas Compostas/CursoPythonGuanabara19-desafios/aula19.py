# Dictionary

#   DECLARATION SYNTAX
#
#       <dict_name1> = dict()
#       <dict_name1> = {<field1>:<content1>, <field2>:<content2>}
#
#   the dictionary <dict_name1> will have two contents inside it, each one with a field that act as identifier,
#   instead of an index number:
#
#       <dict_name1>
#       [<content1>][<content2>] ... [<contentN>]
#         <field1>    <field2>   ...   <fieldN>
#
#   to access and display the contents of ONE specific subject of the dictionary <dict_name1>, use:
#       print(<dict_name1>[<field1> or <field_2> or ... <fieldN>])
#
#   to delete the contents of ONE specific subject of the dictionary <dict_name1>, use:
#       del <dict_name1>[<field1> or <field_2> or ... <fieldN>]
#
#   to access and display ALL the contents of the dictionary <dict_name1>, use:
#       print(<dict_name1>.values())
#
#   to access and display ALL the fields (identifiers) of the dictionary <dict_name1>, use:
#       print(<dict_name1>.keys())
#
#   to access and display ALL the contents and its fields (indentifiers) of the dictionary <dict_name1>, use:
#       print(<dict_name1>.items()) 
#
#   use [:] to copy the contents of the dictionary



# Dictionary inside a list
#
#   step by step:
#
#   1 - create a dicitionary and insert it inside a list:
#
#       <dict1> = {<field1a>:<content1a>, <field1b>:<content1b> ... <field1N>:<content1N>}
#       <dict2> = {<field2a>:<content2a>, <field2b>:<content2b> ... <field2N>:<content2N>}
#       ...
#       <dictN> = {<fieldNa>:<contentNa>, <fieldNb>:<contentNb> ... <fieldNN>:<contentNN>}
#       
#       <list_name1> = [<dict1>, <dict2>, ... <dictN>]
#
#       the list <list_name1> now have dictionaries inside it:
#       <list_name1>
#       [<dict1>][<dict2>] ... [<dictN]
#           0        1     ...     N