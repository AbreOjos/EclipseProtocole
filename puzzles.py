import random


def password_crack_game(difficulty="easy"):
    print("\n🔓 HACKING CHALLENGE: Password Cracker")

    # Difficulty Settings
    difficulty_settings = {
        "easy": {"length": 4, "attempts": 6},
        "medium": {"length": 5, "attempts": 5},
        "hard": {"length": 6, "attempts": 4}
    }

    settings = difficulty_settings.get(difficulty, difficulty_settings["easy"])
    length = settings["length"]
    max_attempts = settings["attempts"]

    # Sample words by length
    word_bank = {
        4: ["NODE", "FIRE", "CODE", "ZERO", "RISK", "DATA"],
        5: ["LOGIC", "CLOUD", "PROXY", "CRASH", "PATCH", "VIRUS"],
        6: ["SERVER", "BREACH", "PACKET", "BUFFER", "ATTACK", "SECURE"]
    }

    password = random.choice(word_bank[length])
    score = 0

    print(f"🎯 Crack the {length}-letter password. You have {max_attempts} attempts.\n")

    for attempt in range(1, max_attempts+1):
        while True:
            guess = input(f"Attempt {attempt}/{max_attempts}: ").upper()
            if len(guess) != length:
                print(f"❗ Password must be exactly {length} letters.")
            else:
                break
        if guess == password:
            print("✅ Access granted. Password correct.")
            score = (max_attempts - attempt + 1) * 10 # Reward for speed
            break
        else:
            hint = []
            for i in range(length):
                if guess[i] == password[i]:
                    hint.append("🟩")
                elif guess[i] in password:
                    hint.append("🟨")
                else:
                    hint.append("⬛")
            print("Hint: " + "".join(hint))
    else:
        print("❌ Access denied. Password failed.")

    print(f"\n🔢 Score: {score}")
    return score > 0, score
