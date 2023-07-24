from sqlalchemy.orm import Session
from model import Menu, Submenu, Dishes
from schemas import MenuSchema, SubMenuSchema, DishesSchema


# Get all menu data
def get_menu(db:Session, skip:int=0, limit:int=100):
	return db.query(Menu).offset(skip).limit(limit).all()

# Get by ud menu data
def get_menu_by_id(db:Session, menu_id: int):
	return db.query(Menu).filter(Menu.id == menu_id).first()

# Create menu data
def create_menu(db:Session, menu: MenuSchema):
	_menu = Menu(title=menu.title, description=menu.description)
	db.add(_menu)
	db.commit()
	db.refresh(_menu)
	return _menu

# Remove menu data
def remove_menu(db:Session, menu_id:int):
	_menu = get_menu_by_id(db=db, menu_id=menu_id)
	db.delete(_menu)
	db.commit()

# Update menu data
def update_menu(db:Session, menu_id:int, title:str, description:str):
	_menu = get_menu_by_id(db=db, menu_id=menu_id)
	_menu.title = title
	_menu.description = description
	db.commit()
	db.refresh(_menu)
	return _menu