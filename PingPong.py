def convert_in2cm(inches):
    return inches * 2.54
def convert_lb2kg(pounds):
    return pounds / 2.2

pingpongs = int(input("Enter amount of pingpongs "))



pingpong_toweight = round(pingpongs/1000*2.7)
pingpong_height = round(pingpongs*4)

print("At", pingpongs, "pingpongs")
print("you measure", pingpong_height,"cm")
print("you weigh the same as", pingpong_toweight, "pounds")
