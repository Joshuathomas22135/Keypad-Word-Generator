""" Write a python program to build a Keypad Word Generator using recursion. You will first understand how recursive thinking breaks a large problem into
smaller repeated steps. Then, you will practise Tower of Hanoi, generate phone keypad word combinations, and trace how recursion trees grow as more
choices are added."""

# Tower of Hanoi
print("Tower Of Hanoi")
def towerOfHanoi(disks, source, aux, destination):
    if disks == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    towerOfHanoi(disks - 1, source, aux, destination)
    print(f"Move disk {disks} from {source} to {destination}")

    towerOfHanoi(disks - 1, aux, source, destination)

towerOfHanoi(3, "A", "B", "C")
print()

print("Phone Keypad")

keys = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9":["w","x","y","z"]
}

def generateWords(digits, currentWord):
    if len(digits) == 0:
        print(currentWord)
        return

    firstDigit = digits[0]
    remainingDigits = digits[1:]

    for letter in keys[firstDigit]:
    generateWords(remainingDigits, currentWord + letter)