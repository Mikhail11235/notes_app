from datetime import datetime
from db.base_class import Base
from sqlalchemy import Column, Integer, Text, DateTime
# from sqlalchemy.orm import relationship


class Note(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
