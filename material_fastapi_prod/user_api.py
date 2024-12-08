from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import user_models, user_schemas, user_crud
from user_models import SessionLocal

app = FastAPI()

# Dependency für die Datenbank-Sitzung
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Benutzer erstellen
@app.post("/users/", response_model=user_schemas.UserResponse)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    # Prüfen, ob Benutzer mit dieser E-Mail existiert
    db_user = db.query(user_models.User).filter(user_models.User.Email == user.Email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db, user)

# Alle Benutzer abrufen
@app.get("/users/", response_model=list[user_schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    data = user_crud.get_users(db, skip=skip, limit=limit)
    return data

# Benutzer nach ID abrufen
@app.get("/users/{user_id}", response_model=user_schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)