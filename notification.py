import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Reminder",
            message="This is your periodic notification.",
            app_name="Notifier",
            timeout=15
            
        )
        time.sleep(20*60*60)  # Wait for 1 hour before sending the next notification