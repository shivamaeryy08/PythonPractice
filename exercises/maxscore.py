scores = input("Enter the student scores: ").split()

max = scores[0]

for score in scores:
    if int(score) > int(max):
        max = score
        
print(f"The highest score is {max}")