from fastapi import FastAPI
from pydantic import BaseModel
import json
import compile

class Item(BaseModel):
    source: str
    lang: str
    id: int
    

app = FastAPI()

@app.post("/compile/")
async def create_item(item: Item):
    op = compile.run(item.source,item.lang,item.id)
    op = op.replace("\n","<br />").replace("\t","&nbsp;&nbsp;&nbsp;&nbsp;")  

    # print(op)
    data={
      'msg': op
    }
    data=json.dumps(data)
    return data

     