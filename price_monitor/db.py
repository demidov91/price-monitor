from decimal import Decimal

PRODUCTS = [
    {
        'source': 'evroopt',
        'identifier': '1207465',
        'categories': ['chicken', 'meat'],
        'name_ru': 'Тушка цыпленка-бройлера «Петруха» потрошеная, охлажденная 1 кг',
    },
    {
        'source': 'evroopt',
        'identifier': '440852',
        'categories': ['chicken', 'meat'],
        'name_ru': 'Тушка цыплёнка-бройлера охлаждённая, 1 кг., фасовка 1.4 кг',
        'coefficients': {
            'chicken': Decimal('1.0371'),
        },
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '601522',
        'categories': ['chicken', 'meat'],
        'name_ru': 'Тушка цыпленка-бройлера «Петруха» 1 кг., фасовка 1.62 - 1.87 кг',
        'coefficients': {
            'chicken': Decimal('0.9192'),
        },
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '567997',
        'categories': ['milk_low_fat', 'milk', 'dairy'],
        'name_ru': '«Бабушкина крынка» ультрапастеризованное, 1.5%, 900 мл',
        'coefficients': {
            'milk_low_fat': Decimal('1.1111'),
        }
    },
    {
        'source': 'evroopt',
        'identifier': '696039',
        'categories': ['milk_low_fat', 'milk', 'dairy'],
        'name_ru': 'Молоко «Поставы городок» пастеризованное, 1.5%, 1 л',
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '474138',
        'categories': ['milk_low_fat', 'milk', 'dairy'],
        'name_ru': '«Молочный гостинец» ультрапастеризованное, 1.5%, 930 мл',
    },
    {
        'source': 'evroopt',
        'identifier': '911715',
        'categories': ['milk_low_fat', 'milk', 'dairy'],
        'name_ru': '«Савушкин» ультрапастеризованное, 1.5%, 1 л',
    },
    {
        'source': 'evroopt',
        'identifier': '568002',
        'categories': ['milk_high_fat', 'milk', 'dairy'],
        'name_ru': '«Бабушкина крынка» ультрапастеризованное, 3.2%, 900 мл',
        'coefficients': {
            'milk_high_fat': Decimal('1.1111'),
        }
    },
    {
        'source': 'evroopt',
        'identifier': '322984',
        'categories': ['milk_high_fat', 'milk', 'dairy'],
        'name_ru': '«Сафiйка» ультрапастеризованное, 3.2%, 950 мл',
        'coefficients': {
            'milk_high_fat': Decimal('1.0526'),
        }
    },
    {
        'source': 'evroopt',
        'identifier': '819616',
        'categories': ['milk_high_fat', 'milk', 'dairy'],
        'name_ru': '«Молочный гостинец» ультрапастеризованное, 3.2%, 950 мл',
        'coefficients': {
            'milk_high_fat': Decimal('1.0526'),
        }
    },
    {
        'source': 'evroopt',
        'identifier': '761990',
        'categories': ['cheese', 'dairy'],
        'name_ru': '«Брест-Литовск» Классический, 45 %, 200 г',
    },
    {
        'source': 'evroopt',
        'identifier': '967482',
        'categories': ['cheese', 'dairy'],
        'name_ru': '«Брест-Литовск» Российский, 50%, 200 г',
        'coefficients': {
            'cheese': Decimal('1.0895'),
        },
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '761983',
        'categories': ['cheese', 'dairy'],
        'name_ru': '«Брест-Литовск» Легкий, 35 %, 200 г',
        'coefficients': {
            'cheese': Decimal('1.0569'),
        },
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '761994',
        'categories': ['cheese', 'dairy'],
        'name_ru': '«Брест-Литовск» Сливочный, 50 %, 200 г',
        'coefficients': {
            'cheese': Decimal('0.9592'),
        },
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '684114',
        'categories': ['tvaroh', 'dairy'],
        'name_ru': 'Творог рассыпчатый «Савушкин», 5%, 350 г',
    },
    {
        'source': 'evroopt',
        'identifier': '880935',
        'categories': ['tvaroh', 'dairy'],
        'name_ru': 'Творог рассыпчатый «Савушкин», 2%, 350 г',
        'coefficients': {
            'tvaroh': Decimal('1.0506'),
        },
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '598810',
        'categories': ['tvaroh', 'dairy'],
        'name_ru': 'Творог рассыпчатый «Савушкин», 9%, 350 г',
        'coefficients': {
            'tvaroh': Decimal('0.9614'),
        },
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '225378',
        'categories': ['egg'],
        'name_ru': '«Оршанская Птицефабрика» Семейный завтрак, С1, 10 шт',
    },
    {
        'source': 'evroopt',
        'identifier': '35073',
        'categories': ['egg'],
        'name_ru': '«Оршанская Птицефабрика» Столовые, С1, 10 шт',
    },
    {
        'source': 'evroopt',
        'identifier': '24541',
        'categories': ['egg'],
        'name_ru': '«1-я Минская птицефабрика» С1, 10 шт',
    },
    {
        'source': 'evroopt',
        'identifier': '379379',
        'categories': ['egg'],
        'name_ru': '«1-я Минская птицефабрика» С1, 10 шт',
    },
    {
        'source': 'evroopt',
        'identifier': '1222130',
        'categories': ['egg'],
        'name_ru': '«Родное подворье» С1, 10 шт',
    },
    {
        'source': 'evroopt',
        'identifier': '1192',
        'categories': ['oatmeal', 'porridge'],
        'name_ru': 'Хлопья овсяные «Экстра» № 3, 500 г',
    },
    {
        'source': 'evroopt',
        'identifier': '1057058',
        'categories': ['oatmeal', 'porridge'],
        'name_ru': 'Хлопья овсяные «Экстра» № 1, 500 г',
        'coefficients': {
            'oatmeal': Decimal('1.0119'),
        },
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '882055',
        'categories': ['bread'],
        'name_ru': 'Хлеб «Майский» традиционный, 450 г',
    },
    {
        'source': 'evroopt',
        'identifier': '533163',
        'categories': ['bread'],
        'name_ru': 'Хлеб «Водар Темный» нарезанный, 410 г',
        'coefficients': {
            'oatmeal': Decimal('1.09756'),
        },
    },
    {
        'source': 'evroopt',
        'identifier': '560208',
        'categories': ['bread'],
        'name_ru': 'Хлеб «Водар» светлый, нарезанный, 430 г',
        'coefficients': {
            'oatmeal': Decimal('1.0465'),
        },
    },
    {
        'source': 'evroopt',
        'identifier': '1256057',
        'categories': ['bread'],
        'name_ru': 'Хлеб «Ржано-пшеничный Классика-6» нарезанный, 450 г',
        'prefer': False,
    },
    {
        'source': 'evroopt',
        'identifier': '33827',
        'categories': ['kaubasa', 'meat'],
        'name_ru': '«Докторская» высшего сорта, 1 кг, фасовка 0.6 - 0.8 кг',
    },
    {
        'source': 'evroopt',
        'identifier': '365111',
        'categories': ['kaubasa', 'meat'],
        'name_ru': '«Докторская с маслицем» высшего сорта, 1 кг, фасовка 0.6 - 0.8 кг',
    },
    {
        'source': 'evroopt',
        'identifier': '537240',
        'categories': ['kaubasa', 'meat'],
        'name_ru': 'Колбаса вареная «Докторская» 400 г',
        'coefficients': {
            'oatmeal': Decimal('2.5'),
        },
    },
    {
        'source': 'evroopt',
        'identifier': '457685',
        'categories': ['kaubasa', 'meat'],
        'name_ru': 'Колбаса вареная «Молочная» новая 400 г',
        'coefficients': {
            'oatmeal': Decimal('2.5'),
        },
    },
]