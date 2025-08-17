from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas.journal_schema import JournalBase, JournalResponse, JournalUpdate
from database.models.journal_model import Journal




def create_journal(db: Session, request:JournalBase) -> JournalResponse:
    """
    Function to create a new journal entry for a user.
    """
    new_journal = Journal(
        user_id=request.user_id,
        entry_date=request.entry_date,
        content=request.content,
        mood_rating=request.mood_rating,
    )

    db.add(new_journal)
    db.commit()
    db.refresh(new_journal)

    return JournalResponse(
        journal_id=new_journal.journal_id,
        user_id=new_journal.user_id,
        entry_date=new_journal.entry_date,
        content=new_journal.content,
        mood_rating=new_journal.mood_rating,
    )
    


def update_journal(db: Session, journal_id: int, request: JournalUpdate) -> JournalResponse:
    """
    Function to update an existing journal entry.

    Args:
        db (Session): Database session.
        journal_id (int): ID of the journal entry to update.
        request (JournalBase): Updated journal entry data.

    Returns:
        JournalResponse: Response model containing the updated journal entry details.
    """
    journal = db.query(Journal).filter(Journal.journal_id == journal_id).first()
    if not journal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Journal entry not found"
        )

    journal.content = request.content if request.content else journal.content
    journal.mood_rating = request.mood_rating if request.mood_rating else journal.mood_rating

    db.commit()
    db.refresh(journal)

    return JournalResponse(
        journal_id=journal.journal_id,
        user_id=journal.user_id,
        entry_date=journal.entry_date,
        content=journal.content,
        mood_rating=journal.mood_rating,
    )




def get_journal_by_id(db: Session, journal_id: int) -> JournalResponse:
    """
    Function to retrieve a journal entry by its ID.
    Args:
        db (Session): Database session.
        journal_id (int): ID of the journal entry to retrieve.

    Returns:
        JournalResponse: Response model containing the journal entry details.
    """
    journal = db.query(Journal).filter(Journal.journal_id == journal_id).first()
    if not journal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Journal entry not found"
        )

    return JournalResponse(
        journal_id=journal.journal_id,
        user_id=journal.user_id,
        entry_date=journal.entry_date,
        content=journal.content,
        mood_rating=journal.mood_rating,
    )
    


def get_all_user_journals(db: Session, user_id: int) -> list[JournalResponse]:
    """
    Function to retrieve all journal entries for a user.

    Args:
        db (Session): Database session.
        user_id (int): ID of the user whose journal entries are to be retrieved.

    Returns:
        list[JournalResponse]: List of journal entries for the user.
    """
    journals = db.query(Journal).filter(Journal.user_id == user_id).all()
    return [JournalResponse(
        journal_id=journal.journal_id,
        user_id=journal.user_id,
        entry_date=journal.entry_date,
        content=journal.content,
        mood_rating=journal.mood_rating,
    ) for journal in journals]


def delete_journal(db: Session, journal_id: int) -> None:
    """
    Function to delete a journal entry by its ID.

    Args:
        db (Session): Database session.
        journal_id (int): ID of the journal entry to delete.
    """
    journal = db.query(Journal).filter(Journal.journal_id == journal_id).first()
    if not journal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Journal entry not found"
        )

    db.delete(journal)
    db.commit()