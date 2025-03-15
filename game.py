class Game:
    def __init__(self):
        self.state = {
            "location": "HQ",
            "reputation": 50, # Player's influence
            "inventory": []
        }

    def show_intro(self):
        print("\n🔍 Welcome to *Eclipse Protocol*")
        print("You are an elite cybersecurity analyst responding to a cyber threat.")
        self.show_options()

    def show_options(self):
        print("\nWhat do you want to do?")
        print("1. Investigate the threat")
        print("2. Ignore the report")
        print("3. Shut down critical systems (RISKY)")

        choice = input("> ")
        self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == "1":
            print("\n✅ You analyze the logs and discover an unauthorized access attempt.")
            self.state["reputation"] += 10
        elif choice == "2":
            print("\n⚠️ You ignore the report. Hours later, a major data breach occurs.")
            self.state["reputation"] -= 20
        elif choice == "3":
            print("\n🚨 You shut down all systems, causing panic, but stopping the attack.")
            self.state["reputation"] -= 5
        else:
            print("\nInvalid choice, try again.")
            self.show_options()

        print(f"\nReputation: {self.state['reputation']}")
        self.next_stage()

    def next_stage(self):
        print("\n[Next part of the story unfolds...]")
        # This will expand later to include new scenes.

if __name__ == "__main__":
    game = Game()
    game.show_intro()
