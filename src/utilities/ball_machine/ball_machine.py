import csv

from pathlib import Path
from sqlalchemy.orm import Session

from src import DATA_FOLDER, BALL_MACHINE_USAGE_FILE
from src.db import BallMachineUsage
from src.schemas.ball_machine_usage import BallMachineUsageCreate


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
        return result

    # def add_entry(self):
    #     _file_name = self._file_name
    #     with open(_file_name) as csv_file:
    #         csv_reader = csv.DictReader(csv_file, delimiter=',')

    def add_usage(self, ball_machine_usage: BallMachineUsageCreate):
        usage_in = BallMachineUsage(
            usage_date=ball_machine_usage.usage_date,
            usage_hours=ball_machine_usage.usage_hours
        )
        self._db.add(usage_in)
        self._db.commit()
        self._db.refresh(usage_in)

    # def add_ball_machine_usage(db: Session, security: SecurityCreate):
    #     """ Create new security entry in db """
    #     unique_id = str(uuid4())
    #     security_in = models.Security(id=unique_id, symbol=security.symbol, long_name=security.long_name)
    #     db.add(security_in)
    #     db.commit()
    #     db.refresh(security_in)
    #     return security_in
