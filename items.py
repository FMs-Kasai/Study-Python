def print_items(items_dict,left_width,right_width):
    print("Items".center(left_width + right_width, "-"))
    for k,v in items_dict.items():
        print(k.ljust(left_width, ".") + str(v).rjust(right_width))

items = {"dragon-sword": 1, "white-shild": 3, "orb": 2,"Herbs": 39}
print_items(items,12,5)
print_items(items,20,6)