import tkinter as tk
import threading

def background_task(stop_event):
    while not stop_event.is_set():
        # Perform your background task here
        print("Background task running")

def start_background_task():
    global stop_event
    stop_event = threading.Event()  # Create a threading Event object

    # Create and start a new thread for the background task
    thread = threading.Thread(target=background_task, args=(stop_event,))
    thread.daemon = True  # Set the thread as a daemon so it terminates when the main thread exits
    thread.start()

def stop_background_task():
    stop_event.set()  # Set the threading Event to signal the thread to stop

# Create the Tkinter app
root = tk.Tk()

# Create a button to start the background task
start_button = tk.Button(root, text="Start Background Task", command=start_background_task)
start_button.pack()

# Create a button to stop the background task
stop_button = tk.Button(root, text="Stop Background Task", command=stop_background_task)
stop_button.pack()

# Run the Tkinter main loop
root.mainloop()
