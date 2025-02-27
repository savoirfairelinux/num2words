# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

TEST_CASES_CARDINAL = (
    (1, 'uno'),
    (2, 'dos'),
    (3, 'tres'),
    (5.5, 'cinco punto cinco'),
    (11, 'once'),
    (12, 'doce'),
    (16, 'dieciséis'),
    (17.42, 'diecisiete punto cuatro dos'),
    (19, 'diecinueve'),
    (20, 'veinte'),
    (21, 'veintiuno'),
    (26, 'veintiséis'),
    (27.312, 'veintisiete punto tres uno dos'),
    (28, 'veintiocho'),
    (30, 'treinta'),
    (31, 'treinta y uno'),
    (40, 'cuarenta'),
    (44, 'cuarenta y cuatro'),
    (50, 'cincuenta'),
    (53.486, 'cincuenta y tres punto cuatro ocho seis'),
    (55, 'cincuenta y cinco'),
    (60, 'sesenta'),
    (67, 'sesenta y siete'),
    (70, 'setenta'),
    (79, 'setenta y nueve'),
    (89, 'ochenta y nueve'),
    (95, 'noventa y cinco'),
    (100, 'cien'),
    (101, 'ciento uno'),
    (199, 'ciento noventa y nueve'),
    (203, 'doscientos tres'),
    (287, 'doscientos ochenta y siete'),
    (300.42, 'trescientos punto cuatro dos'),
    (356, 'trescientos cincuenta y seis'),
    (400, 'cuatrocientos'),
    (434, 'cuatrocientos treinta y cuatro'),
    (578, 'quinientos setenta y ocho'),
    (689, 'seiscientos ochenta y nueve'),
    (729, 'setecientos veintinueve'),
    (894, 'ochocientos noventa y cuatro'),
    (999, 'novecientos noventa y nueve'),
    (1000, 'mil'),
    (1001, 'mil uno'),
    (1097, 'mil noventa y siete'),
    (1104, 'mil ciento cuatro'),
    (1243, 'mil doscientos cuarenta y tres'),
    (2385, 'dos mil trescientos ochenta y cinco'),
    (3766, 'tres mil setecientos sesenta y seis'),
    (4196, 'cuatro mil ciento noventa y seis'),
    (4196.42, 'cuatro mil ciento noventa y seis punto cuatro dos'),
    (5846, 'cinco mil ochocientos cuarenta y seis'),
    (6459, 'seis mil cuatrocientos cincuenta y nueve'),
    (7232, 'siete mil doscientos treinta y dos'),
    (8569, 'ocho mil quinientos sesenta y nueve'),
    (9539, 'nueve mil quinientos treinta y nueve'),
    (1000000, 'un millón'),
    (1000001, 'un millón uno'),
    (4000000, 'cuatro millones'),
    (10000000000000, 'diez billones'),
    (100000000000000, 'cien billones'),
    (1000000000000000000, 'un trillón'),
    (1000000000000000000000, 'mil trillones'),
    (10000000000000000000000000, 'diez cuatrillones')
)

TEST_CASES_ORDINAL = (
    (1, 'primero'),
    (8, 'octavo'),
    (12, 'decimosegundo'),
    (14, 'decimocuarto'),
    (28, 'vigesimoctavo'),
    (48, 'cuadragésimo octavo'),
    (100, 'centésimo'),
    (1000, 'milésimo'),
    (12345, 'docemilésimo tricentésimo cuadragésimo quinto'),
    (1000000, 'millonésimo'),
    (1000000000000000, 'cuadrillonésimo'),
    (1000000000000000000, 'un trillón')  # over 1e18 is not supported
)

TEST_CASES_ORDINAL_FEM = (
    (1, 'primera'),
    (8, 'octava'),
    (12, 'decimosegunda'),
    (14, 'decimocuarta'),
    (28, 'vigesimoctava'),
    (48, 'cuadragésima octava'),
    (100, 'centésima'),
    (1000, 'milésima'),
    (12345, 'docemilésima tricentésima cuadragésima quinta'),
    (1000000, 'millonésima'),
    (1000000000000000, 'cuadrillonésima'),
    (1000000000000000000, 'un trillón')  # over 1e18 is not supported
)

TEST_CASES_ORDINAL_NUM = (
    (1, '1º'),
    (8, '8º'),
    (12, '12º'),
    (14, '14º'),
    (28, '28º'),
    (100, '100º'),
    (1000, '1000º'),
    (1000000, '1000000º')
)

TEST_CASES_TO_CURRENCY = (
    (1.00, 'un euro con cero céntimos'),
    (1.01, 'un euro con un céntimo'),
    (2.00, 'dos euros con cero céntimos'),
    (8.00, 'ocho euros con cero céntimos'),
    (12.00, 'doce euros con cero céntimos'),
    (21.00, 'veintiún euros con cero céntimos'),
    (81.25, 'ochenta y un euros con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta euros con noventa céntimos'),
    (100.00, 'cien euros con cero céntimos'),
)

TEST_CASES_TO_CURRENCY_ESP = (
    (1.00, 'una peseta con cero céntimos'),
    (1.01, 'una peseta con un céntimo'),
    (2.00, 'dos pesetas con cero céntimos'),
    (8.00, 'ocho pesetas con cero céntimos'),
    (12.00, 'doce pesetas con cero céntimos'),
    (21.00, 'veintiuna pesetas con cero céntimos'),
    (81.25, 'ochenta y una pesetas con veinticinco céntimos'),
    (350.90, 'trescientas cincuenta pesetas con noventa céntimos'),
    (100.00, 'cien pesetas con cero céntimos'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'un dólar con cero centavos'),
    (2.00, 'dos dólares con cero centavos'),
    (8.00, 'ocho dólares con cero centavos'),
    (12.00, 'doce dólares con cero centavos'),
    (21.00, 'veintiún dólares con cero centavos'),
    (81.25, 'ochenta y un dólares con veinticinco centavos'),
    (350.90, 'trescientos cincuenta dólares con noventa centavos'),
    (100.00, 'cien dólares con cero centavos'),
)

TEST_CASES_TO_CURRENCY_PEN = (
    (1.00, 'un sol con cero céntimos'),
    (2.00, 'dos soles con cero céntimos'),
    (8.00, 'ocho soles con cero céntimos'),
    (12.00, 'doce soles con cero céntimos'),
    (21.00, 'veintiún soles con cero céntimos'),
    (81.25, 'ochenta y un soles con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta soles con noventa céntimos'),
    (100.00, 'cien soles con cero céntimos'),
)

TEST_CASES_TO_CURRENCY_CRC = (
    (1.00, 'un colón con cero centavos'),
    (2.00, 'dos colones con cero centavos'),
    (8.00, 'ocho colones con cero centavos'),
    (12.00, 'doce colones con cero centavos'),
    (21.00, 'veintiún colones con cero centavos'),
    (81.25, 'ochenta y un colones con veinticinco centavos'),
    (350.90, 'trescientos cincuenta colones con noventa centavos'),
    (100.00, 'cien colones con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta colones con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, 'una libra con cero peniques'),
    (1.01, 'una libra con un penique'),
    (2.00, 'dos libras con cero peniques'),
    (8.00, 'ocho libras con cero peniques'),
    (12.00, 'doce libras con cero peniques'),
    (21.00, 'veintiuna libras con cero peniques'),
    (81.25, 'ochenta y una libras con veinticinco peniques'),
    (350.90, 'trescientas cincuenta libras con noventa peniques'),
    (100.00, 'cien libras con cero peniques'),
    (4150.83,
        'cuatro mil ciento cincuenta libras con ochenta y tres peniques'),
)

TEST_CASES_TO_CURRENCY_RUB = (
    (1.00, 'un rublo con cero kopeykas'),
    (2.00, 'dos rublos con cero kopeykas'),
    (8.00, 'ocho rublos con cero kopeykas'),
    (12.00, 'doce rublos con cero kopeykas'),
    (21.00, 'veintiún rublos con cero kopeykas'),
    (81.25, 'ochenta y un rublos con veinticinco kopeykas'),
    (350.90, 'trescientos cincuenta rublos con noventa kopeykas'),
    (100.00, 'cien rublos con cero kopeykas'),
    (4150.83,
        'cuatro mil ciento cincuenta rublos con ochenta y tres kopeykas'),
)

TEST_CASES_TO_CURRENCY_SEK = (
    (1.00, 'una corona con cero öre'),
    (2.00, 'dos coronas con cero öre'),
    (8.00, 'ocho coronas con cero öre'),
    (12.00, 'doce coronas con cero öre'),
    (21.00, 'veintiuna coronas con cero öre'),
    (81.25, 'ochenta y una coronas con veinticinco öre'),
    (350.90, 'trescientas cincuenta coronas con noventa öre'),
    (100.00, 'cien coronas con cero öre'),
    (4150.83,
        'cuatro mil ciento cincuenta coronas con ochenta y tres öre'),
)

TEST_CASES_TO_CURRENCY_NOK = (
    (1.00, 'una corona con cero øre'),
    (2.00, 'dos coronas con cero øre'),
    (8.00, 'ocho coronas con cero øre'),
    (12.00, 'doce coronas con cero øre'),
    (21.00, 'veintiuna coronas con cero øre'),
    (81.25, 'ochenta y una coronas con veinticinco øre'),
    (350.90, 'trescientas cincuenta coronas con noventa øre'),
    (100.00, 'cien coronas con cero øre'),
    (4150.83,
        'cuatro mil ciento cincuenta coronas con ochenta y tres øre'),
)

TEST_CASES_TO_CURRENCY_PLN = (
    (1.00, 'un zloty con cero groszy'),
    (2.00, 'dos zlotys con cero groszy'),
    (8.00, 'ocho zlotys con cero groszy'),
    (12.00, 'doce zlotys con cero groszy'),
    (21.00, 'veintiún zlotys con cero groszy'),
    (81.25, 'ochenta y un zlotys con veinticinco groszy'),
    (350.90, 'trescientos cincuenta zlotys con noventa groszy'),
    (100.00, 'cien zlotys con cero groszy'),
    (4150.83,
        'cuatro mil ciento cincuenta zlotys con ochenta y tres groszy'),
)

TEST_CASES_TO_CURRENCY_MXN = (
    (1.00, 'un peso con cero centavos'),
    (2.00, 'dos pesos con cero centavos'),
    (8.00, 'ocho pesos con cero centavos'),
    (12.00, 'doce pesos con cero centavos'),
    (21.00, 'veintiún pesos con cero centavos'),
    (81.25, 'ochenta y un pesos con veinticinco centavos'),
    (350.90, 'trescientos cincuenta pesos con noventa centavos'),
    (100.00, 'cien pesos con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta pesos con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_RON = (
    (1.00, 'un leu con cero bani'),
    (2.00, 'dos leus con cero bani'),
    (8.00, 'ocho leus con cero bani'),
    (12.00, 'doce leus con cero bani'),
    (21.00, 'veintiún leus con cero bani'),
    (81.25, 'ochenta y un leus con veinticinco bani'),
    (350.90, 'trescientos cincuenta leus con noventa bani'),
    (100.00, 'cien leus con cero bani'),
    (4150.83,
        'cuatro mil ciento cincuenta leus con ochenta y tres bani'),
)

TEST_CASES_TO_CURRENCY_INR = (
    (1.00, 'una rupia con cero paisas'),
    (2.00, 'dos rupias con cero paisas'),
    (8.00, 'ocho rupias con cero paisas'),
    (12.00, 'doce rupias con cero paisas'),
    (21.00, 'veintiuna rupias con cero paisas'),
    (81.25, 'ochenta y una rupias con veinticinco paisas'),
    (350.90, 'trescientas cincuenta rupias con noventa paisas'),
    (100.00, 'cien rupias con cero paisas'),
    (4150.83,
        'cuatro mil ciento cincuenta rupias con ochenta y tres paisas'),
)

TEST_CASES_TO_CURRENCY_HUF = (
    (1.00, 'un florín con cero fillér'),
    (2.00, 'dos florines con cero fillér'),
    (8.00, 'ocho florines con cero fillér'),
    (12.00, 'doce florines con cero fillér'),
    (21.00, 'veintiún florines con cero fillér'),
    (81.25, 'ochenta y un florines con veinticinco fillér'),
    (350.90, 'trescientos cincuenta florines con noventa fillér'),
    (100.00, 'cien florines con cero fillér'),
    (4150.83,
        'cuatro mil ciento cincuenta florines con ochenta y tres fillér'),
)

TEST_CASES_TO_CURRENCY_FRF = (
    (1.00, 'un franco con cero céntimos'),
    (2.00, 'dos francos con cero céntimos'),
    (8.00, 'ocho francos con cero céntimos'),
    (12.00, 'doce francos con cero céntimos'),
    (21.00, 'veintiún francos con cero céntimos'),
    (81.25, 'ochenta y un francos con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta francos con noventa céntimos'),
    (100.00, 'cien francos con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta francos con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_CNY = (
    (1.00, 'un yuan con cero jiaos'),
    (2.00, 'dos yuanes con cero jiaos'),
    (8.00, 'ocho yuanes con cero jiaos'),
    (12.00, 'doce yuanes con cero jiaos'),
    (21.00, 'veintiún yuanes con cero jiaos'),
    (81.25, 'ochenta y un yuanes con veinticinco jiaos'),
    (350.90, 'trescientos cincuenta yuanes con noventa jiaos'),
    (100.00, 'cien yuanes con cero jiaos'),
    (4150.83,
        'cuatro mil ciento cincuenta yuanes con ochenta y tres jiaos'),
)

TEST_CASES_TO_CURRENCY_CZK = (
    (1.00, 'una corona con cero haléř'),
    (2.00, 'dos coronas con cero haléř'),
    (8.00, 'ocho coronas con cero haléř'),
    (12.00, 'doce coronas con cero haléř'),
    (21.00, 'veintiuna coronas con cero haléř'),
    (81.25, 'ochenta y una coronas con veinticinco haléř'),
    (350.90, 'trescientas cincuenta coronas con noventa haléř'),
    (100.00, 'cien coronas con cero haléř'),
    (4150.83,
        'cuatro mil ciento cincuenta coronas con ochenta y tres haléř'),
)

TEST_CASES_TO_CURRENCY_NIO = (
    (1.00, 'un córdoba con cero centavos'),
    (2.00, 'dos córdobas con cero centavos'),
    (8.00, 'ocho córdobas con cero centavos'),
    (12.00, 'doce córdobas con cero centavos'),
    (21.00, 'veintiún córdobas con cero centavos'),
    (81.25, 'ochenta y un córdobas con veinticinco centavos'),
    (350.90, 'trescientos cincuenta córdobas con noventa centavos'),
    (100.00, 'cien córdobas con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta córdobas con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_VES = (
    (1.00, 'un bolívar con cero céntimos'),
    (2.00, 'dos bolívares con cero céntimos'),
    (8.00, 'ocho bolívares con cero céntimos'),
    (12.00, 'doce bolívares con cero céntimos'),
    (21.00, 'veintiún bolívares con cero céntimos'),
    (81.25, 'ochenta y un bolívares con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta bolívares con noventa céntimos'),
    (100.00, 'cien bolívares con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta bolívares con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_BRL = (
    (1.00, 'un real con cero centavos'),
    (2.00, 'dos reales con cero centavos'),
    (8.00, 'ocho reales con cero centavos'),
    (12.00, 'doce reales con cero centavos'),
    (21.00, 'veintiún reales con cero centavos'),
    (81.25, 'ochenta y un reales con veinticinco centavos'),
    (350.90, 'trescientos cincuenta reales con noventa centavos'),
    (100.00, 'cien reales con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta reales con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_JPY = (
    (1.00, 'un yen con cero sen'),
    (2.00, 'dos yenes con cero sen'),
    (8.00, 'ocho yenes con cero sen'),
    (12.00, 'doce yenes con cero sen'),
    (21.00, 'veintiún yenes con cero sen'),
    (81.25, 'ochenta y un yenes con veinticinco sen'),
    (350.90, 'trescientos cincuenta yenes con noventa sen'),
    (100.00, 'cien yenes con cero sen'),
    (4150.83,
        'cuatro mil ciento cincuenta yenes con ochenta y tres sen'),
)

TEST_CASES_TO_CURRENCY_KRW = (
    (1.00, 'un won con cero jeon'),
    (2.00, 'dos wones con cero jeon'),
    (8.00, 'ocho wones con cero jeon'),
    (12.00, 'doce wones con cero jeon'),
    (21.00, 'veintiún wones con cero jeon'),
    (81.25, 'ochenta y un wones con veinticinco jeon'),
    (350.90, 'trescientos cincuenta wones con noventa jeon'),
    (100.00, 'cien wones con cero jeon'),
    (4150.83,
        'cuatro mil ciento cincuenta wones con ochenta y tres jeon'),
)

TEST_CASES_TO_CURRENCY_KPW = (
    (1.00, 'un won con cero chon'),
    (2.00, 'dos wones con cero chon'),
    (8.00, 'ocho wones con cero chon'),
    (12.00, 'doce wones con cero chon'),
    (21.00, 'veintiún wones con cero chon'),
    (81.25, 'ochenta y un wones con veinticinco chon'),
    (350.90, 'trescientos cincuenta wones con noventa chon'),
    (100.00, 'cien wones con cero chon'),
    (4150.83,
        'cuatro mil ciento cincuenta wones con ochenta y tres chon'),
)

TEST_CASES_TO_CURRENCY_TRY = (
    (1.00, 'una lira con cero kuruş'),
    (2.00, 'dos liras con cero kuruş'),
    (8.00, 'ocho liras con cero kuruş'),
    (12.00, 'doce liras con cero kuruş'),
    (21.00, 'veintiuna liras con cero kuruş'),
    (81.25, 'ochenta y una liras con veinticinco kuruş'),
    (350.90, 'trescientas cincuenta liras con noventa kuruş'),
    (100.00, 'cien liras con cero kuruş'),
    (4150.83,
        'cuatro mil ciento cincuenta liras con ochenta y tres kuruş'),
)

TEST_CASES_TO_CURRENCY_ZAR = (
    (1.00, 'un rand con cero céntimos'),
    (2.00, 'dos rands con cero céntimos'),
    (8.00, 'ocho rands con cero céntimos'),
    (12.00, 'doce rands con cero céntimos'),
    (21.00, 'veintiún rands con cero céntimos'),
    (81.25, 'ochenta y un rands con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta rands con noventa céntimos'),
    (100.00, 'cien rands con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta rands con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_KZT = (
    (1.00, 'un tenge con cero tïın'),
    (2.00, 'dos tenges con cero tïın'),
    (8.00, 'ocho tenges con cero tïın'),
    (12.00, 'doce tenges con cero tïın'),
    (21.00, 'veintiún tenges con cero tïın'),
    (81.25, 'ochenta y un tenges con veinticinco tïın'),
    (350.90, 'trescientos cincuenta tenges con noventa tïın'),
    (100.00, 'cien tenges con cero tïın'),
    (4150.83,
        'cuatro mil ciento cincuenta tenges con ochenta y tres tïın'),
)

TEST_CASES_TO_CURRENCY_UAH = (
    (1.00, 'un hryvnia con cero kopiykas'),
    (2.00, 'dos hryvnias con cero kopiykas'),
    (8.00, 'ocho hryvnias con cero kopiykas'),
    (12.00, 'doce hryvnias con cero kopiykas'),
    (21.00, 'veintiún hryvnias con cero kopiykas'),
    (81.25, 'ochenta y un hryvnias con veinticinco kopiykas'),
    (350.90, 'trescientos cincuenta hryvnias con noventa kopiykas'),
    (100.00, 'cien hryvnias con cero kopiykas'),
    (4150.83,
        'cuatro mil ciento cincuenta hryvnias con ochenta y tres kopiykas'),
)

TEST_CASES_TO_CURRENCY_THB = (
    (1.00, 'un baht con cero satang'),
    (2.00, 'dos bahts con cero satang'),
    (8.00, 'ocho bahts con cero satang'),
    (12.00, 'doce bahts con cero satang'),
    (21.00, 'veintiún bahts con cero satang'),
    (81.25, 'ochenta y un bahts con veinticinco satang'),
    (350.90, 'trescientos cincuenta bahts con noventa satang'),
    (100.00, 'cien bahts con cero satang'),
    (4150.83,
        'cuatro mil ciento cincuenta bahts con ochenta y tres satang'),
)

TEST_CASES_TO_CURRENCY_AED = (
    (1.00, 'un dirham con cero fils'),
    (2.00, 'dos dirhams con cero fils'),
    (8.00, 'ocho dirhams con cero fils'),
    (12.00, 'doce dirhams con cero fils'),
    (21.00, 'veintiún dirhams con cero fils'),
    (81.25, 'ochenta y un dirhams con veinticinco fils'),
    (350.90, 'trescientos cincuenta dirhams con noventa fils'),
    (100.00, 'cien dirhams con cero fils'),
    (4150.83,
        'cuatro mil ciento cincuenta dirhams con ochenta y tres fils'),
)

TEST_CASES_TO_CURRENCY_AFN = (
    (1.00, 'un afghani con cero puls'),
    (2.00, 'dos afghanis con cero puls'),
    (8.00, 'ocho afghanis con cero puls'),
    (12.00, 'doce afghanis con cero puls'),
    (21.00, 'veintiún afghanis con cero puls'),
    (81.25, 'ochenta y un afghanis con veinticinco puls'),
    (350.90, 'trescientos cincuenta afghanis con noventa puls'),
    (100.00, 'cien afghanis con cero puls'),
    (4150.83,
        'cuatro mil ciento cincuenta afghanis con ochenta y tres puls'),
)

TEST_CASES_TO_CURRENCY_ALL = (
    (1.00, 'un lek  con cero qindarka'),
    (2.00, 'dos leke con cero qindarka'),
    (8.00, 'ocho leke con cero qindarka'),
    (12.00, 'doce leke con cero qindarka'),
    (21.00, 'veintiún leke con cero qindarka'),
    (81.25, 'ochenta y un leke con veinticinco qindarka'),
    (350.90, 'trescientos cincuenta leke con noventa qindarka'),
    (100.00, 'cien leke con cero qindarka'),
    (4150.83,
        'cuatro mil ciento cincuenta leke con ochenta y tres qindarka'),
)

TEST_CASES_TO_CURRENCY_AMD = (
    (1.00, 'un dram con cero lumas'),
    (2.00, 'dos drams con cero lumas'),
    (8.00, 'ocho drams con cero lumas'),
    (12.00, 'doce drams con cero lumas'),
    (21.00, 'veintiún drams con cero lumas'),
    (81.25, 'ochenta y un drams con veinticinco lumas'),
    (350.90, 'trescientos cincuenta drams con noventa lumas'),
    (100.00, 'cien drams con cero lumas'),
    (4150.83,
        'cuatro mil ciento cincuenta drams con ochenta y tres lumas'),
)

TEST_CASES_TO_CURRENCY_ANG = (
    (1.00, 'un florín con cero centavos'),
    (2.00, 'dos florines con cero centavos'),
    (8.00, 'ocho florines con cero centavos'),
    (12.00, 'doce florines con cero centavos'),
    (21.00, 'veintiún florines con cero centavos'),
    (81.25, 'ochenta y un florines con veinticinco centavos'),
    (350.90, 'trescientos cincuenta florines con noventa centavos'),
    (100.00, 'cien florines con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta florines con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_AOA = (
    (1.00, 'un kwanza con cero céntimos'),
    (2.00, 'dos kwanzas con cero céntimos'),
    (8.00, 'ocho kwanzas con cero céntimos'),
    (12.00, 'doce kwanzas con cero céntimos'),
    (21.00, 'veintiún kwanzas con cero céntimos'),
    (81.25, 'ochenta y un kwanzas con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta kwanzas con noventa céntimos'),
    (100.00, 'cien kwanzas con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta kwanzas con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_AWG = (
    (1.00, 'un florín con cero centavos'),
    (2.00, 'dos florines con cero centavos'),
    (8.00, 'ocho florines con cero centavos'),
    (12.00, 'doce florines con cero centavos'),
    (21.00, 'veintiún florines con cero centavos'),
    (81.25, 'ochenta y un florines con veinticinco centavos'),
    (350.90, 'trescientos cincuenta florines con noventa centavos'),
    (100.00, 'cien florines con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta florines con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_AZN = (
    (1.00, 'un manat con cero qəpik'),
    (2.00, 'dos manat con cero qəpik'),
    (8.00, 'ocho manat con cero qəpik'),
    (12.00, 'doce manat con cero qəpik'),
    (21.00, 'veintiún manat con cero qəpik'),
    (81.25, 'ochenta y un manat con veinticinco qəpik'),
    (350.90, 'trescientos cincuenta manat con noventa qəpik'),
    (100.00, 'cien manat con cero qəpik'),
    (4150.83,
        'cuatro mil ciento cincuenta manat con ochenta y tres qəpik'),
)

TEST_CASES_TO_CURRENCY_BDT = (
    (1.00, 'un taka con cero paisas'),
    (2.00, 'dos takas con cero paisas'),
    (8.00, 'ocho takas con cero paisas'),
    (12.00, 'doce takas con cero paisas'),
    (21.00, 'veintiún takas con cero paisas'),
    (81.25, 'ochenta y un takas con veinticinco paisas'),
    (350.90, 'trescientos cincuenta takas con noventa paisas'),
    (100.00, 'cien takas con cero paisas'),
    (4150.83,
        'cuatro mil ciento cincuenta takas con ochenta y tres paisas'),
)

TEST_CASES_TO_CURRENCY_BGN = (
    (1.00, 'un lev con cero stotinki'),
    (2.00, 'dos leva con cero stotinki'),
    (8.00, 'ocho leva con cero stotinki'),
    (12.00, 'doce leva con cero stotinki'),
    (21.00, 'veintiún leva con cero stotinki'),
    (81.25, 'ochenta y un leva con veinticinco stotinki'),
    (350.90, 'trescientos cincuenta leva con noventa stotinki'),
    (100.00, 'cien leva con cero stotinki'),
    (4150.83,
        'cuatro mil ciento cincuenta leva con ochenta y tres stotinki'),
)

TEST_CASES_TO_CURRENCY_BHD = (
    (1.00, 'un dinar con cero fils'),
    (2.00, 'dos dinares con cero fils'),
    (8.00, 'ocho dinares con cero fils'),
    (12.00, 'doce dinares con cero fils'),
    (21.00, 'veintiún dinares con cero fils'),
    (81.25, 'ochenta y un dinares con veinticinco fils'),
    (350.90, 'trescientos cincuenta dinares con noventa fils'),
    (100.00, 'cien dinares con cero fils'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres fils'),
)

TEST_CASES_TO_CURRENCY_BOB = (
    (1.00, 'un boliviano con cero centavos'),
    (2.00, 'dos bolivianos con cero centavos'),
    (8.00, 'ocho bolivianos con cero centavos'),
    (12.00, 'doce bolivianos con cero centavos'),
    (21.00, 'veintiún bolivianos con cero centavos'),
    (81.25, 'ochenta y un bolivianos con veinticinco centavos'),
    (350.90, 'trescientos cincuenta bolivianos con noventa centavos'),
    (100.00, 'cien bolivianos con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta bolivianos con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_BTN = (
    (1.00, 'un ngultrum con cero chetrum'),
    (2.00, 'dos ngultrum con cero chetrum'),
    (8.00, 'ocho ngultrum con cero chetrum'),
    (12.00, 'doce ngultrum con cero chetrum'),
    (21.00, 'veintiún ngultrum con cero chetrum'),
    (81.25, 'ochenta y un ngultrum con veinticinco chetrum'),
    (350.90, 'trescientos cincuenta ngultrum con noventa chetrum'),
    (100.00, 'cien ngultrum con cero chetrum'),
    (4150.83,
        'cuatro mil ciento cincuenta ngultrum con ochenta y tres chetrum'),
)

TEST_CASES_TO_CURRENCY_BWP = (
    (1.00, 'un pula con cero thebes'),
    (2.00, 'dos pulas con cero thebes'),
    (8.00, 'ocho pulas con cero thebes'),
    (12.00, 'doce pulas con cero thebes'),
    (21.00, 'veintiún pulas con cero thebes'),
    (81.25, 'ochenta y un pulas con veinticinco thebes'),
    (350.90, 'trescientos cincuenta pulas con noventa thebes'),
    (100.00, 'cien pulas con cero thebes'),
    (4150.83,
        'cuatro mil ciento cincuenta pulas con ochenta y tres thebes'),
)

TEST_CASES_TO_CURRENCY_BYN = (
    (1.00, 'un rublo con cero kópeks'),
    (2.00, 'dos rublos con cero kópeks'),
    (8.00, 'ocho rublos con cero kópeks'),
    (12.00, 'doce rublos con cero kópeks'),
    (21.00, 'veintiún rublos con cero kópeks'),
    (81.25, 'ochenta y un rublos con veinticinco kópeks'),
    (350.90, 'trescientos cincuenta rublos con noventa kópeks'),
    (100.00, 'cien rublos con cero kópeks'),
    (4150.83,
        'cuatro mil ciento cincuenta rublos con ochenta y tres kópeks'),
)

TEST_CASES_TO_CURRENCY_BYR = (
    (1.00, 'un rublo con cero kópeks'),
    (2.00, 'dos rublos con cero kópeks'),
    (8.00, 'ocho rublos con cero kópeks'),
    (12.00, 'doce rublos con cero kópeks'),
    (21.00, 'veintiún rublos con cero kópeks'),
    (81.25, 'ochenta y un rublos con veinticinco kópeks'),
    (350.90, 'trescientos cincuenta rublos con noventa kópeks'),
    (100.00, 'cien rublos con cero kópeks'),
    (4150.83,
        'cuatro mil ciento cincuenta rublos con ochenta y tres kópeks'),
)

TEST_CASES_TO_CURRENCY_BZD = (
    (1.00, 'un dólar con cero céntimos'),
    (2.00, 'dos dólares con cero céntimos'),
    (8.00, 'ocho dólares con cero céntimos'),
    (12.00, 'doce dólares con cero céntimos'),
    (21.00, 'veintiún dólares con cero céntimos'),
    (81.25, 'ochenta y un dólares con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta dólares con noventa céntimos'),
    (100.00, 'cien dólares con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta dólares con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_CVE = (
    (1.00, 'un escudo con cero centavos'),
    (2.00, 'dos escudos con cero centavos'),
    (8.00, 'ocho escudos con cero centavos'),
    (12.00, 'doce escudos con cero centavos'),
    (21.00, 'veintiún escudos con cero centavos'),
    (81.25, 'ochenta y un escudos con veinticinco centavos'),
    (350.90, 'trescientos cincuenta escudos con noventa centavos'),
    (100.00, 'cien escudos con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta escudos con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_CYP = (
    (1.00, 'una libra con cero céntimos'),
    (2.00, 'dos libras con cero céntimos'),
    (8.00, 'ocho libras con cero céntimos'),
    (12.00, 'doce libras con cero céntimos'),
    (21.00, 'veintiuna libras con cero céntimos'),
    (81.25, 'ochenta y una libras con veinticinco céntimos'),
    (350.90, 'trescientas cincuenta libras con noventa céntimos'),
    (100.00, 'cien libras con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta libras con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_DKK = (
    (1.00, 'una corona con cero øre'),
    (2.00, 'dos coronas con cero øre'),
    (8.00, 'ocho coronas con cero øre'),
    (12.00, 'doce coronas con cero øre'),
    (21.00, 'veintiuna coronas con cero øre'),
    (81.25, 'ochenta y una coronas con veinticinco øre'),
    (350.90, 'trescientas cincuenta coronas con noventa øre'),
    (100.00, 'cien coronas con cero øre'),
    (4150.83,
        'cuatro mil ciento cincuenta coronas con ochenta y tres øre'),
)

TEST_CASES_TO_CURRENCY_DZD = (
    (1.00, 'un dinar con cero céntimos'),
    (2.00, 'dos dinares con cero céntimos'),
    (8.00, 'ocho dinares con cero céntimos'),
    (12.00, 'doce dinares con cero céntimos'),
    (21.00, 'veintiún dinares con cero céntimos'),
    (81.25, 'ochenta y un dinares con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta dinares con noventa céntimos'),
    (100.00, 'cien dinares con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_ECS = (
    (1.00, 'un sucre con cero centavos'),
    (2.00, 'dos sucres con cero centavos'),
    (8.00, 'ocho sucres con cero centavos'),
    (12.00, 'doce sucres con cero centavos'),
    (21.00, 'veintiún sucres con cero centavos'),
    (81.25, 'ochenta y un sucres con veinticinco centavos'),
    (350.90, 'trescientos cincuenta sucres con noventa centavos'),
    (100.00, 'cien sucres con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta sucres con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_EGP = (
    (1.00, 'una libra con cero piastras'),
    (2.00, 'dos libras con cero piastras'),
    (8.00, 'ocho libras con cero piastras'),
    (12.00, 'doce libras con cero piastras'),
    (21.00, 'veintiuna libras con cero piastras'),
    (81.21, 'ochenta y una libras con veintiuna piastras'),
    (81.25, 'ochenta y una libras con veinticinco piastras'),
    (350.90, 'trescientas cincuenta libras con noventa piastras'),
    (100.00, 'cien libras con cero piastras'),
    (4150.83,
        'cuatro mil ciento cincuenta libras con ochenta y tres piastras'),
)

TEST_CASES_TO_CURRENCY_ERN = (
    (1.00, 'un nakfa con cero céntimos'),
    (2.00, 'dos nakfas con cero céntimos'),
    (8.00, 'ocho nakfas con cero céntimos'),
    (12.00, 'doce nakfas con cero céntimos'),
    (21.00, 'veintiún nakfas con cero céntimos'),
    (81.25, 'ochenta y un nakfas con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta nakfas con noventa céntimos'),
    (100.00, 'cien nakfas con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta nakfas con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_ETB = (
    (1.00, 'un birr con cero céntimos'),
    (2.00, 'dos birrs con cero céntimos'),
    (8.00, 'ocho birrs con cero céntimos'),
    (12.00, 'doce birrs con cero céntimos'),
    (21.00, 'veintiún birrs con cero céntimos'),
    (81.25, 'ochenta y un birrs con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta birrs con noventa céntimos'),
    (100.00, 'cien birrs con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta birrs con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_FKP = (
    (1.00, 'una libra con cero peniques'),
    (2.00, 'dos libras con cero peniques'),
    (8.00, 'ocho libras con cero peniques'),
    (12.00, 'doce libras con cero peniques'),
    (21.00, 'veintiuna libras con cero peniques'),
    (81.25, 'ochenta y una libras con veinticinco peniques'),
    (350.90, 'trescientas cincuenta libras con noventa peniques'),
    (100.00, 'cien libras con cero peniques'),
    (4150.83,
        'cuatro mil ciento cincuenta libras con ochenta y tres peniques'),
)

TEST_CASES_TO_CURRENCY_GEL = (
    (1.00, 'un lari con cero tetris'),
    (2.00, 'dos laris con cero tetris'),
    (8.00, 'ocho laris con cero tetris'),
    (12.00, 'doce laris con cero tetris'),
    (21.00, 'veintiún laris con cero tetris'),
    (81.25, 'ochenta y un laris con veinticinco tetris'),
    (350.90, 'trescientos cincuenta laris con noventa tetris'),
    (100.00, 'cien laris con cero tetris'),
    (4150.83,
        'cuatro mil ciento cincuenta laris con ochenta y tres tetris'),
)

TEST_CASES_TO_CURRENCY_GHS = (
    (1.00, 'un cedi con cero pesewas'),
    (2.00, 'dos cedis con cero pesewas'),
    (8.00, 'ocho cedis con cero pesewas'),
    (12.00, 'doce cedis con cero pesewas'),
    (21.00, 'veintiún cedis con cero pesewas'),
    (81.25, 'ochenta y un cedis con veinticinco pesewas'),
    (350.90, 'trescientos cincuenta cedis con noventa pesewas'),
    (100.00, 'cien cedis con cero pesewas'),
    (4150.83,
        'cuatro mil ciento cincuenta cedis con ochenta y tres pesewas'),
)

TEST_CASES_TO_CURRENCY_GMD = (
    (1.00, 'un dalasi con cero bututs'),
    (2.00, 'dos dalasis con cero bututs'),
    (8.00, 'ocho dalasis con cero bututs'),
    (12.00, 'doce dalasis con cero bututs'),
    (21.00, 'veintiún dalasis con cero bututs'),
    (81.25, 'ochenta y un dalasis con veinticinco bututs'),
    (350.90, 'trescientos cincuenta dalasis con noventa bututs'),
    (100.00, 'cien dalasis con cero bututs'),
    (4150.83,
        'cuatro mil ciento cincuenta dalasis con ochenta y tres bututs'),
)

TEST_CASES_TO_CURRENCY_GTQ = (
    (1.00, 'un quetzal con cero centavos'),
    (2.00, 'dos quetzales con cero centavos'),
    (8.00, 'ocho quetzales con cero centavos'),
    (12.00, 'doce quetzales con cero centavos'),
    (21.00, 'veintiún quetzales con cero centavos'),
    (81.25, 'ochenta y un quetzales con veinticinco centavos'),
    (350.90, 'trescientos cincuenta quetzales con noventa centavos'),
    (100.00, 'cien quetzales con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta quetzales con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_HNL = (
    (1.00, 'un lempira con cero centavos'),
    (2.00, 'dos lempiras con cero centavos'),
    (8.00, 'ocho lempiras con cero centavos'),
    (12.00, 'doce lempiras con cero centavos'),
    (21.00, 'veintiún lempiras con cero centavos'),
    (81.25, 'ochenta y un lempiras con veinticinco centavos'),
    (350.90, 'trescientos cincuenta lempiras con noventa centavos'),
    (100.00, 'cien lempiras con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta lempiras con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_HRK = (
    (1.00, 'un kuna con cero lipas'),
    (2.00, 'dos kunas con cero lipas'),
    (8.00, 'ocho kunas con cero lipas'),
    (12.00, 'doce kunas con cero lipas'),
    (21.00, 'veintiún kunas con cero lipas'),
    (81.25, 'ochenta y un kunas con veinticinco lipas'),
    (350.90, 'trescientos cincuenta kunas con noventa lipas'),
    (100.00, 'cien kunas con cero lipas'),
    (4150.83,
        'cuatro mil ciento cincuenta kunas con ochenta y tres lipas'),
)

TEST_CASES_TO_CURRENCY_HTG = (
    (1.00, 'un gourde con cero céntimos'),
    (2.00, 'dos gourdes con cero céntimos'),
    (8.00, 'ocho gourdes con cero céntimos'),
    (12.00, 'doce gourdes con cero céntimos'),
    (21.00, 'veintiún gourdes con cero céntimos'),
    (81.25, 'ochenta y un gourdes con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta gourdes con noventa céntimos'),
    (100.00, 'cien gourdes con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta gourdes con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_IDR = (
    (1.00, 'una rupia con cero céntimos'),
    (2.00, 'dos rupias con cero céntimos'),
    (8.00, 'ocho rupias con cero céntimos'),
    (12.00, 'doce rupias con cero céntimos'),
    (21.00, 'veintiuna rupias con cero céntimos'),
    (81.25, 'ochenta y una rupias con veinticinco céntimos'),
    (350.90, 'trescientas cincuenta rupias con noventa céntimos'),
    (100.00, 'cien rupias con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta rupias con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_ILS = (
    (1.00, 'un séquel con cero agoras'),
    (2.00, 'dos séqueles con cero agoras'),
    (8.00, 'ocho séqueles con cero agoras'),
    (12.00, 'doce séqueles con cero agoras'),
    (21.00, 'veintiún séqueles con cero agoras'),
    (81.25, 'ochenta y un séqueles con veinticinco agoras'),
    (350.90, 'trescientos cincuenta séqueles con noventa agoras'),
    (100.00, 'cien séqueles con cero agoras'),
    (4150.83,
        'cuatro mil ciento cincuenta séqueles con ochenta y tres agoras'),
)

TEST_CASES_TO_CURRENCY_IQD = (
    (1.00, 'un dinar con cero fils'),
    (2.00, 'dos dinares con cero fils'),
    (8.00, 'ocho dinares con cero fils'),
    (12.00, 'doce dinares con cero fils'),
    (21.00, 'veintiún dinares con cero fils'),
    (81.25, 'ochenta y un dinares con veinticinco fils'),
    (350.90, 'trescientos cincuenta dinares con noventa fils'),
    (100.00, 'cien dinares con cero fils'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres fils'),
)

TEST_CASES_TO_CURRENCY_IRR = (
    (1.00, 'un rial con cero dinares'),
    (2.00, 'dos riales con cero dinares'),
    (8.00, 'ocho riales con cero dinares'),
    (12.00, 'doce riales con cero dinares'),
    (21.00, 'veintiún riales con cero dinares'),
    (81.25, 'ochenta y un riales con veinticinco dinares'),
    (350.90, 'trescientos cincuenta riales con noventa dinares'),
    (100.00, 'cien riales con cero dinares'),
    (4150.83,
        'cuatro mil ciento cincuenta riales con ochenta y tres dinares'),
)

TEST_CASES_TO_CURRENCY_ISK = (
    (1.00, 'una corona con cero aurar'),
    (2.00, 'dos coronas con cero aurar'),
    (8.00, 'ocho coronas con cero aurar'),
    (12.00, 'doce coronas con cero aurar'),
    (21.00, 'veintiuna coronas con cero aurar'),
    (81.25, 'ochenta y una coronas con veinticinco aurar'),
    (350.90, 'trescientas cincuenta coronas con noventa aurar'),
    (100.00, 'cien coronas con cero aurar'),
    (4150.83,
        'cuatro mil ciento cincuenta coronas con ochenta y tres aurar'),
)

TEST_CASES_TO_CURRENCY_ITL = (
    (1.00, 'una lira con cero céntimos'),
    (2.00, 'dos liras con cero céntimos'),
    (8.00, 'ocho liras con cero céntimos'),
    (12.00, 'doce liras con cero céntimos'),
    (21.00, 'veintiuna liras con cero céntimos'),
    (81.25, 'ochenta y una liras con veinticinco céntimos'),
    (350.90, 'trescientas cincuenta liras con noventa céntimos'),
    (100.00, 'cien liras con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta liras con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_JOD = (
    (1.00, 'un dinar con cero piastras'),
    (2.00, 'dos dinares con cero piastras'),
    (8.00, 'ocho dinares con cero piastras'),
    (12.00, 'doce dinares con cero piastras'),
    (21.00, 'veintiún dinares con cero piastras'),
    (81.25, 'ochenta y un dinares con veinticinco piastras'),
    (350.90, 'trescientos cincuenta dinares con noventa piastras'),
    (100.00, 'cien dinares con cero piastras'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres piastras'),
)

TEST_CASES_TO_CURRENCY_KES = (
    (1.00, 'un chelín con cero céntimos'),
    (2.00, 'dos chelines con cero céntimos'),
    (8.00, 'ocho chelines con cero céntimos'),
    (12.00, 'doce chelines con cero céntimos'),
    (21.00, 'veintiún chelines con cero céntimos'),
    (81.25, 'ochenta y un chelines con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta chelines con noventa céntimos'),
    (100.00, 'cien chelines con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta chelines con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_KGS = (
    (1.00, 'un som con cero tyiyn'),
    (2.00, 'dos som con cero tyiyn'),
    (8.00, 'ocho som con cero tyiyn'),
    (12.00, 'doce som con cero tyiyn'),
    (21.00, 'veintiún som con cero tyiyn'),
    (81.25, 'ochenta y un som con veinticinco tyiyn'),
    (350.90, 'trescientos cincuenta som con noventa tyiyn'),
    (100.00, 'cien som con cero tyiyn'),
    (4150.83,
        'cuatro mil ciento cincuenta som con ochenta y tres tyiyn'),
)

TEST_CASES_TO_CURRENCY_KHR = (
    (1.00, 'un riel con cero céntimos'),
    (2.00, 'dos rieles con cero céntimos'),
    (8.00, 'ocho rieles con cero céntimos'),
    (12.00, 'doce rieles con cero céntimos'),
    (21.00, 'veintiún rieles con cero céntimos'),
    (81.25, 'ochenta y un rieles con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta rieles con noventa céntimos'),
    (100.00, 'cien rieles con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta rieles con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_KWD = (
    (1.00, 'un dinar con cero fils'),
    (2.00, 'dos dinares con cero fils'),
    (8.00, 'ocho dinares con cero fils'),
    (12.00, 'doce dinares con cero fils'),
    (21.00, 'veintiún dinares con cero fils'),
    (81.25, 'ochenta y un dinares con veinticinco fils'),
    (350.90, 'trescientos cincuenta dinares con noventa fils'),
    (100.00, 'cien dinares con cero fils'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres fils'),
)

TEST_CASES_TO_CURRENCY_LAK = (
    (1.00, 'un kip con cero att'),
    (2.00, 'dos kips con cero att'),
    (8.00, 'ocho kips con cero att'),
    (12.00, 'doce kips con cero att'),
    (21.00, 'veintiún kips con cero att'),
    (81.25, 'ochenta y un kips con veinticinco att'),
    (350.90, 'trescientos cincuenta kips con noventa att'),
    (100.00, 'cien kips con cero att'),
    (4150.83,
        'cuatro mil ciento cincuenta kips con ochenta y tres att'),
)

TEST_CASES_TO_CURRENCY_LKR = (
    (1.00, 'una rupia con cero céntimos'),
    (2.00, 'dos rupias con cero céntimos'),
    (8.00, 'ocho rupias con cero céntimos'),
    (12.00, 'doce rupias con cero céntimos'),
    (21.00, 'veintiuna rupias con cero céntimos'),
    (81.25, 'ochenta y una rupias con veinticinco céntimos'),
    (350.90, 'trescientas cincuenta rupias con noventa céntimos'),
    (100.00, 'cien rupias con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta rupias con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_LSL = (
    (1.00, 'un loti con cero céntimos'),
    (2.00, 'dos lotis con cero céntimos'),
    (8.00, 'ocho lotis con cero céntimos'),
    (12.00, 'doce lotis con cero céntimos'),
    (21.00, 'veintiún lotis con cero céntimos'),
    (81.25, 'ochenta y un lotis con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta lotis con noventa céntimos'),
    (100.00, 'cien lotis con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta lotis con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_LTL = (
    (1.00, 'un lita con cero céntimos'),
    (2.00, 'dos litas con cero céntimos'),
    (8.00, 'ocho litas con cero céntimos'),
    (12.00, 'doce litas con cero céntimos'),
    (21.00, 'veintiún litas con cero céntimos'),
    (81.25, 'ochenta y un litas con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta litas con noventa céntimos'),
    (100.00, 'cien litas con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta litas con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_LVL = (
    (1.00, 'un lat con cero céntimos'),
    (2.00, 'dos lats con cero céntimos'),
    (8.00, 'ocho lats con cero céntimos'),
    (12.00, 'doce lats con cero céntimos'),
    (21.00, 'veintiún lats con cero céntimos'),
    (81.25, 'ochenta y un lats con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta lats con noventa céntimos'),
    (100.00, 'cien lats con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta lats con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_LYD = (
    (1.00, 'un dinar con cero dírhams'),
    (2.00, 'dos dinares con cero dírhams'),
    (8.00, 'ocho dinares con cero dírhams'),
    (12.00, 'doce dinares con cero dírhams'),
    (21.00, 'veintiún dinares con cero dírhams'),
    (81.25, 'ochenta y un dinares con veinticinco dírhams'),
    (350.90, 'trescientos cincuenta dinares con noventa dírhams'),
    (100.00, 'cien dinares con cero dírhams'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres dírhams'),
)

TEST_CASES_TO_CURRENCY_MAD = (
    (1.00, 'un dírham con cero céntimos'),
    (2.00, 'dos dirhams con cero céntimos'),
    (8.00, 'ocho dirhams con cero céntimos'),
    (12.00, 'doce dirhams con cero céntimos'),
    (21.00, 'veintiún dirhams con cero céntimos'),
    (81.25, 'ochenta y un dirhams con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta dirhams con noventa céntimos'),
    (100.00, 'cien dirhams con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta dirhams con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_MDL = (
    (1.00, 'un leu con cero bani'),
    (2.00, 'dos lei con cero bani'),
    (8.00, 'ocho lei con cero bani'),
    (12.00, 'doce lei con cero bani'),
    (21.00, 'veintiún lei con cero bani'),
    (81.25, 'ochenta y un lei con veinticinco bani'),
    (350.90, 'trescientos cincuenta lei con noventa bani'),
    (100.00, 'cien lei con cero bani'),
    (4150.83,
        'cuatro mil ciento cincuenta lei con ochenta y tres bani'),
)

TEST_CASES_TO_CURRENCY_MGA = (
    (1.00, 'un ariary con cero iraimbilanja'),
    (2.00, 'dos ariaris con cero iraimbilanja'),
    (8.00, 'ocho ariaris con cero iraimbilanja'),
    (12.00, 'doce ariaris con cero iraimbilanja'),
    (21.00, 'veintiún ariaris con cero iraimbilanja'),
    (81.25, 'ochenta y un ariaris con veinticinco iraimbilanja'),
    (350.90, 'trescientos cincuenta ariaris con noventa iraimbilanja'),
    (100.00, 'cien ariaris con cero iraimbilanja'),
    (4150.83,
        'cuatro mil ciento cincuenta ariaris con ochenta y tres iraimbilanja'),
)

TEST_CASES_TO_CURRENCY_MKD = (
    (1.00, 'un denar con cero denis'),
    (2.00, 'dos denares con cero denis'),
    (8.00, 'ocho denares con cero denis'),
    (12.00, 'doce denares con cero denis'),
    (21.00, 'veintiún denares con cero denis'),
    (81.25, 'ochenta y un denares con veinticinco denis'),
    (350.90, 'trescientos cincuenta denares con noventa denis'),
    (100.00, 'cien denares con cero denis'),
    (4150.83,
        'cuatro mil ciento cincuenta denares con ochenta y tres denis'),
)

TEST_CASES_TO_CURRENCY_MMK = (
    (1.00, 'un kiat con cero pyas'),
    (2.00, 'dos kiats con cero pyas'),
    (8.00, 'ocho kiats con cero pyas'),
    (12.00, 'doce kiats con cero pyas'),
    (21.00, 'veintiún kiats con cero pyas'),
    (81.25, 'ochenta y un kiats con veinticinco pyas'),
    (350.90, 'trescientos cincuenta kiats con noventa pyas'),
    (100.00, 'cien kiats con cero pyas'),
    (4150.83,
        'cuatro mil ciento cincuenta kiats con ochenta y tres pyas'),
)

TEST_CASES_TO_CURRENCY_MNT = (
    (1.00, 'un tugrik con cero möngö'),
    (2.00, 'dos tugriks con cero möngö'),
    (8.00, 'ocho tugriks con cero möngö'),
    (12.00, 'doce tugriks con cero möngö'),
    (21.00, 'veintiún tugriks con cero möngö'),
    (81.25, 'ochenta y un tugriks con veinticinco möngö'),
    (350.90, 'trescientos cincuenta tugriks con noventa möngö'),
    (100.00, 'cien tugriks con cero möngö'),
    (4150.83,
        'cuatro mil ciento cincuenta tugriks con ochenta y tres möngö'),
)

TEST_CASES_TO_CURRENCY_MOP = (
    (1.00, 'un pataca con cero avos'),
    (2.00, 'dos patacas con cero avos'),
    (8.00, 'ocho patacas con cero avos'),
    (12.00, 'doce patacas con cero avos'),
    (21.00, 'veintiún patacas con cero avos'),
    (81.25, 'ochenta y un patacas con veinticinco avos'),
    (350.90, 'trescientos cincuenta patacas con noventa avos'),
    (100.00, 'cien patacas con cero avos'),
    (4150.83,
        'cuatro mil ciento cincuenta patacas con ochenta y tres avos'),
)

TEST_CASES_TO_CURRENCY_MRO = (
    (1.00, 'un ouguiya con cero khoums'),
    (2.00, 'dos ouguiyas con cero khoums'),
    (8.00, 'ocho ouguiyas con cero khoums'),
    (12.00, 'doce ouguiyas con cero khoums'),
    (21.00, 'veintiún ouguiyas con cero khoums'),
    (81.25, 'ochenta y un ouguiyas con veinticinco khoums'),
    (350.90, 'trescientos cincuenta ouguiyas con noventa khoums'),
    (100.00, 'cien ouguiyas con cero khoums'),
    (4150.83,
        'cuatro mil ciento cincuenta ouguiyas con ochenta y tres khoums'),
)

TEST_CASES_TO_CURRENCY_MRU = (
    (1.00, 'un ouguiya con cero khoums'),
    (2.00, 'dos ouguiyas con cero khoums'),
    (8.00, 'ocho ouguiyas con cero khoums'),
    (12.00, 'doce ouguiyas con cero khoums'),
    (21.00, 'veintiún ouguiyas con cero khoums'),
    (81.25, 'ochenta y un ouguiyas con veinticinco khoums'),
    (350.90, 'trescientos cincuenta ouguiyas con noventa khoums'),
    (100.00, 'cien ouguiyas con cero khoums'),
    (4150.83,
        'cuatro mil ciento cincuenta ouguiyas con ochenta y tres khoums'),
)

TEST_CASES_TO_CURRENCY_MUR = (
    (1.00, 'una rupia con cero céntimos'),
    (2.00, 'dos rupias con cero céntimos'),
    (8.00, 'ocho rupias con cero céntimos'),
    (12.00, 'doce rupias con cero céntimos'),
    (21.00, 'veintiuna rupias con cero céntimos'),
    (81.25, 'ochenta y una rupias con veinticinco céntimos'),
    (350.90, 'trescientas cincuenta rupias con noventa céntimos'),
    (100.00, 'cien rupias con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta rupias con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_MVR = (
    (1.00, 'un rufiyaa con cero laari'),
    (2.00, 'dos rufiyaas con cero laari'),
    (8.00, 'ocho rufiyaas con cero laari'),
    (12.00, 'doce rufiyaas con cero laari'),
    (21.00, 'veintiún rufiyaas con cero laari'),
    (81.25, 'ochenta y un rufiyaas con veinticinco laari'),
    (350.90, 'trescientos cincuenta rufiyaas con noventa laari'),
    (100.00, 'cien rufiyaas con cero laari'),
    (4150.83,
        'cuatro mil ciento cincuenta rufiyaas con ochenta y tres laari'),
)

TEST_CASES_TO_CURRENCY_MWK = (
    (1.00, 'un kuacha con cero tambalas'),
    (2.00, 'dos kuachas con cero tambalas'),
    (8.00, 'ocho kuachas con cero tambalas'),
    (12.00, 'doce kuachas con cero tambalas'),
    (21.00, 'veintiún kuachas con cero tambalas'),
    (81.25, 'ochenta y un kuachas con veinticinco tambalas'),
    (350.90, 'trescientos cincuenta kuachas con noventa tambalas'),
    (100.00, 'cien kuachas con cero tambalas'),
    (4150.83,
        'cuatro mil ciento cincuenta kuachas con ochenta y tres tambalas'),
)

TEST_CASES_TO_CURRENCY_MYR = (
    (1.00, 'un ringgit con cero céntimos'),
    (2.00, 'dos ringgit con cero céntimos'),
    (8.00, 'ocho ringgit con cero céntimos'),
    (12.00, 'doce ringgit con cero céntimos'),
    (21.00, 'veintiún ringgit con cero céntimos'),
    (81.25, 'ochenta y un ringgit con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta ringgit con noventa céntimos'),
    (100.00, 'cien ringgit con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta ringgit con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_MZN = (
    (1.00, 'un metical con cero centavos'),
    (2.00, 'dos metical con cero centavos'),
    (8.00, 'ocho metical con cero centavos'),
    (12.00, 'doce metical con cero centavos'),
    (21.00, 'veintiún metical con cero centavos'),
    (81.25, 'ochenta y un metical con veinticinco centavos'),
    (350.90, 'trescientos cincuenta metical con noventa centavos'),
    (100.00, 'cien metical con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta metical con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_NGN = (
    (1.00, 'un naira con cero kobo'),
    (2.00, 'dos nairas con cero kobo'),
    (8.00, 'ocho nairas con cero kobo'),
    (12.00, 'doce nairas con cero kobo'),
    (21.00, 'veintiún nairas con cero kobo'),
    (81.25, 'ochenta y un nairas con veinticinco kobo'),
    (350.90, 'trescientos cincuenta nairas con noventa kobo'),
    (100.00, 'cien nairas con cero kobo'),
    (4150.83,
        'cuatro mil ciento cincuenta nairas con ochenta y tres kobo'),
)

TEST_CASES_TO_CURRENCY_NPR = (
    (1.00, 'una rupia con cero paisas'),
    (2.00, 'dos rupias con cero paisas'),
    (8.00, 'ocho rupias con cero paisas'),
    (12.00, 'doce rupias con cero paisas'),
    (21.00, 'veintiuna rupias con cero paisas'),
    (81.25, 'ochenta y una rupias con veinticinco paisas'),
    (350.90, 'trescientas cincuenta rupias con noventa paisas'),
    (100.00, 'cien rupias con cero paisas'),
    (4150.83,
        'cuatro mil ciento cincuenta rupias con ochenta y tres paisas'),
)

TEST_CASES_TO_CURRENCY_OMR = (
    (1.00, 'un rial con cero baisa'),
    (2.00, 'dos riales con cero baisa'),
    (8.00, 'ocho riales con cero baisa'),
    (12.00, 'doce riales con cero baisa'),
    (21.00, 'veintiún riales con cero baisa'),
    (81.25, 'ochenta y un riales con veinticinco baisa'),
    (350.90, 'trescientos cincuenta riales con noventa baisa'),
    (100.00, 'cien riales con cero baisa'),
    (4150.83,
        'cuatro mil ciento cincuenta riales con ochenta y tres baisa'),
)

TEST_CASES_TO_CURRENCY_PAB = (
    (1.00, 'un balboa con cero centésimos'),
    (2.00, 'dos balboas con cero centésimos'),
    (8.00, 'ocho balboas con cero centésimos'),
    (12.00, 'doce balboas con cero centésimos'),
    (21.00, 'veintiún balboas con cero centésimos'),
    (81.25, 'ochenta y un balboas con veinticinco centésimos'),
    (350.90, 'trescientos cincuenta balboas con noventa centésimos'),
    (100.00, 'cien balboas con cero centésimos'),
    (4150.83,
        'cuatro mil ciento cincuenta balboas con ochenta y tres centésimos'),
)

TEST_CASES_TO_CURRENCY_PGK = (
    (1.00, 'un kina con cero toea'),
    (2.00, 'dos kinas con cero toea'),
    (8.00, 'ocho kinas con cero toea'),
    (12.00, 'doce kinas con cero toea'),
    (21.00, 'veintiún kinas con cero toea'),
    (81.25, 'ochenta y un kinas con veinticinco toea'),
    (350.90, 'trescientos cincuenta kinas con noventa toea'),
    (100.00, 'cien kinas con cero toea'),
    (4150.83,
        'cuatro mil ciento cincuenta kinas con ochenta y tres toea'),
)

TEST_CASES_TO_CURRENCY_PKR = (
    (1.00, 'una rupia con cero paisas'),
    (2.00, 'dos rupias con cero paisas'),
    (8.00, 'ocho rupias con cero paisas'),
    (12.00, 'doce rupias con cero paisas'),
    (21.00, 'veintiuna rupias con cero paisas'),
    (81.25, 'ochenta y una rupias con veinticinco paisas'),
    (350.90, 'trescientas cincuenta rupias con noventa paisas'),
    (100.00, 'cien rupias con cero paisas'),
    (4150.83,
        'cuatro mil ciento cincuenta rupias con ochenta y tres paisas'),
)

TEST_CASES_TO_CURRENCY_PLZ = (
    (1.00, 'un zloty con cero groszy'),
    (2.00, 'dos zlotys con cero groszy'),
    (8.00, 'ocho zlotys con cero groszy'),
    (12.00, 'doce zlotys con cero groszy'),
    (21.00, 'veintiún zlotys con cero groszy'),
    (81.25, 'ochenta y un zlotys con veinticinco groszy'),
    (350.90, 'trescientos cincuenta zlotys con noventa groszy'),
    (100.00, 'cien zlotys con cero groszy'),
    (4150.83,
        'cuatro mil ciento cincuenta zlotys con ochenta y tres groszy'),
)

TEST_CASES_TO_CURRENCY_PYG = (
    (1.00, 'un guaraní con cero céntimos'),
    (2.00, 'dos guaranís con cero céntimos'),
    (8.00, 'ocho guaranís con cero céntimos'),
    (12.00, 'doce guaranís con cero céntimos'),
    (21.00, 'veintiún guaranís con cero céntimos'),
    (81.25, 'ochenta y un guaranís con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta guaranís con noventa céntimos'),
    (100.00, 'cien guaranís con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta guaranís con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_QAR = (
    (1.00, 'un rial con cero dírhams'),
    (2.00, 'dos riales con cero dírhams'),
    (8.00, 'ocho riales con cero dírhams'),
    (12.00, 'doce riales con cero dírhams'),
    (21.00, 'veintiún riales con cero dírhams'),
    (81.25, 'ochenta y un riales con veinticinco dírhams'),
    (350.90, 'trescientos cincuenta riales con noventa dírhams'),
    (100.00, 'cien riales con cero dírhams'),
    (4150.83,
        'cuatro mil ciento cincuenta riales con ochenta y tres dírhams'),
)

TEST_CASES_TO_CURRENCY_RSD = (
    (1.00, 'un dinar con cero para'),
    (2.00, 'dos dinares con cero para'),
    (8.00, 'ocho dinares con cero para'),
    (12.00, 'doce dinares con cero para'),
    (21.00, 'veintiún dinares con cero para'),
    (81.25, 'ochenta y un dinares con veinticinco para'),
    (350.90, 'trescientos cincuenta dinares con noventa para'),
    (100.00, 'cien dinares con cero para'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres para'),
)

TEST_CASES_TO_CURRENCY_RUR = (
    (1.00, 'un rublo con cero kopeks'),
    (2.00, 'dos rublos con cero kopeks'),
    (8.00, 'ocho rublos con cero kopeks'),
    (12.00, 'doce rublos con cero kopeks'),
    (21.00, 'veintiún rublos con cero kopeks'),
    (81.25, 'ochenta y un rublos con veinticinco kopeks'),
    (350.90, 'trescientos cincuenta rublos con noventa kopeks'),
    (100.00, 'cien rublos con cero kopeks'),
    (4150.83,
        'cuatro mil ciento cincuenta rublos con ochenta y tres kopeks'),
)

TEST_CASES_TO_CURRENCY_SAR = (
    (1.00, 'un riyal con cero halalas'),
    (2.00, 'dos riales con cero halalas'),
    (8.00, 'ocho riales con cero halalas'),
    (12.00, 'doce riales con cero halalas'),
    (21.00, 'veintiún riales con cero halalas'),
    (81.25, 'ochenta y un riales con veinticinco halalas'),
    (350.90, 'trescientos cincuenta riales con noventa halalas'),
    (100.00, 'cien riales con cero halalas'),
    (4150.83,
        'cuatro mil ciento cincuenta riales con ochenta y tres halalas'),
)

TEST_CASES_TO_CURRENCY_SCR = (
    (1.00, 'una rupia con cero céntimos'),
    (2.00, 'dos rupias con cero céntimos'),
    (8.00, 'ocho rupias con cero céntimos'),
    (12.00, 'doce rupias con cero céntimos'),
    (21.00, 'veintiuna rupias con cero céntimos'),
    (81.25, 'ochenta y una rupias con veinticinco céntimos'),
    (350.90, 'trescientas cincuenta rupias con noventa céntimos'),
    (100.00, 'cien rupias con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta rupias con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_SHP = (
    (1.00, 'una libra con cero peniques'),
    (2.00, 'dos libras con cero peniques'),
    (8.00, 'ocho libras con cero peniques'),
    (12.00, 'doce libras con cero peniques'),
    (21.00, 'veintiuna libras con cero peniques'),
    (81.25, 'ochenta y una libras con veinticinco peniques'),
    (350.90, 'trescientas cincuenta libras con noventa peniques'),
    (100.00, 'cien libras con cero peniques'),
    (4150.83,
        'cuatro mil ciento cincuenta libras con ochenta y tres peniques'),
)

TEST_CASES_TO_CURRENCY_SKK = (
    (1.00, 'una corona con cero haliers'),
    (2.00, 'dos coronas con cero haliers'),
    (8.00, 'ocho coronas con cero haliers'),
    (12.00, 'doce coronas con cero haliers'),
    (21.00, 'veintiuna coronas con cero haliers'),
    (81.25, 'ochenta y una coronas con veinticinco haliers'),
    (350.90, 'trescientas cincuenta coronas con noventa haliers'),
    (100.00, 'cien coronas con cero haliers'),
    (4150.83,
        'cuatro mil ciento cincuenta coronas con ochenta y tres haliers'),
)

TEST_CASES_TO_CURRENCY_SLL = (
    (1.00, 'una leona con cero céntimos'),
    (2.00, 'dos leonas con cero céntimos'),
    (8.00, 'ocho leonas con cero céntimos'),
    (12.00, 'doce leonas con cero céntimos'),
    (21.00, 'veintiuna leonas con cero céntimos'),
    (81.25, 'ochenta y una leonas con veinticinco céntimos'),
    (350.90, 'trescientas cincuenta leonas con noventa céntimos'),
    (100.00, 'cien leonas con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta leonas con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_STD = (
    (1.00, 'un dobra con cero céntimos'),
    (2.00, 'dos dobras con cero céntimos'),
    (8.00, 'ocho dobras con cero céntimos'),
    (12.00, 'doce dobras con cero céntimos'),
    (21.00, 'veintiún dobras con cero céntimos'),
    (81.25, 'ochenta y un dobras con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta dobras con noventa céntimos'),
    (100.00, 'cien dobras con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta dobras con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_SVC = (
    (1.00, 'un colón con cero centavos'),
    (2.00, 'dos colones con cero centavos'),
    (8.00, 'ocho colones con cero centavos'),
    (12.00, 'doce colones con cero centavos'),
    (21.00, 'veintiún colones con cero centavos'),
    (81.25, 'ochenta y un colones con veinticinco centavos'),
    (350.90, 'trescientos cincuenta colones con noventa centavos'),
    (100.00, 'cien colones con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta colones con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_SZL = (
    (1.00, 'un lilangeni con cero céntimos'),
    (2.00, 'dos emalangeni con cero céntimos'),
    (8.00, 'ocho emalangeni con cero céntimos'),
    (12.00, 'doce emalangeni con cero céntimos'),
    (21.00, 'veintiún emalangeni con cero céntimos'),
    (81.25, 'ochenta y un emalangeni con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta emalangeni con noventa céntimos'),
    (100.00, 'cien emalangeni con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta emalangeni con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_TJS = (
    (1.00, 'un somoni con cero dirames'),
    (2.00, 'dos somonis con cero dirames'),
    (8.00, 'ocho somonis con cero dirames'),
    (12.00, 'doce somonis con cero dirames'),
    (21.00, 'veintiún somonis con cero dirames'),
    (81.25, 'ochenta y un somonis con veinticinco dirames'),
    (350.90, 'trescientos cincuenta somonis con noventa dirames'),
    (100.00, 'cien somonis con cero dirames'),
    (4150.83,
        'cuatro mil ciento cincuenta somonis con ochenta y tres dirames'),
)

TEST_CASES_TO_CURRENCY_TMT = (
    (1.00, 'un manat con cero tenge'),
    (2.00, 'dos manat con cero tenge'),
    (8.00, 'ocho manat con cero tenge'),
    (12.00, 'doce manat con cero tenge'),
    (21.00, 'veintiún manat con cero tenge'),
    (81.25, 'ochenta y un manat con veinticinco tenge'),
    (350.90, 'trescientos cincuenta manat con noventa tenge'),
    (100.00, 'cien manat con cero tenge'),
    (4150.83,
        'cuatro mil ciento cincuenta manat con ochenta y tres tenge'),
)

TEST_CASES_TO_CURRENCY_TND = (
    (1.00, 'un dinar con cero milésimos'),
    (2.00, 'dos dinares con cero milésimos'),
    (8.00, 'ocho dinares con cero milésimos'),
    (12.00, 'doce dinares con cero milésimos'),
    (21.00, 'veintiún dinares con cero milésimos'),
    (81.25, 'ochenta y un dinares con veinticinco milésimos'),
    (350.90, 'trescientos cincuenta dinares con noventa milésimos'),
    (100.00, 'cien dinares con cero milésimos'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres milésimos'),
)

TEST_CASES_TO_CURRENCY_TOP = (
    (1.00, 'un paanga con cero céntimos'),
    (2.00, 'dos paangas con cero céntimos'),
    (8.00, 'ocho paangas con cero céntimos'),
    (12.00, 'doce paangas con cero céntimos'),
    (21.00, 'veintiún paangas con cero céntimos'),
    (81.25, 'ochenta y un paangas con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta paangas con noventa céntimos'),
    (100.00, 'cien paangas con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta paangas con ochenta y tres céntimos'),
)

wordamount = "{} {}".format("cuatro mil ciento cincuenta",
                            "nuevos dólares con ochenta y tres céntimos")

TEST_CASES_TO_CURRENCY_TWD = (
    (1.00, 'un nuevo dólar con cero céntimos'),
    (2.00, 'dos nuevos dólares con cero céntimos'),
    (8.00, 'ocho nuevos dólares con cero céntimos'),
    (12.00, 'doce nuevos dólares con cero céntimos'),
    (21.00, 'veintiún nuevos dólares con cero céntimos'),
    (81.25, 'ochenta y un nuevos dólares con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta nuevos dólares con noventa céntimos'),
    (100.00, 'cien nuevos dólares con cero céntimos'),
    (4150.83, wordamount),
)

TEST_CASES_TO_CURRENCY_TZS = (
    (1.00, 'un chelín con cero céntimos'),
    (2.00, 'dos chelines con cero céntimos'),
    (8.00, 'ocho chelines con cero céntimos'),
    (12.00, 'doce chelines con cero céntimos'),
    (21.00, 'veintiún chelines con cero céntimos'),
    (81.25, 'ochenta y un chelines con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta chelines con noventa céntimos'),
    (100.00, 'cien chelines con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta chelines con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_UAG = (
    (1.00, 'un hryvnia con cero kopiykas'),
    (2.00, 'dos hryvnias con cero kopiykas'),
    (8.00, 'ocho hryvnias con cero kopiykas'),
    (12.00, 'doce hryvnias con cero kopiykas'),
    (21.00, 'veintiún hryvnias con cero kopiykas'),
    (81.25, 'ochenta y un hryvnias con veinticinco kopiykas'),
    (350.90, 'trescientos cincuenta hryvnias con noventa kopiykas'),
    (100.00, 'cien hryvnias con cero kopiykas'),
    (4150.83,
        'cuatro mil ciento cincuenta hryvnias con ochenta y tres kopiykas'),
)

TEST_CASES_TO_CURRENCY_UGX = (
    (1.00, 'un chelín con cero céntimos'),
    (2.00, 'dos chelines con cero céntimos'),
    (8.00, 'ocho chelines con cero céntimos'),
    (12.00, 'doce chelines con cero céntimos'),
    (21.00, 'veintiún chelines con cero céntimos'),
    (81.25, 'ochenta y un chelines con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta chelines con noventa céntimos'),
    (100.00, 'cien chelines con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta chelines con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_UYU = (
    (1.00, 'un peso con cero centésimos'),
    (2.00, 'dos pesos con cero centésimos'),
    (8.00, 'ocho pesos con cero centésimos'),
    (12.00, 'doce pesos con cero centésimos'),
    (21.00, 'veintiún pesos con cero centésimos'),
    (81.25, 'ochenta y un pesos con veinticinco centésimos'),
    (350.90, 'trescientos cincuenta pesos con noventa centésimos'),
    (100.00, 'cien pesos con cero centésimos'),
    (4150.83,
        'cuatro mil ciento cincuenta pesos con ochenta y tres centésimos'),
)

TEST_CASES_TO_CURRENCY_UZS = (
    (1.00, 'un sum con cero tiyin'),
    (2.00, 'dos sum con cero tiyin'),
    (8.00, 'ocho sum con cero tiyin'),
    (12.00, 'doce sum con cero tiyin'),
    (21.00, 'veintiún sum con cero tiyin'),
    (81.25, 'ochenta y un sum con veinticinco tiyin'),
    (350.90, 'trescientos cincuenta sum con noventa tiyin'),
    (100.00, 'cien sum con cero tiyin'),
    (4150.83,
        'cuatro mil ciento cincuenta sum con ochenta y tres tiyin'),
)

wordamount = "{} {}".format("cuatro mil ciento cincuenta",
                            "bolívares fuertes con ochenta y tres céntimos")

TEST_CASES_TO_CURRENCY_VEF = (
    (1.00, 'un bolívar fuerte con cero céntimos'),
    (2.00, 'dos bolívares fuertes con cero céntimos'),
    (8.00, 'ocho bolívares fuertes con cero céntimos'),
    (12.00, 'doce bolívares fuertes con cero céntimos'),
    (21.00, 'veintiún bolívares fuertes con cero céntimos'),
    (81.25, 'ochenta y un bolívares fuertes con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta bolívares fuertes con noventa céntimos'),
    (100.00, 'cien bolívares fuertes con cero céntimos'),
    (4150.83, wordamount),
)

TEST_CASES_TO_CURRENCY_VND = (
    (1.00, 'un dong con cero xu'),
    (2.00, 'dos dongs con cero xu'),
    (8.00, 'ocho dongs con cero xu'),
    (12.00, 'doce dongs con cero xu'),
    (21.00, 'veintiún dongs con cero xu'),
    (81.25, 'ochenta y un dongs con veinticinco xu'),
    (350.90, 'trescientos cincuenta dongs con noventa xu'),
    (100.00, 'cien dongs con cero xu'),
    (4150.83,
        'cuatro mil ciento cincuenta dongs con ochenta y tres xu'),
)

TEST_CASES_TO_CURRENCY_VUV = (
    (1.00, 'un vatu con cero nenhum'),
    (2.00, 'dos vatu con cero nenhum'),
    (8.00, 'ocho vatu con cero nenhum'),
    (12.00, 'doce vatu con cero nenhum'),
    (21.00, 'veintiún vatu con cero nenhum'),
    (81.25, 'ochenta y un vatu con veinticinco nenhum'),
    (350.90, 'trescientos cincuenta vatu con noventa nenhum'),
    (100.00, 'cien vatu con cero nenhum'),
    (4150.83,
        'cuatro mil ciento cincuenta vatu con ochenta y tres nenhum'),
)

TEST_CASES_TO_CURRENCY_WST = (
    (1.00, 'un tala con cero centavos'),
    (2.00, 'dos tala con cero centavos'),
    (8.00, 'ocho tala con cero centavos'),
    (12.00, 'doce tala con cero centavos'),
    (21.00, 'veintiún tala con cero centavos'),
    (81.25, 'ochenta y un tala con veinticinco centavos'),
    (350.90, 'trescientos cincuenta tala con noventa centavos'),
    (100.00, 'cien tala con cero centavos'),
    (4150.83,
        'cuatro mil ciento cincuenta tala con ochenta y tres centavos'),
)

TEST_CASES_TO_CURRENCY_XAF = (
    (1.00, 'un franco CFA con cero céntimos'),
    (2.00, 'dos francos CFA con cero céntimos'),
    (8.00, 'ocho francos CFA con cero céntimos'),
    (12.00, 'doce francos CFA con cero céntimos'),
    (21.00, 'veintiún francos CFA con cero céntimos'),
    (81.25, 'ochenta y un francos CFA con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta francos CFA con noventa céntimos'),
    (100.00, 'cien francos CFA con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta francos CFA con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_XPF = (
    (1.00, 'un franco CFP con cero céntimos'),
    (2.00, 'dos francos CFP con cero céntimos'),
    (8.00, 'ocho francos CFP con cero céntimos'),
    (12.00, 'doce francos CFP con cero céntimos'),
    (21.00, 'veintiún francos CFP con cero céntimos'),
    (81.25, 'ochenta y un francos CFP con veinticinco céntimos'),
    (350.90, 'trescientos cincuenta francos CFP con noventa céntimos'),
    (100.00, 'cien francos CFP con cero céntimos'),
    (4150.83,
        'cuatro mil ciento cincuenta francos CFP con ochenta y tres céntimos'),
)

TEST_CASES_TO_CURRENCY_YER = (
    (1.00, 'un rial con cero fils'),
    (2.00, 'dos riales con cero fils'),
    (8.00, 'ocho riales con cero fils'),
    (12.00, 'doce riales con cero fils'),
    (21.00, 'veintiún riales con cero fils'),
    (81.25, 'ochenta y un riales con veinticinco fils'),
    (350.90, 'trescientos cincuenta riales con noventa fils'),
    (100.00, 'cien riales con cero fils'),
    (4150.83,
        'cuatro mil ciento cincuenta riales con ochenta y tres fils'),
)

TEST_CASES_TO_CURRENCY_YUM = (
    (1.00, 'un dinar con cero para'),
    (2.00, 'dos dinares con cero para'),
    (8.00, 'ocho dinares con cero para'),
    (12.00, 'doce dinares con cero para'),
    (21.00, 'veintiún dinares con cero para'),
    (81.25, 'ochenta y un dinares con veinticinco para'),
    (350.90, 'trescientos cincuenta dinares con noventa para'),
    (100.00, 'cien dinares con cero para'),
    (4150.83,
        'cuatro mil ciento cincuenta dinares con ochenta y tres para'),
)

TEST_CASES_TO_CURRENCY_ZMW = (
    (1.00, 'un kwacha con cero ngwee'),
    (2.00, 'dos kwachas con cero ngwee'),
    (8.00, 'ocho kwachas con cero ngwee'),
    (12.00, 'doce kwachas con cero ngwee'),
    (21.00, 'veintiún kwachas con cero ngwee'),
    (81.25, 'ochenta y un kwachas con veinticinco ngwee'),
    (350.90, 'trescientos cincuenta kwachas con noventa ngwee'),
    (100.00, 'cien kwachas con cero ngwee'),
    (4150.83,
        'cuatro mil ciento cincuenta kwachas con ochenta y tres ngwee'),
)

TEST_CASES_TO_CURRENCY_ZRZ = (
    (1.00, 'un zaire con cero makuta'),
    (2.00, 'dos zaires con cero makuta'),
    (8.00, 'ocho zaires con cero makuta'),
    (12.00, 'doce zaires con cero makuta'),
    (21.00, 'veintiún zaires con cero makuta'),
    (81.25, 'ochenta y un zaires con veinticinco makuta'),
    (350.90, 'trescientos cincuenta zaires con noventa makuta'),
    (100.00, 'cien zaires con cero makuta'),
    (4150.83,
        'cuatro mil ciento cincuenta zaires con ochenta y tres makuta'),
)


class Num2WordsESTest(TestCase):

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='es'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='es', ordinal=True),
                test[1]
            )

    def test_ordinal_fem(self):
        for test in TEST_CASES_ORDINAL_FEM:
            self.assertEqual(
                num2words(test[0], lang='es', ordinal=True, gender='f'),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='es', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency'),
                test[1]
            )

    def test_currency_esp(self):
        for test in TEST_CASES_TO_CURRENCY_ESP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ESP'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='USD'),
                test[1]
            )

    def test_currency_pen(self):
        for test in TEST_CASES_TO_CURRENCY_PEN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='PEN'),
                test[1]
            )

    def test_currency_crc(self):
        for test in TEST_CASES_TO_CURRENCY_CRC:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CRC'),
                test[1]
            )

    def test_currency_aud(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='AUD'),
                test[1]
            )

    def test_currency_cad(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CAD'),
                test[1]
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GBP'),
                test[1]
            )

    def test_currency_rub(self):
        for test in TEST_CASES_TO_CURRENCY_RUB:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='RUB'),
                test[1]
            )

    def test_currency_sek(self):
        for test in TEST_CASES_TO_CURRENCY_SEK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SEK'),
                test[1]
            )

    def test_currency_nok(self):
        for test in TEST_CASES_TO_CURRENCY_NOK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='NOK'),
                test[1]
            )

    def test_currency_pln(self):
        for test in TEST_CASES_TO_CURRENCY_PLN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='PLN'),
                test[1]
            )

    def test_currency_mxn(self):
        for test in TEST_CASES_TO_CURRENCY_MXN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MXN'),
                test[1]
            )

    def test_currency_ron(self):
        for test in TEST_CASES_TO_CURRENCY_RON:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='RON'),
                test[1]
            )

    def test_currency_inr(self):
        for test in TEST_CASES_TO_CURRENCY_INR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='INR'),
                test[1]
            )

    def test_currency_huf(self):
        for test in TEST_CASES_TO_CURRENCY_HUF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='HUF'),
                test[1]
            )

    def test_currency_frf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='FRF'),
                test[1]
            )

    def test_currency_cny(self):
        for test in TEST_CASES_TO_CURRENCY_CNY:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CNY'),
                test[1]
            )

    def test_currency_czk(self):
        for test in TEST_CASES_TO_CURRENCY_CZK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CZK'),
                test[1]
            )

    def test_currency_nio(self):
        for test in TEST_CASES_TO_CURRENCY_NIO:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='NIO'),
                test[1]
            )

    def test_currency_ves(self):
        for test in TEST_CASES_TO_CURRENCY_VES:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='VES'),
                test[1]
            )

    def test_currency_brl(self):
        for test in TEST_CASES_TO_CURRENCY_BRL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BRL'),
                test[1]
            )

    def test_currency_chf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CHF'),
                test[1]
            )

    def test_currency_jpy(self):
        for test in TEST_CASES_TO_CURRENCY_JPY:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='JPY'),
                test[1]
            )

    def test_currency_krw(self):
        for test in TEST_CASES_TO_CURRENCY_KRW:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KRW'),
                test[1]
            )

    def test_currency_kpw(self):
        for test in TEST_CASES_TO_CURRENCY_KPW:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KPW'),
                test[1]
            )

    def test_currency_try(self):
        for test in TEST_CASES_TO_CURRENCY_TRY:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='TRY'),
                test[1]
            )

    def test_currency_zar(self):
        for test in TEST_CASES_TO_CURRENCY_ZAR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ZAR'),
                test[1]
            )

    def test_currency_kzt(self):
        for test in TEST_CASES_TO_CURRENCY_KZT:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KZT'),
                test[1]
            )

    def test_currency_uah(self):
        for test in TEST_CASES_TO_CURRENCY_UAH:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='UAH'),
                test[1]
            )

    def test_currency_thb(self):
        for test in TEST_CASES_TO_CURRENCY_THB:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='THB'),
                test[1]
            )

    def test_currency_aed(self):
        for test in TEST_CASES_TO_CURRENCY_AED:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='AED'),
                test[1]
            )

    def test_currency_afn(self):
        for test in TEST_CASES_TO_CURRENCY_AFN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='AFN'),
                test[1]
            )

    def test_currency_all(self):
        for test in TEST_CASES_TO_CURRENCY_ALL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ALL'),
                test[1]
            )

    def test_currency_amd(self):
        for test in TEST_CASES_TO_CURRENCY_AMD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='AMD'),
                test[1]
            )

    def test_currency_ang(self):
        for test in TEST_CASES_TO_CURRENCY_ANG:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ANG'),
                test[1]
            )

    def test_currency_aoa(self):
        for test in TEST_CASES_TO_CURRENCY_AOA:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='AOA'),
                test[1]
            )

    def test_currency_ars(self):
        for test in TEST_CASES_TO_CURRENCY_MXN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ARS'),
                test[1]
            )

    def test_currency_awg(self):
        for test in TEST_CASES_TO_CURRENCY_AWG:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='AWG'),
                test[1]
            )

    def test_currency_azn(self):
        for test in TEST_CASES_TO_CURRENCY_AZN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='AZN'),
                test[1]
            )

    def test_currency_bbd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BBD'),
                test[1]
            )

    def test_currency_bdt(self):
        for test in TEST_CASES_TO_CURRENCY_BDT:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BDT'),
                test[1]
            )

    def test_currency_bgn(self):
        for test in TEST_CASES_TO_CURRENCY_BGN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BGN'),
                test[1]
            )

    def test_currency_bhd(self):
        for test in TEST_CASES_TO_CURRENCY_BHD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BHD'),
                test[1]
            )

    def test_currency_bif(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BIF'),
                test[1]
            )

    def test_currency_bmd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BMD'),
                test[1]
            )

    def test_currency_bnd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BND'),
                test[1]
            )

    def test_currency_bob(self):
        for test in TEST_CASES_TO_CURRENCY_BOB:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BOB'),
                test[1]
            )

    def test_currency_bsd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BSD'),
                test[1]
            )

    def test_currency_btn(self):
        for test in TEST_CASES_TO_CURRENCY_BTN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BTN'),
                test[1]
            )

    def test_currency_bwp(self):
        for test in TEST_CASES_TO_CURRENCY_BWP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BWP'),
                test[1]
            )

    def test_currency_byn(self):
        for test in TEST_CASES_TO_CURRENCY_BYN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BYN'),
                test[1]
            )

    def test_currency_byr(self):
        for test in TEST_CASES_TO_CURRENCY_BYR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BYR'),
                test[1]
            )

    def test_currency_bzd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='BZD'),
                test[1]
            )

    def test_currency_cdf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CDF'),
                test[1]
            )

    def test_currency_clp(self):
        for test in TEST_CASES_TO_CURRENCY_MXN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CLP'),
                test[1]
            )

    def test_currency_cop(self):
        for test in TEST_CASES_TO_CURRENCY_MXN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='COP'),
                test[1]
            )

    def test_currency_cup(self):
        for test in TEST_CASES_TO_CURRENCY_MXN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CUP'),
                test[1]
            )

    def test_currency_cve(self):
        for test in TEST_CASES_TO_CURRENCY_CVE:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CVE'),
                test[1]
            )

    def test_currency_cyp(self):
        for test in TEST_CASES_TO_CURRENCY_CYP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='CYP'),
                test[1]
            )

    def test_currency_djf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='DJF'),
                test[1]
            )

    def test_currency_dkk(self):
        for test in TEST_CASES_TO_CURRENCY_DKK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='DKK'),
                test[1]
            )

    def test_currency_dop(self):
        for test in TEST_CASES_TO_CURRENCY_MXN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='DOP'),
                test[1]
            )

    def test_currency_dzd(self):
        for test in TEST_CASES_TO_CURRENCY_DZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='DZD'),
                test[1]
            )

    def test_currency_ecs(self):
        for test in TEST_CASES_TO_CURRENCY_ECS:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ECS'),
                test[1]
            )

    def test_currency_egp(self):
        for test in TEST_CASES_TO_CURRENCY_EGP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='EGP'),
                test[1]
            )

    def test_currency_ern(self):
        for test in TEST_CASES_TO_CURRENCY_ERN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ERN'),
                test[1]
            )

    def test_currency_etb(self):
        for test in TEST_CASES_TO_CURRENCY_ETB:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ETB'),
                test[1]
            )

    def test_currency_fjd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='FJD'),
                test[1]
            )

    def test_currency_fkp(self):
        for test in TEST_CASES_TO_CURRENCY_FKP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='FKP'),
                test[1]
            )

    def test_currency_gel(self):
        for test in TEST_CASES_TO_CURRENCY_GEL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GEL'),
                test[1]
            )

    def test_currency_ghs(self):
        for test in TEST_CASES_TO_CURRENCY_GHS:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GHS'),
                test[1]
            )

    def test_currency_gip(self):
        for test in TEST_CASES_TO_CURRENCY_FKP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GIP'),
                test[1]
            )

    def test_currency_gmd(self):
        for test in TEST_CASES_TO_CURRENCY_GMD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GMD'),
                test[1]
            )

    def test_currency_gnf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GNF'),
                test[1]
            )

    def test_currency_gtq(self):
        for test in TEST_CASES_TO_CURRENCY_GTQ:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GTQ'),
                test[1]
            )

    def test_currency_gyd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GYD'),
                test[1]
            )

    def test_currency_hkd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='HKD'),
                test[1]
            )

    def test_currency_hnl(self):
        for test in TEST_CASES_TO_CURRENCY_HNL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='HNL'),
                test[1]
            )

    def test_currency_hrk(self):
        for test in TEST_CASES_TO_CURRENCY_HRK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='HRK'),
                test[1]
            )

    def test_currency_htg(self):
        for test in TEST_CASES_TO_CURRENCY_HTG:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='HTG'),
                test[1]
            )

    def test_currency_idr(self):
        for test in TEST_CASES_TO_CURRENCY_IDR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='IDR'),
                test[1]
            )

    def test_currency_ils(self):
        for test in TEST_CASES_TO_CURRENCY_ILS:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ILS'),
                test[1]
            )

    def test_currency_iqd(self):
        for test in TEST_CASES_TO_CURRENCY_IQD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='IQD'),
                test[1]
            )

    def test_currency_irr(self):
        for test in TEST_CASES_TO_CURRENCY_IRR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='IRR'),
                test[1]
            )

    def test_currency_isk(self):
        for test in TEST_CASES_TO_CURRENCY_ISK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ISK'),
                test[1]
            )

    def test_currency_itl(self):
        for test in TEST_CASES_TO_CURRENCY_ITL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ITL'),
                test[1]
            )

    def test_currency_jmd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='JMD'),
                test[1]
            )

    def test_currency_jod(self):
        for test in TEST_CASES_TO_CURRENCY_JOD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='JOD'),
                test[1]
            )

    def test_currency_kes(self):
        for test in TEST_CASES_TO_CURRENCY_KES:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KES'),
                test[1]
            )

    def test_currency_kgs(self):
        for test in TEST_CASES_TO_CURRENCY_KGS:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KGS'),
                test[1]
            )

    def test_currency_khr(self):
        for test in TEST_CASES_TO_CURRENCY_KHR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KHR'),
                test[1]
            )

    def test_currency_kmf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KMF'),
                test[1]
            )

    def test_currency_kwd(self):
        for test in TEST_CASES_TO_CURRENCY_KWD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KWD'),
                test[1]
            )

    def test_currency_kyd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='KYD'),
                test[1]
            )

    def test_currency_lak(self):
        for test in TEST_CASES_TO_CURRENCY_LAK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='LAK'),
                test[1]
            )

    def test_currency_lbp(self):
        for test in TEST_CASES_TO_CURRENCY_EGP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='LBP'),
                test[1]
            )

    def test_currency_lkr(self):
        for test in TEST_CASES_TO_CURRENCY_LKR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='LKR'),
                test[1]
            )

    def test_currency_lrd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='LRD'),
                test[1]
            )

    def test_currency_lsl(self):
        for test in TEST_CASES_TO_CURRENCY_LSL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='LSL'),
                test[1]
            )

    def test_currency_ltl(self):
        for test in TEST_CASES_TO_CURRENCY_LTL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='LTL'),
                test[1]
            )

    def test_currency_lvl(self):
        for test in TEST_CASES_TO_CURRENCY_LVL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='LVL'),
                test[1]
            )

    def test_currency_lyd(self):
        for test in TEST_CASES_TO_CURRENCY_LYD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='LYD'),
                test[1]
            )

    def test_currency_mad(self):
        for test in TEST_CASES_TO_CURRENCY_MAD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MAD'),
                test[1]
            )

    def test_currency_mdl(self):
        for test in TEST_CASES_TO_CURRENCY_MDL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MDL'),
                test[1]
            )

    def test_currency_mga(self):
        for test in TEST_CASES_TO_CURRENCY_MGA:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MGA'),
                test[1]
            )

    def test_currency_mkd(self):
        for test in TEST_CASES_TO_CURRENCY_MKD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MKD'),
                test[1]
            )

    def test_currency_mmk(self):
        for test in TEST_CASES_TO_CURRENCY_MMK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MMK'),
                test[1]
            )

    def test_currency_mnt(self):
        for test in TEST_CASES_TO_CURRENCY_MNT:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MNT'),
                test[1]
            )

    def test_currency_mop(self):
        for test in TEST_CASES_TO_CURRENCY_MOP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MOP'),
                test[1]
            )

    def test_currency_mro(self):
        for test in TEST_CASES_TO_CURRENCY_MRO:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MRO'),
                test[1]
            )

    def test_currency_mru(self):
        for test in TEST_CASES_TO_CURRENCY_MRU:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MRU'),
                test[1]
            )

    def test_currency_mur(self):
        for test in TEST_CASES_TO_CURRENCY_MUR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MUR'),
                test[1]
            )

    def test_currency_mvr(self):
        for test in TEST_CASES_TO_CURRENCY_MVR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MVR'),
                test[1]
            )

    def test_currency_mwk(self):
        for test in TEST_CASES_TO_CURRENCY_MWK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MWK'),
                test[1]
            )

    def test_currency_myr(self):
        for test in TEST_CASES_TO_CURRENCY_MYR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MYR'),
                test[1]
            )

    def test_currency_mzn(self):
        for test in TEST_CASES_TO_CURRENCY_MZN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='MZN'),
                test[1]
            )

    def test_currency_nad(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='NAD'),
                test[1]
            )

    def test_currency_ngn(self):
        for test in TEST_CASES_TO_CURRENCY_NGN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='NGN'),
                test[1]
            )

    def test_currency_npr(self):
        for test in TEST_CASES_TO_CURRENCY_NPR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='NPR'),
                test[1]
            )

    def test_currency_nzd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='NZD'),
                test[1]
            )

    def test_currency_omr(self):
        for test in TEST_CASES_TO_CURRENCY_OMR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='OMR'),
                test[1]
            )

    def test_currency_pab(self):
        for test in TEST_CASES_TO_CURRENCY_PAB:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='PAB'),
                test[1]
            )

    def test_currency_pgk(self):
        for test in TEST_CASES_TO_CURRENCY_PGK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='PGK'),
                test[1]
            )

    def test_currency_php(self):
        for test in TEST_CASES_TO_CURRENCY_MXN:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='PHP'),
                test[1]
            )

    def test_currency_pkr(self):
        for test in TEST_CASES_TO_CURRENCY_PKR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='PKR'),
                test[1]
            )

    def test_currency_plz(self):
        for test in TEST_CASES_TO_CURRENCY_PLZ:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='PLZ'),
                test[1]
            )

    def test_currency_pyg(self):
        for test in TEST_CASES_TO_CURRENCY_PYG:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='PYG'),
                test[1]
            )

    def test_currency_qar(self):
        for test in TEST_CASES_TO_CURRENCY_QAR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='QAR'),
                test[1]
            )

    def test_currency_qtq(self):
        for test in TEST_CASES_TO_CURRENCY_GTQ:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='GTQ'),
                test[1]
            )

    def test_currency_rsd(self):
        for test in TEST_CASES_TO_CURRENCY_RSD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='RSD'),
                test[1]
            )

    def test_currency_rur(self):
        for test in TEST_CASES_TO_CURRENCY_RUR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='RUR'),
                test[1]
            )

    def test_currency_rwf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='RWF'),
                test[1]
            )

    def test_currency_sar(self):
        for test in TEST_CASES_TO_CURRENCY_SAR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SAR'),
                test[1]
            )

    def test_currency_sbd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SBD'),
                test[1]
            )

    def test_currency_scr(self):
        for test in TEST_CASES_TO_CURRENCY_SCR:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SCR'),
                test[1]
            )

    def test_currency_sdg(self):
        for test in TEST_CASES_TO_CURRENCY_EGP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SDG'),
                test[1]
            )

    def test_currency_sgd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SGD'),
                test[1]
            )

    def test_currency_shp(self):
        for test in TEST_CASES_TO_CURRENCY_SHP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SHP'),
                test[1]
            )

    def test_currency_skk(self):
        for test in TEST_CASES_TO_CURRENCY_SKK:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SKK'),
                test[1]
            )

    def test_currency_sll(self):
        for test in TEST_CASES_TO_CURRENCY_SLL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SLL'),
                test[1]
            )

    def test_currency_srd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SRD'),
                test[1]
            )

    def test_currency_ssp(self):
        for test in TEST_CASES_TO_CURRENCY_EGP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SSP'),
                test[1]
            )

    def test_currency_std(self):
        for test in TEST_CASES_TO_CURRENCY_STD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='STD'),
                test[1]
            )

    def test_currency_svc(self):
        for test in TEST_CASES_TO_CURRENCY_SVC:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SVC'),
                test[1]
            )

    def test_currency_syp(self):
        for test in TEST_CASES_TO_CURRENCY_EGP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SYP'),
                test[1]
            )

    def test_currency_szl(self):
        for test in TEST_CASES_TO_CURRENCY_SZL:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='SZL'),
                test[1]
            )

    def test_currency_tjs(self):
        for test in TEST_CASES_TO_CURRENCY_TJS:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='TJS'),
                test[1]
            )

    def test_currency_tmt(self):
        for test in TEST_CASES_TO_CURRENCY_TMT:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='TMT'),
                test[1]
            )

    def test_currency_tnd(self):
        for test in TEST_CASES_TO_CURRENCY_TND:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='TND'),
                test[1]
            )

    def test_currency_top(self):
        for test in TEST_CASES_TO_CURRENCY_TOP:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='TOP'),
                test[1]
            )

    def test_currency_ttd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='TTD'),
                test[1]
            )

    def test_currency_twd(self):
        for test in TEST_CASES_TO_CURRENCY_TWD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='TWD'),
                test[1]
            )

    def test_currency_tzs(self):
        for test in TEST_CASES_TO_CURRENCY_TZS:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='TZS'),
                test[1]
            )

    def test_currency_uag(self):
        for test in TEST_CASES_TO_CURRENCY_UAG:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='UAG'),
                test[1]
            )

    def test_currency_ugx(self):
        for test in TEST_CASES_TO_CURRENCY_UGX:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='UGX'),
                test[1]
            )

    def test_currency_uyu(self):
        for test in TEST_CASES_TO_CURRENCY_UYU:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='UYU'),
                test[1]
            )

    def test_currency_uzs(self):
        for test in TEST_CASES_TO_CURRENCY_UZS:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='UZS'),
                test[1]
            )

    def test_currency_vef(self):
        for test in TEST_CASES_TO_CURRENCY_VEF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='VEF'),
                test[1]
            )

    def test_currency_vnd(self):
        for test in TEST_CASES_TO_CURRENCY_VND:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='VND'),
                test[1]
            )

    def test_currency_vuv(self):
        for test in TEST_CASES_TO_CURRENCY_VUV:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='VUV'),
                test[1]
            )

    def test_currency_wst(self):
        for test in TEST_CASES_TO_CURRENCY_WST:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='WST'),
                test[1]
            )

    def test_currency_xaf(self):
        for test in TEST_CASES_TO_CURRENCY_XAF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='XAF'),
                test[1]
            )

    def test_currency_xcd(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='XCD'),
                test[1]
            )

    def test_currency_xof(self):
        for test in TEST_CASES_TO_CURRENCY_XAF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='XOF'),
                test[1]
            )

    def test_currency_xpf(self):
        for test in TEST_CASES_TO_CURRENCY_XPF:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='XPF'),
                test[1]
            )

    def test_currency_yer(self):
        for test in TEST_CASES_TO_CURRENCY_YER:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='YER'),
                test[1]
            )

    def test_currency_yum(self):
        for test in TEST_CASES_TO_CURRENCY_YUM:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='YUM'),
                test[1]
            )

    def test_currency_zmw(self):
        for test in TEST_CASES_TO_CURRENCY_ZMW:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ZMW'),
                test[1]
            )

    def test_currency_zrz(self):
        for test in TEST_CASES_TO_CURRENCY_ZRZ:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ZRZ'),
                test[1]
            )

    def test_currency_zwl(self):
        for test in TEST_CASES_TO_CURRENCY_BZD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', currency='ZWL'),
                test[1]
            )
