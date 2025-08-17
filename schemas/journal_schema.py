from pydantic import BaseModel, Field, PositiveInt, PastDatetime
from datetime import datetime
from typing import Optional



class JournalBase(BaseModel):
    """
    Base model for journal entries, used for creating and updating journal entries.
    """

    user_id: PositiveInt = Field(
        ..., description="ID of the user associated with the journal entry"
    )
    entry_date: PastDatetime = Field(..., description="Date of the journal entry")
    content: str = Field(..., description="Content of the journal entry")
    mood_rating: PositiveInt = Field(..., description="rating of the mood between 1 & 10")
    
    
    
    
class JournalResponse(BaseModel):
    """
    This class is for returning the journal base response when user send and want
    to get the response.

    Args:
        BaseModel (__type__): pydantic base model
    """
    journal_id: int 
    user_id: int 
    entry_date: datetime 
    content: str 
    mood_rating: int

    class Config:
        orm_mode = True