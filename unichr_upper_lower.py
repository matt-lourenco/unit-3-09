# Created on 27 oct 2016
# Created by: Matthew Lourenco
# this is a program that displays the english alphabet in upper case containing the english alphabet in lower case.
for index_upper in range(65, 91):
    for index_lower in range(97, 123):
        print(unichr(index_upper) + ' -> ' + unichr(index_lower))
