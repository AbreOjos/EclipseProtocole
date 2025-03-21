import json

from player import Player


class Game:
    def __init__(self, story_file):
        with open(story_file, "r") as f:
            self.story = json.loads(f.read())
        self.current_scene = "intro"
        self.player = Player()

    def apply_stat_changes(self, changes):
        for stat, value in changes.items():
            self.player.modify_stat(stat, value)

    def handle_stat_check(self, scene):
        requirements = scene["stat_requirements"]
        passed = all(
            self.player.skills.get(skill, 0) >= level
            for skill, level in requirements.items()
        )

        if passed:
            print("\n✅ Skill check passed! You meet all required skills.")
            success = scene["success"]
            print(success["text"])
            if "stat_changes" in success:
                self.apply_stat_changes(success["stat_changes"])
            return success["next"]
        else:
            print("\n❌ Skill check failed! You don't meet the required skills.")
            failure = scene["failure"]
            print(failure["text"])
            if "stat_changes" in failure:
                self.apply_stat_changes(failure["stat_changes"])
            return failure["next"]

    def play(self):
        while self.current_scene:
            scene = self.story.get(self.current_scene, {})
            print(f"\n{scene.get('text', 'No content found.')}")

            # Apply initial stat changes for the scene
            if "stat_changes" in scene:
                self.apply_stat_changes(scene["stat_changes"])

            self.player.display_stats()

            # Handle stat-based scenes
            if "stat_requirements" in scene:
                self.current_scene = self.handle_stat_check(scene)
                continue

            # Handle regular choices
            options = scene.get("options", {})
            if not options:
                print("\n[End of story]")
                break

            for key, value in options.items():
                print(f"{key}. {value}")

            choice = input("> ").strip()
            self.current_scene = scene["next"].get(choice, None)

        print("\nGame Over")

if __name__ == "__main__":
    game = Game("story.json")
    game.play()
