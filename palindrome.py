def palindrome():
    data = input("Enter data string:")
    data = data.replace(' ', '')
    reverse_data = data[::-1]
    if reverse_data.__eq__(data):
        print("Palindrome String")
    else:
        print("Not Palindrome String")
