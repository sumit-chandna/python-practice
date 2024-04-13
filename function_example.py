def say_hi(name, age):
    print(f"Hello {name}!!,You are {age} old")


def cube(num):
    return num * num * num


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


def animal_cracker(text):
    wordList = text.lower().split()
    return wordList[0][0] == wordList[1][0]


def make_twenty(n1, n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20


