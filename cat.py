# catpics telegram bot
# Copyright (C) 2023  Mr.X
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
print("""    catpics bot  Copyright (C) 2023  Mr.X
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions;""")
import telebot, os, time
bot = telebot.TeleBot('TOKEN')
while True:
    os.system("wget https://cataas.com/cat  --output-document=cat.jpg")
    bot.send_photo(chat_id="@linux_nerdcat",photo=open('cat.jpg','rb'))
    time.sleep(60)
