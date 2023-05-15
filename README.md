# :zap: DogecoinAPI

This is an API written in python with the fastapi library and easy peasy to read and use!

It will create endpoints that will forward handselected RPC calls to your dogecoin full node.

# :athletic_shoe: Run the API

You will need to set those variables in main.py:
````
rpcuser = "rpcuser"
rpcpassword = "rpcpassword"
rpcport = 22555
rpchost = "127.0.0.1"
````

The port is the standard port but must be defined. Password and username must be defined in your ``dogecoin.conf``

If you don't run your node on the same machine make sure to also change the IP address here:
````
# new connection
rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
````

To run the the API endpoints just fire up this python script
``python main.py``

You will be able to access the documentation in your browser under http://localhost

# :dark_sunglasses: See the results

If you want to see the API "live" use this link: http://easypeasy.eastus.cloudapp.azure.com/

# :page_with_curl: To Do List

- [ ] Missing RPC Calls
- [ ] Improve Error Handling
- [X] Automate Documentation
- [ ] DOS Protection
- [ ] Log stats
- [ ] Cache data (frequent queries)


And a couple of server tasks (run as a service, SSL, get a domain)

# :flying_saucer: Misc

To get more infos about the API you can use curl in verbose mode:

``curl http://easypeasy.eastus.cloudapp.azure.com/api/blockchain/getrawmempool -v``

---

:clown_face: Does this code comes with warranty or SLAs on the service? No. __Hell no!__ This is just to demonstrate how stuff could be done. Use at own risk and please don't break it or it will become less easy peasy.
