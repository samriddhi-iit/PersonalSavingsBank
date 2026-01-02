// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SavingsBank {

    address payable public owner;

    // Set the owner when the contract is deployed
    constructor() {
        owner = payable(msg.sender);
    }

    // Anyone can deposit Ether into the contract
    function deposit() public payable {
    }

    // Returns the total Ether balance stored in the contract
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    // Only the owner can withdraw Ether
    function withdraw(uint _amount) public {
        require(msg.sender == owner, "Not owner");
        require(_amount <= address(this).balance, "Not enough balance");

        owner.transfer(_amount);
    }
}
