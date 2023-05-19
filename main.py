import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import config
from rpc_connection import RPC_Connection


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

# Models for parameters


class Verifymessage(BaseModel):
    address: str
    signature: str
    message: str


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

# app.mount('/web', StaticFiles(directory='static',html=True))

# @app.get("/api/blockchain/getbestblockhash", response_model=BestBlockhash)


@app.get("/api/blockchain/getbestblockhash")
def get_best_blockhash():
    """
    Returns the hash of the best (tip) block in the longest blockchain.
    """
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    try:
        data = rpc.command(method="getbestblockhash")
        # return BestBlockhash(best_blockhash=data)
        return data
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=418, detail="Something went wrong")


@app.get("/api/blockchain/getblock/{hashval}")
async def get_block(hashval):
    """
    Returns an Object with information about block <hash>.
    Always in "verbose" mode.
    """
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    try:
        print(hashval)
        data = rpc.command("getblock", params=[hashval])
        return data
    except:
        raise HTTPException(status_code=418, detail="Something went wrong")


@app.get("/api/blockchain/getblockchaininfo")
def get_blockchain_info():
    """
    Returns an object containing various state info regarding blockchain processing.
    """
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("getblockcount")
        return data
    except Exception as e:
        # raise UnicornException(name="getbestblockhash")
        # print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")


@app.get("/api/blockchain/getblockhash/{height}")
async def get_blockhash(height):
    """
    Returns hash of block in best-block-chain at height provided.
    """
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        # print (height)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    # data = {}
    try:
        data = rpc.command("getblockheader", params=[hashval])
        return data
    except Exception as e:
        print(e)
        raise HTTPException(status_code=418, detail="Something went wrong")


@app.get("/api/blockchain/getchaintips")
def get_chaintips():
    """
    Return information about all known tips in the block tree, including the main chain as well as orphaned branches.
    """
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("gettxout", params=[txid, n])
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")

# gettxoutproof
# gettxoutsetinfo
# preciousblock "blockhash"
# pruneblockchain
# verifychain ( checklevel nblocks )
# verifytxoutproof "proof"

# CONTROL


@app.get("/api/blockchain/getinfo")
def get_info():
    """
    DEPRECATED. Returns an object containing various state info.
    """
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    print(command)
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
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("getnettotals")
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")


# == Rawtransactions ==
# createrawtransaction [{"txid":"id","vout":n},...] {"address":amount,"data":"hex",...} ( locktime )
# fundrawtransaction "hexstring" ( options )
# getrawtransaction "txid" ( verbose )
# sendrawtransaction "hexstring" ( allowhighfees )
# signrawtransaction "hexstring" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )


@app.get("/api/rawtransactions/decoderawtransaction/{hexstring}")
async def decode_rawtransaction(hexstring):
    """"
    Returns an Object with information about blockheader <hash>.
    """
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("decoderawtransaction", params=[hexstring])
        return data
    except Exception as e:
        # raise UnicornException(name="getbestblockhash")
        print(e)
        raise HTTPException(status_code=418, detail="Something went wrong")


@app.get("/api/rawtransactions/decodescript/{hexstring}")
async def decode_script(hexstring):
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("decodescript", params=[hexstring])
        return data
    except Exception as e:
        # raise UnicornException(name="getbestblockhash")
        print(e)
        raise HTTPException(status_code=418, detail="Something went wrong")


@app.get("/api/rawtransactions/getrawtransaction/{txid}")
async def get_rawtransaction(txid):
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("getrawtransaction", params=[txid, True])
        return data
    except Exception as e:
        # raise UnicornException(name="getbestblockhash")
        print(e)
        raise HTTPException(status_code=418, detail="Something went wrong")


@app.get("/api/rawtransactions/sendrawtransaction/{hexstring}")
async def send_rawtransaction(hexstring):
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("sendrawtransaction", params=[hexstring])
        return data
    except Exception as e:
        # raise UnicornException(name="getbestblockhash")
        print(e)
        raise HTTPException(status_code=418, detail="Something went wrong")


# UTIL
@app.get("/api/rawtransactions/validateaddress/{address}")
async def validate_address(address):
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("validateaddress", params=[address])
        return data
    except Exception as e:
        # raise UnicornException(name="getbestblockhash")
        print(e)
        raise HTTPException(status_code=418, detail="Something went wrong")


@app.post("/api/rawtransactions/verifymessage")
def verify_message(verifyMessage: Verifymessage):
    """
    Verify a signed message.
    1. "address"         (string, required) The dogecoin address to use for the signature.
    2. "signature"       (string, required) The signature provided by the signer in base 64 encoding (see signmessage).
    3. "message"         (string, required) The message that was signed.

    Example:
     curl -X 'POST' \
        'https://easypeasy.eastus.cloudapp.azure.com/api/rawtransactions/verifymessage' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
            "address": "D6sFXiE9gobpPfSSjEWZcMXT8LADLigMn9",
            "signature": "HzdtnvCQFAY3SijChINYs4aWNBxVW4Fm+41BJisBBkDod+cbW21MxQ5nl8gAxWoGM1EUAL2wg2xB0LpLBx7+ELA=",
            "message": "To the moon (:"
        }'
    """
    rpc = RPC_Connection(
        config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    data = {}
    try:
        data = rpc.command("verifymessage", params=[
                           verifyMessage.address, verifyMessage.signature, verifyMessage.message])
        return data
    except Exception as e:
        raise HTTPException(status_code=418, detail="Something went wrong")


"""
@app.get("/api/test")
def read_root():
    rpc = RPC_Connection(config.RPC_USER, config.RPC_PASSWORD, config.RPC_HOST, config.RPC_PORT)
    try:
        data = rpc.command("getbestblockhash")
        return data
    except:
        #raise UnicornException(name="getbestblockhash")
        raise HTTPException(status_code=418, detail="Something went wrong")
"""

if __name__ == "__main__":
    uvicorn.run(  # type: ignore
        "main:app",
        host=config.HOST,
        log_level=config.LOG_LEVEL,
        port=config.PORT,
        reload=True if config.ENV == "DEV" else False,
        ssl_keyfile=config.SSL_KEYFILE,
        ssl_certfile=config.SSL_CERTFILE
    )
