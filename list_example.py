def custom_list():
    lucky_numbers = [4, 8, 15, 16, 23, 42]
    list_data = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
    print(f"initial List                                     {list_data}")
    print(f"list_data[1:] => From index 1 to End             {list_data[1:]}")
    print(f"list_data[1:3] => From index 1 to 3rd element    {list_data[1:3]}")
    print(f"list_data[::-1] => Reverse                       {list_data[::-1]}")
    list_data.append("dwight")
    print(f"list_data.append(\"dwight\") => append data       {list_data}")
    list_data.extend(lucky_numbers)
    print(f"list_data.extend(lucky_numbers) => append data   {list_data}")


def custom_list_comprehension():
    my_list = [num for num in range(0, 11)]
    print(f"My  List : [num for num in range(0, 11)]:  {my_list}")
    my_list = [num ** 2 for num in range(0, 11)]
    print(f"My squared list :[num ** 2 for num in range(0, 11)]:  {my_list}")
    my_list = [num for num in range(0, 11) if num % 2 == 0]
    print(f"even list : [num for num in range(0, 11) if num % 2 == 0]:  {my_list}")
    celcius = [0, 10, 20, 30]
    fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
    print(f"celcius:  {celcius}")
    print(f"fahrenheit : [((9 / 5) * temp + 32) for temp in celcius]:  {fahrenheit}")
