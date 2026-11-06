# -*- coding: utf-8 -*-
# آلة حاسبة بسيطة بنافذة وأزرار
# نستخدم مكتبة tkinter (تأتي مع Python) لصنع النافذة

import tkinter as tk

# إنشاء النافذة الرئيسية
window = tk.Tk()
window.title("آلة الحاسبة")
window.geometry("320x420")
window.resizable(False, False)

# هذا المتغير يحمل النص الذي يظهر في الشاشة
display_text = tk.StringVar()
display_text.set("0")

# الشاشة التي تعرض الأرقام والنتيجة
display = tk.Entry(
    window,
    textvariable=display_text,
    font=("Arial", 26),
    justify="right",
    bd=10,
    relief="ridge",
    state="readonly",
)
display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=8, pady=8)

# متغير نتذكّر به إذا كنا قد حسبنا النتيجة للتو
just_calculated = False


def press_number(num):
    """تعمل عند الضغط على زر رقم"""
    global just_calculated
    current = display_text.get()
    # إذا كانت الشاشة تعرض "0" أو "خطأ" أو نتيجة سابقة، نبدأ من جديد
    if just_calculated or current in ("0", "خطأ"):
        display_text.set(str(num))
        just_calculated = False
    else:
        display_text.set(current + str(num))


def press_operator(op):
    """تعمل عند الضغط على زر عملية (+ أو - أو * أو / أو .)"""
    global just_calculated
    just_calculated = False
    current = display_text.get()
    if current == "خطأ":
        display_text.set("0" + op)
    else:
        display_text.set(current + op)


def clear():
    """زر C يمسح الشاشة ويعيدها إلى 0"""
    global just_calculated
    display_text.set("0")
    just_calculated = False


def calculate():
    """زر = يحسب النتيجة ويعرضها"""
    global just_calculated
    try:
        result = eval(display_text.get())
        display_text.set(str(result))
    except Exception:
        display_text.set("خطأ")
    just_calculated = True


def make_command(text):
    """ترجع الدالة المناسبة لكل زر حسب نصه"""
    if text in "0123456789":
        return lambda: press_number(text)
    elif text in "+-*/.":
        return lambda: press_operator(text)
    elif text == "C":
        return clear


# قائمة الأزرار: (النص، الصف، العمود)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
]

# وضع كل زر في مكانه داخل النافذة
for text, row, col in buttons:
    btn = tk.Button(
        window,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=make_command(text),
    )
    btn.grid(row=row, column=col, padx=4, pady=4)

# زر "=" بعرض كامل في الأسفل
equal_btn = tk.Button(
    window,
    text="=",
    font=("Arial", 18),
    height=2,
    bg="#4CAF50",
    fg="white",
    command=calculate,
)
equal_btn.grid(row=5, column=0, columnspan=4, sticky="ew", padx=4, pady=4)

# تشغيل النافذة (يبقيها مفتوحة حتى يغلقها المستخدم)
window.mainloop()
