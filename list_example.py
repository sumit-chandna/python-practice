def custom_list():
    lucky_numbers = [4, 8, 15, 16, 23, 42]
    list_data = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
    print(f"initial List                                     {list_data}")
    print(f"list_data[1:] => From index 1 to End             {list_data[1:]}")
    print(f"list_data[1:3] => From index 1 to 3rd element    {list_data[1:3]}")
    print(f"list_data[::-1] => Reverse                       {list_data[::-1]}")
    list_data.append("dwight")
    print(f"list_data.append(\"dwight\") => append data       {list_data}")
    list_data = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
    list_data.extend(lucky_numbers)
    print(f"list_data.extend(lucky_numbers) => append data   {list_data}")
