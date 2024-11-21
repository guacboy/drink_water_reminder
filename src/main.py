from win10toast import ToastNotifier
from tkinter import *
import threading

toast = ToastNotifier()
root = Tk()

# main window
root.title("Drink Water Reminder")
root.geometry("340x380")
root.config(background="#454545")

count_in_minutes = 20
reset_minutes = count_in_minutes
count_in_seconds = 0
reset_seconds = 59
is_on = False

# widget management
class Util:
    def create_label(window) -> Label:
        return Label(window,
                     bg="#454545",
                     fg="#e9e9e9",
                     font=("Roboto", 20, "bold"),
                     bd=0)
    
    def create_button(window) -> Button:
        return Button(window,
                      bg="#707070",
                      fg="#e9e9e9",
                      font=("Roboto", 24, "bold"),
                      bd=0)

# main app
class App:
    def main() -> bool:
        global current_status
        global start_button
        global timer_label
        
        title_label = Util.create_label(root)
        title_label.config(text="Drink Water Reminder")
        title_label.pack(side=TOP,
                         pady=20)
        
        status_label = Util.create_label(root)
        status_label.config(text="STATUS:")
        status_label.pack(side=TOP)
        
        current_status = Util.create_label(root)
        current_status.pack(side=TOP)
        
        timer_label = Util.create_label(root)
        timer_label.config(text="20:00")
        timer_label.pack(side=TOP,
                         pady=50)
        
        start_button = Util.create_button(root)
        start_button.pack(side=BOTTOM,
                          pady=20)
        
        App.update(False)
    
    # updates the text display
    def update(status) -> None:
        global is_on

        is_on = status
        
        if is_on:
            current_status.config(text="ON",
                                  fg="#07fe3b")
            start_button.config(text="STOP",
                                command=lambda: App.update(False))
        else:
            current_status.config(text="OFF",
                                  fg="#fa0001")
            start_button.config(text="START",
                                command=lambda: [App.update(True), App.timer(count_in_minutes,
                                                                             count_in_seconds)])

    # 20 mins delay before each notification
    def timer(count_in_minutes: int,
              count_in_seconds: int) -> None:
        if is_on:
            # if count_in_seconds == 60:
            #     timer_label.config(text=f"{count_in_minutes:02}:00")
            # else:
            timer_label.config(text=f"{count_in_minutes:02}:{count_in_seconds:02}")
            
            
            if count_in_minutes > 0 and count_in_seconds == 0: # counts down minute and resets seconds
                root.after(1000, App.timer, count_in_minutes - 1, reset_seconds)
            elif count_in_minutes == 0 and count_in_seconds == 0: # plays reminder and resets timer
                threading.Thread(target=App.reminder, daemon=True).start()
                root.after(1000, App.timer, reset_minutes, reset_seconds)
            elif count_in_minutes >= 0: # counts down second
                root.after(1000, App.timer, count_in_minutes, count_in_seconds - 1)
    
    # reminder controls
    def reminder() -> None:
        print("Message printed.")
        toast.show_toast(
            title="Hydrate!",
            msg="Drink water, please.",
            duration = 10,
        )
        print("Message deleted.")

if __name__ == "__main__":
    App.main()
    root.mainloop()