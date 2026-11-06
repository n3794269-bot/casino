import aiosqlite
DB = "casino.db"

async def init_db():
    async with aiosqlite.connect(DB) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY, username TEXT,
            balance INTEGER DEFAULT 0, banned INTEGER DEFAULT 0,
            spins_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS deposits (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
            amount_rub INTEGER, coins INTEGER, status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS withdrawals (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
            amount INTEGER, wallet TEXT, status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
            game TEXT, amount INTEGER, result TEXT, payout INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        await db.commit()

async def get_user(uid):
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM users WHERE user_id=?", (uid,)) as c:
            return await c.fetchone()

async def create_user(uid, username, start=1000):
    async with aiosqlite.connect(DB) as db:
        await db.execute("INSERT OR IGNORE INTO users (user_id,username,balance) VALUES (?,?,?)", (uid,username,start))
        await db.commit()

async def update_balance(uid, delta):
    async with aiosqlite.connect(DB) as db:
        await db.execute("UPDATE users SET balance=balance+? WHERE user_id=?", (delta,uid))
        await db.commit()

async def inc_spins(uid):
    async with aiosqlite.connect(DB) as db:
        await db.execute("UPDATE users SET spins_count=spins_count+1 WHERE user_id=?", (uid,))
        await db.commit()

async def log_history(uid, game, amount, result, payout):
    async with aiosqlite.connect(DB) as db:
        await db.execute("INSERT INTO history (user_id,game,amount,result,payout) VALUES (?,?,?,?,?)", (uid,game,amount,result,payout))
        await db.commit()

async def get_history(uid, limit=30):
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT game,amount,result,payout,created_at FROM history WHERE user_id=? ORDER BY id DESC LIMIT ?", (uid,limit)) as c:
            return await c.fetchall()

async def create_deposit(uid, rub, coins):
    async with aiosqlite.connect(DB) as db:
        cur = await db.execute("INSERT INTO deposits (user_id,amount_rub,coins) VALUES (?,?,?)", (uid,rub,coins))
        await db.commit()
        return cur.lastrowid

async def get_deposit(dep_id):
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM deposits WHERE id=?", (dep_id,)) as c:
            return await c.fetchone()

async def set_deposit_status(dep_id, status):
    async with aiosqlite.connect(DB) as db:
        await db.execute("UPDATE deposits SET status=? WHERE id=?", (status,dep_id))
        await db.commit()

async def pending_deposits():
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM deposits WHERE status='pending'") as c:
            return await c.fetchall()

async def create_withdrawal(uid, amount, wallet):
    async with aiosqlite.connect(DB) as db:
        cur = await db.execute("INSERT INTO withdrawals (user_id,amount,wallet) VALUES (?,?,?)", (uid,amount,wallet))
        await db.commit()
        return cur.lastrowid

async def get_withdrawal(wid):
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM withdrawals WHERE id=?", (wid,)) as c:
            return await c.fetchone()

async def set_withdrawal_status(wid, status):
    async with aiosqlite.connect(DB) as db:
        await db.execute("UPDATE withdrawals SET status=? WHERE id=?", (status,wid))
        await db.commit()

async def pending_withdrawals():
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM withdrawals WHERE status='pending'") as c:
            return await c.fetchall()

async def all_users():
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT user_id,username,balance,banned FROM users") as c:
            return await c.fetchall()

async def set_banned(uid, v):
    async with aiosqlite.connect(DB) as db:
        await db.execute("UPDATE users SET banned=? WHERE user_id=?", (v,uid))
        await db.commit()