from win10toast import ToastNotifier
from tkinter import *
import time

toast = ToastNotifier()
root = Tk()

# main window
root.title("Drink Water Reminder")
root.geometry("340x380")
root.config(background="#454545")

is_on = True

# widget management
class Util:
    def create_button(window) -> Button:
        return Button(window)

# main app
def main() -> None:
    pass

# reminder controls
def reminder() -> None:
    print("Timer initiated.")
    time.sleep(1800) # delay before each notification
    print("Timer completed.")
    
    print("Message printed.")
    toast.show_toast(
        title="Hydrate!",
        msg="Drink water, please.",
        duration = 15,
    )
    print("Message deleted.")
    
    # calls itself if enabled
    if is_on:
        reminder()

if __name__ == "__main__":
    root.mainloop()