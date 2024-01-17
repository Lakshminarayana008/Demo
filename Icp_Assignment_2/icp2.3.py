def convert_heights_nested_loop(heights_inches):
    heights_cm = []
    for height in heights_inches:
        height_cm = height * 2.54
        heights_cm.append(round(height_cm, 2))
    return heights_cm

def convert_heights_list_comprehension(heights_inches):
    
    heights_cm = [round(height * 2.54, 2) for height in heights_inches]
    return heights_cm


heights_list = [150, 155, 145, 148]


heights_cm_nested_loop = convert_heights_nested_loop(heights_list)
print("Using Nested Interactive Loop:", heights_cm_nested_loop)


heights_cm_list_comprehension = convert_heights_list_comprehension(heights_list)
print("Using List Comprehension:", heights_cm_list_comprehension)
