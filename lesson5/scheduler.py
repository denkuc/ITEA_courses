from apscheduler.schedulers.background import BackgroundScheduler

schedule = BackgroundScheduler()


def some_job():
    print("Every 10 seconds")


schedule.add_job(some_job, 'interval', seconds=1)
schedule.start()

while True:
    pass
