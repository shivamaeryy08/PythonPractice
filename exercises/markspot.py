#Program that takes in a integer [col,row] and adds a 'X' at that location in in the map (lists of lists)

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_col = int(position[0])

position_row = int(position[1])

if position_col > 3 or position_row > 3:
    print("Invalid input")
else:
    map[position_col-1][position_row-1] = "X"
    print(f"{row1}\n{row2}\n{row3}")


