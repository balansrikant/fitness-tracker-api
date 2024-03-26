from pydantic import BaseModel
from datetime import datetime
from typing import Sequence


class BallMachineUsageBase(BaseModel):
    usage_date: datetime
    usage_hours: float


class BallMachineUsage(BallMachineUsageBase):
    id: int

    class Config:
        from_attributes = True


class BallMachineUsageCreate(BallMachineUsageBase):
    class Config:
        from_attributes = True


class BallMachineUsageResult(BaseModel):
    items: Sequence[BallMachineUsage]
