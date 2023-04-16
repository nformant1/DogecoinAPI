from fastapi import FastAPI, HTTPException
from fastapi import Request
#from fastapi.responses import HTMLResponse
import uvicorn
from rpc_connection import RPC_Connection
from fastapi.middleware.cors import CORSMiddleware
#from fastapi.staticfiles import StaticFiles
#from fastapi.responses import JSONResponse

#from models import BestBlockhash

from multiprocessing import cpu_count, freeze_support
#import time

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

# credentials for dogecoin node
rpcuser = "rpcuser"
rpcpassword = "rpcpassword"
rpcport = 22555
rpchost = "127.0.0.1"


app = FastAPI(
    title="DogeAPI",
    description='''Welcome to our fully unsupported online service that answers all your blockchain queries faster than the time it takes for a Bitcoin transaction to confirm! Our service is so fast, you'll be able to check the status of the Dogecoin network before Elon Musk has time to tweet about it. So whether you want to know the current mempool or check if your grandma's P2SH scripts still work, we've got you covered!

This service comes without warranty. Use at own risk. Only hobby project (:

''',
    redoc_url="/",
    docs_url=None
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
"""

#app.mount('/web', StaticFiles(directory='static',html=True))

#@app.get("/api/blockchain/getbestblockhash", response_model=BestBlockhash)
@app.get("/api/blockchain/getbestblockhash")
def get_best_blockhash():
    """
    Returns the hash of the best (tip) block in the longest blockchain.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    try:
        data = rpc.command("getbestblockhash")
        #return BestBlockhash(best_blockhash=data)
        return data
    except:
        raise HTTPException(status_code=418, detail="Something went wrong")
    

@app.get("/api/blockchain/getblock/{hashval}")
async def get_block(hashval):
    """
    Returns an Object with information about block <hash>.
    Always in "verbose" mode.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    try:
        print (hashval)
        data = rpc.command("getblock", params=[hashval])
        return data
    except:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getblockchaininfo")
def get_blockchain_info():
    """
    Returns an object containing various state info regarding blockchain processing.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getblockchaininfo")
        return data
    except:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getblockcount")
def get_blockcount():
    """
    Returns the number of blocks in the longest blockchain.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getblockcount")
        return data
    except Exception as e:
        #raise UnicornException(name="getbestblockhash")
        #print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getblockhash/{height}")
async def get_blockhash(height):
    """
    Returns hash of block in best-block-chain at height provided.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        #print (height)
        data = rpc.command("getblockhash", params=[int(height)])
        return data
    except:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getblockheader/{hashval}")
async def get_blockheader(hashval):
    """
    Returns an Object with information about blockheader <hash>.
    Always in "verbose" mode.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    #data = {}
    try:
        data = rpc.command("getblockheader", params=[hashval])
        return data
    except Exception as e:
        print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getchaintips")
def get_chaintips():
    """
    Return information about all known tips in the block tree, including the main chain as well as orphaned branches.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getchaintips")
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")
    
@app.get("/api/blockchain/getdifficulty")
def get_difficulty():
    """
    Returns the proof-of-work difficulty as a multiple of the minimum difficulty.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getdifficulty")
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getmempoolancestors/{txid}")
async def get_mempool_ancestors(txid):
    """
    If txid is in the mempool, returns all in-mempool ancestors.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getmempoolancestors", params=[txid])
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getmempooldescendants/{txid}")
async def get_mempool_descendants(txid):
    """
    If txid is in the mempool, returns all in-mempool descendants.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getmempooldescendants", params=[txid])
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getmempoolentry/{txid}")
async def get_mempool_entry(txid):
    """
    Returns mempool data for given transaction.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getmempoolentry", params=[txid])
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getmempoolinfo")
def get_mempool_info():
    """
    Returns details on the active state of the TX memory pool.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getmempoolinfo")
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getrawmempool")
def get_raw_mempool():
    """
    Returns all transaction ids in memory pool as a json array of string transaction ids.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getrawmempool")
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/gettxout/{txid}/{n}")
def get_txout(txid: str, n: int):
    """
    Returns details about an unspent transaction output.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("gettxout", params=[txid, n])
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")

#gettxoutproof
#gettxoutsetinfo
#preciousblock "blockhash"
#pruneblockchain
#verifychain ( checklevel nblocks )
#verifytxoutproof "proof"

# CONTROL
@app.get("/api/blockchain/getinfo")
def get_info():
    """
    DEPRECATED. Returns an object containing various state info.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getinfo")
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")
    
@app.get("/api/blockchain/help")
def help_all():
    """
    List all commands, or get help for a specified command.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("help")
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")
@app.get("/api/blockchain/help/{command}")
async def help(command):
    """
    List all commands, or get help for a specified command.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    print (command)
    try:
        if command == "":
            data = rpc.command("getinfo")
        else:
            data = rpc.command("getinfo", params=[command])
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")


# NETWORK
@app.get("/api/blockchain/getnettotals")
def get_net_totals():
    """
    Returns all transaction ids in memory pool as a json array of string transaction ids.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getnettotals")
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")


#== Rawtransactions ==
#createrawtransaction [{"txid":"id","vout":n},...] {"address":amount,"data":"hex",...} ( locktime )
#fundrawtransaction "hexstring" ( options )
#getrawtransaction "txid" ( verbose )
#sendrawtransaction "hexstring" ( allowhighfees )
#signrawtransaction "hexstring" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )



    
@app.get("/api/rawtransactions/decoderawtransaction/{hexstring}")
async def decode_rawtransaction(hexstring):
    """"
    Returns an Object with information about blockheader <hash>.
    """
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("decoderawtransaction", params=[hexstring])
        return data
    except Exception as e:
        #raise UnicornException(name="getbestblockhash")
        print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/rawtransactions/decodescript/{hexstring}")
async def decode_script(hexstring):
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("decodescript", params=[hexstring])
        return data
    except Exception as e:
        #raise UnicornException(name="getbestblockhash")
        print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/rawtransactions/getrawtransaction/{txid}")
async def get_rawtransaction(txid):
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("getrawtransaction", params=[txid, True])
        return data
    except Exception as e:
        #raise UnicornException(name="getbestblockhash")
        print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/rawtransactions/sendrawtransaction/{hexstring}")
async def send_rawtransaction(hexstring):
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("sendrawtransaction", params=[hexstring])
        return data
    except Exception as e:
        #raise UnicornException(name="getbestblockhash")
        print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")




# UTIL
@app.get("/api/rawtransactions/validateaddress/{address}")
async def validate_address(address):
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    try:
        data = rpc.command("validateaddress", params=[address])
        return data
    except Exception as e:
        #raise UnicornException(name="getbestblockhash")
        print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")

"""@app.get("/api/rawtransactions/verifymessage/")
async def verify_message(signature: str, mes: str):
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    data = {}
    print ("S: " + signature)
    print ("M: " + mes)
    try:
        data = rpc.command("verifymessage", params=[signature, mes])
        return data
    except Exception as e:
        #raise UnicornException(name="getbestblockhash")
        print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")"""


"""
@app.get("/api/test")
def read_root():
    rpc = RPC_Connection(rpcuser, rpcpassword, rpchost, rpcport)
    try:
        data = rpc.command("getbestblockhash")
        return data
    except:
        #raise UnicornException(name="getbestblockhash")
        raise HTTPException(status_code=418, detail="Something went wrong")
"""

if __name__ == "__main__":
    #uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="debug", reload=True)
    uvicorn.run("main:app",
                host="0.0.0.0",
                log_level="debug",
                port=443,
                reload=True
                ,ssl_keyfile="C:\\Certbot\\live\\easypeasy.eastus.cloudapp.azure.com\\privkey.pem"
                ,ssl_certfile="C:\\Certbot\\live\\easypeasy.eastus.cloudapp.azure.com\\fullchain.pem"
                )

    #freeze_support()
    #uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=False,workers=4,loop="asyncio",)
