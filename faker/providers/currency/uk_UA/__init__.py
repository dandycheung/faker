from typing import Tuple

from ... import ElementsType
from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # see full list in Ukrainian @ Wiki
    # https://uk.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B0%D1%81%D0%B8%D1%84%D1%96%D0%BA%D0%B0%D1%86%D1%96%D1%8F_%D0%B2%D0%B0%D0%BB%D1%8E%D1%82_(ISO_4217)#%D0%9F%D0%B5%D1%80%D0%B5%D0%BB%D1%96%D0%BA_%D0%B4%D1%96%D1%8E%D1%87%D0%B8%D1%85_%D0%BA%D0%BE%D0%B4%D1%96%D0%B2
    currencies: ElementsType[Tuple[str, str]] = (
        ("AED", "Дирхам ОАЕ"),
        ("AFN", "Афганістанський афгані"),
        ("ALL", "Албанський лек"),
        ("AMD", "Вірменський драм"),
        ("ANG", "Гульден Нідерландських Антилів"),
        ("AOA", "Ангольська кванза"),
        ("ARS", "Аргентинське песо"),
        ("AUD", "Австралійський долар"),
        ("AWG", "Арубський флорин"),
        ("AZN", "Азербайджанський манат"),
        ("BAM", "Конвертовна марка Боснії і Герцоговини"),
        ("BBD", "Барбадоський долар"),
        ("BDT", "Бангладешська така"),
        ("BGN", "Болгарський лев"),
        ("BHD", "Бахрейнський динар"),
        ("BIF", "Бурундійський франк"),
        ("BMD", "Бермудський долар"),
        ("BND", "Брунейський долар"),
        ("BOB", "Болівійський болівіано"),
        ("BRL", "Бразильський реал"),
        ("BSD", "Багамський долар"),
        ("BTN", "Бутанський нґултрум"),
        ("BWP", "Ботсванська пула"),
        ("BYR", "Білоруський рубль"),
        ("BZD", "Белізький долар"),
        ("CAD", "Канадський долар"),
        ("CDF", "Конголезький франк"),
        ("CHF", "Швейцарський франк"),
        ("CLP", "Чилійське песо"),
        ("CNY", "Китайський юань"),
        ("COP", "Колумбійське песо"),
        ("CRC", "Коста-риканський колон"),
        ("CUP", "Кубинське песо"),
        ("CVE", "Ескудо Кабо-Верде"),
        ("CZK", "Чеська крона"),
        ("DJF", "Джибутійський франк"),
        ("DKK", "Данська крона"),
        ("DOP", "Домініканське песо"),
        ("DZD", "Алжирський динар"),
        ("EGP", "Єгипетський фунт"),
        ("ERN", "Еритрейська накфа"),
        ("ETB", "Ефіопський бир"),
        ("EUR", "Євро"),
        ("FJD", "Фіджійський долар"),
        ("FKP", "Фолклендський фунт"),
        ("GBP", "Фунт стерлінгів"),
        ("GEL", "Грузинський ларі"),
        ("GHS", "Ганський седі"),
        ("GIP", "Ґібралтарський фунт"),
        ("GMD", "Гамбійський даласі"),
        ("GNF", "Гвінейський франк"),
        ("GTQ", "Ґватемальський кетсаль"),
        ("GYD", "Гаянський долар"),
        ("HKD", "Гонконгівський долар"),
        ("HNL", "Гондураська лемпіра"),
        ("HTG", "Ґурд Республіки Гаїті"),
        ("HUF", "Угорський форинт"),
        ("IDR", "Індонезійська рупія"),
        ("ILS", "Новий ізраїльський шекель"),
        ("NIS", "Новий ізраїльський шекель"),
        ("INR", "Індійська рупія"),
        ("IQD", "Іракський динар"),
        ("IRR", "Іранський ріал"),
        ("ISK", "Ісландська крона"),
        ("JMD", "Ямайський долар"),
        ("JOD", "Йорданський динар"),
        ("JPY", "Японська єна"),
        ("KES", "Кенійський шилінг"),
        ("KGS", "Киргизький сом"),
        ("KHR", "Камбоджійський рієль"),
        ("KMF", "Коморський франк"),
        ("KPW", "Північно-корейська вона"),
        ("KRW", "Південно-корейська вона"),
        ("KWD", "Кувейтський динар"),
        ("KYD", "Долар Кайманових островів"),
        ("KZT", "Казахстанський теньґе"),
        ("LAK", "Лаоський кіп"),
        ("LBP", "Ліванський фунт"),
        ("LKR", "Рупія Шрі-Ланки"),
        ("LRD", "Ліберійський долар"),
        ("LSL", "Лоті Королівства Лесото"),
        ("LTL", "Литовська лита"),
        ("LYD", "Лівійський динар"),
        ("MAD", "Марокканський дирхам"),
        ("MDL", "Молдовський лей"),
        ("MGA", "Малагасійський аріарі"),
        ("MKD", "Македонський денар"),
        ("MMK", "М'янмський к'ят"),
        ("MNT", "Монгольський тугрик"),
        ("MOP", "Маканська патака"),
        ("MRO", "Мавританська уґія"),
        ("MUR", "Маврикійська рупія"),
        ("MVR", "Мальдівська руфія"),
        ("MWK", "Малавійська квача"),
        ("MXN", "Мексиканське песо"),
        ("MYR", "Малайзійський рингіт"),
        ("MZN", "Мозамбіцький метикал"),
        ("NAD", "Намібійський долар"),
        ("NGN", "Ніґерійська найра"),
        ("NIO", "Золота кордоба"),
        ("NOK", "Норвезька крона"),
        ("NPR", "Непальська рупія"),
        ("NZD", "Новозеландський долар"),
        ("OMR", "Оманський ріал"),
        ("PAB", "Панамське бальбоа"),
        ("PEN", "Перуанський соль"),
        ("PGK", "Папуановогвинейська кіна"),
        ("PHP", "Філіппінський песо"),
        ("PKR", "Пакистанська рупія"),
        ("PLN", "Польский злотий"),
        ("PYG", "Парагвайський ґуарані"),
        ("QAR", "Катарський ріал"),
        ("RON", "Румунський лей"),
        ("RSD", "Сербський динар"),
        ("RUB", "Російський рубль"),
        ("RWF", "Руандійський франк"),
        ("SAR", "Саудівський ріал"),
        ("SBD", "Долар Соломонових Островів"),
        ("SCR", "Сейшельська рупія"),
        ("SDG", "Суданський фунт"),
        ("SEK", "Шведська крона"),
        ("SGD", "Сінгапурський долар"),
        ("SHP", "Фунт Святої Єлени"),
        ("SLL", "Леоне Сьєрра-Леоне"),
        ("SOS", "Сомалійський шилінг"),
        ("SRD", "Суринамський долар"),
        ("STD", "Добра Сан-Томе і Принсіпі"),
        ("SVC", "Сальвадорський колон"),
        ("SYP", "Сирійський фунт"),
        ("SZL", "Свазілендський ліланґені"),
        ("THB", "Таїландський бат"),
        ("TJS", "Таджицький сомоні"),
        ("TMT", "Туркменський манат"),
        ("TND", "Туніський динар"),
        ("TOP", "Тонґська паанга"),
        ("TRY", "Турецька ліра"),
        ("TTD", "Долар Тринідаду і Тобаго"),
        ("TWD", "Новий тайванський долар"),
        ("TZS", "Танзанійський шилінг"),
        ("UAH", "Українська гривня"),
        ("UGX", "Угандійський шилінг"),
        ("USD", "Долар США"),
        ("UYU", "Уругвайське песо"),
        ("UZS", "Узбецький сум"),
        ("VEF", "Венесуельский болівар"),
        ("VND", "В'єтнамський донг"),
        ("VUV", "Вануатська вану"),
        ("WST", "Самоанська тала"),
        ("XAF", "Центральноафриканський франк"),
        ("XCD", "Східнокарибський долар"),
        ("XDR", "Спеціальні права запозичення"),
        ("XOF", "Західноафриканський франк"),
        ("XPF", "Французький тихоокеанський франк"),
        ("YER", "Єменський ріал"),
        ("ZAR", "Південноафриканський ранд"),
        ("ZMW", "Замбійська квача"),
        ("ZWD", "Зімбабвійський долар"),
    )

    price_formats = ["#,##", "%#,##", "%##,##", "% ###,##", "%# ###,##"]

    def pricetag(self) -> str:
        return self.numerify(self.random_element(self.price_formats)) + "\N{no-break space}грн."
