import logging

from sqlalchemy.orm import Session

# from src import schemas
# from src.routes import crud
# from src.db.init_db import init_db
from src.db.database import SessionLocal, engine
from src.db import models, Base
from src.utilities.ball_machine.ball_machine import BallMachine
from src.schemas.ball_machine_usage import BallMachineUsageCreate
# from initial_data import SECURITIES, OPTIONS, MARKET_DATA

logger = logging.getLogger(__name__)


def init() -> None:
    logger.info("...creating db")
    # models.Base.metadata.create_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def add_initial_data() -> None:
    logger.info("...adding initial data")
    db = SessionLocal()

    logger.info("adding current ball machine usages ...")
    ball_machine = BallMachine(db)
    usages = ball_machine.get_entries_from_file()
    db_usages = ball_machine.get_usages()
    if not db_usages:
        for usage in usages:
            usage_in = BallMachineUsageCreate(
                usage_date=f'{usage["usage_date"]} 00:00:00',
                usage_hours=usage["usage_hours"]
            )
            ball_machine.add_usage(usage_in)

    # securities = crud.get_securities(db=db)
    # if not securities:
    #     for security in SECURITIES:
    #         security_in = schemas.SecurityCreate(
    #             symbol=security["symbol"],
    #             long_name=security["long_name"]
    #         )
    #         crud.create_security(db=db, security=security_in)


def main() -> None:
    logger.info("initializing db ...")
    init()

    logger.info("adding initial data ...")
    add_initial_data()

    logger.info("...initialization complete")


if __name__ == "__main__":
    main()
