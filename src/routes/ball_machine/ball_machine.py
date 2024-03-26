from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

# from src.routes import crud
from src.schemas.ball_machine_usage import BallMachineUsageResult
# from src import deps

router = APIRouter()


# @router.get("/{option_id}", status_code=200, response_model=OptionResult)
# def get_option_by_id(*, option_id: str, db: Session = Depends(deps.get_db)) -> dict:
#     """
#     Fetch a single option by ID
#     """
#     result = crud.get_option_by_id(db=db, option_id=option_id)
#     if result:
#         return result
#     else:
#         raise HTTPException(
#             status_code=404, detail=f"Option with ID {option_id} not found"
#         )
