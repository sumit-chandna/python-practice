def string_format_demo():
    print("this is a string {}".format("Inserted"))
    print("The {2} {1} {0}".format("fox", "brown", "quick"))
    print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

    # float formatting
    result = 100 / 777
    print("value = {r:1.3f}".format(r=result))
    f = "fox"
    b = "brown"
    q = "quick"
    print(f"The {q} {b} {f}")
    print(f"value = {result:1.3f}")
