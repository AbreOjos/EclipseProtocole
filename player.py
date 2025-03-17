class Player:
    def __init__(self):
        self.reputation = 50
        self.skills = {
            "hacking": 1,
            "analysis": 1,
            "negotiation": 1
        }
        self.resources = {
            "firewall_strength": 3, # Defensive ability
            "exploits": 2, # Offensive hacking tools
            "funding": 10_000 # Money available for operations
        }
        self.time_remaining = 10

    def modify_stat(self, stat, amount):
        if stat in self.__dict__:
            self.__dict__[stat] += amount
        elif stat in self.skills:
            self.skills[stat] = max(1, min(5, self.skills[stat] + amount))
        elif stat in self.resources:
            self.resources[stat] = max(0, self.resources[stat] + amount)

    def display_stats(self):
        """Show current player stats in the UI"""
        print("\n📊 **Player Status:**")
        print(f"Reputation: {self.reputation}")
        print(f"Skills: {self.skills}")
        print(f"Resources: {self.resources}")
        print(f"Time Remaining: {self.time_remaining} turns")

# Example usage
if __name__ == "__main__":
    player = Player()
    player.modify_stat("hacking", 1)  # Level up hacking skill
    player.modify_stat("funding", -2000)  # Spend money
    player.modify_stat("reputation", 10)
    player.modify_stat("time_remaining", -1)
    player.display_stats()