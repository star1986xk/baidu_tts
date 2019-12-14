# -*- coding: utf-8 -*-

import requests
import json
import re
import time
import random

# headers = {
#     'Referer': 'https://wenku.baidu.com/view/38b15f3ca200a6c30c22590102020740be1ecda8.html',
#     'Sec-Fetch-Mode': 'no-cors',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
# }
# range_list = ['0-38748', '38749-75565', '75566-109019', '109020-145391', '145392-180214', '180215-215912',
#               '215913-249219', '249220-284050', '284051-322065', '322066-354575', '354576-391290', '391291-425602',
#               '425603-460342', '460343-494794', '494795-530903', '530904-561778', '561779-595041', '595042-630117',
#               '630118-666193', '666194-700508', '700509-733863', '733864-768731', '768732-800816', '800817-833431',
#               '833432-864515', '864516-898968', '898969-931057', '931058-964314', '964315-994284', '994285-1024599',
#               '1024600-1055706', '1055707-1084852', '1084853-1118016', '1118017-1152458', '1152459-1180906',
#               '1180907-1213001', '1213002-1244642', '1244643-1276073', '1276074-1305472', '1305473-1337122',
#               '1337123-1368103', '1368104-1397993', '1397994-1427266', '1427267-', '0-275', '276-551', '552-827',
#               '828-1103', '1104-1379', '1380-1655', '1656-1931', '1932-2207', '2208-2483', '2484-2759', '2760-3035',
#               '3036-3311', '3312-3587', '3588-3863', '3864-4139', '4140-4415', '4416-4691', '4692-4967', '4968-5243',
#               '5244-5519', '5520-5795', '5796-6071', '6072-6347', '6348-6623', '6624-6899', '6900-7175', '7176-7451',
#               '7452-7727', '7728-8003', '8004-8279', '8280-8555', '8556-8831', '8832-9107', '9108-9383', '9384-9659',
#               '9660-9935', '9936-10211', '10212-10487', '10488-10763', '10764-11039', '11040-11315', '11316-11591',
#               '11592-11867', '11868-']
# token_list = [
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.%2FWO%2B%2FimDiwpc%2FvNIYGTKXdbA%2Fb%2BYFsc1Lb8mOe3S4Ns%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.PfNy8kEucLNjq2MXh8qsbnWeZd74zvXKHPDAnCsmAjY%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.el6q234VQDwerse5CPUAHE7RD3qFhY2xkSYn02OKfdI%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.KC9e6RB4QQhGq4d7a7UjKvai5VAH7l9PIVS1qereK6Q%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.kicgCel98PwKFhou6Bnv%2FYvNfkYrt%2BJqGFUy0hQmXrA%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.a%2FJWGoxUCaojDmqVD9c9IgMHbNvW2pXHAaUM9KXyYSU%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.n2wS0fadC2h%2FYwNAaagUYMzDlUoWK6smcucp5SwpHcA%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.Uyz287cG3YZMf6n4uwRSp83UOuTFXjor22LSoVGlIGQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.VckHV%2BwRyoLk0IDErZ9NAtnFiSHpWx5fRY%2BeUYhDSdE%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.kKeRpNowFfkfebsp6%2BaCwMxr5fUlGUcXmx%2BHy2Xnn3g%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.g3%2BNSpIrUh2ZUkCo9I2H5OUOhb2bT7rcyAh5VtGXbAY%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.MCX4EiDinVT488Wh2Jxc699ekoVkbrNPsCjC7fg7rxk%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.CdIV8XmrZKpjMzzjtXSFTggtiXnu7S9PcfRCTLAzOGY%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.2t92eT0x6ZvpnqLrXRqeHpk5jrdjlufP5nyr9289q%2Fs%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.hmi%2B5x2Y90mUYq1NFGL%2BaScGHdzV7xLrcyH65x3Z9DQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.%2BtSyGks%2B7RIl5cKqv%2BaJ65jCKsmeNxbiOBTGPBW%2FSvQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.KlGfFfF5u2IhOyjIxvvASUcFe%2FenpIjGtNW90jUT4Z4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.wPqI88TMCearcAQgGl8pT3ogDU%2Fu6ddfaPm722BX0cU%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.oL4efP9uhzMxfaS%2B2%2BGZiwZeYRFk%2FJTpF3qv6AfBUTE%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.uaFP1TDtBhOwPPVMV1yNkq4HP2EJJCa5z6MIsjR8HSQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.0CoIos0mYju%2BQsT3xKtdIq%2BncQKpDdBmIcJV5bEyfXk%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.x6RYdVdHECxkalbR7tEhLymRwNWAquhVZwutQ7i44%2F4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.%2FojIdCVriUVMvGXgJASPO9CqDNT7AHkkXk1%2FyudAiEU%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.y1304SaRNnUmjfbULSuGOVc2fEDo7ZFbTHWaoBhmlKw%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.MIC6Xbo1Vpf6hSUiaZeAZ5jpzhKv%2Fjl8QWHY2gaal7M%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.X2%2BVatBptmECuYZoa5dhtLdLYd7s0SsuYAaSBL33bAY%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.62nYeoFqMb8t5dwZTP5awqfdiIF4eOpk%2BW41dQA3mBQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.Zc%2Fo4PiiocjDhKPSj0aSYxK4F4LWMyTa2JfPMDq%2Fw1I%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.dhxfGN7lGYnD9oITvKcPEgtUP6vLLg6e%2BiP%2FQiNcVFQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.fhlcXz0MrOlfD2TssI%2FOZKDi9Bq5XZWOuKJe2kod7Xo%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.o0U3wUmtcRdRuWd%2BAPdATOUOuG83vMtR7dzpygqf0NE%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.k6o3imWkH%2Fqh%2FR0tXX1WSxERZCnZz3pJe8SLzxOmaBQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.LO38hvIprWcDptXvQhKFryS0zKRC%2FdN5YepqGrpG6yo%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.ZOUdCCe6RV%2BWdCEQSTuXhS8WC2RehEnS63dsGYxlwxc%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.i0%2BXUXDI%2F%2FGBFkIfAwr43JAfiIl1e8alSILz3PyfcUw%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.wfogtKC1N29kQq3jIdvlY1yQQEXsRd3SmpN8SPnGynU%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.4H8T%2BfdAqN8GVOtLekec1lbjck0VrowAYsYHh7w%2FWaY%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.0VZUh4nPDArLrTXj4OUS%2BTMRIPVe14vWbxwhyHF13jA%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.TQlut1mKN1b9HNDXhNlH4mwL79vzBqGfAfvB%2Boyw5U8%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.WASagY9fVJ%2BIq%2B42dSBZYqczPLvgIJNBEswI0S6dE%2Bg%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.UjP%2FIsdKgDL%2BKIATdVmmFffVpWrXQlYz%2B%2Fwj3H5WT1o%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.g9ZQMMFl%2B07qUeV7ecD1PWimg0TshJ51Cdbozow9sx0%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.qiVTrj8vCP9Mbu28WCJMzRa9m7z0qKg4yiGME5LCOIs%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.KmZJInAmuRG%2Bx%2FqpDUTuPIhK5lqB13lF2gPbzef91ys%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.eBDNVtSLTcRE1TV9GwLbj0SiYmYoWw0fminiKjUDDxY%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.hZiGpAJdRpHyC46PorTpB62ASJouEzIwdfhzSvitoa4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.x%2F4XrthMrXnM6fOm44pW00IoDWhTqlzk8NvQJsBgii4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.HP2%2BTMVWsPk1FeKEEnI8z2qvoAa0mJkFp59vFYDxFi4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.87uxQJ2W7LlHLzPAkDAtiAfzR%2BK%2FZxxlw%2FFsSVW2FTI%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.JjxlEIot%2F84LL1X5Iu5EWSmuwexB2gWx4TNdBqpQdfw%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.6Xd66EA6n5HqwY18lms3q%2BA9%2F9n7PpunDOePPMDVFWQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.6pKlqXIsfXHugYMA1bi70xlpEO4vQEBbcNCceq4LDb8%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.0EGqrIPXtXaAjdNoX1rL2s4cGu1tnSmAcYw3HKv3a5Q%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.nnzEL%2BqqG78AX4%2FvVLdh9WuMbqp7Fv45qECofnaVLWM%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.B2Ij2kbH6EpzqKDywzYSgbVklVFTN%2FdTfKVApiWvCeY%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.S4nJ9H0l6JegH9cbLZbIlaX78EC4h4566N%2BLSAExu%2BQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.hih4a2870dG%2FDettHtUpLL4Ms1ebZY9Ngtdw%2FTpOUY0%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.QXEY126yRcgo05CdxB8lauA1nvAvjscrn1Z4gDE4k0o%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.uasuUEVTHQ6%2FkFGUF60oBJa0JE6hBm%2BRK7mY%2Fif%2FCBw%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.ghfL2TUaUonvbRdPNYqaD9HXCybDU9hQ3XkvGcHAOTY%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.MmYN0Gxf9Z99tO%2BeDOI%2FIYSn514ywKEORk7DLeHaFx4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.Fhb0k0Cxnmg%2F%2BVKtlOyu2%2BrVC2g1j2zJYJdgPs9Ej%2B4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.EoE%2FFUvyWKi9fwwZ%2BvIR3fsCEIqQS2dVxEVbm%2BW5GGo%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.KAeaBYQZl2vPMdTDIciK2bkurA3r%2BbTWh9egjU77vjE%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.qk4ZYkluUp42FyfMxXYBj1EPGArY7hrc2j2N9ibJYp4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.HsIh51jiPhDoBEALvDxCodLZZO4JFYdSuXkimpKHZLk%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.MTtljxnNVh4TiNE%2FebbXSSrgCdTFcCotYbHVtZz%2FyGc%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.lUuq16bsvyjHgRpFPitq8fixm08u5HbrA0R8FsqFcw4%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.do7dSvbGuMleZbRl9jZGrxC%2BgsONVuKjJEjypEGsYzk%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.biZZwhJc9vFl1Zm4DcG5SCFttWDe6X2cfP1ODKov%2FXg%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.GqN213guOy%2BuwpI9miv9yuztOR%2F3M9UtikE9Pqdvmvc%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.GPx16tqoY1p4wLvjR3FTEiNfO3FnyXm39SSczbYYDno%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.eBCrihc0vDn%2FFaw70UDc0wAtgrk7wZ9YzhlyHapkjIs%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.j6c%2BPPS%2FFEynywglS9ayJWWv8hLEzo9bPy12tVKmWEg%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.aK6u0VL6sezzWyTUwoQUbiR2TgTZYNX97tLLVZrEWyQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.xqRnXD0iGaDyAt3AreJBwBsu20an8fmrTm2TbvSeBzU%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.h5tbg3uP430rJypodX6%2FwaLzup1PLGJ0N%2B0Ru9QFYLo%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.xIOgUBWg1zw8xbb3onxHGD94oVNM8L0TnvmQJNMPPzE%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.bPzsg98ePBiOQ9IYirC7MnhN0hNIcLzx3ZgxwKI5aOQ%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.iMamJ75%2BJyrx3IDZUWZJiV%2B6iH9FhQLNZjNAt%2B4rRJg%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.m9ywF9dwWjq8%2FjACGLpkGLrPFJSCgMix8DBBABZw36Q%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.K27uINdGjukoi89TiJ7x8%2Fr5vSBYTaokfCvX94JZ6Ig%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.iIeRlgsvkGWRGxnMcxIV9pjUXKIT%2Fy%2FGzqTWj%2FxBw2c%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.GSwWUedKVwnaRDBqFH8V0eX5d4Os0nBdHD9yTTlKR2g%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.kQl6lNfG4hUn1GZXYzslv5aFoDu0oUkNbngeVw1OXuU%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.0%2FEWdz4CsYaqoY0z1FsGhaVkHsokN7KtDxYiav7Ca7w%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.ZuXTe5QmRNZIwHuot7jefkWU6Q22M5tUaMWVeDZ407Y%3D.1576225840',
#     'eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjIyNTg0MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.xEHrnJP2XqgzIPsx1KbN8EOJTtgPCUnwY6FMEHm18TY%3D.1576225840']
#
# url = 'https://wkbjcloudbos.bdimg.com/v1/docconvert5944/wk/0511f666aed7e292aa22212c49c398d4/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Mon%2C%2027%20Jan%202020%2015%3A30%3A40%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-12-13T07%3A30%3A40Z%2F3600%2Fhost%2F1c244b0baada0ca90f8546b8c1cef8f98642d3e38f9802fd5795b417fe2683be&x-bce-range={}&token={}'
#
# data_list = [(a, b) for a, b in zip(range_list, token_list)]
#
# for i in data_list:
#     time.sleep(random.uniform(1,5))
#     response = requests.get(url.format(i[0],i[1]),headers=headers)
#     jsons = re.search('wenku_.*?\((.*)\)',response.text,re.S)
#     list_word = []
#     html = json.loads(jsons[1])
#     for i in html['body']:
#         if i.get('t') == 'word':
#             list_word.append(i.get('c'))
#     with open('1.txt','a') as f:
#         f.write(str(list_word)+'\n')
s = ''
with open('1.txt', 'r') as f:
    word = f.readlines()
for w in word:
    s += w.replace('\n','')

sss= s.split(' \' \', ')
for a in sss:
    print(a)
print(len(sss))