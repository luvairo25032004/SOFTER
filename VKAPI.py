import discord 
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import asyncio 
import random
import os
donating=620950579442745345
bot_loggs=620152202836574208
client = discord.Client()
Bot=commands.Bot(command_prefix="=")
@Bot.event
async def on_ready():
	print("------------")
	print("Logged in as...")
	print("BILLY HERRINGTON")
	print("status==True///succesfully turned on")
	print("Let's get started!")
	print("------------")
	game = discord.Game(r"=to_know commands")
	await Bot.change_presence(status=discord.Status.idle, activity=game)
@Bot.command(pass_contex=True)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "сервер":
        await message.channel.send(message.channel, "Приветствую тебя, мой друг. \n Напоминаю, что ты находишься на сервере MULTYSERVER ```(212.77.158.148:7777)```. \n Подробнее ознакомиться с командами бота можно через =to_knpw commands")

@Bot.event # фильтрация чата 
async def on_message(message):
	await Bot.process_commands(message) # Проверяет, если сообщение это команда, то команда все равно выполнится
	if message.author == Bot.user:
		pass
	else:
		ban_message=["сука","тварь","мразь","урод","ублюдок","нахуй","пидорас","пидарас","сучка","пидар","блядь","блять","говна","гавна","говно","гавно","хуй","йеблуша","йеблан","еблан",
"ебал","ебать","уебать","уебал","хер","херня","бля","мать твою", "блядиада", "ёбаный","ёбанный", "гад","придурок","дурак","придурак", "козлоёб", "изъебнуться","хуепутало","гнида",
"наебал", "наебать", "насрать", "уебался", "пиздуй", "пиздовать", "пиздуй","нахуй","пиздолиз","уебан","влагалище","блядина","гандон","мудак","шлюха","гандон","гондон","чмо","мудазвон","мудозвон","козёл","казёл","пидор","пидар","лох"]
		msgl = message.content.lower()
		try:
			for i in ban_message:
				if i in msgl:
					await message.delete()
					await message.channel.send("***Be tolerant!***")
					await asyncio.sleep(20)
					await ctx.message.delete()			
		except:
			pass
@Bot.event #Присоединение игрока
async def on_member_join(member):
	try:
		role = discord.utils.get(member.guild.roles, name=role_on_member_join)
		await  member.add_roles(role)
		await  member.send(content=f"Hello, {author}. Tnaks for visiting our server! \n Bip-bop?")
	except:
		pass
@Bot.event
async def on_message_delete(message):
	channel = Bot.get_channel(bot_loggs)
	if message.guild is None:
		pass
	else:
		if message.author.id == bot_id:
			pass
		else:
			emb = discord.Embed(title='***Deleted messages***',
				description=f'**Message author:**\n<@{message.author.id}>\n**ID**:\n`{message.author.id}`\n**Channel:**\n<#{message.channel.id}>\n**Message:**\n`{message.content}`',
				colour= 0x800080)			
			emb.set_footer(text=message.created_at.now())
			await channel.send(embed = emb)
@Bot.command()
async def ivent_random(ctx, arg):
	if not arg:
		await ctx.send("!Укажите количество игроков!")
	else:
		if int(arg) >= 10:
			run = random.randint(1,4)
			if run == 1:
				emb = discord.Embed(title = "***Случайный ивента Для > 10 Игроков***", colour = 0x800080)
				emb.add_field(name = "***Название Ивента:***", value = "```Предатели```")
				emb.add_field(name = "***Правила проведения: ***" , value = "```1.Все игроки спавнятся, как в обычной игре, но у некоторых случайным образом появляется в инвентаре монета \n2.Игроки с монеткой - предатели и их цель убить всё живое на карте, кроме таких же предателей \n3.Удачного проведения!```")
				emb.add_field(name = "~~~Вызвано:~~~", value =  ctx.message.author.mention )
				await ctx.send(embed=emb)
			if run == 2:
				emb = discord.Embed(title = "***Случайный ивента Для > 10 Игроков***", colour = 0x800080)
				emb.add_field(name = "***Название Ивента:***", value = "```Охота на SCP-939```")
				emb.add_field(name = "***Правила проведения: ***" , value = "```1.В зависимости от кол-ва игроков на сервере спавнятся один или два объекта SCP-939. \n2.Остальные люди играют за мтф \n3.Цель у SCP и людей остаётся такой же \n4.Удачного проведения! ```")
				emb.add_field(name = "~~~Вызвано:~~~", value = ctx.message.author.mention )
				await ctx.send(embed=emb)
			if run == 3:
				emb = discord.Embed(title = "***Случайный ивента Для > 10 Игроков***", colour = 0x800080)
				emb.add_field(name = "***Название Ивента:***", value = "```Осада крыши```")
				emb.add_field(name = "***Правила проведения: ***" , value = "```1.В зависимости от кол-ва игроков на сервере спавнятся отряд МТФ и ХАОСА. \n2.Отряд МТФ устанавливается на warp roof и отстреливает N-е кол-во волн хаоситов (Обычно 5). \n4.Удачного проведения! ```")
				emb.add_field(name = "~~~Вызвано:~~~", value =  ctx.message.author.mention )
				await ctx.send(embed=emb)
			if run == 4:
				emb = discord.Embed(title = "***Случайный ивента Для > 10 Игроков***", colour = 0x800080)
				emb.add_field(name = "***Название Ивента:***", value = "```Мафия```")
				emb.add_field(name = "***Правила проведения: ***" , value = "```1.Данный ивент проводится по правилам настольной игры \"Мафия\" \n2.Администраторы следят за процессом игры и убивают выбывших игроков \n3.Удачного проведения! ```")
				emb.add_field(name = "~~~Вызвано:~~~", value =  ctx.message.author.mention)
				await ctx.send(embed=emb)	
		else:
			await ctx.send("```На количество игроков < 10 пока что не предусмотрены никакие ивенты! \nЕсли вы хотите добавить какой-либо новый пункт - свяжитесь с @Азотистая Кислота```")

@Bot.command()
async def to_know(ctx, command = None,user=discord.Member):
	if not command:
		await ctx.send("```!Please, select category!```")
	elif command == "commands":
		emb = discord.Embed(title = "***Commands request***", colour = 0x800080)
		emb.add_field(name = "```=mute @Player```", value = "Замутить игрока(время отсутствует)")
		emb.add_field(name = "```=unmute @Player```", value = "Размутить игрока(время отсутствует)")
		emb.add_field(name = "```=Ban @Player Reason Time```", value = "Блокировка Игрока(можно без причины и времени)")
		emb.add_field(name = "```=roll NUM1 NUM2```", value = "Вывод случайного числа в заданном диапазоне")
		emb.add_field(name = "```=say CHANNEL_NAME Text```", value = "Отправлять сообщения от лица бота")
		emb.add_field(name = "```=luck Red (or) White```", value = "Игра-угадывание конечного результата")
		emb.add_field(name = "```=clear Ammount```", value = "Удаление заданного кол-ва сообщений")
		emb.add_field(name = "```=info @Player```", value = "Вывод информации об игроке")
		emb.add_field(name = "```=to_know CATEGOTY```", value = "Вывод информации по заданной категории(К примеру о командах бота)")
		emb.add_field(name = "```=players```", value = "Показывает игроков на сервере дискорд")
		emb.add_field(name="```=donate TEXT```", value = "Отправка Запроса Доната, после слова =donate можете писать свободным текстом")
		emb.add_field(name="```=ivent_random PLAYERS```", value = "Вывод одного случайного ивента, укажите кол-во игроков!")

		await ctx.send(embed=emb, delete_after=180)
	elif command == "roles":
		emb = discord.Embed(title = "***Roles request***", colour = 0x800080)
		emb.add_field(name="```Президент Сервера```", value = "Главная роль, так же является создателем")
		emb.add_field(name="```Главный администратор```", value = "Глава администрации")
		emb.add_field(name= "```Администратор```", value = "Администрирует сервер Scp")
		emb.add_field(name="```SOFT-WARE BOT ENGINEER```", value = "Тех.поддержка по ботам на сервере")
		emb.add_field(name="```Discord Moderator(Moderations)```", value = "Следит за сервером дискорд")
		emb.add_field(name="```SoundPad User```", value = "Активный пользователь программы SoundPad")
		emb.add_field(name="```ТестРаб```", value = "Обычный участник сообщества")
		emb.add_field(name="```!Muted!```", value = "Нарушитель правил сообщества")
		emb.add_field(name="```Sad```", value = "Грустный человек")
		emb.add_field(name="```Админ-Тестирование```", value = "Админ, находящийся на тестовом сроке")
		emb.add_field(name="```Comittee```", value = "Коммитет по одбору управления сервева")
		await ctx.send(embed=emb, delete_after=180)
	elif command == "donate":
		emb = discord.Embed(title="Информация о донатных услугах", colour=0x800080)
		emb.add_field(name="Оформление запроса доната через бота", value = "```Для того, чтобы оформить донат-услугу просто напишите =donate ВАШ ТЕКСТ и ожидайте ответа администрации! \n P.s: Отправка сообщений спама или флуда карается 4 предупреждениями и блокировкой!```")
		emb.add_field(name="Права ***Администратора*** на всех серверах проекта (навсегда)",value=  "```2000 руб```")
		emb.add_field(name="Права ***Администратора*** на всех серверах проекта(временно)" ,value= "```300 руб/месяц```")
		emb.add_field(name="Права ***Администратора*** на всех серверах проекта (навсегда)" ,value= "```2000 руб```")
		emb.add_field(name="Отдельный Тэг на всех серверах проекта (навсегда)" ,value= "```50 руб + (цвет тэга) 10 руб```")
		emb.add_field(name="Смена Тэга на всех серверах проекта (навсегда)" ,value= "```100 руб + (цвет) 30 руб```")
		emb.add_field(name="Права ***Администратора*** на всех серверах проекта (навсегда)" ,value= "```2000 руб```")
		await ctx.send(embed=emb, delete_after=180)
@Bot.command(pass_context=True)
async def donate(ctx, * , cnt):
	channel=Bot.get_channel(donating)
	if not cnt:
		await ctx.send("```It's not possible to send ad empty request```")
	else:
		emb=discord.Embed(title="```Покупка Донат-Услуги```",colour=0x800080)
		emb.add_field(name="***Имя Пользователя:***", value=ctx.message.author.mention)
		emb.add_field(name="***Текст сообщения:***", value=cnt)
		await channel.send(embed=emb)
@Bot.command(pass_context=True)
async def luck(ctx, arg):
	effects=["red","white"]
	run=random.choice(effects)
	if arg.lower() == run:
		await ctx.send(f"It landed on __{arg}__ , and you won! :grinning: {ctx.message.author.mention}")
		await asyncio.sleep(30)
		await ctx.message.delete()
	else:
		await ctx.send(f"It didn't land on __{arg}__ , and you lose! :fearful: {ctx.message.author.mention}")
		await asyncio.sleep(30)
		await ctx.message.delete()
@Bot.command() ###MUTE
async def mute(ctx, member:discord.Member):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = "___!Muted!___")
	channel = Bot.get_channel(bot_loggs)
	permissions123 = ctx.message.author.guild_permissions.administrator
	if permissions123:
		if mute_role in member.roles:
			await ctx.send("This person is already muted!, {}".format(ctx.message.author.mention))
		else:
			mutid = discord.Embed(description=f'**{member.mention} succesfully muted by Administrator! {ctx.message.author.mention}**', colour= 0xFF0000)
			mutid.set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
			await channel.send(embed= mutid)
			await member.add_roles(mute_role)	
	else:
		await ctx.send("!You don't have permissions to use this command!")
@Bot.command()	###UNMUTE
async def unmute(ctx, member: discord.Member):
	permissions1234 = ctx.message.author.guild_permissions.administrator
	channel = Bot.get_channel(bot_loggs)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = "___!Muted!___")
	if permissions1234:
		if mute_role not in member.roles:
			await ctx.send("This person is already unmuted , {}".format(ctx.message.author.mention))
		else:
			mutid1=discord.Embed(description=f'**{member.mention} succesfully unmuted by Administrator! {ctx.message.author.mention}!**', colour= 0xFF0000)
			mutid1.set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
			await channel.send(embed= mutid1)
			await member.remove_roles(mute_role)
	else:
		await ctx.send("!You don't have permissions to use this command!")
@Bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	for i in user.roles:
		bomb=user.roles[1:2]
	emb=discord.Embed(title= "***Information about player***", color=0x39d0d6)
	emb.add_field(name= "***Name***", value="```"+str(user.name)+"```")
	emb.add_field(name="***ID***", value="```"+str(user.id)+"```")
	emb.add_field(name="***Date of creating:***", value="```"+str(user.created_at)+"```")
	emb.add_field(name="***Date of joining:***",value="```"+str(user.joined_at)+"```")
	emb.add_field(name="***Server:***", value="```MULTYSERVER```")
	emb.add_field(name="***Roles on this server:***", value="```"+str(bomb[:1])+"```")
	emb.add_field(name="***Place of living:***", value="```"+"~~~[ДАННЫЕ УДАЛЕНЫ]~~~"+"```")
	emb.set_thumbnail(url=user.avatar_url)
	emb.set_author(name=Bot.user.name, url ="https://discordapp.com/oauth2/authorized")
	emb.set_footer(text="***Called:*** {}".format(user.name), icon_url=user.avatar_url)
	await ctx.send(embed=emb)
@Bot.command()
async def roll(ctx, first: int, second: int):
	roll = random.randint(first, second)
	author = ctx.message.author
	await ctx.send(f"{author.mention} rolled: " + str(roll))
@Bot.command()
async def clear(ctx, amount: int):
	permissions = ctx.message.author.guild_permissions.administrator
	if permissions==True:
		await ctx.channel.purge(limit=amount)
	else:
		await ctx.send("***You don't have permissions to use this command!***")
@Bot.command()
async def players(ctx):
	player=len(ctx.author.guild.members)
	counter = 0
	for i in ctx.author.guild.members:
		if not i.bot: counter =+ 1 
		delta = i
		await ctx.send("```" + str(delta) + "```")
	await ctx.send("```Amount of players: " + str(player) + "```")

@Bot.command()
async def ban(ctx, member: discord.Member = None, tm ="infinite" , *, reason = "Не указана"):
	permissions = ctx.message.author.guild_permissions.administrator
	channel = Bot.get_channel(bot_loggs)
	if permissions == True:
		if not member:
			await ctx.send("Select user!", delete_after=180)
			await asyncio.sleep(180)
			await ctx.message.delete()	
		if not tm:
			await ctx.send("Select ban time!", delete_after=180)
			await asyncio.sleep(180)
			await ctx.message.delete()
		else:
			if tm == "infinite":
				banid = discord.Embed(description=f'**{member.mention} unbanned!**\n\n**Time:**\nUntil administrator unban you\n\n**Reason:**\n' + reason, colour= 0xFF0000)
				banid.set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
				await ctx.message.delete()			
				await channel.send(embed= banid)			
				await member.ban()
			else:
				t = (int(tm) * 60)
				await member.ban()
				banid = discord.Embed(description=f'**{member.mention} was banned!**\n\n**Time:**\n{tm}.\n**Reason:**\n{reason}', colour= 0xFF0000)
				banid.set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
				await ctx.message.delete()					
				await channel.send(embed= banid)
				await asyncio.sleep(t)
				await member.unban()
				await channel.send(embed=discord.Embed(description=f'**{member.mention} unbanned!**', colour= 0x0080FF).set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url))
	else:
		await ctx.send("You don't have permission to use this command!", delete_after=180)
		await asyncio.sleep(180)	
		await ctx.message.delete()	
@Bot.command()
@commands.has_permissions(administrator = True) # Могут использовать лишь пользователи с правами Администратора
async def say(ctx, channel: discord.TextChannel, *, cnt):
   await ctx.message.delete() # Удаляет написанное вами сообщение
   embed = discord.Embed(description = cnt, colour = 0x00ff80) # Генерация красивого сообщения
   await channel.send(embed=embed)
token = os.environ.get("BOT_TOKEN")
Bot.run(str(token))

