from sanic import Sanic, json
from sanic.response import text

app = Sanic("SimpleAPI")
rows = []
HOST = "localhost"
PORT = 8000

@app.get("/getrows")
async def get_rows(request):
    return json(rows)

@app.post("/addrow")
async def add_row(request):
    # get json data
    json_data = request.json
    rows.append(json_data["row"])
    return text("Added row")

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)