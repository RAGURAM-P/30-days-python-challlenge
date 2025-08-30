import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw

class MiniPaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Paint App")
        self.root.geometry("900x650")

        # Canvas settings
        self.bg_color = "white"
        self.brush_color = "#222222"
        self.brush_size = 6
        self.eraser_mode = False

        # Backing image to enable crisp PNG save
        self.img = Image.new("RGB", (1200, 800), self.bg_color)
        self.draw = ImageDraw.Draw(self.img)

        # UI
        self._build_toolbar()
        self._build_canvas()

        # Mouse state
        self.last_x = None
        self.last_y = None

    def _build_toolbar(self):
        bar = tk.Frame(self.root, padx=8, pady=6)
        bar.pack(side=tk.TOP, fill=tk.X)

        # Color button
        tk.Button(bar, text="🎨 Color", command=self.choose_color).pack(side=tk.LEFT)

        # Brush size
        tk.Label(bar, text=" Brush ").pack(side=tk.LEFT)
        self.size_var = tk.IntVar(value=self.brush_size)
        tk.Scale(bar, from_=1, to=60, orient=tk.HORIZONTAL, variable=self.size_var,
                 length=180, command=lambda e: self._update_size()).pack(side=tk.LEFT)

        # Eraser toggle
        self.eraser_var = tk.BooleanVar(value=False)
        tk.Checkbutton(bar, text="Eraser", variable=self.eraser_var,
                       command=self.toggle_eraser).pack(side=tk.LEFT, padx=8)

        # Clear
        tk.Button(bar, text="🧹 Clear", command=self.clear_canvas).pack(side=tk.LEFT, padx=8)

        # Save
        tk.Button(bar, text="💾 Save PNG", command=self.save_png).pack(side=tk.LEFT)

        # Hint
        tk.Label(bar, text="   Tip: Hold mouse and draw.").pack(side=tk.LEFT, padx=10)

    def _build_canvas(self):
        self.canvas = tk.Canvas(self.root, bg=self.bg_color, width=1200, height=800, cursor="pencil")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind events
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Resize handling (keeps drawing area visible but backing image fixed for quality)
        self.canvas.bind("<Configure>", self.on_resize)

    # --- Drawing logic ---
    def on_press(self, event):
        self.last_x, self.last_y = event.x, event.y
        self._dot(event.x, event.y)

    def on_drag(self, event):
        x, y = event.x, event.y
        if self.last_x is not None and self.last_y is not None:
            color = self.bg_color if self.eraser_mode else self.brush_color
            width = self.brush_size
            # Draw on canvas
            self.canvas.create_line(self.last_x, self.last_y, x, y,
                                    fill=color, width=width, capstyle=tk.ROUND, smooth=True)
            # Draw on PIL image
            self.draw.line([(self.last_x, self.last_y), (x, y)],
                           fill=color, width=width, joint="curve")
        self.last_x, self.last_y = x, y

    def on_release(self, _):
        self.last_x, self.last_y = None, None

    def _dot(self, x, y):
        color = self.bg_color if self.eraser_mode else self.brush_color
        r = self.brush_size / 2
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=color)
        self.draw.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=color)

    # --- Controls ---
    def choose_color(self):
        color = colorchooser.askcolor(title="Pick Brush Color", initialcolor=self.brush_color)[1]
        if color:
            self.brush_color = color
            if self.eraser_mode:
                self.toggle_eraser(force=False)

    def _update_size(self):
        self.brush_size = int(self.size_var.get())

    def toggle_eraser(self, force=None):
        if force is None:
            self.eraser_mode = self.eraser_var.get()
        else:
            self.eraser_mode = force
            self.eraser_var.set(force)

    def clear_canvas(self):
        if messagebox.askyesno("Clear", "Clear the canvas?"):
            self.canvas.delete("all")
            # Reset backing image
            self.img.paste(self.bg_color, [0, 0, *self.img.size])

    def save_png(self):
        fname = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG image", "*.png")],
                                             title="Save drawing as...")
        if not fname:
            return
        try:
            self.img.save(fname, "PNG")
            messagebox.showinfo("Saved", f"Image saved:\n{fname}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save image:\n{e}")

    def on_resize(self, event):
        # Keep a minimum canvas size; backing image remains 1200x800 for consistent saves
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniPaint(root)
    root.mainloop()
