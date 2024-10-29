input_data = input().split()


int_value = int(input_data[0])
long_long_value = int(input_data[1])
char_value = input_data[2]
float_value = float(input_data[3])
double_value = float(input_data[4])

# Print each value on a new line
print(int_value)
print(long_long_value)
print(char_value)
print(f"{float_value:.2f}")  # Format the float with 2 decimal places
print(f"{double_value:.1f}")  # Format the double with 1 decimal place
