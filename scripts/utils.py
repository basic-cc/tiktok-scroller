import datetime

def log_event(filename, event, extra=""):
    with open(filename, "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"{timestamp}, {event}, {extra}\n")
