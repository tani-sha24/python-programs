import time
import random

# -----------------------------
#  Finger Placement Tutorial
# -----------------------------
def tutorial():
    print("\n=== Finger Placement Tutorial ===")
    print("""
Place your fingers on the HOME ROW keys:

Left Hand:
A = Little finger
S = Ring finger
D = Middle finger
F = Index finger

Right Hand:
J = Index finger
K = Middle finger
L = Ring finger
; = Little finger

Thumbs rest on SPACEBAR.
""")
    input("Press ENTER to continue...")

# -----------------------------
#  Word Lists
# -----------------------------
EASY_WORDS = ["apple", "water", "school", "mouse", "train", "happy", "light"]

MEDIUM_WORDS = [
    "InForMaTion", "PyThOn", "AccuRaCy", "StAtiOn", "coMpuTEr",
    "PraCtiCe", "LEarnIng", "KeyBoArd", "noTeBooK", "miXeDCase"
]

HARD_PARAGRAPH = """
Th3 Qu!ck Br0wn F0x jumP$ 0ver th3 L@zy D0g! 
Typ3 th!$ l!ne ex@ctly @s it 1$$ t0 t3st y0ur sp33d & @ccur@cy.
C@n y0u h@ndl3 c@p$ + numb3r$ + $ymb0l$ @ll t0g3th3r?
"""

HARD_WORDS = [
    "p@ssw0rd!", "C0d!ng123", "PyTh0n#1", "D@t@-Sci3nce", "H@rd#L3v3l"
]

# -----------------------------
#  Function to Calculate Accuracy
# -----------------------------
def calculate_accuracy(original, typed):
    correct = 0
    for o, t in zip(original, typed):
        if o == t:
            correct += 1
    return (correct / len(original)) * 100

# -----------------------------
#  Typing Test Function
# -----------------------------
def typing_test(words):
    random_text = random.choice(words)
    print("\nType this:\n", random_text)
    
    input("Press ENTER when ready...")
    start = time.time()
    typed = input("Start typing: ")
    end = time.time()

    time_taken = end - start
    wpm = (len(typed) / 5) / (time_taken / 60)
    accuracy = calculate_accuracy(random_text, typed)

    print("\n=== Result ===")
    print(f"Time Taken: {round(time_taken, 2)} seconds")
    print(f"WPM: {round(wpm, 2)}")
    print(f"Accuracy: {round(accuracy, 2)}%")

# -----------------------------
#  Paragraph Test (Hard)
# -----------------------------
def paragraph_test():
    print("\n=== HARD PARAGRAPH ===")
    print(HARD_PARAGRAPH)

    input("Press ENTER when ready...")
    start = time.time()
    typed = input("Type paragraph here:\n")
    end = time.time()

    time_taken = end - start
    wpm = (len(typed) / 5) / (time_taken / 60)
    accuracy = calculate_accuracy(HARD_PARAGRAPH, typed)

    print("\n=== Result ===")
    print(f"Time Taken: {round(time_taken, 2)} seconds")
    print(f"WPM: {round(wpm, 2)}")
    print(f"Accuracy: {round(accuracy, 2)}%")

# -----------------------------
#  Main Menu
# -----------------------------
def main():
    while True:
        print("\n===== TYPING TUTOR =====")
        print("1. Finger Placement Tutorial")
        print("2. Easy Mode (Simple Words)")
        print("3. Medium Mode (Random Capital Letters)")
        print("4. Hard Mode (Digits + Symbols)")
        print("5. Hard Paragraph Challenge")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            tutorial()
        elif choice == "2":
            typing_test(EASY_WORDS)
        elif choice == "3":
            typing_test(MEDIUM_WORDS)
        elif choice == "4":
            typing_test(HARD_WORDS)
        elif choice == "5":
            paragraph_test()
        elif choice == "6":
            print("Goodbye! Keep practicing ❤️")
            break
        else:
            print("Invalid choice. Try again.")

# -----------------------------
#  Run Program
# -----------------------------
main()
