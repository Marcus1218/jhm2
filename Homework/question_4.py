#define the height
def height_def(student):
    #use while true loop to check the input
    while True:
        #use try to confilm the input
        try:
            #input height
            height = float(input(f"Input the height of student {student} in cm: "))
            #check height are suitable condition
            if height < 0:
                print("Height must be positive.")
            elif height > 200:
                print("Height is greater than 200cm.")
            else:
                return height
        except ValueError:
            print("Invalid input. Please enter a number.")

#height array
heights = []
for i in range(1, 5):
    height = height_def(i)
    heights.append(height)
#end of input
print("End of input.")
#caculate the average height
average_height = sum(heights) / len(heights)
#find the maximum height
max_height = max(heights)

#print out the result
print(f"The average height of these students is {average_height:.2f} cm.")
print(f"The maximum height of these students is {max_height:.2f} cm.")