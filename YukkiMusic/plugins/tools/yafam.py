







@app.on_message(
     command(["سورس","المطور","السورس","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def Ahmed(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG_URL}",
        caption=f"""**Bot channel and bot updates**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(f"• {SUDO_NAME} •", url=f"{SUDO_USER}"),
                ],[
                InlineKeyboardButton(f"• {YAFA_NAME} •", url=f"{YAFA_CHANNEL}"),
                ],[
                InlineKeyboardButton("• أضفني الى مجموعتك •", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),  
                ]
            ]
        ),
    )