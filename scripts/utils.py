import datetime

def log_event(filename, event):
    with open(filename, "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"{timestamp}, {event}\n")
