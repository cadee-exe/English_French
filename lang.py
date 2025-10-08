def lang(x):
    t = 0
    s = 0
    for char in x:
        if char == "1" or "T":
            t+=1
        elif char == "s" or "S":
            s+=1
    if t > s:
        print("english")
    else:
        print("france")
lang("ttttttttttttTTTTTTTTTTTssssssssssssSSSSSSSSSSSSSSSS")





