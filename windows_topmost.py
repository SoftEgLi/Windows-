import win32gui
import win32con
import keyboard
import tkinter as tk
from tkinter import messagebox

# 记录置顶的窗口句柄
TOPMOST_WINDOWS = set()

def toggle_topmost():
    """切换当前窗口的置顶状态"""
    hwnd = win32gui.GetForegroundWindow()  # 获取当前活动窗口的句柄
    if hwnd in TOPMOST_WINDOWS:
        # 如果窗口已经置顶，取消置顶
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        TOPMOST_WINDOWS.remove(hwnd)
        print(f"窗口取消置顶: {hwnd}")
    else:
        # 如果窗口未置顶，设置置顶
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        TOPMOST_WINDOWS.add(hwnd)
        print(f"窗口置顶: {hwnd}")

# 创建主窗口
def create_ui():
    root = tk.Tk()
    root.title("窗口置顶工具")
    root.geometry("300x150")
    root.resizable(False, False)

    label = tk.Label(root, text="按 F7 键切换窗口置顶状态", font=("Arial", 12))
    label.pack(pady=30)

    def on_close():
        if messagebox.askokcancel("退出", "确定要退出程序吗？"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    return root

# 注册快捷键
keyboard.add_hotkey('F7', toggle_topmost)

print("程序已启动，按 F7 切换窗口置顶状态。按 Ctrl+C 退出程序。")

# 启动 UI
ui = create_ui()
try:
    ui.mainloop()
except KeyboardInterrupt:
    print("程序已退出。")
