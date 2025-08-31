from pydantic import BaseModel, Field, PositiveInt

# Achivement model schemas

class AchivementBase(BaseModel):
    """
    Achivement class for creating the achivement obj

    Args:
        BaseModel (_type_): _Pydantic BaseModel_
    """
    
    name: str = Field(..., description="Name of the badge")
    description: str = Field(..., description="description of the badge")
    days_required: PositiveInt = Field(..., description="days required to unlock the badge")
    
    
class AchivementResponse(BaseModel):
    """
    Achivement response class for returning the achivement obj

    Args:
        BaseModel (_type_): _Pydantic BaseModel_
    """
    
    achivenet_id: PositiveInt
    name: str
    description: str
    days_required: PositiveInt

    model_config = {"from_attributes": True}