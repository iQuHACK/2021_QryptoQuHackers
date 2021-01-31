# QryptoQuHackers
## Implementing Quantum Digital Signature on Classical Blockchain Model
 
Julian Yocum, Kevin Greenman, William Nolan, Steven Raphael, Hope Fu
 
## Abstract

Since the invention of Bitcoin in 2008, Cryptocurrency has demonstrated its advantages of decentralization, security, and protection of privacy. However, since it is a well known application of quantum computers to break the mathematical difficulty underlying most security protocols, it became obvious that quantum computing poses a threat to the security of cryptocurrencies. A decentralized online quantum cash system, called Qubitcoin, is described here.  As quantum computing introduces more reliable cryptographic methods, our project applies quantum cryptography protocols to the validation of digital currency transactions.
 
In this project we are using quantum gates to implement the quantum digital signature and quantum hash function of a bitcoin blockchain toy model based on published research.
 
## Blockchain
We've used the blockchain implemented [here](https://github.com/dvf/blockchain).
 
To start the blockchain, run
```
python blockchain/blockchain.py - p XXXX
```
where XXXX is the port number (default is 5000).
 
Next, open a new terminal window and you'll be able to use the following commands (replace 5000 with your port number if applicable):
```
curl http://localhost:5000/chain
 
curl http://localhost:5000/mine
 
curl http://localhost:5000/nodes/resolve
 
curl -X POST -H "Content-Type: application/json" -d '{"nodes": ["http://localhost:5001"]}' 'http://localhost:5001/nodes/register'
 
curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"
```
 
For further description of what each of these commands does, please see this [article](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46).
 
## Quantum Digital Signature
The quantum digital signature is a protocol proven to be unconditionally secure digital signatures given limited numbers of copies in circulation.
 
The quantum digital signature is generated from a message and the private key. The public key then, is generated from the crypto_hash one-way function (from hash.py) and has properties similar to classical hash pre-image and collision resistance:
```
"f_k0":[crypto_hash(ki, priv_keys["k0"]) for ki in priv_keys["k0"]]
```
In our implementation, when calling the Signed_Transaction() class, a dict is returned containing the message, private keys, and public keys.
 
Please see this [article](https://arxiv.org/pdf/quant-ph/0105032.pdf) for more detailed information on the theorem and protocol.
 
## Implementing Digital Signature to Blockchain
The quantum digital signature is generated uniquely for each transaction when calling new_transcation function:
Each transaction is added to the next blockchain, and they are verified when mining the next blockchain using the validate() function in signature.py. The transaction will be removed from the blockchain if we detect more than 10% total bit failure. (The function returns pass/fail and the percentage of failure).
 
## Demonstration:
To demonstrate how the protocol would react to forgery of digital signature, we introduced an eavesdropper trying to fake a digital signature with the class Forgery() in signature.py. The forge_transaction() function forges a new set of private keys to generate public keys. In our demonstration, when the fake transaction goes through the mining process, ...
 
## Proposal for future work
Compared to the classical bitcoin blockchains, implementing the quantum digital signature enables the transactions to be validated through the mining process and its security is based on fundamental principles of quantum physics instead of mathematical complexity.
Commented demonstrations of specific functions can also be found under the overview.ipynb file. 
 
For future works, some important goals are

- Utilizing quantum systems more efficiently to use less qubits
- Speeding up the time required to make a transaction and generate a signature
- Testing how the cryptocurrency holds up as the blockchain grows
