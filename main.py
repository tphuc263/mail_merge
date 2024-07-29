PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        per_name = name.strip()
        per_let = letter_content.replace(PLACEHOLDER, per_name)
        with open(f"./Output/ReadyToSend/{per_name}.txt", mode="w") as send_t:
            send_t.write(per_let)
