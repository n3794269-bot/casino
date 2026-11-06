import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]

DEPOSIT_CARD = os.getenv("DEPOSIT_CARD", "2200 0000 0000 0000")
DEPOSIT_NAME = os.getenv("DEPOSIT_NAME", "Иван И.")
DEPOSIT_BANK = "Альфа-Банк"

START_BALANCE = 1000
HONEY_SPINS = 8
HONEY_WIN_CHANCE = 0.82
NORMAL_WIN_CHANCE = 0.28

PACKAGES = {
    50:   {"coins": 50,   "bonus": 0},
    100:  {"coins": 100,  "bonus": 0},
    500:  {"coins": 550,  "bonus": 10},
    1000: {"coins": 1200, "bonus": 20},
    2000: {"coins": 2600, "bonus": 30},
    5000: {"coins": 7000, "bonus": 40},
}
CUSTOM_MIN = 50
CUSTOM_RATE = 1.0
DEPOSIT_WAIT_TEXT = "в течение дня"

WITHDRAW_MIN = 500
WITHDRAW_AUTO = 5000

SLOTS = {
    "zeus":    {"name":"⚡ Зевс",     "symbols":["⚡","🏛️","🍇","🏺","👑"], "payouts":{"⚡":25,"🏛️":10,"🍇":6,"🏺":4,"👑":3},    "bg":"linear-gradient(135deg,#1a1a2e,#16213e,#0f3460)"},
    "pharaoh": {"name":"🐫 Фараон",   "symbols":["🐫","🏺","🐍","☀️","👁️"], "payouts":{"🐫":20,"🏺":12,"🐍":7,"☀️":5,"👁️":3},   "bg":"linear-gradient(135deg,#3e2723,#5d4037,#8d6e63)"},
    "dragon":  {"name":"🐉 Дракон",   "symbols":["🐉","🔥","💎","🏮","🎋"], "payouts":{"🐉":30,"🔥":12,"💎":8,"🏮":5,"🎋":3},    "bg":"linear-gradient(135deg,#b71c1c,#d32f2f,#f57c00)"},
    "classic": {"name":"🎰 Классика", "symbols":["🍒","🍋","🍊","🔔","7️⃣"], "payouts":{"🍒":3,"🍋":4,"🍊":6,"🔔":12,"7️⃣":50},   "bg":"linear-gradient(135deg,#1b5e20,#2e7d32,#388e3c)"},
    "space":   {"name":"🌌 Космос",   "symbols":["🚀","🌙","⭐","🪐","👽"], "payouts":{"🚀":8,"🌙":10,"⭐":6,"🪐":15,"👽":35},   "bg":"linear-gradient(135deg,#000428,#004e92,#000428)"},
    "dead":    {"name":"💀 Мёртвый",  "symbols":["💀","🦴","🕷️","🕸️","🩸"], "payouts":{"💀":40,"🦴":5,"🕷️":10,"🕸️":6,"🩸":20}, "bg":"linear-gradient(135deg,#1a0000,#330000,#4d0000)"},
}
ROULETTE_PAYOUTS = {"red":2, "black":2, "green":14}