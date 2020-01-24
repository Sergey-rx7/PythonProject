set1 = set(['1', '2', '3'])
set2 = (['1', '4', '3'])


# sel = (['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
# sel = '1 2 3 4 5 6 7 8 9 10'


def my_function(set2):
    if len(set1.intersection(set2)) > 2:
        # return "YES"
        print("YES")
    else:
        print(len(set1.intersection(set2)))



my_function(set2)