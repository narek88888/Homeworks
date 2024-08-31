# 7-1 Arrange
# Arrange string characters such that lowercase letters should come first

x = "pYtHoN"

font_box_lower = []
font_box_upper = []

for i in x :
    if i.islower() :
        font_box_lower.append(i)
    elif i.isupper() :
        font_box_upper.append(i)

lower = "".join(font_box_lower)
upper = "".join(font_box_upper)


print(lower + upper)