def while_demo():
    i = 1
    while i <= 10:
        print(i, end="\t")
        i += 1
    print("\nWhile Loop Completed")


def for_demo():
    for letter in "Kumar":
        print(letter, end="\t")
    print("\n")
    for num in range(10):
        print(num, end="\t")
    coordinates = [(32.446, 53.987), (2.446, 5.987), (44.446, 53.987), (882.446, 53.987)]
    print(f"\nCoordinates : {coordinates}")
    for lat, long in coordinates:
        print(f"latitude : {lat}, longitude : {long}")
    print("---------For Loops Completed---------")
