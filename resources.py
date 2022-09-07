# # # # # # # # # # # # CONSTANTS # # # # # # # # # # # #

en_to_en_file_path = './dictionaries/en-en.json'
en_to_amh_file_path = 'dictionaries/en-amh.json'
learned_json_file_path = "learned_db.json"

en_to_en_emoji = '🏴󠁧󠁢󠁥󠁮󠁧󠁿' + ' to ' + '🏴󠁧󠁢󠁥󠁮󠁧󠁿'
en_to_amh_emoji = '🏴󠁧󠁢󠁥󠁮󠁧󠁿' + ' to ' + '🇪🇹'
gear_emoji = '⚙️'
info_emoji = 'ℹ️'
computer_emoji = '👨🏽‍💻'
bot_emoji = '🤖'
features_emoji = '💻'
search_emoji = '🔍'
book_emoji = '📒'

modes = [{'emoji':en_to_en_emoji, 'file_path': en_to_en_file_path, 'buttons': ["{} Random", "{} Already learned", "{} Features", "{} Settings"]}, {'emoji':en_to_amh_emoji, 'file_path': en_to_amh_file_path, 'buttons': ["{} ራንደም ስጠኝ", "{} ከዚህ በፊት የማውቃቸው", "{} ፊቸሮች", "{} ማስተካከያዎች"]}]

contact = """
{} I'm Fikernew, a Programmer. I usually programm web-apps and ocasionally desktop tools. 
I program telegram bots just for fun. I can be serious, though 😁. 
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