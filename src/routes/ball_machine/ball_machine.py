import logging

from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from datetime import datetime

# from src.routes import crud
from src.schemas.ball_machine_usage import BallMachineUsageResult, BallMachineUsageCreate
from src.utilities.ball_machine.ball_machine import BallMachine
from src import deps

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/ball-machine-usages/", status_code=201)
def create_ball_machine_usage(
        ball_machine_usage: BallMachineUsageCreate,
        db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a single ball machine usage
    """
    ball_machine = BallMachine(db=db)
    usage_dict = {
        "usage_date": datetime.strftime(ball_machine_usage.usage_date, "%Y-%m-%d"),
        "usage_hours": ball_machine_usage.usage_hours
    }
    logger.info(f"usage: {usage_dict}")
    result = ball_machine.add_usage(ball_machine_usage=ball_machine_usage)
    logger.info(result)
    if result:
        return usage_dict
    else:
        raise HTTPException(
            status_code=400, detail="Bad request"
        )
    # return ball_machine_usage.__dict__


@router.get("/ball-machine-usages/", status_code=200)
def get_ball_machine_usages(db: Session = Depends(deps.get_db)) -> dict:
    """
    Return all ball machine usages
    """

    ball_machine = BallMachine(db=db)
    result = ball_machine.get_usages()

    if result:
        return result
    else:
        raise HTTPException(
            status_code=400, detail="Bad request"
        )
