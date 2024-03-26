# from sqlalchemy import Float, Column, ForeignKey, String, Integer, DateTime
# from sqlalchemy.orm import relationship
#
# from src.db.tables import BallMachineUsage
# from src.db.database import Base

#
#
# class BallMachineUsage(Base):
#     __tablename__ = "BallMachineUsage"
#     id = Column(name="Id", type=Integer, primary_key=True, index=True)
#     usage_date = Column(name="UsageDate", type=DateTime, nullable=False, unique=False)
#     usage_hours = Column(name="UsageHours", type=Float, nullable=False)
#     deleted = Column(name="Deleted", type=Integer, nullable=False, default="0")


# class Security(Base):
#     __tablename__ = "securities"
#     id = Column(String, primary_key=True, index=True)
#     symbol = Column(String, unique=False)
#     long_name = Column(String, unique=False)
#     options = relationship("Option", back_populates="security")
#     marketdata = relationship("MarketData", back_populates="security")
#
#
# class MarketData(Base):
#     __tablename__ = "marketdata"
#     id = Column(String, primary_key=True, index=True)
#     date = Column(String)
#     price = Column(Float)
#     security_id = Column(String, ForeignKey("securities.id"), nullable=True)
#     security = relationship("Security", back_populates="marketdata", uselist=False)

