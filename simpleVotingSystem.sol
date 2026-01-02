// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VotingSystem {

    address public admin;

    uint public candidate1Votes;
    uint public candidate2Votes;

    bool public votingOn;

    mapping(address => bool) public hasVoted;

    constructor() {
        admin = msg.sender;
        votingOn = true;
    }

    function vote(uint _candidateId) public {
        require(votingOn == true, "Voting is off");
        require(hasVoted[msg.sender] == false, "Already voted");
        require(_candidateId == 1 || _candidateId == 2, "Invalid candidate");

        hasVoted[msg.sender] = true;

        if (_candidateId == 1) {
            candidate1Votes++;
        } else {
            candidate2Votes++;
        }
    }

    function getVotes() public view returns (uint, uint) {
        return (candidate1Votes, candidate2Votes);
    }

    function toggleVoting() public {
        require(msg.sender == admin, "Not admin");
        votingOn = !votingOn;
    }
}
