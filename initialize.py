import logging

from src.db.database import SessionLocal, engine
from src.db import Base
from src.utilities.ball_machine.ball_machine import BallMachine
from src.schemas.ball_machine_usage import BallMachineUsageCreate

logger = logging.getLogger(__name__)


def init() -> None:
    logger.info("...creating db")
    Base.metadata.create_all(bind=engine)


def add_initial_data() -> None:
    logger.info("...adding initial data")
    db = SessionLocal()
    db_usages = []

    logger.info("adding current ball machine usages ...")
    ball_machine = BallMachine(db)
    flat_file_usages = ball_machine.get_entries_from_file()
    if flat_file_usages:
        logger.info(f"{len(flat_file_usages)} usages found in file...")

    db_usages_result = ball_machine.get_usages()
    if db_usages_result:
        db_usages = db_usages_result.get("result")

    if not db_usages:
        logger.info("no usages found in db ...")
        for usage in flat_file_usages:
            logger.info("adding entry ...")
            usage_in = BallMachineUsageCreate(
                usage_date=f'{usage["usage_date"]} 00:00:00',
                usage_hours=usage["usage_hours"]
            )
            ball_machine.add_usage(usage_in)
    else:
        logger.info(f"{len(db_usages)} usages found in db ...")


def main() -> None:
    logger.info("initializing db ...")
    init()

    logger.info("adding initial data ...")
    add_initial_data()

    logger.info("...initialization complete")


if __name__ == "__main__":
    main()
