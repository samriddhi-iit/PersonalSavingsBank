# PersonalSavingsBank
Ownership Logic

The contract stores an owner address.

The owner is set when the contract is deployed using msg.sender.

Anyone can deposit Ether into the contract using the deposit function.

The total balance of the contract can be checked using getBalance.

Only the owner is allowed to withdraw Ether.

The withdraw function checks:

The caller is the owner

The contract has enough balance

If both conditions pass, Ether is transferred to the owner.

# Voting system
The contract has an admin address.

The admin is set when the contract is deployed using msg.sender.

Only the admin can turn voting on or off using toggleVoting.

Voting is controlled by the votingOn boolean.

Users can vote only when voting is enabled.

Each address is allowed to vote only once, tracked using hasVoted.

Votes are counted separately for each candidate.

Anyone can view the current vote count using getVotes.
# Blockchain Python
Block Structure

Each block stores data, timestamp, previous block hash, and its own hash.

Blocks are linked using the previous block’s hash.

Validation Logic

The hash is recalculated to verify block data.

Any change in data breaks the hash link.

Mismatched hashes indicate tampering.

Proof-of-Work

A nonce is used to generate a valid hash.

The hash must start with a set number of zeros.

Higher difficulty requires more computation.
