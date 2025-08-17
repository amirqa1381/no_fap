from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from schemas.journal_schema import JournalBase, JournalResponse, JournalUpdate
from database.db_connection import get_db
from database.actions.journal_action import create_journal, update_journal, get_journal_by_id, get_all_user_journals, delete_journal




router = APIRouter(prefix="/journal", tags=["Journal"])


@router.post("/new", response_model=JournalResponse)
async def create_journal_route(request: JournalBase, db: Session = Depends(get_db)):
    """
    Route to create a new journal entry.

    Args:
        request (JournalBase): Journal entry data.
        db (Session, optional):  Defaults to Depends(get_db).
    """
    return create_journal(db=db, request=request)



@router.put("/update/{journal_id}", response_model=JournalResponse)
async def update_journal_route(journal_id: int, request: JournalUpdate, db: Session = Depends(get_db)):
    """
    Route to update an existing journal entry.

    Args:
        journal_id (int): ID of the journal entry to update.
        request (JournalUpdate): Updated journal entry data.
        db (Session, optional): Database session. Defaults to Depends(get_db).
    """
    return update_journal(db=db, journal_id=journal_id, request=request)



@router.get("/{journal_id}", response_model=JournalResponse)
async def get_journal_by_id_route(journal_id: int, db: Session = Depends(get_db)):
    """
    Route to retrieve a journal entry by its ID.

    Args:
        journal_id (int): ID of the journal entry to retrieve.
        db (Session, optional):  Defaults to Depends(get_db).
    """
    return get_journal_by_id(db=db, journal_id=journal_id)


@router.get("/user/{user_id}", response_model=list[JournalResponse])
async def get_all_user_journals_route(user_id: int, db: Session = Depends(get_db)):
    """
    Route to retrieve all journal entries for a user.

    Args:
        user_id (int): ID of the user whose journal entries to retrieve.
        db (Session, optional):  Defaults to Depends(get_db).
    """
    return get_all_user_journals(db=db, user_id=user_id)


@router.delete("/{journal_id}")
async def delete_journal_route(journal_id: int, db: Session = Depends(get_db)):
    """
    Route to delete a journal entry by its ID.

    Args:
        journal_id (int): ID of the journal entry to delete.
        db (Session, optional):  Defaults to Depends(get_db).
    """
    await delete_journal_route(db=db, journal_id=journal_id)
    return {"message": f"Journal entry {journal_id} deleted successfully"}