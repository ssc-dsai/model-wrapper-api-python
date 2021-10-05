from helpers.blueprint import ModelBlueprint
from pydantic import BaseModel
from typing import List

# Types example
class Record(BaseModel):
    description: str
    ci: str

class Records(BaseModel):
    data: List[Record]


class Model(ModelBlueprint):
    model = None

    def init(self):
        pass

    def run(self, records: Records):
        pass