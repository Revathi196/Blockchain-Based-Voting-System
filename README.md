# Blockchain-Based Voting System

## Overview
This is a simple **Blockchain-Based Voting System** built using Python. The system allows users to submit votes, and each vote is stored as a block in a blockchain. This system demonstrates how blockchain can be used to ensure transparency, security, and immutability in voting systems.

## Features
- **Vote Submission**: Allows voters to submit their votes for candidates.
- **Blockchain**: Each vote is added to the blockchain as a block, ensuring data integrity.
- **Block Creation**: After a batch of votes, the system can create a new block to store the votes.
- **Blockchain Validation**: The system can validate the integrity of the blockchain.
- **View Blockchain**: Display the current blockchain and its contents.

## Dependencies
This system requires Python 3.x and the following libraries:
- **hashlib**: For hashing blocks.
- **json**: For serializing block data.
- **time**: For timestamping blocks.

## How to Run the System

### Prerequisites:
- Python 3.x installed.

### Steps:
1. **Clone or download** the repository to your local machine.

2. **Navigate to the folder** where the `voting_system.py` and `blockchain.py` files are located.

3. **Run the script** by typing the following command:
   ```bash
   python voting_system.py
