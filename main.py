import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# -----------------------------------------
# Start Message (reusable)
# -----------------------------------------
async def start_message():
    keyboard = [
        [InlineKeyboardButton("📚 Resources", callback_data="resources")],
        [InlineKeyboardButton("📐 Theories", callback_data="theories")]
    ]
    return "Hello! I am the Nuclear Physics Bot ⚛️\nPlease choose an option:", keyboard

# -----------------------------------------
# /start Command Handler
# -----------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text, keyboard = await start_message()
    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# -----------------------------------------
# Resources Section
# -----------------------------------------
async def resources_message():
    keyboard = [
        [InlineKeyboardButton("📘 Book", url="https://drive.google.com/file/d/1Mm3ljRrEFFfvikHDF-gtOIhcJHasqpln/view")],
        [InlineKeyboardButton("📑 Slides", url="https://drive.google.com/file/d/1CbjBDLMpaGFKtR7dmoasLG60GRRvPLiZ/view")],
        [InlineKeyboardButton("🎥 YouTube ", url="https://youtube.com/playlist?list=PLRN3HroZGu2n_j3Snd_fSYNLvCkao8HIx&si=0S1nWRLekM3fELFJ")],
        [InlineKeyboardButton("📝 Past Exams", callback_data="years")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_to_start")]
    ]
    return "Here are useful resources for Nuclear Physics:\nChoose from the options below:", keyboard

# -----------------------------------------
# Past Exams (Years Section)
# -----------------------------------------
async def years_message():
    keyboard = [
        [InlineKeyboardButton("📄 Exam 1", url="https://sg.docworkspace.com/d/sIOnXgIXJApuj0MkG")],
        [InlineKeyboardButton("📄 Exam 2", url="https://sg.docworkspace.com/d/sIBPXgIXJAuyk0MkG")],
        [InlineKeyboardButton("📄 Exam 3", url="https://sg.docworkspace.com/d/sIDfXgIXJAoil0MkG")],
        [InlineKeyboardButton("⬅️ Back", callback_data="resources")]
    ]
    return "📘 Past Exam Papers:\nSelect a year:", keyboard

# -----------------------------------------
# Theories Section
# -----------------------------------------
async def theories_message():
    keyboard = [
        [InlineKeyboardButton("🎬 Theory Video 1", url="https://youtu.be/QCZQCi_uKpM?si=eN6ZMitgWBMe1v2F")],
        [InlineKeyboardButton("🎬 Theory Video 2", url="https://youtu.be/iGr6atucsBw?si=wPfSDUgjBTBDT2go")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_to_start")]
    ]
    return "Important Nuclear Physics Theory Videos:", keyboard

# -----------------------------------------
# Callback Query Handler
# -----------------------------------------
async def callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "resources":
        text, keyboard = await resources_message()
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "years":
        text, keyboard = await years_message()
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "theories":
        text, keyboard = await theories_message()
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "back_to_start":
        text, keyboard = await start_message()
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

# -----------------------------------------
# Run Bot
# -----------------------------------------
# استدعاء التوكن من متغير البيئة على Render
TOKEN = os.environ.get("TOKEN")  # "TOKEN" هو اسم متغير البيئة على Render

if not TOKEN:
    raise ValueError("No BOT TOKEN found. Please set TOKEN environment variable on Render.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(callbacks))

app.run_polling()
