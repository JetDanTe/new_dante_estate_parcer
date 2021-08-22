from telebot import types


# city state buttons
class CityStateButtons:
    od_button = types.InlineKeyboardButton(text='Одесса', callback_data='nextstate:OdessaState')
    ky_button = types.InlineKeyboardButton(text='Киев', callback_data='nextstate:KievState')
    kh_button = types.InlineKeyboardButton(text='Харьков', callback_data='nextstate:KharkovState')
    lv_button = types.InlineKeyboardButton(text='Львов', callback_data='nextstate:LvovState')


# price state buttons
class PriceStateButtons:
    f2t5State = types.InlineKeyboardButton(text='От 2000 до 5000', callback_data='nextstate:f2t5State')
    f5t7State = types.InlineKeyboardButton(text='От 5000 до 7000', callback_data='nextstate:f5t7State')
    f7t10State = types.InlineKeyboardButton(text='От 7000 до 10000', callback_data='nextstate:f7t10State')


# search state buttons
class SearchButton:
    search = types.InlineKeyboardButton(text='Начать поиск!', callback_data='nextstate:searchState')
