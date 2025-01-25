import time
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler
from telegram.ext import Application, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update
from datetime import datetime, date
from telegram.ext import CallbackQueryHandler,ConversationHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

from my_package.English.english import english_button
from my_package.gujrati.gujrati import gujrati_button
from my_package.hindi.hindi import hindi_button

from my_package.English.about import about_us
from my_package.English.academic import academic
from my_package.English.administration import administration
from my_package.English.library import library
from my_package.English.pg import pg
from my_package.English.ug import ug
from my_package.English.certificate import certificate
from my_package.English.diploma import diploma
from my_package.English.mca import mca, mca_admission
from my_package.English.bca import bca, bca_admission
from my_package.English.pgdca import pgdca, pgdca_admission
from my_package.English.cspt import cspt, cspt_admission
from my_package.English.kvk import kvk

from my_package.gujrati.academic_guj import academic_guj
from my_package.gujrati.ug_guj import ug_guj 
from my_package.gujrati.pg_guj import pg_guj 
from my_package.gujrati.certificate_guj import certificate_guj 
from my_package.gujrati.diploma_guj import diploma_guj 
from my_package.gujrati.about_guj import about_us_guj
from my_package.gujrati.administration_guj import administration_guj
from my_package.gujrati.library_guj import library_guj
from my_package.gujrati.mca_guj import mca_guj, mca_admission_guj
from my_package.gujrati.bca_guj import bca_guj, bca_admission_guj
from my_package.gujrati.pgdca_guj import pgdca_guj, pgdca_admission_guj
from my_package.gujrati.cspt_guj import cspt_guj, cspt_admission_guj
from my_package.gujrati.kvk_guj import kvk_guj

from my_package.hindi.academic_hin import academic_hin
from my_package.hindi.ug_hin import ug_hin 
from my_package.hindi.pg_hin import pg_hin 
from my_package.hindi.certificate_hin import certificate_hin 
from my_package.hindi.diploma_hin import diploma_hin
from my_package.hindi.about_hin import about_us_hin
from my_package.hindi.administration_hin import administration_hin
from my_package.hindi.library_hin import library_hin
from my_package.hindi.mca_hin import mca_hin, mca_admission_hin
from my_package.hindi.bca_hin import bca_hin, bca_admission_hin
from my_package.hindi.pgdca_hin import pgdca_hin, pgdca_admission_hin
from my_package.hindi.cspt_hin import cspt_hin, cspt_admission_hin
from my_package.hindi.kvk_hin import kvk_hin

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Chatbot"]

dblist = myclient.list_database_names()
if "Chatbot" in dblist:
  print("The database exists.")

collist = mydb.list_collection_names()
if "gvpbot" in collist:
  print("The collection exists.")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

GENDER, ADDRESS, EMAIL, PHONE = range(4)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    currentTime = time.strftime('%H:%M')
    hour = datetime.now().hour
    userid = str(user.id)
    uid = userid.lstrip()

    dateTime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(dateTime)

    chat_id=update.effective_chat.id
    print("Chat ID : ",chat_id)

    if chat_id == mydb.gvpbot.find({"_id":uid}):
        print("Update")
        mydb.gvpbot.update_one({"_id":uid},{"$set":{"DateTime":dateTime}})
    else:
        print("New Update")
        mydb.gvpbot.update_one({"_id":uid},{"$set":{"_id":uid,"fName":user.first_name,"lName":user.last_name,"DateTime":dateTime}},upsert=True)
    
    if hour < 12 :
        await update.message.reply_html(
            rf"Hi.. {user.mention_html()}, Good Morning ",
            #reply_markup=ForceReply(selective=False),
        )
    
    if hour >= 12 and hour < 18:
        await update.message.reply_html(
            rf"Hi.. {user.mention_html()}, Good Afternoon",
            #reply_markup=ForceReply(selective=False),
        )
    if hour > 18 :
        await update.message.reply_html(
            rf"Hi.. {user.mention_html()}, Good Evening",
            #reply_markup=ForceReply(selective=False),
        )

    await update.message.reply_html(
        rf"I'm Gujarat Vidyapith Student Assistent. I Will Help You With Every Information About Gujarat Vidyapith. https://www.gujaratvidyapith.org",
        #reply_markup=ForceReply(selective=False),
    )

    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [["MALE", "FEMALE"]]

    await update.message.reply_text(
        "Send /cancel to stop talking to me.\n\n"
        "Are you a MALE or a FEMALE?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="MALE or FEMALE?"
        ),
    )
    return GENDER


async def gender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    uid = str(user.id)
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    mydb.gvpbot.update_one({"_id":uid},{"$set":{"Gender":update.message.text}},upsert=True)
    await update.message.reply_text(
        "Please send me City/Area Name of yours ! or send /skip to skip location.",
        reply_markup=ForceReply(selective=False),
    )

    return ADDRESS

async def address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    uid = str(user.id)
    logger.info("Address of %s: %s", user.first_name, update.message.text)
    mydb.gvpbot.update_one({"_id":uid},{"$set":{"Address":update.message.text}},upsert=True)
    await update.message.reply_text(
        "Thank You. Can You Provide Your Email : or send /skip to next step.",
        reply_markup=ForceReply(selective=False),
    )

    return EMAIL

async def skip_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the address and asks for a email."""
    user = update.message.from_user
    logger.info("User %s did not send address.", user.first_name)
    await update.message.reply_text(
        "Thank You. Can You Provide Your Email : or send /skip to next step.",
        reply_markup=ForceReply(selective=False),
    )

    return EMAIL

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    uid = str(user.id)
    logger.info("EMAIL of %s: %s", user.first_name, update.message.text)
    mydb.gvpbot.update_one({"_id":uid},{"$set":{"Email_ID":update.message.text}},upsert=True)
    await update.message.reply_text(
        "Thank You. Can You Provide Your Mobile No :",
        reply_markup=ForceReply(selective=False),
    )

    return PHONE

async def skip_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the address and asks for a email."""
    user = update.message.from_user
    logger.info("User %s did not send email.", user.first_name)
    await update.message.reply_text(
        "Thank You. Can You Provide Your Mobile No :",
        reply_markup=ForceReply(selective=False),
    )
    return PHONE

async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    uid = str(user.id)
    logger.info("Mobile No of %s: %s", user.first_name, update.message.text)
    mydb.gvpbot.update_one({"_id":uid},{"$set":{"Mobile_No":update.message.text}},upsert=True)
    await update.message.reply_html(
        "Thank You ! \nHow May I Help You Today ?",
        #reply_markup=ForceReply(selective=False),
    )

    await update.message.reply_html(
        rf"Available Languages",
        #reply_markup=ForceReply(selective=False),
    )

    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="1"),
            InlineKeyboardButton("ગુજરાતી", callback_data="2"),
        ],
        [InlineKeyboardButton("हिन्दी", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    user = update.effective_user  
    query = update.callback_query
    uid = str(user.id)
    await query.answer()

    # await query.edit_message_text(text=f"Selected option: {query.data}")
    button_choice=query.data
    print(type(button_choice))
    if button_choice=='1':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"English_Language":1}},upsert=True)
        await english_button(update, context)
    if button_choice=='2':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"Gujarati_Language":1}},upsert=True)
        await gujrati_button(update, context)
    if button_choice=='3':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"Hindi_Language":1}},upsert=True)
        await hindi_button(update,context)


    if button_choice=='1.1':
        await about_us(update,context)
    if button_choice=='1.2':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"Academic_English":1}},upsert=True)
        await academic(update,context)
    if button_choice =="0.1.1":
        await english_button(update,context)
    if button_choice =="0.1.2":
        await english_button(update,context)
    if button_choice == "0.1.2.1":
        await academic(update,context)
    if button_choice=="1.3":
        await administration(update, context)
    if button_choice=='1.4':
        await library(update,context)
    if button_choice=='1.2.1':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"Graduate_English":1}},upsert=True)
        await ug(update,context)
    if button_choice=='1.2.2':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"PG_English":1}},upsert=True)
        await pg(update,context)
    if button_choice=='1.2.3':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"Certi_English":1}},upsert=True)
        await certificate(update,context)
    if button_choice=='1.2.4':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"Diploma_English":1}},upsert=True)
        await diploma(update,context)
    if button_choice=='1.2.2.1':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"MCA_English":1}},upsert=True)
        await mca(update,context)
    
    # About us
    if button_choice=='1.1.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/overview.htm")
    if button_choice=='1.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/history.htm")
    if button_choice=='1.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/roadmap.htm")
    if button_choice=='1.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/values.htm")
    if button_choice=='1.1.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/emblem.htm")
    if button_choice=='1.1.6':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/annualreportsaccounts.htm")
    if button_choice=='1.1.7':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://gujaratvidyapith.org/newsandevents/IIQA%20Undertaking.pdf")

    #MCA
    if button_choice=="pg_back":
        await academic(update,context)
    if button_choice=='mca_back':
        await pg(update,context)
    if button_choice=="mca_home":
        await english_button(update,context)
    if button_choice=='1.2.2.1.1':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"MCAAdmission_English":1}},upsert=True)
        await mca_admission(update,context)    
    if button_choice=='1.2.2.1.2':
         mydb.gvpbot.update_one({"_id":uid},{"$inc":{"MCASyllabus_English":1}},upsert=True)
         await context.bot.send_message(chat_id=update.effective_chat.id, text="To Check Syllabus Click The Following Link. https://gujaratvidyapith.org/dcs/syllabus.php")
    if button_choice=='1.2.2.1.3':
         mydb.gvpbot.update_one({"_id":uid},{"$inc":{"MCAFacluty_English":1}},upsert=True)
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Faculty Details Click The Following Link. https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='1.2.2.1.4':
         mydb.gvpbot.update_one({"_id":uid},{"$inc":{"MCAFacilities_English":1}},upsert=True)
         await context.bot.send_message(chat_id=update.effective_chat.id, text="FACILITIES PROVIDED BY DEPARTMENT OF COMPUTER SCIENCE")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Software Development : https://gujaratvidyapith.org/dcs/swlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Internet of Things : https://gujaratvidyapith.org/dcs/iotlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Machine Learning : https://gujaratvidyapith.org/dcs/mllab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Cyber Security : https://gujaratvidyapith.org/dcs/cslab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Library : https://gujaratvidyapith.org/dcs/library.php")

    if button_choice=="1.2.2.1.5":
         mydb.gvpbot.update_one({"_id":uid},{"$inc":{"MCAPlacement_English":1}},upsert=True)
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Placement Details Click on this link : https://gujaratvidyapith.org/dcs/placement.php")
    
    if button_choice=='1.2.2.1.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="INTAKE : 60 Students")
    if button_choice=='1.2.2.1.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="DURATION : 2 Years (Four Semester)")
    if button_choice=='1.2.2.1.1.1':
         mydb.gvpbot.update_one({"_id":uid},{"$inc":{"MCAFee_English":1}},upsert=True)
         await context.bot.send_message(chat_id=update.effective_chat.id, text="FEES : Approx 10,000 /- Per Year..")
    if button_choice=='1.2.2.1.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ELIGIBILITY : BCA / Bachelor Degree in Computer Science, Engineering or Equivalent Degree. OR B.Sc. / B.Com. / B.A. with mathematics at 10+2 level or at Graduation level (With additional bridge courses as per the norms of the concerned university). Obtained at least 50% marks (45% marks in case of candidates belonging to reserved category) in the qualifying examination.")

    #BCA
    if button_choice=='1.2.1.1':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"BCA_English":1}},upsert=True)
        await bca(update,context)
    if button_choice=='1.2.1.1.1':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"BCAAdmission_English":1}},upsert=True)
        await bca_admission(update,context)
    if button_choice=='bca_back':
        await ug(update,context)
    if button_choice=="bca_home":
        await english_button(update,context)
    if button_choice=='1.2.1.1.2':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"BCASyllabus_English":1}},upsert=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Syllabus : Not Available Now")
    if button_choice=='1.2.1.1.3':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"BCAFaculty_English":1}},upsert=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="For Faculty Details Click The Following Link. https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='1.2.1.1.4':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"BCAFacilities_English":1}},upsert=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="FACILITIES PROVIDED BY DEPARTMENT OF COMPUTER SCIENCE")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Software Development : https://gujaratvidyapith.org/dcs/swlab.php")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Internet of Things : https://gujaratvidyapith.org/dcs/iotlab.php")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Machine Learning : https://gujaratvidyapith.org/dcs/mllab.php")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Cyber Security : https://gujaratvidyapith.org/dcs/cslab.php")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Library : https://gujaratvidyapith.org/dcs/library.php")

    #PGDCA
    if button_choice=="diploma_back":
        await academic(update,context)
    if button_choice=='pgdca_back':
        await diploma(update,context)
    if button_choice=="pgdca_home":
        await english_button(update,context)
    if button_choice=='1.2.4.3':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"PGDCA_English":1}},upsert=True)
        await pgdca(update,context)
    if button_choice=='1.2.4.3.1':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"PGDCAAdmission_English":1}},upsert=True)
        await pgdca_admission(update,context)
    if button_choice=='1.2.4.3.2':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"PGDCASyllabus_English":1}},upsert=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Syllabus : https://gujaratvidyapith.org/dcs/syllabus.php")
    if button_choice=='1.2.4.3.3':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"PGDCAFaculty_English":1}},upsert=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="For Faculty Details Click The Following Link. https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='1.2.4.3.4':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"PGDCAFacilities_English":1}},upsert=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="FACILITIES PROVIDED BY DEPARTMENT OF COMPUTER SCIENCE")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Software Development : https://gujaratvidyapith.org/dcs/swlab.php")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Internet of Things : https://gujaratvidyapith.org/dcs/iotlab.php")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Machine Learning : https://gujaratvidyapith.org/dcs/mllab.php")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Cyber Security : https://gujaratvidyapith.org/dcs/cslab.php")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Library : https://gujaratvidyapith.org/dcs/library.php")

    #CSPT
    if button_choice=="certi_back":
        await academic(update,context)
    if button_choice=='cspt_back':
        await certificate(update,context)
    if button_choice=="cspt_home":
        await english_button(update,context)
    if button_choice=='1.2.3.6':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"CSPT_English":1}},upsert=True)
        await cspt(update,context)
    if button_choice=='1.2.3.6.1':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"CSPTAdmission_English":1}},upsert=True)
        await cspt_admission(update,context)
    if button_choice=='1.2.3.6.2':
        mydb.gvpbot.update_one({"_id":uid},{"$inc":{"CSPTSyllabus_English":1}},upsert=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Syllabus : https://gujaratvidyapith.org/usic/Solar%20Syllabus.pdf")
    # if button_choice=='1.2.3.6.3':
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text="For Faculty Details Click The Following Link. https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='1.2.3.6.4':
         mydb.gvpbot.update_one({"_id":uid},{"$inc":{"CSPTFacilities_English":1}},upsert=True)
         await context.bot.send_message(chat_id=update.effective_chat.id, text="FACILITIES PROVIDED BY USIC Department")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Library Facilities \nLaboratory Facilities")

    #Administration
    if button_choice=="admin_back":
        await english_button(update,context)
    if button_choice=='1.3.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Information of Governing Council Click on this link: https://gujaratvidyapith.org/admin.htm")
    if button_choice=='1.3.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Information about Chancellors Click on this link: https://gujaratvidyapith.org/chancellor.htm")
    if button_choice=='1.3.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Information about Vice-Chancellors Click on this link: https://gujaratvidyapith.org/vice-chancellors.htm")
    if button_choice=='1.3.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Information about Registrars Click on this link: https://gujaratvidyapith.org/registrars.htm")

    #Library
    if button_choice=="lib_back":
        await english_button(update,context)
    if button_choice=='1.4.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Central Library Information : https://gujaratvidyapith.org/centrallibrary.htm")
    if button_choice=='1.4.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Online Library Access  : http://192.168.205.201/webopac/")
    if button_choice=='1.4.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Book Catalogue Searching : http://library.gujaratvidyapith.org/LibrarySystem/")
    if button_choice=='1.4.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Membership Registration Form : http://links.gujaratvidyapith.org/LibrarySystem/MembershipRegistrationform.pdf")
    if button_choice=='1.4.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Book Purchase Request Form : http://links.gujaratvidyapith.org/LibrarySystem/BookPurchaseRequestForm.pdf")
    
    #sports
    
    if button_choice=='1.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="SPORTS : \n\nAhmedabad and two other campuses have running track of 400 mtr. There are different grounds for outdoor sports such as Volleyball, Basketball, Handball, Kabaddi, Kho-Kho, Badminton, and Netball. In addition, Vidyapith also has Gymnasium and Swimming pool. All these facilities are being utilised by students, staff and also by citizens.\n\nSadra campus has well known, well developed physical education college where B.PEd and M.PEd courses are offered. There are separate grounds for Cricket, Volleyball, Basketball and Football. A big Gymnasium hall of national standard prepares the students to compete at higher level. A big open stadium is also available at Sadra campus. A well facilitated indoor stadium for Tennis, Carom, and Weight lifting is also available. The impressive facilities of the physical education department including a large variety of sports and necessary equipment for students under the able guidance and supervision of highly qualified teachers acts as a positive incentive for the students.\n\nGujarat Vidyapith have 4 Multipurpose Play Ground, 1 Tennis, 7 Volley Ball, 2 Basket Ball, 2 Hand Bal, 4 Kabaddi, 2 Kho-Kho, 3 Badminton and 1 Net Ball Courts for Indoor and Outdoor games. 2 400 meters Tracks and Fields, 2 Gymnasium and 2 Outdoor Stadium.")

    #up coming program

    if button_choice=='1.6':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="UPCOMING PROGRAM : ")

    #Rural center
    if button_choice=='1.7':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="UPCOMING PROGRAM : ")

    #KVK
    if button_choice=='1.8':
        await kvk(update, context)
    if button_choice=='1.8.1':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://gvkvkkheda.org/Faculty.php")
    if button_choice=='1.8.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://www.kvkgandhinagar.org/aboutkvk.php")
    if button_choice=='1.8.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://www.kvkvalsad.org/")
    if button_choice=='kvk_back':
        await english_button(update,context)

    #Meseum
    if button_choice=='1.9':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="UPCOMING PROGRAM : ")

    #heritage walk
    if button_choice=='1.10':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="For Registration of Gujarat Vidyapith Heritage Walk Register Here : https://docs.google.com/forms/d/e/1FAIpQLScitYUHLuLPjKQzwtvvUB13HQVBlYtVCAPQaxV0Fe-n_fbEUg/viewform")

    if button_choice=='0':
        await back(update,context)
        

    ##### GUJARATI #####

    # About us
    if button_choice=="2.1":
        await about_us_guj(update,context)
    if button_choice=="about_back_guj":
        await gujrati_button(update,context)
    
    if button_choice=='2.1.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ઝાંખી માટે અહીં ક્લિક કરો. https://www.gujaratvidyapith.org/overview.htm")
    if button_choice=='2.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ઇતિહાસ માટે અહીં ક્લિક કરો. https://www.gujaratvidyapith.org/history.htm")
    if button_choice=='2.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="સામાન્ય માહિતી માટે અહીં ક્લિક કરો. https://www.gujaratvidyapith.org/roadmap.htm")
    if button_choice=='2.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="મૂલ્યો માટે અહીં ક્લિક કરો. https://www.gujaratvidyapith.org/values.htm")
    if button_choice=='2.1.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="પ્રતીક માટે અહીં ક્લિક કરો. https://www.gujaratvidyapith.org/emblem.htm")
    if button_choice=='2.1.6':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="વાર્ષિક હિસાબ માટે અહીં ક્લિક કરો. https://www.gujaratvidyapith.org/annualreportsaccounts.htm")
    if button_choice=='2.1.7':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="IIQA ઉપક્રમ માટે અહીં ક્લિક કરો. https://gujaratvidyapith.org/newsandevents/IIQA%20Undertaking.pdf")


    #acedemic gujrati
    if button_choice=="aca_back_guj":
        await gujrati_button(update,context)
    if button_choice=="ug_back_guj":
        await academic_guj(update,context)
    if button_choice=='2.2':
       await academic_guj(update,context)
    if button_choice=='2.2.1':
        await ug_guj(update,context)
    if button_choice=='2.2.2':
        await pg_guj(update,context)
    if button_choice=='2.2.3':
        await certificate_guj(update,context)
    if button_choice=='2.2.4':
        await diploma_guj(update,context)
    
    #MCA GUJ
    if button_choice=="mca_back_guj":
        await pg_guj(update,context)
    if button_choice=="mca_home_guj":
        await gujrati_button(update,context) 
    if button_choice=="pg_back_guj":
        await academic_guj(update,context)
    if button_choice=="pg_home_guj":
        await gujrati_button(update,context) 
    if button_choice=='2.2.2.1':
        await mca_guj(update,context)
    if button_choice=='2.2.2.1.1':
        await mca_admission_guj(update,context)
    if button_choice=='2.2.2.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="અભ્યાસક્રમ તપાસવા માટે નીચેની લિંક પર ક્લિક કરો : https://gujaratvidyapith.org/dcs/syllabus.php")
    if button_choice=='2.2.2.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ફેકલ્ટી વિગતો માટે નીચેની લિંક પર ક્લિક કરો : https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='2.2.2.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="કોમ્પ્યુટર સાયન્સ વિભાગ દ્વારા પૂરી પાડવામાં આવતી સુવિધાઓ")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="સોફ્ટવેર ડેવેલોપેમેન્ટ : https://gujaratvidyapith.org/dcs/swlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ઈન્ટરનેટ ઓફ થિંગ્સ : https://gujaratvidyapith.org/dcs/iotlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="મશીન લર્નિંગ : https://gujaratvidyapith.org/dcs/mllab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="સાયબર સેક્યુરીટી : https://gujaratvidyapith.org/dcs/cslab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="પુસ્તકાલય : https://gujaratvidyapith.org/dcs/library.php")
    if button_choice=="2.2.2.1.5":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="પ્લેસમેન્ટની વિગતો માટે આ લિંક પર ક્લિક કરો : https://gujaratvidyapith.org/dcs/placement.php")
    if button_choice=='2.2.2.1.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ઇન્ટેક : 60 વિદ્યાર્થીઓ")
    if button_choice=='2.2.2.1.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="સમયગાળો : 2 વર્ષ (ચાર સેમેસ્ટર)")
    if button_choice=='2.2.2.1.1.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ફી : 12050 પ્રતિ વર્ષ")
    if button_choice=='2.2.2.1.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="લાયકાત : કમ્પ્યુટર સાયન્સ, એન્જિનિયરિંગ અથવા સમકક્ષ ડિગ્રીમાં BCA / બેચલર ડિગ્રી. અથવા B.Sc. / બી.કોમ. / B.A. 10+2 સ્તરે અથવા સ્નાતક સ્તરે ગણિત સાથે (સંબંધિત યુનિવર્સિટીના ધોરણો અનુસાર વધારાના બ્રિજ અભ્યાસક્રમો સાથે). લાયકાતની પરીક્ષામાં ઓછામાં ઓછા 50% ગુણ (અનામત વર્ગના ઉમેદવારોના કિસ્સામાં 45% ગુણ) મેળવ્યા.")

    # BCA Guj
    if button_choice=="bca_back_guj":
        await ug_guj(update,context)
    if button_choice=="bca_home_guj":
        await gujrati_button(update,context)
    if button_choice=='2.2.1.1':
        await bca_guj(update,context)
    if button_choice=='2.2.1.1.1':
        await bca_admission_guj(update,context)
    if button_choice=='2.2.1.1.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="અભ્યાસક્રમ : --")
    if button_choice=='2.2.1.1.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="ફેકલ્ટી વિગતો માટે નીચેની લિંક પર ક્લિક કરો : https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='2.2.1.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="કોમ્પ્યુટર સાયન્સ વિભાગ દ્વારા પૂરી પાડવામાં આવતી સુવિધાઓ")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="સોફ્ટવેર ડેવેલોપેમેન્ટ : https://gujaratvidyapith.org/dcs/swlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ઈન્ટરનેટ ઓફ થિંગ્સ : https://gujaratvidyapith.org/dcs/iotlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="મશીન લર્નિંગ : https://gujaratvidyapith.org/dcs/mllab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="સાયબર સેક્યુરીટી : https://gujaratvidyapith.org/dcs/cslab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="પુસ્તકાલય : https://gujaratvidyapith.org/dcs/library.php")

    #PDGCA Guj
    if button_choice=="pgdca_back_guj":
        await diploma_guj(update,context)
    if button_choice=="pgdca_home_guj":
        await gujrati_button(update,context)
    if button_choice=="dip_back_guj":
        await academic_guj(update,context)
    if button_choice=='2.2.4.3':
        await pgdca_guj(update,context)
    if button_choice=='2.2.4.3.1':
        await pgdca_admission_guj(update,context)
    if button_choice=='2.2.4.3.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="અભ્યાસક્રમ : https://gujaratvidyapith.org/dcs/syllabus.php")
    if button_choice=='2.2.4.3.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="ફેકલ્ટી વિગતો માટે નીચેની લિંક પર ક્લિક કરો : https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='2.2.4.3.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="કોમ્પ્યુટર સાયન્સ વિભાગ દ્વારા પૂરી પાડવામાં આવતી સુવિધાઓ")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="સોફ્ટવેર ડેવેલોપેમેન્ટ : https://gujaratvidyapith.org/dcs/swlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ઈન્ટરનેટ ઓફ થિંગ્સ : https://gujaratvidyapith.org/dcs/iotlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="મશીન લર્નિંગ : https://gujaratvidyapith.org/dcs/mllab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="સાયબર સેક્યુરીટી : https://gujaratvidyapith.org/dcs/cslab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="પુસ્તકાલય : https://gujaratvidyapith.org/dcs/library.php")

    # CSPT GUJ
    if button_choice=="cspt_back_guj":
        await certificate_guj(update,context)
    if button_choice=="cspt_home_guj":
        await gujrati_button(update,context)
    if button_choice=="certi_back_guj":
        await academic_guj(update,context)
    if button_choice=='2.2.3.6':
        await cspt_guj(update,context)
    if button_choice=='2.2.3.6.1':
        await cspt_admission_guj(update,context)
    if button_choice=='2.2.3.6.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="અભ્યાસક્રમ : https://gujaratvidyapith.org/usic/Solar%20Syllabus.pdf")
    # if button_choice=='1.2.3.6.3':
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text="For Faculty Details Click The Following Link. https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='2.2.3.6.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="USIC વિભાગ દ્વારા પૂરી પાડવામાં આવતી સુવિધાઓ")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="લાયબ્રેરી સુવિધાઓ \nલેબોરેટરી સુવિધાઓ")

    #administration
    if button_choice=="admin_back_guj":
        await gujrati_button(update,context)
    if button_choice=="2.3":
        await administration_guj(update, context)
    if button_choice=='2.3.1':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="ગવર્નિંગ કાઉન્સિલ માટે અહીં ક્લિક કરો : https://gujaratvidyapith.org/admin.htm")
    if button_choice=='2.3.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="ચાન્સેલરો માટે અહીં ક્લિક કરો : https://gujaratvidyapith.org/chancellor.htm")
    if button_choice=='2.3.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="વાઇસ ચાન્સેલર માટે અહીં ક્લિક કરો : https://gujaratvidyapith.org/vice-chancellors.htm")
    if button_choice=='2.3.4':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="રજીસ્ટ્રાર માટે અહીં ક્લિક કરો : https://gujaratvidyapith.org/registrars.htm")

    #Library
    if button_choice=="lib_back_guj":
        await gujrati_button(update,context)
    if button_choice=='2.4':
        await library_guj(update,context)
    if button_choice=='2.4.1':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="કેન્દ્રીય પુસ્તકાલય માટે અહીં ક્લિક કરો : https://gujaratvidyapith.org/centrallibrary.htm")
    if button_choice=='2.4.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="ઓનલાઈન લાઈબ્રેરી એક્સેસ માટે અહીં ક્લિક કરો  : http://192.168.205.201/webopac/")
    if button_choice=='2.4.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="પુસ્તકો કેટલોગ શોધ માટે અહીં ક્લિક કરો : http://library.gujaratvidyapith.org/LibrarySystem/")
    if button_choice=='2.4.4':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="સભ્યપદ ફોર્મ માટે અહીં ક્લિક કરો : http://links.gujaratvidyapith.org/LibrarySystem/MembershipRegistrationform.pdf")
    if button_choice=='2.4.5':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="પુસ્તક ખરીદી ફોર્મ માટે અહીં ક્લિક કરો : http://links.gujaratvidyapith.org/LibrarySystem/BookPurchaseRequestForm.pdf")
    
    #Sports Gujarati
    
    if button_choice=='2.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="રમતગમત : \nઅમદાવાદ અને અન્ય બે કેમ્પસમાં 400 મીટરનો રનિંગ ટ્રેક છે. વોલીબોલ, બાસ્કેટબોલ, હેન્ડબોલ, કબડ્ડી, ખો-ખો, બેડમિન્ટન અને નેટબોલ જેવી આઉટડોર રમતો માટે અલગ અલગ મેદાન છે. આ ઉપરાંત વિદ્યાપીઠમાં જિમ્નેશિયમ અને સ્વિમિંગ પૂલ પણ છે. આ તમામ સુવિધાઓનો વિદ્યાર્થીઓ, સ્ટાફ અને નાગરિકો દ્વારા પણ ઉપયોગ કરવામાં આવી રહ્યો છે.\n\nસાદરા કેમ્પસમાં જાણીતી, સારી રીતે વિકસિત શારીરિક શિક્ષણ કોલેજ છે જ્યાં B.PEd અને M.PEd અભ્યાસક્રમો આપવામાં આવે છે. ક્રિકેટ, વોલીબોલ, બાસ્કેટબોલ અને ફૂટબોલ માટે અલગ મેદાન છે. રાષ્ટ્રીય ધોરણનો મોટો જિમ્નેશિયમ હોલ વિદ્યાર્થીઓને ઉચ્ચ સ્તરે સ્પર્ધા કરવા માટે તૈયાર કરે છે. સાદરા કેમ્પસમાં એક મોટું ઓપન સ્ટેડિયમ પણ ઉપલબ્ધ છે. ટેનિસ, કેરમ અને વેઇટ લિફ્ટિંગ માટે સારી સુવિધાયુક્ત ઇન્ડોર સ્ટેડિયમ પણ ઉપલબ્ધ છે. ઉચ્ચ લાયકાત ધરાવતા શિક્ષકોના સક્ષમ માર્ગદર્શન અને દેખરેખ હેઠળ વિદ્યાર્થીઓ માટે વિવિધ પ્રકારની રમતો અને જરૂરી સાધનો સહિત શારીરિક શિક્ષણ વિભાગની પ્રભાવશાળી સુવિધાઓ વિદ્યાર્થીઓ માટે સકારાત્મક પ્રોત્સાહન તરીકે કામ કરે છે.\n\nગુજરાત વિદ્યાપીઠ પાસે 4 બહુહેતુક પ્લે ગ્રાઉન્ડ છે, 1 ઇન્ડોર અને આઉટડોર રમતો માટે ટેનિસ, 7 વોલી બોલ, 2 બાસ્કેટ બોલ, 2 હેન્ડ બોલ, 4 કબડ્ડી, 2 ખો-ખો, 3 બેડમિન્ટન અને 1 નેટ બોલ કોર્ટ. 2 400 મીટર ટ્રેક અને ફિલ્ડ્સ, 2 જિમ્નેશિયમ અને 2 આઉટડોર સ્ટેડિયમ.")

    #KVK Gujarati
    if button_choice=='2.8.1':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://gvkvkkheda.org/Faculty.php")
    if button_choice=='2.8.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://www.kvkgandhinagar.org/aboutkvk.php")
    if button_choice=='2.8.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://www.kvkvalsad.org/")
    if button_choice=='kvk_back_guj':
        await gujrati_button(update,context)

    ##### HINDI #####

    if button_choice=='back_hin':
        await back(update,context)

    # About us Hindi
    if button_choice=="back_about_hin":
        await hindi_button(update,context)
    if button_choice=="ug_back_hin":
        await academic_hin(update,context)
    if button_choice=="3.1":
        await about_us_hin(update,context)
    if button_choice=='3.1.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="अवलोकन के लिए यहां क्लिक करें : https://www.gujaratvidyapith.org/overview.htm")
    if button_choice=='3.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="इतिहास के लिए यहां क्लिक करें : https://www.gujaratvidyapith.org/history.htm")
    if button_choice=='3.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="सामान्य जानकारी के लिए यहां क्लिक करें : https://www.gujaratvidyapith.org/roadmap.htm")
    if button_choice=='3.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="मूल्यों के लिए यहां क्लिक करें : https://www.gujaratvidyapith.org/values.htm")
    if button_choice=='3.1.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="प्रतीक के लिए यहां क्लिक करें : https://www.gujaratvidyapith.org/emblem.htm")
    if button_choice=='3.1.6':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="वार्षिक रिपोर्ट के लिए यहां क्लिक करें : https://www.gujaratvidyapith.org/annualreportsaccounts.htm")
    if button_choice=='3.1.7':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="IIQA उपक्रम के लिए यहां क्लिक करें : https://gujaratvidyapith.org/newsandevents/IIQA%20Undertaking.pdf")

    #acedemic hindi
    if button_choice=="aca_back_hin":
        await hindi_button(update,context)
    if button_choice=='3.2':
       await academic_hin(update,context)
    if button_choice=='3.2.1':
        await ug_hin(update,context)
    if button_choice=='3.2.2':
        await pg_hin(update,context)
    if button_choice=='3.2.3':
        await certificate_hin(update,context)
    if button_choice=='3.2.4':
        await diploma_hin(update,context)
    
    #MCA Hindi
    if button_choice=="mca_back_hin":
        await pg_hin(update,context)
    if button_choice=="mca_home_hin":
        await hindi_button(update,context) 
    if button_choice=='3.2.2.1':
        await mca_hin(update,context)
    if button_choice=='3.2.2.1.1':
        await mca_admission_hin(update,context)
    if button_choice=='3.2.2.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="कोर्स चेक करने के लिए नीचे दिए गए लिंक पर क्लिक करें: https://gujaratvidyapith.org/dcs/syllabus.php")
    if button_choice=='3.2.2.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="शिक्षक विवरण के लिए निम्न लिंक पर क्लिक करें: https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='3.2.2.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="कंप्यूटर विज्ञान विभाग द्वारा प्रदान की जाने वाली सुविधाएं")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="सॉफ्टवेयर डेवलपमेंट : https://gujaratvidyapith.org/dcs/swlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="इंटरनेट ऑफ थिंग्स : https://gujaratvidyapith.org/dcs/iotlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="मशीन लर्निंग : https://gujaratvidyapith.org/dcs/mllab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="साइबर सुरक्षा : https://gujaratvidyapith.org/dcs/cslab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="पुस्तकालय : https://gujaratvidyapith.org/dcs/library.php")
    if button_choice=="3.2.2.1.5":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="प्लेसमेंट विवरण के लिए इस लिंक पर क्लिक करें : https://gujaratvidyapith.org/dcs/placement.php")
    if button_choice=='3.2.2.1.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="दाखिले : 60 छात्र")
    if button_choice=='3.2.2.1.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="अवधि: 2 साल (चार सेमेस्टर)")
    if button_choice=='3.2.2.1.1.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="शुल्क: 12050 प्रति वर्ष")
    if button_choice=='3.2.2.1.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="योग्यता: बीसीए / कंप्यूटर साइंस, इंजीनियरिंग या समकक्ष में स्नातक की डिग्री। या बी.एससी. / बी.कॉम. / बी ० ए। गणित के साथ 10 + 2 स्तर पर या स्नातक स्तर पर (संबंधित विश्वविद्यालय के मानकों के अनुसार अतिरिक्त ब्रिज कोर्स के साथ)। अर्हक परीक्षा में कम से कम 50% अंक (आरक्षित वर्ग के उम्मीदवारों के मामले में 45% अंक) प्राप्त किए।")

    # BCA Hindi
    if button_choice=="bca_back_hin":
        await ug_hin(update,context)
    if button_choice=="bca_home_hin":
        await hindi_button(update,context) 
    if button_choice=='3.2.1.1':
        await bca_hin(update,context)
    if button_choice=='3.2.1.1.1':
        await bca_admission_hin(update,context)
    if button_choice=='3.2.1.1.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="पाठ्यक्रम : --")
    if button_choice=='3.2.1.1.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="शिक्षक विवरण के लिए निम्न लिंक पर क्लिक करें: https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='3.2.1.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="कंप्यूटर विज्ञान विभाग द्वारा प्रदान की जाने वाली सुविधाएं")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="सॉफ्टवेयर डेवलपमेंट : https://gujaratvidyapith.org/dcs/swlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="इंटरनेट ऑफ थिंग्स : https://gujaratvidyapith.org/dcs/iotlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="मशीन लर्निंग : https://gujaratvidyapith.org/dcs/mllab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="साइबर सुरक्षा : https://gujaratvidyapith.org/dcs/cslab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="पुस्तकालय : https://gujaratvidyapith.org/dcs/library.php")

    #PDGCA Hindi
    if button_choice=="pgdca_back_hin":
        await diploma_hin(update,context)
    if button_choice=="pgdca_home_hin":
        await hindi_button(update,context) 
    if button_choice=='3.2.4.3':
        await pgdca_hin(update,context)
    if button_choice=='3.2.4.3.1':
        await pgdca_admission_hin(update,context)
    if button_choice=='3.2.4.3.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="पाठ्यक्रम : https://gujaratvidyapith.org/dcs/syllabus.php")
    if button_choice=='3.2.4.3.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="शिक्षक विवरण के लिए निम्न लिंक पर क्लिक करें: https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='3.2.4.3.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="कंप्यूटर विज्ञान विभाग द्वारा प्रदान की जाने वाली सुविधाएं")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="सॉफ्टवेयर डेवलपमेंट : https://gujaratvidyapith.org/dcs/swlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="इंटरनेट ऑफ थिंग्स : https://gujaratvidyapith.org/dcs/iotlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="मशीन लर्निंग : https://gujaratvidyapith.org/dcs/mllab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="साइबर सुरक्षा : https://gujaratvidyapith.org/dcs/cslab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="पुस्तकालय : https://gujaratvidyapith.org/dcs/library.php")

    # CSPT Hindi
    if button_choice=="cspt_back_hin":
        await certificate_hin(update,context)
    if button_choice=="cspt_home_hin":
        await hindi_button(update,context) 
    if button_choice=='3.2.3.6':
        await cspt_hin(update,context)
    if button_choice=='3.2.3.6.1':
        await cspt_admission_hin(update,context)
    if button_choice=='3.2.3.6.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="पाठ्यक्रम : https://gujaratvidyapith.org/usic/Solar%20Syllabus.pdf")
    # if button_choice=='1.2.3.6.3':
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text="For Faculty Details Click The Following Link. https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='3.2.3.6.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="USIC विभाग द्वारा प्रदान की जाने वाली सुविधाएं")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="पुस्तकालय सुविधाएं \nप्रयोगशाला सुविधाएं")

    #administration Hindi
    if button_choice=="admin_back_hin":
        await hindi_button(update,context)
    if button_choice=="3.3":
        await administration_hin(update, context)
    if button_choice=='3.3.1':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="गवर्निंग काउंसिल के लिए यहां क्लिक करें : https://gujaratvidyapith.org/admin.htm")
    if button_choice=='3.3.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="कुलपति के लिए यहां क्लिक करें : https://gujaratvidyapith.org/chancellor.htm")
    if button_choice=='3.3.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="उपाध्यक्ष कुलपति के लिए यहां क्लिक करें : https://gujaratvidyapith.org/vice-chancellors.htm")
    if button_choice=='3.3.4':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="रजिस्ट्रार के लिए यहां क्लिक करें : https://gujaratvidyapith.org/registrars.htm")

    #Library Hindi
    if button_choice=="lib_back_hin":
        await hindi_button(update,context)
    if button_choice=='3.4':
        await library_hin(update,context)
    if button_choice=='3.4.1':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="केंद्रीय पुस्तकालय के लिए यहां क्लिक करें : https://gujaratvidyapith.org/centrallibrary.htm")
    if button_choice=='3.4.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="ऑनलाइन लाइब्रेरी तक पहुंचने के लिए यहां क्लिक करें : http://192.168.205.201/webopac/")
    if button_choice=='3.4.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="किताबों की सूची खोजने के लिए यहां क्लिक करें : http://library.gujaratvidyapith.org/LibrarySystem/")
    if button_choice=='3.4.4':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="सदस्यता फॉर्म के लिए यहां क्लिक करें : http://links.gujaratvidyapith.org/LibrarySystem/MembershipRegistrationform.pdf")
    if button_choice=='3.4.5':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="पुस्तक खरीद फॉर्म के लिए यहां क्लिक करें : http://links.gujaratvidyapith.org/LibrarySystem/BookPurchaseRequestForm.pdf")
    
    #Sports Hindi
    
    if button_choice=='3.5':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="खेल-कूद : \nअहमदाबाद और दो अन्य परिसरों में 400 मीटर रनिंग ट्रैक है। वॉलीबॉल, बास्केटबॉल, हैंडबॉल, कबड्डी, खो-खो, बैडमिंटन और नेटबॉल जैसे आउटडोर खेलों के लिए अलग-अलग मैदान हैं। विश्वविद्यालय में एक व्यायामशाला और एक स्विमिंग पूल भी है। इन सभी सुविधाओं का उपयोग छात्र, कर्मचारी और नागरिक भी कर रहे हैं। \n\nसदरा कैंपस में एक प्रसिद्ध, अच्छी तरह से विकसित शारीरिक शिक्षा कॉलेज है जहाँ B.PEd और M.PEd पाठ्यक्रम पेश किए जाते हैं। क्रिकेट, वॉलीबॉल, बास्केटबॉल और फुटबॉल के लिए अलग-अलग मैदान हैं। बड़ा राष्ट्रीय मानक व्यायामशाला हॉल छात्रों को उच्च स्तर पर प्रतिस्पर्धा करने के लिए तैयार करता है। मुख्य परिसर में एक बड़ा खुला स्टेडियम भी उपलब्ध है। टेनिस, कैरम और भारोत्तोलन के लिए एक सुसज्जित इनडोर स्टेडियम भी है। शारीरिक शिक्षा विभाग की प्रभावशाली सुविधाएं, जिसमें विभिन्न प्रकार के खेल और उच्च योग्य शिक्षकों के सक्षम मार्गदर्शन और पर्यवेक्षण के तहत छात्रों के लिए आवश्यक उपकरण शामिल हैं, छात्रों के लिए एक सकारात्मक प्रोत्साहन के रूप में कार्य करते हैं। \n\nगुजरात विश्वविद्यालय में 4 बहुउद्देश्यीय खेल के मैदान हैं, 1 इनडोर और आउटडोर खेलों के लिए, टेनिस, 7 वॉलीबॉल, 2 बास्केटबॉल, 2 हैंड बॉल, 4 कबड्डी, 2 खो-खो, 3 बैडमिंटन और 1 नेट बॉल कोर्ट। 2 400 मीटर ट्रैक और फील्ड, 2 व्यायामशाला और 2 आउटडोर स्टेडियम।")

    #KVK Gujarati
    if button_choice=='3.8.1':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://gvkvkkheda.org/Faculty.php")
    if button_choice=='3.8.2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://www.kvkgandhinagar.org/aboutkvk.php")
    if button_choice=='3.8.3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="http://www.kvkvalsad.org/")
    if button_choice=='kvk_back_hin':
        await hindi_button(update,context)

async def reply(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="To Clear History Click on Three dots at top right croner and click on clear history, you can also stop the bot from that menu. \nTo cancel the chat send /cancel .")


async def back(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="1"),
            InlineKeyboardButton("ગુજરાતી", callback_data="2"),
        ],
        [InlineKeyboardButton("हिन्दी", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id,text="Please Choose Language:", reply_markup=reply_markup)
# 5547103630:AAFafbPlUAPFcr3tCdhkdYQpJd8V23SPIB0 Akash
# 5329459226:AAFmA9lwqHDhb1kdmvM97sBTwVEhJm0ca7Q Nikhil
if __name__ == '__main__':
    application = ApplicationBuilder().token('5329459226:AAFmA9lwqHDhb1kdmvM97sBTwVEhJm0ca7Q').build()
    
    # application.add_handler(CallbackQueryHandler(gender))
    # application.add_handler(CallbackQueryHandler(address))
    # application.add_handler(CallbackQueryHandler(email))
    # application.add_handler(CallbackQueryHandler(phone))
    application.add_handler(CallbackQueryHandler(button))
    
    # Add conversation handler with the states GENDER, Address, Email and Phone
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            GENDER: [MessageHandler(filters.Regex("^(MALE|FEMALE)$"), gender)],
            ADDRESS: [
                        MessageHandler(filters.TEXT & ~filters.COMMAND, address),
                        CommandHandler("skip", skip_address)
                    ],
            EMAIL:  [
                        MessageHandler(filters.TEXT & ~filters.COMMAND, email),
                        CommandHandler("skip", skip_email)
                    ],
            PHONE:  [MessageHandler(filters.TEXT & ~filters.COMMAND, phone)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(CallbackQueryHandler(button))

    application.add_handler(conv_handler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,reply))
    
    application.run_polling()