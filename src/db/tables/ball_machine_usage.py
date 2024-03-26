from sqlalchemy import Float, Column, Integer, DateTime
from src.db.database import Base


class BallMachineUsage(Base):
    __tablename__ = "BallMachineUsage"
    id = Column("Id", Integer, primary_key=True, index=True, nullable=False)
    usage_date = Column("UsageDate", DateTime, nullable=False, unique=False)
    usage_hours = Column("UsageHours", Float, nullable=False)
    deleted = Column("Deleted", Integer, nullable=False, default="0")
