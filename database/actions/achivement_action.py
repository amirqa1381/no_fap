from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from database.models.achivement_model import Achievement, UserAchievement
from schemas.achivement_schema import AchivementBase, AchivementResponse
from database.models.user_model import User
from database.models.achivement_model import Achievement
from datetime import datetime


# Achivement model actions


def create_achievement(db: Session, request: AchivementBase) -> AchivementResponse:
    """
    create a new achivement in the database

    Args:
        db (Session): db session
        request (AchivementBase): achivement request body

    Returns:
        AchivementResponse: _description_
    """
    new_achivement = Achievement(
        name=request.name,
        description=request.description,
        days_required=request.days_required,
    )

    db.add(new_achivement)
    db.commit()
    db.refresh(new_achivement)

    # returning the achivement response
    return AchivementResponse(
        achivenet_id=new_achivement.achivenet_id,
        name=new_achivement.name,
        description=new_achivement.description,
        days_required=new_achivement.days_required,
    )
