import json

from player import Player


class Game:
    def __init__(self, story_file):
        with open(story_file, "r") as f:
            self.story = json.loads(f.read())
        self.current_scene = "intro"
        self.player = Player()

    def play(self):
        while self.current_scene:
            scene = self.story.get(self.current_scene, {})
            print(f"\n{scene.get('text', 'No content found.')}")

            # Apply any stat changes from the scene
            if "stat_changes" in scene:
                for stat, value in scene["stat_changes"].items():
                    self.player.modify_stat(stat, value)

            self.player.display_stats()

            # Handle choices
            options = scene.get("options", {})
            if not options:
                print("\n[End of story]")
                break

            for key, value in options.items():
                print(f"{key}. {value}")

            choice = input("> ")

            self.current_scene = scene["next"].get(choice, None)

        print("\nGame Over")

    # def show_intro(self):
    #     print("\n🔍 Welcome to *Eclipse Protocol*")
    #     print("You are an elite cybersecurity analyst responding to a cyber threat.")
    #     self.show_options()
    #
    # def show_options(self):
    #     print("\nWhat do you want to do?")
    #     print("1. Investigate the threat")
    #     print("2. Ignore the report")
    #     print("3. Shut down critical systems (RISKY)")
    #
    #     choice = input("> ")
    #     self.handle_choice(choice)

    # def handle_choice(self, choice):
    #     if choice == "1":
    #         print("\n✅ You analyze the logs and discover an unauthorized access attempt.")
    #         self.state["reputation"] += 10
    #     elif choice == "2":
    #         print("\n⚠️ You ignore the report. Hours later, a major data breach occurs.")
    #         self.state["reputation"] -= 20
    #     elif choice == "3":
    #         print("\n🚨 You shut down all systems, causing panic, but stopping the attack.")
    #         self.state["reputation"] -= 5
    #     else:
    #         print("\nInvalid choice, try again.")
    #         self.show_options()
    #
    #     print(f"\nReputation: {self.state['reputation']}")
    #     self.next_stage()

    # def next_stage(self):
    #     print("\n[Next part of the story unfolds...]")
    #     # This will expand later to include new scenes.

if __name__ == "__main__":
    game = Game("story.json")
    game.play()
