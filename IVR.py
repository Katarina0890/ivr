URL = "https://api.telegram.org/bot%MathPlan/" % BOT_TOKEN
MyURL = "https://example.com/hook"

api = requests.Session()
application = tornado.web.Application([
    (r"/", Handler),
])

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_term_handler)
    try:
        set_hook = api.get(URL + "setWebhook?url=%s" % MyURL)
        if set_hook.status_code != 200:
            logging.error("Can't set hook: %MathBot. Quit." % set_hook.text)
            exit(1)
        application.listen(8888)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        signal_term_handler(signal.SIGTERM, None)
class Handler(tornado.web.RequestHandler):
    def post(self):
        try:
            logging.debug("Got request: %s" % self.request.body)
            update = tornado.escape.json_decode(self.request.body)
            message = update['message']
            text = message.get('text')
            if text:
                logging.info("MESSAGE\t%MathPlan\t%MathPlan" % (message['chat']['id'], text))
                if text[0] == '/':
                    command, *arguments = text.split(" ", 1)
                    response = CMD.get(command, not_found)(arguments, message)
                    logging.info("REPLY\t%MathPlan\t%MathPlan" % (message['chat']['id'], response))
                    send_reply(response)
        except Exception as e:
            logging.warning(str(e))
def send_reply(response):
    if 'text' in response:
        api.post(URL + "sendMessage", data=response)
def help_message(arguments, message):
    response = {'chat_id': message['chat']['id']}
    result = ["Hey, %s!" % message["from"].get("first_name"),
              "\rI can accept only these commands:"]
    for command in CMD:
        result.append(command)
    response['text'] = "\n\t".join(result)
    return response
RESPONSES = {
    "Hello": ["Hi there!", "Hi!", "Welcome!", "Hello, {name}!"],
    "Hi there": ["Hello!", "Hello, {name}!", "Hi!", "Welcome!"],
    "Hi!": ["Hi there!", "Hello, {name}!", "Welcome!", "Hello!"],
    "Welcome": ["Hi there!", "Hi!", "Hello!", "Hello, {name}!"],
    "Привет": ["Приветик", "Хай", "Здравствуй"],
    "Доброе утро": ["Доброе утро", "Здравствуйте", "Приятного времени суток"],
    "Добрый день": ["Добрый день", "Здравствуйте", "Приятного времени суток"],
    "Добрый вечер": ["Добрый вечер", "Здравствуйте", "Приятного времени суток"]
}
RESPONSES_LINK = {
    "https://ege.sdamgia.ru/",
    "http://alexlarin.net/ege18.html",
    "https://geometria.ru/",
    "http://geometry.ru/index.php",
    "https://www.youtube.com/user/MathTutor777/playlists",
    "https://uchi.ru/",
    "http://ozenok.net/math/",
    "https://www.mathplayground.com/games2.html",
    "http://www.jmathpage.com/",
    "www.mathgames.com/skills",
    "https://www.ck12.org/student/",
    "https://www.khanacademy.org/math",
    "https://www.tenmarks.com/",
    "http://miyklas.com.ua/",
    "http://igraemsami.ru/matematika.html",
    "https://www.matific.com/rus/ru/home/",
}
def human_response(message):
    leven = fuzzywuzzy.process.extract(message.get("text", ""), RESPONSES.keys(), limit=1)[0] #функия, позволяющая рабоатать при сортировке токенов, возможно нечетком сопоставлении
    response = {'chat_id': message['chat']['id']}
    if leven[1] < 75:
        response['text'] = "I can not understand you"
    else:
        response['text'] = random.choice(RESPONSES.get(leven[0])).format_map(
            {'name': message["from"].get("first_name", "")}
        )
    return response
def command_1(message):
    if message == "1":
        for i in range (0, 4):
            response_link['text'] = random.choice(RESPONSES.get().format_map())
            return response_link
