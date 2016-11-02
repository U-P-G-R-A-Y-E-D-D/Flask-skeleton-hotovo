from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Date

from ..database import db
from ..mixins import CRUDModel


class PapirDB(CRUDModel):
    __tablename__ = 'papir'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    DruhPapiru = Column(String, nullable=False, index=True)
    Cena = Column(String, nullable=False, index=True)

