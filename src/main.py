from win10toast import ToastNotifier
from tkinter import *
import time

toast = ToastNotifier()
root = Tk()

# main window
root.title("Drink Water Reminder")
root.geometry("340x380")
root.config(background="#454545")

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
    def main() -> None:
        title_label = Util.create_label(root)
        title_label.config(text="Drink Water Reminder")
        title_label.pack(side=TOP,
                         pady=20)
        
        status_label = Util.create_label(root)
        status_label.config(text="STATUS:")
        status_label.pack(side=TOP)
        
        current_status = Util.create_label(root)
        App.update_status(current_status,
                          is_on)
        current_status.pack(side=TOP)
        
        start_button = Util.create_button(root)
        start_button.config(text="START",
                            command=lambda: App.update_status(current_status,
                                                              True))
        start_button.pack(side=BOTTOM,
                          pady=20)
        
    def update_status(current_status,
                      status) -> BooleanVar:
        is_on = status
        
        if is_on:
            current_status.config(text="ON",
                                  fg="#07fe3b")
        else:
            current_status.config(text="OFF",
                                  fg="#fa0001")
        
        return is_on

    # reminder controls
    def reminder() -> None:
        print("Timer initiated.")
        time.sleep(1200) # 20 mins delay before each notification
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
            App.reminder()

if __name__ == "__main__":
    App.main()
    root.mainloop()