# ------------- Import ----------------
from tkinter import *
from tkinter import ttk, messagebox
import requests
# ------------- Variable ----------------
countries = ['Germany', 'France', 'Italy', 'Russia', 'Spain', 'Netherlands', 'Belgium',
             'Sweden', 'Switzerland', 'Austria', 'Norway', 'Denmark', 'Greece', 'Poland', 'Finland',
             'China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 'Vietnam',
             'Turkey', 'Iran', 'United States', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Australia']

provinces = {
    'Germany': ['Baden-Württemberg', 'Bavaria', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg',
                     'Hesse', 'Lower Saxony', 'Mecklenburg-Vorpommern', 'North Rhine-Westphalia',
                     'Rhineland-Palatinate', 'Saarland', 'Saxony', 'Saxony-Anhalt', 'Schleswig-Holstein',
                     'Thuringia'],

    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg',
                    'Montpellier', 'Bordeaux', 'Lille', 'Rennes', 'Reims', 'Le Havre',
                    'Cergy-Pontoise', 'Saint-Étienne', 'Toulon', 'Angers', 'Grenoble',
                    'Dijon', 'Nîmes'],

    'Italy':  ['Abruzzo', 'Aosta Valley', 'Apulia', 'Basilicata', 'Calabria', 'Campania',
                   'Emilia-Romagna', 'Friuli-Venezia Giulia', 'Lazio', 'Liguria', 'Lombardy',
                   'Marche', 'Molise', 'Piedmont', 'Sardinia', 'Sicily', 'Trentino-South Tyrol',
                   'Tuscany', 'Umbria', 'Veneto'],

    'Russia': ['Altai Krai', 'Altai Republic', 'Amur Oblast', 'Arkhangelsk Oblast',
                    'Astrakhan Oblast', 'Belgorod Oblast', 'Bryansk Oblast', 'Chechen Republic',
                    'Chelyabinsk Oblast', 'Chukotka Autonomous Okrug', 'Chuvash Republic',
                    'Irkutsk Oblast', 'Ivanovo Oblast', 'Jewish Autonomous Oblast',
                    'Kabardino-Balkar Republic', 'Kaliningrad Oblast', 'Kaluga Oblast',
                    'Kamchatka Krai', 'Karachay-Cherkess Republic', 'Kemerovo Oblast',
                    'Khabarovsk Krai', 'Khakass Republic', 'Khanty-Mansi Autonomous Okrug',
                    'Kirov Oblast', 'Komi Republic', 'Kostroma Oblast', 'Krasnodar Krai',
                    'Krasnoyarsk Krai', 'Kurgan Oblast', 'Kursk Oblast', 'Leningrad Oblast',
                    'Lipetsk Oblast', 'Magadan Oblast', 'Mari El Republic', 'Moscow Oblast',
                    'Moscow', 'Murmansk Oblast', 'Nenets Autonomous Okrug', 'Nizhny Novgorod Oblast',
                    'Novgorod Oblast', 'Novosibirsk Oblast', 'Omsk Oblast', 'Orenburg Oblast',
                    'Oryol Oblast', 'Penza Oblast', 'Perm Krai', 'Primorsky Krai', 'Pskov Oblast',
                    'Republic of Adygea', 'Republic of Bashkortostan', 'Republic of Buryatia',
                    'Republic of Dagestan', 'Republic of Ingushetia', 'Republic of Kalmykia',
                    'Republic of Karelia', 'Republic of Khakassia', 'Republic of Mordovia',
                    'Republic of North Ossetia–Alania', 'Republic of Tatarstan', 'Rostov Oblast',
                    'Ryazan Oblast', 'Saint Petersburg', 'Sakha (Yakutia) Republic', 'Sakhalin Oblast',
                    'Samara Oblast', 'Saratov Oblast', 'Sevastopol', 'Smolensk Oblast', 'Stavropol Krai',
                    'Sverdlovsk Oblast', 'Tambov Oblast', 'Tomsk Oblast', 'Tula Oblast', 'Tver Oblast',
                    'Tyumen Oblast', 'Udmurt Republic', 'Ulyanovsk Oblast', 'Vladimir Oblast',
                    'Volgograd Oblast', 'Vologda Oblast', 'Voronezh Oblast', 'Yamalo-Nenets Autonomous Okrug',
                    'Yaroslavl Oblast', 'Zabaykalsky Krai'],

    'Spain': ['Andalusia', 'Aragon', 'Asturias', 'Balearic Islands', 'Basque Country',
                   'Canary Islands', 'Cantabria', 'Castille and León', 'Castille-La Mancha',
                   'Catalonia', 'Extremadura', 'Galicia', 'La Rioja', 'Madrid', 'Murcia',
                   'Navarre', 'Valencian Community'],

    'Netherlands': ['Drenthe', 'Flevoland', 'Friesland', 'Gelderland', 'Groningen',
                         'Limburg', 'North Brabant', 'North Holland', 'Overijssel',
                         'South Holland', 'Utrecht', 'Zeeland'],

    'Belgium': ['Antwerp', 'East Flanders', 'Flemish Brabant', 'Hainaut', 'Liège',
                     'Limburg', 'Luxembourg', 'Namur', 'Walloon Brabant', 'West Flanders'],

    'Sweden': ['Blekinge', 'Dalarna', 'Gotland', 'Gävleborg', 'Halland', 'Jämtland',
                    'Jönköping', 'Kalmar', 'Kronoberg', 'Norrbotten', 'Örebro', 'Östergötland',
                    'Skåne', 'Södermanland', 'Stockholm', 'Uppsala', 'Värmland', 'Västerbotten',
                    'Västernorrland', 'Västmanland', 'Västra Götaland'],

    'Switzerland': ['Aargau', 'Appenzell Ausserrhoden', 'Appenzell Innerrhoden',
                         'Basel-Landschaft', 'Basel-Stadt', 'Bern', 'Fribourg', 'Geneva',
                         'Glarus', 'Graubünden', 'Jura', 'Lucerne', 'Neuchâtel', 'Nidwalden',
                         'Obwalden', 'Schaffhausen', 'Schwyz', 'Solothurn', 'St. Gallen',
                         'Thurgau', 'Ticino', 'Uri', 'Valais', 'Vaud', 'Zug', 'Zurich'],

    'Austria': ['Burgenland', 'Carinthia', 'Lower Austria', 'Upper Austria', 'Salzburg',
                     'Styria', 'Tyrol', 'Vorarlberg', 'Vienna'],

    'Norway': ['Agder', 'Innlandet', 'Møre og Romsdal', 'Nordland', 'Oslo',
                    'Rogaland', 'Troms og Finnmark', 'Trøndelag', 'Vestfold og Telemark', 'Viken'],

    'Denmark': ['Capital Region of Denmark', 'Central Denmark Region', 'North Denmark Region',
                     'Region of Southern Denmark'],

    'Greece': ['Attica', 'Central Greece', 'Central Macedonia', 'Crete',
                    'Eastern Macedonia and Thrace', 'Epirus', 'Ionian Islands', 'Mount Athos',
                    'North Aegean', 'Peloponnese', 'South Aegean', 'Thessaly', 'Western Greece', 'Western Macedonia'],

    'Poland': ['Greater Poland Voivodeship', 'Kuyavian-Pomeranian Voivodeship',
                    'Lesser Poland Voivodeship', 'Łódź Voivodeship', 'Lower Silesian Voivodeship',
                    'Lublin Voivodeship', 'Lubusz Voivodeship', 'Masovian Voivodeship',
                    'Opole Voivodeship', 'Podkarpackie Voivodeship', 'Podlaskie Voivodeship',
                    'Pomeranian Voivodeship', 'Silesian Voivodeship', 'Subcarpathian Voivodeship',
                    'Swietokrzyskie Voivodeship', 'Warmian-Masurian Voivodeship', 'West Pomeranian Voivodeship'],

    'Finland': ['Åland Islands', 'Central Finland', 'Central Ostrobothnia', 'Kainuu',
                     'Kanta-Häme', 'Kymenlaakso', 'Lapland', 'North Karelia', 'Northern Ostrobothnia',
                     'Northern Savonia', 'Ostrobothnia', 'Päijät-Häme', 'Pirkanmaa', 'Satakunta',
                     'South Karelia', 'South Ostrobothnia', 'Southern Savonia', 'Tavastia Proper', 'Uusimaa'],

    'China': ['Anhui', 'Fujian', 'Gansu', 'Guangdong', 'Guizhou', 'Hainan', 'Hebei',
                   'Heilongjiang', 'Henan', 'Hubei', 'Hunan', 'Jiangsu', 'Jiangxi', 'Jilin',
                   'Liaoning', 'Qinghai', 'Shaanxi', 'Shandong', 'Shanxi', 'Sichuan', 'Taiwan',
                   'Tibet', 'Xinjiang', 'Yunnan', 'Zhejiang', 'Beijing', 'Chongqing', 'Shanghai', 'Tianjin'],

    'India': ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh',
                   'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu',
                   'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
                   'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra',
                   'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab',
                   'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                   'Uttarakhand', 'West Bengal'],

    'Indonesia': ['Aceh', 'Bali', 'Bangka Belitung Islands', 'Banten', 'Bengkulu',
                       'Central Java', 'Central Kalimantan', 'Central Sulawesi',
                       'East Java', 'East Kalimantan', 'East Nusa Tenggara',
                       'Gorontalo', 'Jakarta', 'Jambi', 'Lampung', 'Maluku',
                       'North Kalimantan', 'North Maluku', 'North Sulawesi', 'North Sumatra',
                       'Papua', 'Riau', 'Riau Islands', 'South Kalimantan', 'South Sulawesi',
                       'South Sumatra', 'Southeast Sulawesi', 'West Java', 'West Kalimantan',
                       'West Nusa Tenggara', 'West Papua', 'West Sulawesi', 'West Sumatra', 'Yogyakarta'],

    'Pakistan': ['Azad Kashmir', 'Balochistan', 'Gilgit-Baltistan', 'Islamabad Capital Territory',
                      'Khyber Pakhtunkhwa', 'Punjab', 'Sindh'],

    'Bangladesh': ['Dhaka Division', 'Chittagong Division', 'Rajshahi Division',
                        'Khulna Division', 'Barisal Division', 'Sylhet Division',
                        'Rangpur Division', 'Mymensingh Division'],

    'Japan': ['Aichi', 'Akita', 'Aomori', 'Chiba', 'Ehime', 'Fukui', 'Fukuoka',
                   'Fukushima', 'Gifu', 'Gunma', 'Hiroshima', 'Hokkaido', 'Hyogo',
                   'Ibaraki', 'Ishikawa', 'Iwate', 'Kagawa', 'Kagoshima', 'Kanagawa',
                   'Kochi', 'Kumamoto', 'Kyoto', 'Mie', 'Miyagi', 'Miyazaki', 'Nagano',
                   'Nagasaki', 'Nara', 'Niigata', 'Oita', 'Okayama', 'Okinawa', 'Osaka',
                   'Saga', 'Saitama', 'Shiga', 'Shimane', 'Shizuoka', 'Tochigi', 'Tokushima',
                   'Tokyo', 'Tottori', 'Toyama', 'Wakayama', 'Yamagata', 'Yamaguchi', 'Yamanashi'],

    'Philippines': ['Abra', 'Agusan del Norte', 'Agusan del Sur', 'Aklan', 'Albay',
                         'Antique', 'Apayao', 'Aurora', 'Basilan', 'Bataan', 'Batanes',
                         'Batangas', 'Benguet', 'Biliran', 'Bohol', 'Bukidnon', 'Bulacan',
                         'Cagayan', 'Camarines Norte', 'Camarines Sur', 'Camiguin', 'Capiz',
                         'Catanduanes', 'Cavite', 'Cebu', 'Compostela Valley', 'Cotabato',
                         'Davao de Oro', 'Davao del Norte', 'Davao del Sur', 'Davao Occidental',
                         'Davao Oriental', 'Dinagat Islands', 'Eastern Samar', 'Guimaras', 'Ifugao',
                         'Ilocos Norte', 'Ilocos Sur', 'Iloilo', 'Isabela', 'Kalinga', 'La Union',
                         'Laguna', 'Lanao del Norte', 'Lanao del Sur', 'Leyte', 'Maguindanao',
                         'Marinduque', 'Masbate', 'Metro Manila', 'Misamis Occidental',
                         'Misamis Oriental', 'Mountain Province', 'Negros Occidental',
                         'Negros Oriental', 'Northern Samar', 'Nueva Ecija', 'Nueva Vizcaya',
                         'Occidental Mindoro', 'Oriental Mindoro', 'Palawan', 'Pampanga',
                         'Pangasinan', 'Quezon', 'Quirino', 'Rizal', 'Romblon', 'Samar',
                         'Sarangani', 'Siquijor', 'Sorsogon', 'South Cotabato', 'Southern Leyte',
                         'Sultan Kudarat', 'Sulu', 'Surigao del Norte', 'Surigao del Sur', 'Tarlac',
                         'Tawi-Tawi', 'Zambales', 'Zamboanga del Norte', 'Zamboanga del Sur', 'Zamboanga Sibugay'],

    'Vietnam': ['An Giang', 'Bà Rịa - Vũng Tàu', 'Bắc Giang', 'Bắc Kạn', 'Bạc Liêu',
                     'Bắc Ninh', 'Bến Tre', 'Bình Định', 'Bình Dương', 'Bình Phước',
                     'Bình Thuận', 'Cà Mau', 'Cần Thơ', 'Cao Bằng', 'Đà Nẵng', 'Đắk Lắk',
                     'Đắk Nông', 'Điện Biên', 'Đồng Nai', 'Đồng Tháp', 'Gia Lai', 'Hà Giang',
                     'Hà Nam', 'Hà Nội', 'Hà Tĩnh', 'Hải Dương', 'Hải Phòng', 'Hậu Giang',
                     'Hòa Bình', 'Hưng Yên', 'Khánh Hòa', 'Kiên Giang', 'Kon Tum', 'Lai Châu',
                     'Lâm Đồng', 'Lạng Sơn', 'Lào Cai', 'Long An', 'Nam Định', 'Nghệ An',
                     'Ninh Bình', 'Ninh Thuận', 'Phú Thọ', 'Phú Yên', 'Quảng Bình', 'Quảng Nam',
                     'Quảng Ngãi', 'Quảng Ninh', 'Quảng Trị', 'Sóc Trăng', 'Sơn La', 'Tây Ninh',
                     'Thái Bình', 'Thái Nguyên', 'Thanh Hóa', 'Thừa Thiên-Huế', 'Tiền Giang',
                     'Trà Vinh', 'Tuyên Quang', 'Vĩnh Long', 'Vĩnh Phúc', 'Yên Bái'],

    'Turkey': ['Adana', 'Adıyaman', 'Afyon', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin',
              'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa',
              'Çanakkale', 'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ',
              'Erzincan', 'Erzurum', 'Eskişehir', 'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari',
              'Hatay', 'Isparta', 'İçel', 'İstanbul', 'İzmir', 'Kars', 'Kastamonu', 'Kayseri',
              'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 'Manisa',
              'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize',
              'Sakarya', 'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon',
              'Tunceli', 'Şanlıurfa', 'Uşak', 'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt',
              'Karaman', 'Kırıkkale', 'Batman', 'Şırnak', 'Bartın', 'Ardahan', 'Iğdır', 'Yalova',
              'Karabük', 'Kilis', 'Osmaniye', 'Düzce'],

    'Iran': ['Ardabil', 'East Azerbaijan', 'West Azerbaijan', 'Bushehr', 'Chaharmahal and Bakhtiari',
             'Fars', 'Gilan', 'Golestan', 'Hormozgan', 'Ilam', 'Isfahan', 'Kerman', 'Kermanshah',
             'Khuzestan', 'Kohgiluyeh and Boyer-Ahmad', 'Kurdistan', 'Lorestan', 'Markazi',
             'Mazandaran', 'North Khorasan', 'Qazvin', 'Qom', 'Razavi Khorasan', 'Semnan', 'Sistan and Baluchestan',
             'South Khorasan', 'Tehran', 'Yazd', 'Zanjan'],

    'United States': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
                      'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
                      'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
                      'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                      'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
                      'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
                      'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
                      'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
                      'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'],

    'Canada': ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador',
               'Nova Scotia', 'Ontario', 'Prince Edward Island', 'Quebec', 'Saskatchewan'],
    'Mexico': ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Chiapas', 'Chihuahua',
               'Coahuila', 'Colima', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'State of Mexico',
               'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo',
               'San Luis Potosi', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán',
               'Zacatecas'],

    'Brazil': ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo',
               'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba',
               'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul',
               'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'],

    'Argentina': ['Buenos Aires', 'Catamarca', 'Chaco', 'Chubut', 'Córdoba', 'Corrientes', 'Entre Ríos',
                  'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquén',
                  'Rio Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe', 'Santiago del Estero',
                  'Tierra del Fuego', 'Tucumán'],
    'Australia': ['Australian Capital Territory', 'New South Wales', 'Northern Territory', 'Queensland',
                  'South Australia', 'Tasmania', 'Victoria', 'Western Australia']
}

IconCode = {
    'thunderstorm with light rain': '19',
    'thunderstorm with rain': '19',
    'thunderstorm with heavy rain': '19',
    'light thunderstorm': '19',
    'thunderstorm': '19',
    'heavy thunderstorm': '19',
    'ragged thunderstorm': '19',
    'thunderstorm with light drizzle': '19',
    'thunderstorm with drizzle': '19',
    'thunderstorm with heavy drizzle': '19',
    'light intensity drizzle': '01',
    'drizzle': '19',
    'heavy intensity drizzle': '01',
    'light intensity drizzle rain': '01',
    'drizzle rain': '19',
    'heavy intensity drizzle rain': '01',
    'shower rain and drizzle': '01',
    'heavy shower rain and drizzle': '01',
    'shower drizzle': '01',
    'rain': '01',
    'light rain': '01',
    'moderate rain': '01',
    'heavy intensity rain': '01',
    'very heavy rain': '01',
    'extreme rain': '01',
    'light intensity shower rain': '01',
    'shower rain': '01',
    'heavy intensity shower rain': '01',
    'ragged shower rain': '01',
    'freezing rain': '02',
    'shower rain': '01',
    'clear': '00',
    'sleet': '32',
    'clear sky': '00',
    'snow': '02',
    'light snow': '02',
    'heavy snow ': '02',
    'light shower sleet': '02',
    'shower sleet': '02',
    'light rain and snow': '32',
    'rain and snow': '32',
    'light shower snow ': '02',
    'heavy shower snow ': '02',
    'shower snow ': '02',
    'mist': '12',
    'smoke': '50',
    'haze': '50',
    'thunder': '19',
    'wind': '03',
    'dust': '50',
    'fog': '43',
    'sand': '50',
    'ash': '50',
    'squall': '50',
    'overcast': '22',
    'tornado': '50',
    'few clouds': '41',
    'scattered clouds': '06',
    'broken clouds': '22',
    'overcast clouds': '22',
    'clouds': '06',
    'rain thunder': '17',
    'snow_thunder': '21',
    'angry clouds': '49'
}

WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
API_KEY = "your_API"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# ------------- Function ----------------
def CheckInternetConnection():
    try:
        response = requests.get("https://dns.tutorialspoint.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def GetForecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def UpdateWeather():
    if not CheckInternetConnection():
        messagebox.showerror("Internet Error", "Check your connection !!!")
        return
    CountrieSelect = DropDownCountries.get()
    ProvincesSelect = DropDownProvinces.get()
    ForecastData = GetForecast(ProvincesSelect)
    Weather = ForecastData["list"][8]
    CountriesLabel.config(text=f"Countrie: {CountrieSelect}")
    CityLabel.config(text=f"City: {ProvincesSelect}")
    TempLabel.config(text=f"Temperature: {Weather['main']['temp']}°C")
    HumidityLabel.config(text=f"Humidity: {Weather['main']['humidity']}%")
    Description = Weather['weather'][0]['description']
    DescriptionLabel.config(text=f"Description: {Description}")
    try:
        xx = IconCode[str(Description)]
    except:
        xx = '99'
    LINKICON = 'Icon/'+xx+'.png'
    Icon = PhotoImage(file=LINKICON).subsample(6, 6)
    DescriptionLabelImage.config(image=Icon)

def SelectionCountries(event):
    CountrieSelect = DropDownCountries.get()
    DropDownProvinces.config(values=provinces[CountrieSelect])

# ------------- Setting ----------------
root = Tk()

# ------------- Add Photo ----------------
WeatherIcon = PhotoImage(file=r'Icon\weather.png')
BackgroundWeather = PhotoImage(file=r'Photo\background_weather.png')
NullPhoto = PhotoImage(file=r'Icon\99.png').subsample(10, 10)

# ------------- Setting ----------------
root.geometry(f"{626}x{417}")
root.resizable(False, False)
root.iconphoto(False,WeatherIcon)
root.title("Weather")

# ------------- Background----------------
BackgroundApp = Label(root, image = BackgroundWeather).place(x=0, y=0)

# ------------- Drop Down List----------------
DropDownCountries = ttk.Combobox(state="raedonly", values=countries)
DropDownCountries.bind("<<ComboboxSelected>>", SelectionCountries)
DropDownCountries.place(x=10, y=10)
DropDownProvinces = ttk.Combobox(state="raedonly", values=[])
DropDownProvinces.bind("<<ComboboxSelected>>")
DropDownProvinces.place(x=10, y=60)

# ------------- Button Update----------------
ButtonUpdate = Button(root, text="Updated", command=UpdateWeather).place(x=10, y=110)

# ------------- Label ----------------
CountriesLabel = Label(root, text="Countries: ", bg='#4D99E7').place(x=250, y=10)
CityLabel = Label(root, text="City: ", bg='#4D99E7').place(x=400, y=10)
TempLabel = Label(root, text="Temperature: ", bg='#4D99E7').place(x=250, y=70)
HumidityLabel = Label(root, text="Humidity: ", bg='#4D99E7').place(x=400, y=70)
DescriptionLabel = Label(root, text="Description: ", bg='#4D99E7').place(x=250, y=130)
DescriptionLabelImage = Label(root, image=NullPhoto, bg='#4D99E7').place(x=25, y=178)

# ------------- Run ----------------
root.mainloop()