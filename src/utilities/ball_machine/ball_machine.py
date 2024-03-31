import csv
import logging

from pathlib import Path
from sqlalchemy.orm import Session
from datetime import datetime

from src import DATA_FOLDER, BALL_MACHINE_USAGE_FILE
from src.db import BallMachineUsage
from src.schemas.ball_machine_usage import BallMachineUsageCreate

logger = logging.getLogger(__name__)


# noinspection PyTypeChecker
class BallMachine:
    def __init__(self, db: Session):
        self._file_name = str(Path.joinpath(Path(DATA_FOLDER), BALL_MACHINE_USAGE_FILE))
        self._db = db

    def get_entries_from_file(self):
        _file_name = self._file_name
        with open(_file_name) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            usage = []
            for row in csv_reader:
                row_dict = dict(row)
                usage_row = {
                    "usage_date": row_dict.get("usage_date"),
                    "usage_hours": row_dict.get("usage_hours")
                }
                usage.append(usage_row)
            return usage

    def get_usages(self):
        result = self._db.query(BallMachineUsage).all()
        results = []
        for row in result:
            new_row = {
                "id": row.id,
                "usage_date": datetime.strftime(row.usage_date, "%Y-%m-%d"),
                "usage_hours": row.usage_hours
            }
            logger.info(f"new row: {new_row}")
            results.append(new_row)
        response = {
            "result": results
        }
        return response

    def add_usage(self, ball_machine_usage: BallMachineUsageCreate) -> bool:
        usage_dict = {
            "usage_date": datetime.strftime(ball_machine_usage.usage_date, "%Y-%m-%d"),
            "usage_hours": ball_machine_usage.usage_hours
        }
        logger.info(f"about to add usage: {usage_dict}")

        usage_in = BallMachineUsage(
            usage_date=ball_machine_usage.usage_date,
            usage_hours=ball_machine_usage.usage_hours
        )

        self._db.add(usage_in)
        self._db.commit()
        self._db.refresh(usage_in)

        return True
