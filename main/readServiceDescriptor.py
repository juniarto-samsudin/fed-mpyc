datas = [ "data1", "data2", "data3" ]
opType = "col"
operands = [ "covid.col1" ]
computation = {
    "left": "covid.col1",
    "op": "sum",
    "right": None
}

""" for o in operands:
    t = o.split(".")[0]
    col = o.split(".")[1]
    for d in datas:
        dt = db.queryData(name=d)["type"]
        if dt == t:
            col_vals = db.queryDataCol(name=d, col=col)
            if o not in all_cols:
                all_cols[o] = []
            all_cols[o].extends(col_vals) """

all_cols = {}
for o in operands: # o = covid.col1
    t = o.split(".")[0] # covid
    col = o.split(".")[1] # col1
    for d in datas:
        dt = db.queryData(name=d)["type"]
        if dt == t: # if dt == covid
            col_vals = db.queryDataCol(name=d, col=col)
            if o not in all_cols:
                all_cols[o] = []
            all_cols[o].extend(col_vals)

# compute
if opType == "col":
   if computation["left"] in all_cols:
       secret_data = all_cols[computation["left"]]
   else:
       secret_data = db.queryDataCol(...)
 
    if computation["op"] == "sum":
        result = mpc.sum(secret_data)
    elif computation["op"] == "avg":
        result = mpc.avg(secret_data)