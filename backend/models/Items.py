from models import MongoModel, ObjectId, Field

class ItemModel(MongoModel):
    name: str = Field(..., title="Name of the item")
    description: str = Field(..., title="Description of the item")
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Item 1",
                "description:": "This is an item"
            }
        }