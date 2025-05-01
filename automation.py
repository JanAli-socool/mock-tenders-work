# # run_daily.py
import schedule
import time
from extract_tender import extract_fields_from_tender

def process_new_tenders():
     # simulate reprocessing from folder
     pass  # extend as needed
 schedule.every().day.at("01:00").do(process_new_tenders)

while True:
     schedule.run_pending()
     time.sleep(60)
