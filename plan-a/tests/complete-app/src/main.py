
# Import math Library
import math

import tkinter
root = tkinter.Tk()
root.geometry("800x600")

canvas = tkinter.Canvas(root)
canvas.config(width=800, height=600)

elapsed_time = 0

def onNewFrame():
  # register it to run again in a 1/60 (60 frame per seconds)
  root.after(int(1000/60), onNewFrame)

  # increment the time
  global elapsed_time # make it accessible
  elapsed_time += 1/60

  # clear the canvas (draw rectangle over the entire canvas)
  canvas.create_rectangle(0,0, 800,600, fill="grey")

  # increment the time
  cosAngleA = math.cos(elapsed_time)
  sinAngleA = math.sin(elapsed_time)
  cosAngleB = math.cos(elapsed_time + math.pi * 0.5)
  sinAngleB = math.sin(elapsed_time + math.pi * 0.5)

  center: list[float] = [300,300]
  half_size: float = 100

  canvas.create_line(
    center[0] + half_size * cosAngleA, center[1] + half_size * sinAngleA,
    center[0] - half_size * cosAngleA, center[1] - half_size * sinAngleA,
    width=5)

  canvas.create_line(
    center[0] + half_size * cosAngleB, center[1] + half_size * sinAngleB,
    center[0] - half_size * cosAngleB, center[1] - half_size * sinAngleB,
    width=5)

  canvas.pack()

  # print("lol")

onNewFrame()

# start the application
root.mainloop()
