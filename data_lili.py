import telebot
import sqlite3, requests
from datetime import datetime

admin_ids=[
	"1943075949",
	"1868324643",
	"5875543311"
]


admin_user="AAAAi7"
bot_token="5770580281:AAH11YvDxkdK0hkyWhaum75hptOyrQajOQw"
bot_channels=[
	'@Databasebaghdad',
	'@x7xcc',
	'@L_YLYtt',
]

bot = telebot.TeleBot(token=bot_token, num_threads=50)

#############BUTTONS###########

admin_main_page = telebot.types.InlineKeyboardMarkup()
admin_main_page.row_width = 2
add_user = telebot.types.InlineKeyboardButton(text ='➕ اضافة مستخدم ➕', callback_data= 'add_user')
delete_user = telebot.types.InlineKeyboardButton(text ='❌ حذف مستخدم ❌', callback_data= 'delete_user')
change_mode = telebot.types.InlineKeyboardButton(text ='🔄 تغيير الوضع 🔄', callback_data= 'change_mode')
broadcast=telebot.types.InlineKeyboardButton(text ='📢 اذاعة للكل 📢', callback_data= 'broadcast')
admin_main_page.row(delete_user, add_user)
admin_main_page.row(change_mode)
admin_main_page.row(broadcast)


all_city=telebot.types.InlineKeyboardMarkup()
all_city.row_width=2

mesan=telebot.types.InlineKeyboardButton(text ='🔹 ميسان 🔹', callback_data= 'ct_mesan')

muthana=telebot.types.InlineKeyboardButton(text ='🔹 مثنى 🔹', callback_data= 'ct_muthana')

najaf=telebot.types.InlineKeyboardButton(text ='🔹 نجف 🔹', callback_data= 'ct_najaf')

nineveh=telebot.types.InlineKeyboardButton(text ='🔹 نينوى 🔹', callback_data= 'ct_nineveh')

diyala=telebot.types.InlineKeyboardButton(text ='🔹 ديالى 🔹', callback_data= 'ct_diyala')

duhok=telebot.types.InlineKeyboardButton(text ='🔹 دهوك 🔹', callback_data= 'ct_duhok')

erbil=telebot.types.InlineKeyboardButton(text ='🔹 اربيل 🔹', callback_data= 'ct_erbil')

karbalaa=telebot.types.InlineKeyboardButton(text ='🔹 كربلاء 🔹', callback_data= 'ct_karbalaa')

kirkuk=telebot.types.InlineKeyboardButton(text ='🔹 كركوك 🔹', callback_data= 'ct_kirkuk')

qadisiya=telebot.types.InlineKeyboardButton(text ='🔹 قادسية 🔹', callback_data= 'ct_qadisiya')

salahaldeen=telebot.types.InlineKeyboardButton(text ='🔹 صلاح الدين 🔹', callback_data= 'ct_salahaldeen')

sulaymaniyah=telebot.types.InlineKeyboardButton(text ='🔹 سليمانية 🔹', callback_data= 'ct_sulaymaniyah')

wasit=telebot.types.InlineKeyboardButton(text ='🔹 واسط 🔹', callback_data= 'ct_wasit')

babylon=telebot.types.InlineKeyboardButton(text ='🔹 بابل 🔹', callback_data= 'ct_babylon')

baghdad=telebot.types.InlineKeyboardButton(text ='🔹 بغداد 🔹', callback_data= 'ct_baghdad')

balad=telebot.types.InlineKeyboardButton(text ='🔹 بلد 🔹', callback_data= 'ct_balad')

basrah=telebot.types.InlineKeyboardButton(text ='🔹 بصرة 🔹', callback_data= 'ct_basrah')

dhiqar=telebot.types.InlineKeyboardButton(text ='🔹 ذي قار 🔹', callback_data= 'ct_dhiqar')

alanbar=telebot.types.InlineKeyboardButton(text ='🔹 الانبار 🔹', callback_data= 'ct_alanbar')

get_linked_numbers_button=telebot.types.InlineKeyboardButton(text ='📱 البحث عن رقم 📱', callback_data= 'ct_number')

all_city.add(mesan, muthana, najaf, nineveh, diyala, duhok, erbil, karbalaa, kirkuk, qadisiya, salahaldeen, sulaymaniyah, wasit, babylon, baghdad, balad, basrah, dhiqar, alanbar)
all_city.row(get_linked_numbers_button)

back_to_admin_menu=telebot.types.InlineKeyboardMarkup()
back_to_admin_menu.row_width=1
back_to_admin_button=telebot.types.InlineKeyboardButton(text ='رجوع ↩️', callback_data= 'back_to_admin')
back_to_admin_menu.add(back_to_admin_button)

back_to_cities_menu=telebot.types.InlineKeyboardMarkup()
back_to_cities_menu.row_width=1
back_to_cities_button=telebot.types.InlineKeyboardButton(text ='رجوع ↩️', callback_data= 'back_to_cities')
back_to_cities_menu.add(back_to_cities_button)

find_familly=telebot.types.InlineKeyboardMarkup()
find_familly.row_width=1
find_familly_button=telebot.types.InlineKeyboardButton(text ='البحث عن العائلة 🔍', callback_data= 'find_familly')
find_familly.add(find_familly_button)

#############BUTTONS###########


def verify_access(message):
	user_id_bot=message.chat.id
	user_id=message.from_user.id
	mode=str(open('mode.txt', 'r').read())
	subscribed_users=open('users.txt', 'r').read().splitlines()
	if str(user_id_bot) in admin_ids:
		return "admin"
	else:
		is_premium=False
		is_subscribed=0
		is_public=False
		for bot_channel in bot_channels:
			member = bot.get_chat_member(chat_id=bot_channel, user_id=message.chat.id)
			if member.status == "member" or member.status == "administrator" or member.status == "creator":
				is_subscribed+=1
		if mode=="public":
			is_public=True
		elif mode=="private":
			for idd in subscribed_users:
				if str(idd)==str(user_id_bot):
					is_premium=True
					break
	if is_public and is_subscribed==len(bot_channels):
		return "done"
	elif not is_public and is_premium and is_subscribed==len(bot_channels):
		return "done"
	elif not is_public and not is_premium and int(is_subscribed)==len(bot_channels):
		return "not premium"
	elif not is_public and not is_premium and int(is_subscribed)!=len(bot_channels):
		return "not subscribed"
	elif int(is_subscribed)!=len(bot_channels):
		return "not subscribed"





def broadcast_function(message):
	br_msg=bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text="حسنا، الان ارسل الرسالة لاذاعتها لكل مستخدمين البوت.", reply_markup=back_to_admin_menu)
	bot.register_next_step_handler(br_msg, broadcast_message_handler)

def broadcast_message_handler(message):
	wait_msg=bot.reply_to(message, "جاري الاذاعة، الرجاء الانتضار...")
	broadcast_message=message.text
	users_ids=open('ids.txt').read().splitlines()
	done_sent_count=0
	for idd in users_ids:
		try:
			bot.send_message(chat_id=idd, text=broadcast_message)
			done_sent_count+=1
		except:
			pass
	done_sent_count=str(done_sent_count)
	users_count=str(len(users_ids))
	bot.edit_message_text(chat_id=wait_msg.chat.id, message_id=wait_msg.id, text=f"تم ارسال الرسالة : {broadcast_message}\nالى {done_sent_count} شخص من {users_count} شخص.")


@bot.callback_query_handler(func=lambda call: True)
def handle_qwery(call):
	bot.clear_step_handler_by_chat_id(call.message.chat.id)
	stats=verify_access(call.message)
	if stats=="done" or stats=="admin":
		if call.data == 'change_mode':
			change_mode_function(call.message)
		elif call.data == 'add_user':
			add_user_function(call.message)
		elif call.data == 'delete_user':
			delete_user_function(call.message)
		elif call.data == 'back_to_admin':
			back_to_admin_menu_function(call.message)
		elif call.data == 'back_to_cities':
			back_to_cities_menu_function(call.message)
		elif 'ct_' in str(call.data):
			city=str(call.data).split('ct_')[1]
			search_function(call.message, city)
		elif call.data == 'find_familly':
			find_familly_function(call.message)
		elif call.data=='broadcast':
			broadcast_function(call.message)
	elif stats=="not premium":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"انت غير مشترك في البوت، للاشتراك الvip راسل الادمن : @{admin_user}")
	elif stats=="not subscribed":
		channels="\n".join(bot_channels)
		message_text = f"يجب عليك الاشتراك بقناة البوت اولاً\n{channels}\nاشترك ثم اضغط /start"
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=message_text)
		
		


def search_function(message, city):
	city_keys={
	'mesan':'ميسان',
	'muthana':'مثنى',
	'najaf':'نجف',
	'nineveh':'نينوى',
	'diyala':'ديالى',
	'duhok':'دهوك',
	'erbil':'اربيل',
	'karbalaa':'كربلاء',
	'kirkuk':'كركوك',
	'qadisiya':'قادسية',
	'salahaldeen':'صلاح الدين',
	'sulaymaniyah':'سليمانية',
	'wasit':'واسط',
	'babylon':'بابل',
	'baghdad':'بغداد',
	'balad':'بلد',
	'basrah':'بصرة',
	'dhiqar':'ذي قار',
	'alanbar':'الانبار',
	'number':'البحث عن رقم'
	}
	name_msg=bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=f'اخترت : {str(city_keys[str(city)])}\nارسل الاسم الثلاثي الان :', reply_markup=back_to_cities_menu)
	bot.register_next_step_handler(name_msg, search_name_handler, str(city))


def search_name_handler(message, city):
	name=message.text
	if city=="number":
		bot.reply_to(message, "الرجاء الانتضار...")
		return
	try:
		nameg=name.split(' ')[1]
		w_msg=bot.reply_to(message, "الرجاء الانتضار...")
		search_info_by_name(w_msg, name, city)
	except IndexError:
		bot.reply_to(message, "اسم غير صحيح", reply_markup=back_to_cities_menu)



def search_info_by_name(message, name, city):
	city_keys={
	'mesan':'ميسان',
	'muthana':'مثنى',
	'najaf':'نجف',
	'nineveh':'نينوى',
	'diyala':'ديالى',
	'duhok':'دهوك',
	'erbil':'اربيل',
	'karbalaa':'كربلاء',
	'kirkuk':'كركوك',
	'qadisiya':'قادسية',
	'salahaldeen':'صلاح الدين',
	'sulaymaniyah':'سليمانية',
	'wasit':'واسط',
	'babylon':'بابل',
	'baghdad':'بغداد',
	'balad':'بلد',
	'basrah':'بصرة',
	'dhiqar':'ذي قار',
	'alanbar':'الانبار'
	}
	if city=="baghdad":
		town_var="rc_name"
		street_var="f_street"
		work_var="p_job"
	else:
		town_var="ss_br_nm"
		street_var="ss_lg_no"
		work_var="p_work"
	connection = sqlite3.connect(f'db/{str(city)}.db')
	connection.text_factory = str
	cursor = connection.cursor()
	fname=str(str(name).split(' ')[0])
	sname=str(str(name).split(' ')[1])
	try:
		lname=str(str(name).split(' ')[2])
		three=True
	except:
		three=False
	found=False
	deleted=False
	if three:
		query = f"SELECT fam_no, p_first, p_father, p_grand, p_birth, {str(town_var)}, rc_no, seq_no, {str(street_var)}, {str(work_var)} FROM person WHERE p_first LIKE '{fname}%' AND p_father LIKE '{sname}%' AND p_grand LIKE '{lname}%'"
		cursor.execute(query)
		rows = cursor.fetchall()
		if rows:
			found=True
		for row in rows:
			nbr=str(list(row)[0])
			first=str(list(row)[1]).replace("\x84", "")
			second=str(list(row)[2]).replace("\x84", "")
			last=str(list(row)[3]).replace("\x84", "")
			birth=str(list(row)[4])[:4]
			town=str(list(row)[5])
			current_year = int(datetime.now().year)
			try:
				age=str(int(current_year)-int(birth))
			except:
				age="None"
			locality=str(list(row)[6])
			house=str(list(row)[7])
			alley=str(list(row)[8])
			work=str(list(row)[9])
			if not deleted:
				bot.delete_message(chat_id=message.chat.id, message_id=message.id)
				deleted=True
			mes=f"""\nرقم العائلة : {nbr}
الاسم الاول : {first}
الاسم الثاني : {second}
الاسم الثالث : {last}
سنة الولادة : {birth}
العمر : {age}
الوضيفة : {work}
المحافظة : {str(city_keys[str(city)])}
القضاء : {town}
المحلة : {locality}
الزقاق : {alley}
الدار : {house}\n"""
			bot.send_message(message.chat.id, mes, reply_markup=find_familly)
	else:
		query = f"SELECT fam_no, p_first, p_father, p_grand, p_birth, {str(town_var)}, rc_no, seq_no, {str(street_var)}, {str(work_var)} FROM person WHERE p_first LIKE '{fname}%' AND p_father LIKE '{sname}%'"
		cursor.execute(query)
		rows = cursor.fetchall()
		if rows:
			found=True
		for row in rows:
			nbr=str(list(row)[0])
			first=str(list(row)[1]).replace("\x84", "")
			second=str(list(row)[2]).replace("\x84", "")
			last=str(list(row)[3]).replace("\x84", "")
			birth=str(list(row)[4])[:4]
			town=str(list(row)[5])
			current_year = int(datetime.now().year)
			try:
				age=str(int(current_year)-int(birth))
			except:
				age="None"
			locality=str(list(row)[6])
			house=str(list(row)[7])
			alley=str(list(row)[8])
			work=str(list(row)[9])
			if not deleted:
				bot.delete_message(chat_id=message.chat.id, message_id=message.id)
				deleted=True
			mes=f"""\nرقم العائلة : {nbr}
الاسم الاول : {first}
الاسم الثاني : {second}
الاسم الثالث : {last}
سنة الولادة : {birth}
العمر : {age}
الوضيفة : {work}
المحافظة : {str(city_keys[str(city)])}
القضاء : {town}
المحلة : {locality}
الزقاق : {alley}
الدار : {house}\n"""
			bot.send_message(message.chat.id, mes, reply_markup=find_familly)
	if found:
		bot.send_message(message.chat.id, "تم الانتهاء من البحث ✅", reply_markup=back_to_cities_menu)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text="لم يتم العثور على نتائج ❌", reply_markup=back_to_cities_menu)




def find_familly_function(message):
	mess=""
	city_keys={
	'mesan':'ميسان',
	'muthana':'مثنى',
	'najaf':'نجف',
	'nineveh':'نينوى',
	'diyala':'ديالى',
	'duhok':'دهوك',
	'erbil':'اربيل',
	'karbalaa':'كربلاء',
	'kirkuk':'كركوك',
	'qadisiya':'قادسية',
	'salahaldeen':'صلاح الدين',
	'sulaymaniyah':'سليمانية',
	'wasit':'واسط',
	'babylon':'بابل',
	'baghdad':'بغداد',
	'balad':'بلد',
	'basrah':'بصرة',
	'dhiqar':'ذي قار',
	'alanbar':'الانبار'
	}
	inv_city_keys={v: k for k, v in city_keys.items()}
	fam_num=str(message.text.split('رقم العائلة : ')[1].split('\n')[0])
	ar_city=str(message.text.split('المحافظة : ')[1].split('\n')[0])
	city=str(inv_city_keys[str(ar_city)])
	if city=="baghdad":
		town_var="rc_name"
	else:
		town_var="ss_br_nm"
	connection = sqlite3.connect(f'db/{str(city)}.db')
	connection.text_factory = str
	cursor = connection.cursor()
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text="الرجاء الانتضار...", reply_markup=back_to_cities_menu)
	query = f"SELECT fam_no, p_first, p_father, p_grand, p_birth, {str(town_var)} FROM person WHERE fam_no LIKE '{fam_num}%'"
	cursor.execute(query)
	rows = cursor.fetchall()
	for row in rows:
		nbr=str(list(row)[0])
		first=str(list(row)[1]).replace("\x84", "")
		second=str(list(row)[2]).replace("\x84", "")
		last=str(list(row)[3]).replace("\x84", "")
		birth=str(list(row)[4])[:4]
		town=str(list(row)[5])
		current_year = int(datetime.now().year)
		try:
			age=str(int(current_year)-int(birth))
		except:
			age="None"
		mess+=f"""\nرقم العائلة : {nbr}\nالاسم الاول : {first}\nالاسم الثاني : {second}\nالاسم الثالث : {last}\nسنة الولادة : {birth}\nالعمر : {age}\nالقضاء : {town}\nالمحافظة : {str(city_keys[str(city)])}\n"""
		bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=mess, reply_markup=back_to_cities_menu)
		#offset+=batch_size
	mess+="\nتم الانتهاء من البحث ✅"
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=mess, reply_markup=back_to_cities_menu)


@bot.message_handler(commands=['start'])
def start_messaging(message):
	stats=verify_access(message)
	if stats=="admin":
		mode=str(open('mode.txt', 'r').read())
		bot.reply_to(message, f"مرحبا يا ادمن\nالوضع الحالي : {mode}", reply_markup=admin_main_page)
		bot.reply_to(message, f"يرجى اختيار المحافظة من ثم كتابه الاسم الثلاثي فقط من دون المواليد وسوف يضهر لك جميع الاشخاص المطلوبين 🌹", reply_markup=all_city)
	elif stats=="done":
		bot.reply_to(message, f"يرجى اختيار المحافظة من ثم كتابه الاسم الثلاثي فقط من دون المواليد وسوف يضهر لك جميع الاشخاص المطلوبين 🌹", reply_markup=all_city)
	elif stats=="not premium":
		bot.reply_to(message, f"انت غير مشترك في البوت، للاشتراك الvip راسل الادمن : @{admin_user}")
	elif stats=="not subscribed":
		channels="\n".join(bot_channels)
		message_text = f"يجب عليك الاشتراك بقناة البوت اولاً\n{channels}\nاشترك ثم اضغط /start"
		bot.send_message(message.chat.id, message_text)
	id=str(message.from_user.id)
	username=str(message.from_user.username)
	name=str(message.from_user.first_name)
	is_new_user=True
	read=open('ids.txt', 'r').read().splitlines()
	for idd in read:
		if str(idd)==str(id):
			is_new_user=False
		else:
			pass
	if is_new_user==True:
		with open('ids.txt', 'a') as f:
			f.write(str(id)+'\n')
			f.close()
		users=str(len(open('ids.txt', 'r').read().splitlines()))
		for admin_id in admin_ids:
			bot.send_message(admin_id, f"""
مستخدم جديد دخل الى البوت :
الاسم : {name}
اليوزر : @{username}
الايدي : {id}

عدد اجمالي مستخدمين البوت : {users}
""")
	else:
		pass


def change_mode_function(message):
	mode1=str(open('mode.txt', 'r').read())
	mm=open('mode.txt', 'w')
	if mode1=="public":
		mm.write('private')
		mm.close()
	elif mode1=="private":
		mm.write('public')
		mm.close()
	mode2=str(open('mode.txt', 'r').read())
	new_msg=message.text.replace(mode1, mode2)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=new_msg, reply_markup=admin_main_page)



def back_to_admin_menu_function(message):
	mode=str(open('mode.txt', 'r').read())
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=f"مرحبا يا ادمن\nالوضع الحالي : {mode}", reply_markup=admin_main_page)

def back_to_cities_menu_function(message):
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=f"يرجى اختيار المحافظة من ثم كتابه الاسم الثلاثي فقط من دون المواليد وسوف يضهر لك جميع الاشخاص المطلوبين 🌹", reply_markup=all_city)


def add_user_function(message):
	msg1=bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text="حسنا الان ارسل ايدي الشخص لاضافته", reply_markup=back_to_admin_menu)
	bot.register_next_step_handler(msg1, add_user_id_handler)


def add_user_id_handler(message):
	msg=bot.reply_to(message, "الرجاء الانتضار...")
	user_id=message.text
	lst=[]
	f=open('users.txt', 'r').read().splitlines()
	already=False
	for idd in f:
		if str(idd)==str(user_id):
			already=True
	if already==True:
		bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.id, text=f"موجود من قبل ❌", reply_markup=back_to_admin_menu)
	else:
		f=open('users.txt', 'a')
		f.write(user_id+'\n')
		f.close()
		bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.id, text=f"تم اضافة {user_id} ✅", reply_markup=back_to_admin_menu)



def delete_user_function(message):
	ids_msg="جميع ايديات المشتركين : \n\n"
	f=open('users.txt', 'r').read().splitlines()
	for idd in f:
		ids_msg+=f"- `{idd}`\n"
	msg2=bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=f"{ids_msg}\n\nحسنا الان ارسل ايدي الشخص لحذفه", reply_markup=back_to_admin_menu, parse_mode="markdown")
	bot.register_next_step_handler(msg2, delete_user_id_handler)


def delete_user_id_handler(message):
	msg=bot.reply_to(message, "الرجاء الانتضار...")
	user_id=message.text
	lst=[]
	f=open('users.txt', 'r').read().splitlines()
	found=False
	for idd in f:
		if str(idd)==str(user_id):
			found=True
		else:
			lst.append(idd)
	if found==True:
		ff=open('users.txt', 'w')
		for i in lst:
			ff.write(i+'\n')
		ff.close()
		bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.id, text=f"تم حذف {user_id} ✅", reply_markup=back_to_admin_menu)
	else:
		bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.id, text=f"غير موجود ❌", reply_markup=back_to_admin_menu)



bot.infinity_polling()