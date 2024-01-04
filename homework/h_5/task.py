from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trading App"
)


class Stock(BaseModel):
    id: int
    name: str = Field(max_length=10)
    price: float = Field(ge=0)
    quantity: int = Field(ge=0)


class Stock_new(BaseModel):
    name: str = Field(max_length=10)
    price: float = Field(ge=0)
    quantity: int = Field(ge=0)


stocks: list[Stock] = []


@app.get("/action", response_model=list[Stock])
async def get_all_stocks():
    return stocks


@app.get("/action/{stock_id}", response_model=Stock)
async def get_stock(stock_id: int):
    filtered_stock = [stock for stock in stocks if stock.id == stock_id]
    if filtered_stock is None:
        return {"message": "No stocks found"}
    stock = filtered_stock[0]
    return stock


@app.post("/action")
async def create_stock(stock: Stock):
    stocks.append(stock)
    return {"message": "Stock created successfully"}


@app.put("/action/{stock_id}")
async def update_stock(stock_id: int, updated_stock: Stock_new):
    filtered_stock = [stock for stock in stocks if stock.id == stock_id]
    if filtered_stock is None:
        return {"message": "No stocks found"}
    stock = filtered_stock[0]
    stock.name = updated_stock.name
    stock.price = updated_stock.price
    stock.quantity = updated_stock.quantity
    return {"message": "Stock updated successfully"}


@app.delete("/action/{stock_id}")
async def delete_stock(stock_id: int):
    filtered_stock = [stock for stock in stocks if stock.id == stock_id]
    if filtered_stock is None:
        return {"message": "No stocks found"}
    stock = filtered_stock[0]
    stocks.remove(stock)
    return {"message": "Stock deleted successfully"}
