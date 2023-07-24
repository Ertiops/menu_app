from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import MenuSchema, RequestMenu, Response
import crud

router = APIRouter()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@router.post('/create')
async def create(request:RequestMenu, db:Session=Depends(get_db())):
	crud.create_menu(db, menu = request.parameter)
	return Response(code=200, status="Ok", message="Menu created successfully").dict(exclude_none=True)

@router.get("/")
async def get(db:Session=Depends(get_db)):
	crud.get_menu(db, 0, 100)
	return Response(code=200, status="ok", message="Success Fetch all data", result=_menu).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id:int, db:Session = Depends(get_db)):
	_menu = crud.get_menu(db, id)
	return Response(code=200, status="Ok", message="Success get data", result =_menu).dict(exclude_none=True)

@router.post("/update")
async def update_menu(request: RequestMenu, db:Session = Depends(get_db)):
	_menu = crud.update_menu(db, menu_id=request.parameter.id, title=request.parameter.title, description=request.parameter.description)
	return Response(code=200, status="Ok", message="Success update data", result=_menu).dict(exclude_none=True)

@router.delete("/{id}")
async def delete(id:int, db:Session = Depends(get_db)):
	crud.remove_menu(db, menu_id=id)
	return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)
