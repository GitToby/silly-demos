# https://github.com/ajalt/fuckitpy

from typing import Dict

# import fuckit as fuckit
import uvicorn
from fastapi import FastAPI

import internal

# fuckit(fuckit('internal'))

app = FastAPI()


@app.get("/hello")
def hello(name: str = 'world'):
    return f'hello {name}'


@app.put("/book")
def place_booking(name: str, location: str) -> Dict[str, bool]:
    internal.book_location(location, name)
    return {'success': True}


@app.get("/bookings/{my_name}")
def get_me_my_booked_locations(my_name: str) -> internal.Set[str]:
    return internal.get_locations(my_name)


if __name__ == '__main__':
    uvicorn.run(app, port=8080)
