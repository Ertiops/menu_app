from sqlalchemy import Column, Integer, String, ForeignKey
from config import Base


class Menu(Base):
	__tablename__ = "menu"

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	description = Column(String(250), nullable=False)


class Submenu(Base):
	__tablename__ = "submenus"

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	description = Column(String(250), nullable=False)
	menus_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE"))

class Dishes(Base):
	__tablename__ = "dishes"
	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	description = Column(String(250), nullable=False)
	submenu_id = Column(Integer, ForeignKey("submenus.id", ondelete="CASCADE"))

