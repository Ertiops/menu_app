from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey


metadata = MetaData()

menus = Table(
	"menus",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("title", String(100), nullable=False),
	Column("description", String(250),nullable=False),
)

submenus = Table(
	"submenus",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("title", String(100), nullable=False),
	Column("description", String(250),nullable=False),
	Column("menus_id", Integer, ForeignKey("menus.id", ondelete="CASCADE")),
)

dishes = Table(
	"dishes",
	metadata,
	Column("id", Integer, ForeignKey("submenus.id", ondelete="CASCADE")),
	Column("title", String(100), nullable=False),
	Column("description", String(250),nullable=False),
)
