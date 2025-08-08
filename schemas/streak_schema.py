from pydantic import BaseModel, Field, PositiveInt, PastDatetime
from typing import Optional


class StreakBase(BaseModel):
    """
    Base model for streaks, used for creating and updating streaks.
    """

    user_id: PositiveInt = Field(..., description="ID of the user associated with the streak")
    start_date: PastDatetime = Field(..., description="Start date of the streak")
    end_date: Optional[PastDatetime] = Field(None, description="End date of the streak, if applicable")
    relapsed: bool = Field(False, description="Indicates if the user has relapsed during the streak")
    
    

class StreakResponse(StreakBase):
    """
    Response model for streaks, includes the streak ID.
    """

    streak_id: PositiveInt = Field(..., description="Unique identifier for the streak")
    user_id: PositiveInt
    start_date: PastDatetime
    end_date: Optional[PastDatetime] = None
    relapsed: bool = False

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "streak_id": 1,
                "user_id": 123,
                "start_date": "01-01T00:00:00Z",
                "end_date": None,
                "relapsed": False
            }
        }