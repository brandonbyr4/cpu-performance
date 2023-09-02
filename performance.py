import tkinter as tk
from tkinter import ttk
import psutil
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

# Initialize list to store data
cpu_data = []

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def update_usage(i):
    cpu_percent = get_cpu_usage()
    
    # Append CPU usage data to the list
    cpu_data.append(cpu_percent)
    
    # Keep a limited number of data points
    max_data_points = 50
    if len(cpu_data) > max_data_points:
        cpu_data.pop(0)
    
    # Update the CPU usage plot
    ax.clear()
    ax.plot(cpu_data, label='CPU Usage', color='#84cc16')
    ax.fill_between(range(len(cpu_data)), cpu_data, color='#ecfccb', alpha=0.5)

    # Remove y-axis and ticks
    ax.get_xaxis().set_visible(False)

    # Show x-grid lines
    ax.yaxis.grid(True)

    # Add "%" symbol after each value on the y-axis
    ax.yaxis.set_major_formatter('{:.1f}%'.format)

    # Display current usage text
    current_usage_text.set(f"Current Usage: {cpu_percent:.1f}%")

root = tk.Tk()
root.title("CPU Usage Monitor")

# Create a tkinter Frame that fills the entire root window
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire window

# Create a matplotlib figure and axis
fig, ax = plt.subplots(figsize=(8, 4))

# Remove y-axis and ticks
ax.get_xaxis().set_visible(False)

# Show x-grid lines
ax.yaxis.grid(True)

# Add "%" symbol after each value on the y-axis
ax.yaxis.set_major_formatter('{:.1f}%'.format)

# Remove border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Create animated update
ani = FuncAnimation(fig, update_usage, interval=1000)

# Embed the matplotlib plot in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Create a label for current usage text
current_usage_text = tk.StringVar()
current_usage_label = tk.Label(root, textvariable=current_usage_text, font=("Arial", 12, "bold"), fg="#111827")
current_usage_label.pack(anchor="nw", padx=10, pady=10)

root.mainloop()