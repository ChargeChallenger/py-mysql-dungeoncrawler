def tellAStory(stringsArray):
    for i in range(len(stringsArray)):
        print(stringsArray[i])
        input('\nНажмите Enter, чтобы продолжить')

starting = ['Этой пасмурной ночью Вы заходите в бар...',
            '...направляетесь к барной стойке...',
            'Вы: "Бармен, пинту пива мне"',
            'Рослый мужчина, влив пол литра в кружку, передал её Вам',
            'Вы отвлекаетесь на сидящего рядом человека и краем глаза замечаете, как пинта сочного пива скользит по барной стойке и с треском падает с неё.',
            'Вы: "Мля, не больно-то и хотелось"',
            'Бармен замечает ваше негодование. Он медленно закатывает глаза, и на его лице вырастает ехидная ухмылка',
            'Рядом сидящий человек Вам не знаком, Вы впервые видите его в этом месте. Он замечает ваш заинтересованный взгляд',
            'Человек: "Эй, хочешь заполучить несметные богатства?"',
            'Вы подсели ближе к нему',
            'Человек: "Всего лишь стоит сходить в Замок на горе Говерла"',
            'Бармен: "Не стоит тебе этого делать, сколько туда людей ушло и не вернулось"',
            'Несмотря на предупреждение бармена, Вас заинтересовало это предложение. Вы поспешно ретировались из бара для дальнейшей подготовки к походу в замок',]

tutorial = ['У вас есть два параметра: Телосложение и Ловкость',
            'От Телосложения зависит максимальный запас здоровья и эффективность блока',
            'От Ловкости зависит очередность хода в Бою',
            'У вашего оружия также два параметра: Урон и Скорость атаки',
            'От Урона зависит количество наносимого урона по противнику за удар',
            'От Скорости атаки зависит количество ударов за ход',
            'В бою вы можете атаковать, ставить блок и произвести анализ противника, в результате чего можно узнать, когда он бьёт, а когда не бьёт']

ending_win = ['Богатства дурманят вас, Вы ничего не можете с собой поделать',
            'Вы теряете контроль над собой',]

ending_loose = ['Вы падаете замертво, издав противный вопль',
                'Душа покидает тело. Труп поднимается и начинает бродить по замку.',]