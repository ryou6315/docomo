from asyncio.windows_events import NULL
import json
with open("E:\\okta.json") as JsonFile:
    #data=json.load(JsonFile)
    data={
    "code": 0,
    "msg": "ok",
    "data": {
        "list": [
            {
                "stock_id0": "601318.SH",
                "stock_code0": "601318",
                "stock_name0": "中国平安",
            },{
                "stock_id1": "600000.SH",
                "stock_code1": "600000",
                "stock_name1": "浦发银行",
            }
        ]
    },
     "profile":{
                "stock_id2": "600000.SH",
                "stock_code2": "600000",
                "stock_name211": "浦发银行",
            },
    "call_stack": ""
}



def getNodeValues(jsonData,keysVaule):
    for x in jsonData:
        print("x--------:"+x)
        if x=="profile":
            for y in jsonData[x]:
                if y==keysVaule:
                    print("stock_code2-----:"+data[x][y])
                    return data[x][y]
            return ""
if getNodeValues(data,"stock_name2"):
    print("test-vaule---:"+getNodeValues(data,"stock_name2"))
else:
    print("null---------:")