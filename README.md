# :zap: DogecoinAPI

This is an API written in python with the fastapi library and easy peasy to read and use!

It will create endpoints that will forward handselected RPC calls to your dogecoin full node.

# :athletic_shoe: Run the API

You will need to set those variables in main.py:
````
rpcuser = "rpcuser"
rpcpassword = "rpcpassword"
rpcport = 22555
````

The port is the standard port but must be defined. Password and username must be defined in your ``dogecoin.conf``

If you don't run your node on the same machine make sure to also change the IP address here:
````
# new connection
rpc = RPC_Connection(rpcuser, rpcpassword, "127.0.0.1",rpcport)
````

To run the the API endpoints just fire up this python script
``python main.py``

You will be able to access the documentation in your browser under http://localhost:8080/web

# :dark_sunglasses: See the results

If you want to see the APIs "live" use this link: http://easypeasy.eastus.cloudapp.azure.com:8080/web/

# :flying_saucer: Misc

To get more infos about the API you can use curl in verbose mode:

``curl easypeasy.eastus.cloudapp.azure.com:8080/api/blockchain/getblockcount -v``

---

:clown_face: Does this code comes with warranty or SLAs on the service? No. __Hell no!__ This is just to demonstrate how stuff could be done. Use at own risk and please don't break it or it will become less easy peasy.
