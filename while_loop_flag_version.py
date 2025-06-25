def get_starting_number():
    while True:
        user_input = input("How many bottles of beer on the wall? ")
        if user_input.isdigit() and int(user_input) >= 1:
            return int(user_input)

def sing(starting_number):
    bottles = starting_number
    keep_singing = True

    while keep_singing:
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_singing = False
        else:
            next_bottles = bottles - 1
            word_now = "bottle" if bottles == 1 else "bottles"
            word_next = "bottle" if next_bottles == 1 else "bottles"
            print(f"{bottles} {word_now} of beer on the wall, {bottles} {word_now} of beer.")
            print(f"Take one down, pass it around, {next_bottles} {word_next} of beer on the wall.\n")
            bottles -= 1