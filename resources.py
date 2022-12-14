# # # # # # # # # # # # CONSTANTS # # # # # # # # # # # #

en_to_en_file_path = './dictionaries/en-en.json'
en_to_amh_file_path = 'dictionaries/en-amh.json'
learned_json_file_path = "learned_db.json"

en_to_en_emoji = 'đ´ķ §ķ ĸķ Ĩķ Žķ §ķ ŋ' + ' to ' + 'đ´ķ §ķ ĸķ Ĩķ Žķ §ķ ŋ'
en_to_amh_emoji = 'đ´ķ §ķ ĸķ Ĩķ Žķ §ķ ŋ' + ' to ' + 'đĒđš'
gear_emoji = 'âī¸'
info_emoji = 'âšī¸'
computer_emoji = 'đ¨đŊâđģ'
bot_emoji = 'đ¤'
features_emoji = 'đģ'
search_emoji = 'đ'
book_emoji = 'đ'

modes = [{'emoji':en_to_en_emoji, 'file_path': en_to_en_file_path, 'buttons': ["{} Random", "{} Already learned", "{} Features", "{} Settings"]}, {'emoji':en_to_amh_emoji, 'file_path': en_to_amh_file_path, 'buttons': ["{} áĢáá°á áĩá á", "{} á¨áá á ááĩ á¨áááá¸á", "{} áá¸áŽáŊ", "{} ááĩá°áĢá¨áĢááŊ"]}]

contact = """
{} I'm Fikernew, a Programmer. I usually programm web-apps and ocasionally desktop tools. 
I program telegram bots just for fun. I can be serious, though đ. 
If you have a project for me, hit me up and we can definitely collaborate. 
You can find me at @fikernew. 
can't wait.""".format(computer_emoji)

description = """
{} This is your classic dictionary. 
It currently supports getting definitions for english words and getting amharic translations for english words.""".format(info_emoji)

features = """
{} Features currently in action are: 
1. {} searching, 
2. {} getting random words. 
3. {} knowing already learned words""".format(features_emoji, search_emoji, bot_emoji, book_emoji)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #