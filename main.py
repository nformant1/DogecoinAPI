from fastapi import FastAPI, HTTPException
from fastapi import Request
#from fastapi.responses import HTMLResponse
import uvicorn
from rpc_connection import RPC_Connection

from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from multiprocessing import cpu_count, freeze_support
import time

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

# credentials for dogecoin node
rpcuser = "rpcuser"
rpcpassword = "rpcpassword"
rpcport = 22555

# new connection
rpc = RPC_Connection(rpcuser, rpcpassword, "127.0.0.1",rpcport)


app = FastAPI()

"""@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
"""

app.mount('/web', StaticFiles(directory='static',html=True))

@app.get("/api/blockchain/getbestblockhash")
def read_root():
    data = {}
    try:
        data = rpc.command("getbestblockhash")
        return data
    except:
        #raise UnicornException(name="getbestblockhash")
        raise HTTPException(status_code=418, detail="Something went wrong")
    

@app.get("/api/blockchain/getblock")
def read_root():
    return {1337: "Such no, very missing"}

@app.get("/api/blockchain/getblockchaininfo")
def read_root():
    data = {}
    try:
        data = rpc.command("getblockchaininfo")
        return data
    except:
        #raise UnicornException(name="getbestblockhash")
        raise HTTPException(status_code=418, detail="Something went wrong")

@app.get("/api/blockchain/getblockcount")
def read_root():
    data = {}
    try:
        data = rpc.command("getblockcount")
        return data
    except Exception as e:
        #raise UnicornException(name="getbestblockhash")
        print (e)
        raise HTTPException(status_code=418, detail="Something went wrong")


"""@app.get("/api/blockchain/getblockhash/{hashval}")
async def read_item(hashval):
    data = {}
    try:
        print (hashval)
        data = rpc.command("getblockhash", params=[hashval])
        print (data)
        #data = {"what": "is going on"}
    except:
        raise UnicornException(name="getblockhash")
        data = {"unicorn_name": name}
    return data
"""

@app.get("/api/test")
def read_root():
    try:
        data = rpc.command("getbestblockhash")
        return data
    except:
        #raise UnicornException(name="getbestblockhash")
        raise HTTPException(status_code=418, detail="Something went wrong")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="debug", reload=True)
    #freeze_support()
    #uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=False,workers=4,loop="asyncio",)
