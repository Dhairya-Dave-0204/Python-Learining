from sqlalchemy import Column, Integer, Boolean, String, ForeignKey

from src.utils.db import Base

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable= False)
    description = Column(String)
    is_complete = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))