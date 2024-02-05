import schedule
import time
import subprocess


pipeline_run_count = 0

def run_pipeline():
    global pipeline_run_count
    if pipeline_run_count < 5:
        subprocess.run(["python", "./pipeline.py"])
        pipeline_run_count += 1
    else:
        
        schedule.clear()

schedule.every(10).seconds.do(run_pipeline)

while pipeline_run_count < 1:
    schedule.run_pending()
    time.sleep(1)
