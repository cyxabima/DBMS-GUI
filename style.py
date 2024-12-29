from tkinter import ttk, font

h1_font = font.Font(
    family="Arial",
    size=14,
)

btn_style = ttk.Style()
btn_style.configure(
    "Custom.TButton",
    background="#F0BB78",
    font=("Arial", 16, "bold"),
    foreground="#131010",
)
btn_style.map("Custom.TButton", background=[("active", "#8B5C3B")])
