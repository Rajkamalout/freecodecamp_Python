running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays=round(final_bill,2)
print("Each person pays:",each_pays)






# With the tip now included, you have the final amount for the entire group. You have to determine how much each person owes by dividing the total bill by the number of friends.
# In Python, you use the forward slash / to perform division. For example:
# Example Code
# half = 10 / 2
# Create a variable named final_bill and assign it the result of dividing running_total by num_of_friends.
# Finally, use the print() function to display the string Bill per person: followed by a space and the value of final_bill.

final_bill=running_total/num_of_friends
print("Bill per person:",final_bill)


# The bill is split, but division often results in long decimal numbers. Since money is typically represented with two decimal places, you should round the final result.

# In an earlier lesson, you learned about the round() function which takes two arguments: the number you want to round and the number of decimal places to keep. Here's an example:

# Example Code
# num = 4.815162342
# round(num, 3) # 4.815
# Use the round() function to round final_bill to two decimal places and assign the result to a new variable named each_pays.
# Finally, use print() to display the string Each person pays: followed by a space and your each_pays variable.
# With that, the bill splitter workshop is complete.

each_pays=round(final_bill,2)
print("Each person pays:",each_pays)
