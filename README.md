# ⚡️ DogecoinAPI

This is an API written in python with the fastapi library and easy peasy to read and use!

It will create endpoints that will forward handselected RPC calls to your dogecoin full node.

## 👟 Run the API

To run the API you need to set the following environment variables:

```sh
RPC_USER=<YOUR RPC USER>
RPC_PASSWORD=<YOUR RPC PASSWORD>
RPC_HOST=<YOUR RPC HOST>
RPC_PORT=<YOUR RPC PORT>
# optional
SSL_KEYFILE=<PATH TO KEYFILE>
SSL_CERTFILE=<PATH TO CERTFILE>
```

For local development you can create a `.env` file.

An example is given in `.env.example`:

```sh
# environment
ENV=DEV
#LOG_LEVEL=INFO
# server
#HOST=localhost
#PORT=8000
#SSL_KEYFILE=path/to/keyfile
#SSL_CERTFILE=path/to/certfile
# rpc
RPC_USER=<YOUR RPC USER>
RPC_PASSWORD=<YOUR RPC PASSWORD>
#RPC_HOST=<YOUR RPC HOST>
#RPC_PORT=<YOUR RPC PORT>
```

If you are running your node on a different port or host you need also to specify the `RPC_PORT` and `RPC_HOST`.

To run the the API endpoints just run the following commands:

```sh
# install dependencies
python -m pip install -r requirements.txt
# start api
python main.py
```

You will be able to access the documentation in your browser under the specified host and port.

## 🕶 See the results

If you want to see the API "live" use this link: <https://easypeasy.eastus.cloudapp.azure.com/>

## 📃 To Do List

- [ ] Missing RPC Calls
- [ ] Improve Error Handling
- [X] Automate Documentation
- [ ] DOS Protection
- [ ] Log stats
- [ ] Cache data (frequent queries)
- [ ] Restructure code base

And a couple of server tasks (run as a service, SSL, get a domain)

## 🛸 Misc

To get more infos about the API you can use curl in verbose mode:

`curl http://easypeasy.eastus.cloudapp.azure.com/api/blockchain/getrawmempool -v`

---

🤡 Does this code comes with warranty or SLAs on the service? No. __Hell no!__ This is just to demonstrate how stuff could be done. Use at own risk and please don't break it or it will become less easy peasy.
