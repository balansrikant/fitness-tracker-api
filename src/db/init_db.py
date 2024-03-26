# import logging
# from sqlalchemy.orm import Session
#
# # from src import schemas
# # from src.routes import crud
# from src.utilities.ball_machine.ball_machine import BallMachine
# # from initial_data import SECURITIES, OPTIONS, MARKET_DATA
#
# logger = logging.getLogger(__name__)
#
#
# def init_db(db: Session) -> None:
#     logger.info("adding current ball machine usages ...")
#     ball_machine = BallMachine()
#     usages = ball_machine.get_entries()
#     db_usages = ball_machine.get_usages()
#
#     securities = crud.get_securities(db=db)
#     if not securities:
#         for security in SECURITIES:
#             security_in = schemas.SecurityCreate(
#                 symbol=security["symbol"],
#                 long_name=security["long_name"]
#             )
#             crud.create_security(db=db, security=security_in)
