# Welcome to iQuHACK 2021!
Check out some info in the [event's repository](https://github.com/iQuHACK/2021) to get started.

Having a README in your team's repository facilitates judging. A good README contains:
* a clear title for your project,
* a short abstract,
* the motivation/goals for your project,
* a description of the work you did, and
* proposals for future work.

You can find a potential README template in [one of last year's projects](https://github.com/iQuHACK/QuhacMan).

Feel free to contact the staff with questions over our [event's slack](https://iquhack.slack.com), or via iquhack@mit.edu.

Good luck!

## Blockchain
We've used the blockchain implmented [here](https://github.com/dvf/blockchain).

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

curl -X POST -H "Content-Type: application/json" -d '***REMOVED***"nodes": ["http://localhost:5001"]***REMOVED***' 'http://localhost:5001/nodes/register'

curl -X POST -H "Content-Type: application/json" -d '***REMOVED***
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
***REMOVED***' "http://localhost:5000/transactions/new"
```

For further description of what each of these commands does, please see this [article](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46).
