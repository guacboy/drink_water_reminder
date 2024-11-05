from win10toast import ToastNotifier
import time

toast = ToastNotifier()

def reminder() -> None:
    print("Timer initiated.")
    time.sleep(5) # every 30 minutes
    print("Timer completed.")
    
    print("Message printed.")
    toast.show_toast(
        title="Hydrate!",
        msg="Drink water, please.",
        duration = 10,
    )
    print("Message deleted.")

if __name__ == "__main__":
    reminder()