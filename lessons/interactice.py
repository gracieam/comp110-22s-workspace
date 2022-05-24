def grocery_list(inventory: dict[str, int], g_list: dict[str, int]) -> list[str]:
    result: list[str] = []
    for item in g_list:
        if item in inventory:
            if g_list[item] <= inventory[item]:
                result.append(item)
    return result

inventory: dict[str, int] = {"bread" : 3, "chips" : 1, "eggs" : 5}
g_list: dict[str, int] = {"bread" : 2, "chips" : 10, "eggs" : 1}
print(grocery_list(inventory, g_list))