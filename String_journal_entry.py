# This Program is created for manipulating the string and create a 'Journal Entry'.

user_debit = int(input("Enter the debit balance\n"))
user_details = {'dr': user_debit}

debit_side = "{} a/c dr  \t{}\n".format('Cash', user_details.get('dr'))
credit_side = "\tTo {} a/c     \t\t{}".format('Sales', user_details.get('dr'))

Entry = debit_side + credit_side
print(Entry)

debit_side

credit_side

