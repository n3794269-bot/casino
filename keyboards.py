from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo)
from config import PACKAGES, WEBAPP_URL

def main_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🎰 Играть", web_app=WebAppInfo(url=WEBAPP_URL))],
        [KeyboardButton(text="💰 Пополнить"), KeyboardButton(text="💸 Вывод")],
        [KeyboardButton(text="👤 Профиль")],
    ], resize_keyboard=True)

def packages_kb():
    rows = []
    for rub, data in PACKAGES.items():
        label = f"{rub} ₽ → {data['coins']} монет"
        if data["bonus"]:
            label += f" (+{data['bonus']}%)"
        rows.append([InlineKeyboardButton(text=label, callback_data=f"dep:{rub}")])
    rows.append([InlineKeyboardButton(text="✏️ Своя сумма", callback_data="dep:custom")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def confirm_dep_kb(rub):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Я оплатил", callback_data=f"paid:{rub}")],
        [InlineKeyboardButton(text="❌ Отмена", callback_data="dep:cancel")],
    ])

def deposit_decision_kb(dep_id):
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"depok:{dep_id}"),
        InlineKeyboardButton(text="❌ Отклонить", callback_data=f"depno:{dep_id}"),
    ]])

def withdraw_decision_kb(wid):
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ Одобрить", callback_data=f"wdok:{wid}"),
        InlineKeyboardButton(text="❌ Отклонить", callback_data=f"wdno:{wid}"),
    ]])