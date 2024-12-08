from sqlalchemy.orm import Session
import user_models, user_schemas


# Benutzer erstellen
def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = user_models.User(Name=user.Name, Email=user.Email, Adresse=user.Adresse, Geburtsdatum=user.Geburtsdatum)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Alle Benutzer abrufen
def get_users(db: Session, skip: int = 0, limit: int = 10):
    data = db.query(user_models.User).offset(skip).limit(limit).all()
    data = [user_schemas.UserResponse(index=user.index, Name=user.Name, Email=user.Email, Adresse=user.Adresse, Geburtsdatum=user.Geburtsdatum) for user in data]
    return data


# Einzelnen Benutzer abrufen
def get_user_by_id(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.index == user_id).first()
