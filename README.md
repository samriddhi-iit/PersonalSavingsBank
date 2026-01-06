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

#Voting system
