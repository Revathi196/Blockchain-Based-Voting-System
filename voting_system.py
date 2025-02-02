# voting_system.py
from blockchain import Blockchain

class VotingSystem:
    def __init__(self):
        self.blockchain = Blockchain()

    def vote(self, voter_id, candidate_name):
        """Submit a vote."""
        print(f"Voter {voter_id} is voting for {candidate_name}")
        self.blockchain.add_vote(voter_id, candidate_name)

    def create_block(self):
        """Create a new block with the current votes."""
        block = self.blockchain.create_block()
        if block:
            print(f"Block created: {block}")
        else:
            print("No votes to create a block.")

    def validate_votes(self):
        """Validate the blockchain integrity."""
        is_valid = self.blockchain.validate_chain()
        if is_valid:
            print("Blockchain is valid.")
        else:
            print("Blockchain is invalid.")

    def display_chain(self):
        """Display the current blockchain."""
        print("\nCurrent Blockchain:")
        for block in self.blockchain.chain:
            print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}")

def main():
    voting_system = VotingSystem()

    while True:
        print("\nBlockchain-Based Voting System")
        print("1. Vote")
        print("2. Create Block (Finalize Votes)")
        print("3. Validate Blockchain")
        print("4. View Blockchain")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            voter_id = input("Enter voter ID: ").strip()
            candidate_name = input("Enter candidate name: ").strip()
            voting_system.vote(voter_id, candidate_name)

        elif choice == '2':
            voting_system.create_block()

        elif choice == '3':
            voting_system.validate_votes()

        elif choice == '4':
            voting_system.display_chain()

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
