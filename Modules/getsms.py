import json
import os
import requests
from colorama import Fore,init
import time
from datetime import datetime
init(convert=True)

code2pre = {"AF":"+93","AL":"+355","DZ":"+213","AS":"+1","AD":"+376","AO":"+244","AI":"+1","AG":"+1","AR":"+54","AM":"+374","AW":"+297","AC":"+247","AU":"+61","AX":"+672","AT":"+43","AZ":"+994","BS":"+1","BH":"+973","BD":"+880","BB":"+1","BY":"+375","BE":"+32","BZ":"+501","BJ":"+229","BM":"+1","BT":"+975","BO":"+591","BA":"+387","BW":"+267","BR":"+55","VG":"+1","BN":"+673","BG":"+359","BF":"+226","BI":"+257","KH":"+855","CM":"+237","CA":"+1","CV":"+238","KY":"+1","CF":"+236","TD":"+235","CL":"+56","CN":"+86","CO":"+57","KM":"+269","CG":"+242","CK":"+682","CR":"+506","CI":"+225","HR":"+385","CU":"+53","CY":"+357","CZ":"+420","CD":"+243","DK":"+45","DG":"+246","DJ":"+253","DM":"+1","DO":"+1","TL":"+670","EC":"+593","EG":"+20","SV":"+503","GQ":"+240","ER":"+291","EE":"+372","ET":"+251","FK":"+500","FO":"+298","FJ":"+679","FI":"+358","FR":"+33","GF":"+594","PF":"+689","GA":"+241","GM":"+220","GE":"+995","DE":"+49","GH":"+233","GI":"+350","GR":"+30","GL":"+299","GD":"+1","GP":"+590","GU":"+1","GT":"+502","GN":"+224","GW":"+245","GY":"+592","HT":"+509","HN":"+504","HK":"+852","HU":"+36","IS":"+354","IN":"+91","ID":"+62","IR":"+98","IQ":"+964","IE":"+353","IL":"+972","IT":"+39","JM":"+1","JP":"+81","JO":"+962","KZ":"+7","KE":"+254","KI":"+686","XK":"+383","KW":"+965","KG":"+996","LA":"+856","LV":"+371","LB":"+961","LS":"+266","LR":"+231","LY":"+218","LI":"+423","LT":"+370","LU":"+352","MO":"+853","MK":"+389","MG":"+261","MW":"+265","MY":"+60","MV":"+960","ML":"+223","MT":"+356","MH":"+692","MQ":"+596","MR":"+222","MU":"+230","MX":"+52","FM":"+691","MD":"+373","MC":"+377","MN":"+976","ME":"+382","MS":"+1","MA":"+212","MZ":"+258","MM":"+95","NA":"+264","NR":"+674","NP":"+977","NL":"+31","AN":"+599","NC":"+687","NZ":"+64","NI":"+505","NE":"+227","NG":"+234","NU":"+683","KP":"+850","MP":"+1","NO":"+47","OM":"+968","PK":"+92","PW":"+680","PS":"+970","PA":"+507","PG":"+675","PY":"+595","PE":"+51","PH":"+63","PL":"+48","PT":"+351","PR":"+1","QA":"+974","RE":"+262","RO":"+40","RU":"+7","RW":"+250","SH":"+290","KN":"+1","LC":"+1","PM":"+508","VC":"+1","WS":"+685","SM":"+378","ST":"+239","SA":"+966","SN":"+221","RS":"+381","SC":"+248","SL":"+232","SG":"+65","SK":"+421","SI":"+386","SB":"+677","SO":"+252","ZA":"+27","KR":"+82","ES":"+34","LK":"+94","SD":"+249","SR":"+597","SZ":"+268","SE":"+46","CH":"+41","SY":"+963","TW":"+886","TJ":"+992","TZ":"+255","TH":"+66","TG":"+228","TK":"+690","TO":"+676","TT":"+1","TN":"+216","TR":"+90","TM":"+993","TC":"+1","TV":"+688","VI":"+1","UG":"+256","UA":"+380","AE":"+971","GB":"+44","US":"+1","UY":"+598","UZ":"+998","VU":"+678","VA":"+379","VE":"+58","VN":"+84","WF":"+681","YE":"+967","ZM":"+260","ZW":"+263"}
pre2code = [{"country":"Afghanistan","code":"93","iso":"AF"},
{"country":"Albania","code":"355","iso":"AL"},
{"country":"Algeria","code":"213","iso":"DZ"},
{"country":"American Samoa","code":"1-684","iso":"AS"},
{"country":"Andorra","code":"376","iso":"AD"},
{"country":"Angola","code":"244","iso":"AO"},
{"country":"Anguilla","code":"1-264","iso":"AI"},
{"country":"Antarctica","code":"672","iso":"AQ"},
{"country":"Antigua and Barbuda","code":"1-268","iso":"AG"},
{"country":"Argentina","code":"54","iso":"AR"},
{"country":"Armenia","code":"374","iso":"AM"},
{"country":"Aruba","code":"297","iso":"AW"},
{"country":"Australia","code":"61","iso":"AU"},
{"country":"Austria","code":"43","iso":"AT"},
{"country":"Azerbaijan","code":"994","iso":"AZ"},
{"country":"Bahamas","code":"1-242","iso":"BS"},
{"country":"Bahrain","code":"973","iso":"BH"},
{"country":"Bangladesh","code":"880","iso":"BD"},
{"country":"Barbados","code":"1-246","iso":"BB"},
{"country":"Belarus","code":"375","iso":"BY"},
{"country":"Belgium","code":"32","iso":"BE"},
{"country":"Belize","code":"501","iso":"BZ"},
{"country":"Benin","code":"229","iso":"BJ"},
{"country":"Bermuda","code":"1-441","iso":"BM"},
{"country":"Bhutan","code":"975","iso":"BT"},
{"country":"Bolivia","code":"591","iso":"BO"},
{"country":"Bosnia and Herzegovina","code":"387","iso":"BA"},
{"country":"Botswana","code":"267","iso":"BW"},
{"country":"Brazil","code":"55","iso":"BR"},
{"country":"British Indian Ocean Territory","code":"246","iso":"IO"},
{"country":"British Virgin Islands","code":"1-284","iso":"VG"},
{"country":"Brunei","code":"673","iso":"BN"},
{"country":"Bulgaria","code":"359","iso":"BG"},
{"country":"Burkina Faso","code":"226","iso":"BF"},
{"country":"Burundi","code":"257","iso":"BI"},
{"country":"Cambodia","code":"855","iso":"KH"},
{"country":"Cameroon","code":"237","iso":"CM"},
{"country":"Canada","code":"1","iso":"CA"},
{"country":"Cape Verde","code":"238","iso":"CV"},
{"country":"Cayman Islands","code":"1-345","iso":"KY"},
{"country":"Central African Republic","code":"236","iso":"CF"},
{"country":"Chad","code":"235","iso":"TD"},
{"country":"Chile","code":"56","iso":"CL"},
{"country":"China","code":"86","iso":"CN"},
{"country":"Christmas Island","code":"61","iso":"CX"},
{"country":"Cocos Islands","code":"61","iso":"CC"},
{"country":"Colombia","code":"57","iso":"CO"},
{"country":"Comoros","code":"269","iso":"KM"},
{"country":"Cook Islands","code":"682","iso":"CK"},
{"country":"Costa Rica","code":"506","iso":"CR"},
{"country":"Croatia","code":"385","iso":"HR"},
{"country":"Cuba","code":"53","iso":"CU"},
{"country":"Curacao","code":"599","iso":"CW"},
{"country":"Cyprus","code":"357","iso":"CY"},
{"country":"Czech Republic","code":"420","iso":"CZ"},
{"country":"Democratic Republic of the Congo","code":"243","iso":"CD"},
{"country":"Denmark","code":"45","iso":"DK"},
{"country":"Djibouti","code":"253","iso":"DJ"},
{"country":"Dominica","code":"1-767","iso":"DM"},
{"country":"Dominican Republic","code":"1-809, 1-829, 1-849","iso":"DO"},
{"country":"East Timor","code":"670","iso":"TL"},
{"country":"Ecuador","code":"593","iso":"EC"},
{"country":"Egypt","code":"20","iso":"EG"},
{"country":"El Salvador","code":"503","iso":"SV"},
{"country":"Equatorial Guinea","code":"240","iso":"GQ"},
{"country":"Eritrea","code":"291","iso":"ER"},
{"country":"Estonia","code":"372","iso":"EE"},
{"country":"Ethiopia","code":"251","iso":"ET"},
{"country":"Falkland Islands","code":"500","iso":"FK"},
{"country":"Faroe Islands","code":"298","iso":"FO"},
{"country":"Fiji","code":"679","iso":"FJ"},
{"country":"Finland","code":"358","iso":"FI"},
{"country":"France","code":"33","iso":"FR"},
{"country":"French Polynesia","code":"689","iso":"PF"},
{"country":"Gabon","code":"241","iso":"GA"},
{"country":"Gambia","code":"220","iso":"GM"},
{"country":"Georgia","code":"995","iso":"GE"},
{"country":"Germany","code":"49","iso":"DE"},
{"country":"Ghana","code":"233","iso":"GH"},
{"country":"Gibraltar","code":"350","iso":"GI"},
{"country":"Greece","code":"30","iso":"GR"},
{"country":"Greenland","code":"299","iso":"GL"},
{"country":"Grenada","code":"1-473","iso":"GD"},
{"country":"Guam","code":"1-671","iso":"GU"},
{"country":"Guatemala","code":"502","iso":"GT"},
{"country":"Guernsey","code":"44-1481","iso":"GG"},
{"country":"Guinea","code":"224","iso":"GN"},
{"country":"Guinea-Bissau","code":"245","iso":"GW"},
{"country":"Guyana","code":"592","iso":"GY"},
{"country":"Haiti","code":"509","iso":"HT"},
{"country":"Honduras","code":"504","iso":"HN"},
{"country":"Hong Kong","code":"852","iso":"HK"},
{"country":"Hungary","code":"36","iso":"HU"},
{"country":"Iceland","code":"354","iso":"IS"},
{"country":"India","code":"91","iso":"IN"},
{"country":"Indonesia","code":"62","iso":"ID"},
{"country":"Iran","code":"98","iso":"IR"},
{"country":"Iraq","code":"964","iso":"IQ"},
{"country":"Ireland","code":"353","iso":"IE"},
{"country":"Isle of Man","code":"44-1624","iso":"IM"},
{"country":"Israel","code":"972","iso":"IL"},
{"country":"Italy","code":"39","iso":"IT"},
{"country":"Ivory Coast","code":"225","iso":"CI"},
{"country":"Jamaica","code":"1-876","iso":"JM"},
{"country":"Japan","code":"81","iso":"JP"},
{"country":"Jersey","code":"44-1534","iso":"JE"},
{"country":"Jordan","code":"962","iso":"JO"},
{"country":"Kazakhstan","code":"7","iso":"KZ"},
{"country":"Kenya","code":"254","iso":"KE"},
{"country":"Kiribati","code":"686","iso":"KI"},
{"country":"Kosovo","code":"383","iso":"XK"},
{"country":"Kuwait","code":"965","iso":"KW"},
{"country":"Kyrgyzstan","code":"996","iso":"KG"},
{"country":"Laos","code":"856","iso":"LA"},
{"country":"Latvia","code":"371","iso":"LV"},
{"country":"Lebanon","code":"961","iso":"LB"},
{"country":"Lesotho","code":"266","iso":"LS"},
{"country":"Liberia","code":"231","iso":"LR"},
{"country":"Libya","code":"218","iso":"LY"},
{"country":"Liechtenstein","code":"423","iso":"LI"},
{"country":"Lithuania","code":"370","iso":"LT"},
{"country":"Luxembourg","code":"352","iso":"LU"},
{"country":"Macao","code":"853","iso":"MO"},
{"country":"Macedonia","code":"389","iso":"MK"},
{"country":"Madagascar","code":"261","iso":"MG"},
{"country":"Malawi","code":"265","iso":"MW"},
{"country":"Malaysia","code":"60","iso":"MY"},
{"country":"Maldives","code":"960","iso":"MV"},
{"country":"Mali","code":"223","iso":"ML"},
{"country":"Malta","code":"356","iso":"MT"},
{"country":"Marshall Islands","code":"692","iso":"MH"},
{"country":"Mauritania","code":"222","iso":"MR"},
{"country":"Mauritius","code":"230","iso":"MU"},
{"country":"Mayotte","code":"262","iso":"YT"},
{"country":"Mexico","code":"52","iso":"MX"},
{"country":"Micronesia","code":"691","iso":"FM"},
{"country":"Moldova","code":"373","iso":"MD"},
{"country":"Monaco","code":"377","iso":"MC"},
{"country":"Mongolia","code":"976","iso":"MN"},
{"country":"Montenegro","code":"382","iso":"ME"},
{"country":"Montserrat","code":"1-664","iso":"MS"},
{"country":"Morocco","code":"212","iso":"MA"},
{"country":"Mozambique","code":"258","iso":"MZ"},
{"country":"Myanmar","code":"95","iso":"MM"},
{"country":"Namibia","code":"264","iso":"NA"},
{"country":"Nauru","code":"674","iso":"NR"},
{"country":"Nepal","code":"977","iso":"NP"},
{"country":"Netherlands","code":"31","iso":"NL"},
{"country":"Netherlands Antilles","code":"599","iso":"AN"},
{"country":"New Caledonia","code":"687","iso":"NC"},
{"country":"New Zealand","code":"64","iso":"NZ"},
{"country":"Nicaragua","code":"505","iso":"NI"},
{"country":"Niger","code":"227","iso":"NE"},
{"country":"Nigeria","code":"234","iso":"NG"},
{"country":"Niue","code":"683","iso":"NU"},
{"country":"North Korea","code":"850","iso":"KP"},
{"country":"Northern Mariana Islands","code":"1-670","iso":"MP"},
{"country":"Norway","code":"47","iso":"NO"},
{"country":"Oman","code":"968","iso":"OM"},
{"country":"Pakistan","code":"92","iso":"PK"},
{"country":"Palau","code":"680","iso":"PW"},
{"country":"Palestine","code":"970","iso":"PS"},
{"country":"Panama","code":"507","iso":"PA"},
{"country":"Papua New Guinea","code":"675","iso":"PG"},
{"country":"Paraguay","code":"595","iso":"PY"},
{"country":"Peru","code":"51","iso":"PE"},
{"country":"Philippines","code":"63","iso":"PH"},
{"country":"Pitcairn","code":"64","iso":"PN"},
{"country":"Poland","code":"48","iso":"PL"},
{"country":"Portugal","code":"351","iso":"PT"},
{"country":"Puerto Rico","code":"1-787, 1-939","iso":"PR"},
{"country":"Qatar","code":"974","iso":"QA"},
{"country":"Republic of the Congo","code":"242","iso":"CG"},
{"country":"Reunion","code":"262","iso":"RE"},
{"country":"Romania","code":"40","iso":"RO"},
{"country":"Russia","code":"7","iso":"RU"},
{"country":"Rwanda","code":"250","iso":"RW"},
{"country":"Saint Barthelemy","code":"590","iso":"BL"},
{"country":"Saint Helena","code":"290","iso":"SH"},
{"country":"Saint Kitts and Nevis","code":"1-869","iso":"KN"},
{"country":"Saint Lucia","code":"1-758","iso":"LC"},
{"country":"Saint Martin","code":"590","iso":"MF"},
{"country":"Saint Pierre and Miquelon","code":"508","iso":"PM"},
{"country":"Saint Vincent and the Grenadines","code":"1-784","iso":"VC"},
{"country":"Samoa","code":"685","iso":"WS"},
{"country":"San Marino","code":"378","iso":"SM"},
{"country":"Sao Tome and Principe","code":"239","iso":"ST"},
{"country":"Saudi Arabia","code":"966","iso":"SA"},
{"country":"Senegal","code":"221","iso":"SN"},
{"country":"Serbia","code":"381","iso":"RS"},
{"country":"Seychelles","code":"248","iso":"SC"},
{"country":"Sierra Leone","code":"232","iso":"SL"},
{"country":"Singapore","code":"65","iso":"SG"},
{"country":"Sint Maarten","code":"1-721","iso":"SX"},
{"country":"Slovakia","code":"421","iso":"SK"},
{"country":"Slovenia","code":"386","iso":"SI"},
{"country":"Solomon Islands","code":"677","iso":"SB"},
{"country":"Somalia","code":"252","iso":"SO"},
{"country":"South Africa","code":"27","iso":"ZA"},
{"country":"South Korea","code":"82","iso":"KR"},
{"country":"South Sudan","code":"211","iso":"SS"},
{"country":"Spain","code":"34","iso":"ES"},
{"country":"Sri Lanka","code":"94","iso":"LK"},
{"country":"Sudan","code":"249","iso":"SD"},
{"country":"Suriname","code":"597","iso":"SR"},
{"country":"Svalbard and Jan Mayen","code":"47","iso":"SJ"},
{"country":"Swaziland","code":"268","iso":"SZ"},
{"country":"Sweden","code":"46","iso":"SE"},
{"country":"Switzerland","code":"41","iso":"CH"},
{"country":"Syria","code":"963","iso":"SY"},
{"country":"Taiwan","code":"886","iso":"TW"},
{"country":"Tajikistan","code":"992","iso":"TJ"},
{"country":"Tanzania","code":"255","iso":"TZ"},
{"country":"Thailand","code":"66","iso":"TH"},
{"country":"Togo","code":"228","iso":"TG"},
{"country":"Tokelau","code":"690","iso":"TK"},
{"country":"Tonga","code":"676","iso":"TO"},
{"country":"Trinidad and Tobago","code":"1-868","iso":"TT"},
{"country":"Tunisia","code":"216","iso":"TN"},
{"country":"Turkey","code":"90","iso":"TR"},
{"country":"Turkmenistan","code":"993","iso":"TM"},
{"country":"Turks and Caicos Islands","code":"1-649","iso":"TC"},
{"country":"Tuvalu","code":"688","iso":"TV"},
{"country":"U.S. Virgin Islands","code":"1-340","iso":"VI"},
{"country":"Uganda","code":"256","iso":"UG"},
{"country":"Ukraine","code":"380","iso":"UA"},
{"country":"United Arab Emirates","code":"971","iso":"AE"},
{"country":"United Kingdom","code":"44","iso":"GB"},
{"country":"United States","code":"1","iso":"US"},
{"country":"Uruguay","code":"598","iso":"UY"},
{"country":"Uzbekistan","code":"998","iso":"UZ"},
{"country":"Vanuatu","code":"678","iso":"VU"},
{"country":"Vatican","code":"379","iso":"VA"},
{"country":"Venezuela","code":"58","iso":"VE"},
{"country":"Vietnam","code":"84","iso":"VN"},
{"country":"Wallis and Futuna","code":"681","iso":"WF"},
{"country":"Western Sahara","code":"212","iso":"EH"},
{"country":"Yemen","code":"967","iso":"YE"},
{"country":"Zambia","code":"260","iso":"ZM"},
{"country":"Zimbabwe","code":"263","iso":"ZW"}]

twoandthreelet = [
    {"name":"Afghanistan","let2":" AF","let3":"AFG"},
    {"name":"Albania","let2":"AL","let3":"ALB"},
    {"name":"Algeria","let2":"DZ","let3":"DZA"},
    {"name":"American Samoa","let2":"AS","let3":"ASM"},
    {"name":"Andorra","let2":"AD","let3":"AND"},
    {"name":"Angola","let2":"AO","let3":"AGO"},
    {"name":"Anguilla","let2":"AI","let3":"AIA"},
    {"name":"Antigua and Barbuda","let2":"AG","let3":"ATG"},
    {"name":"Argentina","let2":"AR","let3":"ARG"},
    {"name":"Armenia","let2":"AM","let3":"ARM"},
    {"name":"Aruba","let2":"AW","let3":"ABW"},
    {"name":"Australia","let2":"AU","let3":"AUS"},
    {"name":"Austria","let2":"AT","let3":"AUT"},
    {"name":"Azerbaijan","let2":"AZ","let3":"AZE"},
    {"name":"Bahamas","let2":"BS","let3":"BHS"},
    {"name":"Bahrain","let2":"BH","let3":"BHR"},
    {"name":"Bangladesh","let2":"BD","let3":"BGD"},
    {"name":"Barbados","let2":"BB","let3":"BRB"},
    {"name":"Belarus","let2":"BY","let3":"BLR"},
    {"name":"Belgium","let2":"BE","let3":"BEL"},
    {"name":"Belize","let2":"BZ","let3":"BLZ"},
    {"name":"Benin","let2":"BJ","let3":"BEN"},
    {"name":"Bermuda","let2":"BM","let3":"BMU"},
    {"name":"Bhutan","let2":"BT","let3":"BTN"},
    {"name":"Bolivia","let2":"BO","let3":"BOL"},
    {"name":"Bosnia and Herzegovina","let2":"BA","let3":"BIH"},
    {"name":"Botswana","let2":"BW","let3":"BWA"},
    {"name":"Brazil","let2":"BR","let3":"BRA"},
    {"name":"British Virgin Islands","let2":"VG","let3":"VGB"},
    {"name":"Brunei Darussalam","let2":"BN","let3":"BRN"},
    {"name":"Bulgaria","let2":"BG","let3":"BGR"},
    {"name":"Burkina Faso","let2":"BF","let3":"BFA"},
    {"name":"Burundi","let2":"BI","let3":"BDI"},
    {"name":"Cambodia","let2":"KH","let3":"KHM"},
    {"name":"Cameroon","let2":"CM","let3":"CMR"},
    {"name":"Canada","let2":"CA","let3":"CAN"},
    {"name":"Cape Verde","let2":"CV","let3":"CPV"},
    {"name":"Central African Republic","let2":"CF","let3":"CAF"},
    {"name":"Chad","let2":"TD","let3":"TCD"},
    {"name":"Chile","let2":"CL","let3":"CHL"},
    {"name":"China","let2":"CN","let3":"CHN"},
    {"name":"Hong Kong","let2":"HK","let3":"HKG"},
    {"name":"Macao","let2":"MO","let3":"MAC"},
    {"name":"Colombia","let2":"CO","let3":"COL"},
    {"name":"Comoros","let2":"KM","let3":"COM"},
    {"name":"Congo","let2":"CG","let3":"COG"},
    {"name":"Costa Rica","let2":"CR","let3":"CRI"},
    {"name":"Côte d'Ivoire","let2":"CI","let3":"CIV"},
    {"name":"Croatia","let2":"HR","let3":"HRV"},
    {"name":"Cuba","let2":"CU","let3":"CUB"},
    {"name":"Cyprus","let2":"CY","let3":"CYP"},
    {"name":"Czech Republic","let2":"CZ","let3":"CZE"},
    {"name":"Denmark","let2":"DK","let3":"DNK"},
    {"name":"Djibouti","let2":"DJ","let3":"DJI"},
    {"name":"Dominica","let2":"DM","let3":"DMA"},
    {"name":"Dominican Republic","let2":"DO","let3":"DOM"},
    {"name":"Ecuador","let2":"EC","let3":"ECU"},
    {"name":"Egypt","let2":"EG","let3":"EGY"},
    {"name":"El Salvador","let2":"SV","let3":"SLV"},
    {"name":"Equatorial Guinea","let2":"GQ","let3":"GNQ"},
    {"name":"Eritrea","let2":"ER","let3":"ERI"},
    {"name":"Estonia","let2":"EE","let3":"EST"},
    {"name":"Ethiopia","let2":"ET","let3":"ETH"},
    {"name":"Faroe Islands","let2":"FO","let3":" FRO"},
    {"name":"Fiji","let2":"FJ","let3":"FJI"},
    {"name":"Finland","let2":"FI","let3":"FIN"},
    {"name":"France","let2":"FR","let3":"FRA"},
    {"name":"French Guiana","let2":"GF","let3":"GUF"},
    {"name":"French Polynesia","let2":"PF","let3":"PYF"},
    {"name":"Gabon","let2":"GA","let3":"GAB"},
    {"name":"Gambia","let2":"GM","let3":"GMB"},
    {"name":"Georgia","let2":"GE","let3":"GEO"},
    {"name":"Germany","let2":"DE","let3":"DEU"},
    {"name":"Ghana","let2":"GH","let3":"GHA"},
    {"name":"Greece","let2":"GR","let3":"GRC"},
    {"name":"Greenland","let2":"GL","let3":"GRL"},
    {"name":"Grenada","let2":"GD","let3":"GRD"},
    {"name":"Guadeloupe","let2":"GP","let3":"GLP"},
    {"name":"Guam","let2":"GU","let3":"GUM"},
    {"name":"Guatemala","let2":"GT","let3":"GTM"},
    {"name":"Guinea-Bissau","let2":"GW","let3":"GNB"},
    {"name":"Haiti","let2":"HT","let3":"HTI"},
    {"name":"Honduras","let2":"HN","let3":"HND"},
    {"name":"Iceland","let2":"IS","let3":"ISL"},
    {"name":"Indonesia","let2":"ID","let3":"IDN"},
    {"name":"Iraq","let2":"IQ","let3":"IRQ"},
    {"name":"Italy","let2":"IT","let3":"ITA"},
    {"name":"Japan","let2":"JP","let3":"JPN"},
    {"name":"Jordan","let2":"JO","let3":"JOR"},
    {"name":"Kazakhstan","let2":"KZ","let3":"KAZ"},
    {"name":"Kenya","let2":"KE","let3":"KEN"},
    {"name":"Kiribati","let2":"KI","let3":"KIR"},
    {"name":"Korea","let2":"KP","let3":"PRK"},
    {"name":"Korea","let2":"KR","let3":"KOR"},
    {"name":"Kuwait","let2":"KW","let3":"KWT"},
    {"name":"Kyrgyzstan","let2":"KG","let3":"KGZ"},
    {"name":"Lao PDR","let2":"LA","let3":"LAO"},
    {"name":"Latvia","let2":"LV","let3":"LVA"},
    {"name":"Lebanon","let2":"LB","let3":"LBN"},
    {"name":"Lesotho","let2":"LS","let3":"LSO"},
    {"name":"Liberia","let2":"LR","let3":"LBR"},
    {"name":"Libya","let2":"LY","let3":"LBY"},
    {"name":"Liechtenstein","let2":"LI","let3":"LIE"},
    {"name":"Lithuania","let2":"LT","let3":"LTU"},
    {"name":"Luxembourg","let2":"LU","let3":"LUX"},
    {"name":"Madagascar","let2":"MG","let3":"MDG"},
    {"name":"Malawi","let2":"MW","let3":"MWI"},
    {"name":"Malaysia","let2":"MY","let3":"MYS"},
    {"name":"Maldives","let2":"MV","let3":"MDV"},
    {"name":"Mali","let2":"ML","let3":"MLI"},
    {"name":"Malta","let2":"MT","let3":"MLT"},
    {"name":"Marshall Islands","let2":"MH","let3":"MHL"},
    {"name":"Martinique","let2":"MQ","let3":"MTQ"},
    {"name":"Mauritania","let2":"MR","let3":"MRT"},
    {"name":"Mauritius","let2":"MU","let3":"MUS"},
    {"name":"Mexico","let2":"MX","let3":"MEX"},
    {"name":"Micronesia, Federated States of","let2":"FM","let3":"FSM"},
    {"name":"Moldova","let2":"MD","let3":"MDA"},
    {"name":"Monaco","let2":"MC","let3":"MCO"},
    {"name":"Mongolia","let2":"MN","let3":"MNG"},
    {"name":"Montenegro","let2":"ME","let3":"MNE"},
    {"name":"Montserrat","let2":"MS","let3":"MSR"},
    {"name":"Morocco","let2":"MA","let3":"MAR"},
    {"name":"Mozambique","let2":"MZ","let3":"MOZ"},
    {"name":"Myanmar","let2":"MM","let3":"MMR"},
    {"name":"Namibia","let2":"NA","let3":"NAM"},
    {"name":"Nauru","let2":"NR","let3":"NRU"},
    {"name":"Nepal","let2":"NP","let3":"NPL"},
    {"name":"Netherlands","let2":"NL","let3":"NLD"},
    {"name":"Netherlands Antilles","let2":"AN","let3":"ANT"},
    {"name":"New Caledonia","let2":"NC","let3":"NCL"},
    {"name":"New Zealand","let2":"NZ","let3":"NZL"},
    {"name":"Nicaragua","let2":"NI","let3":"NIC"},
    {"name":"Niger","let2":"NE","let3":"NER"},
    {"name":"Nigeria","let2":"NG","let3":"NGA"},
    {"name":"Northern Mariana Islands","let2":"MP","let3":"MNP"},
    {"name":"Norway","let2":"NO","let3":"NOR"},
    {"name":"Oman","let2":"OM","let3":"OMN"},
    {"name":"Pakistan","let2":"PK","let3":"PAK"},
    {"name":"Palau","let2":"PW","let3":"PLW"},
    {"name":"Palestinian Territory","let2":"PS","let3":"PSE"},
    {"name":"Panama","let2":"PA","let3":"PAN"},
    {"name":"Papua New Guinea","let2":"PG","let3":"PNG"},
    {"name":"Paraguay","let2":"PY","let3":"PRY"},
    {"name":"Peru","let2":"PE","let3":"PER"},
    {"name":"Philippines","let2":"PH","let3":"PHL"},
    {"name":"Pitcairn","let2":"PN","let3":"PCN"},
    {"name":"Poland","let2":"PL","let3":"POL"},
    {"name":"Portugal","let2":"PT","let3":"PRT"},
    {"name":"Puerto Rico","let2":"PR","let3":"PRI"},
    {"name":"Qatar","let2":"QA","let3":"QAT"},
    {"name":"Réunion","let2":"RE","let3":"REU"},
    {"name":"Romania","let2":"RO","let3":"ROU"},
    {"name":"Russian Federation","let2":"RU","let3":"RUS"},
    {"name":"Rwanda","let2":"RW","let3":"RWA"},
    {"name":"Saint Kitts and Nevis","let2":"KN","let3":"KNA"},
    {"name":"Saint Lucia","let2":"LC","let3":"LCA"},
    {"name":"Saint Vincent and Grenadines","let2":"VC","let3":"VCT"},
    {"name":"Samoa","let2":"WS","let3":"WSM"},
    {"name":"San Marino","let2":"SM","let3":"SMR"},
    {"name":"Sao Tome and Principe","let2":"ST","let3":"STP"},
    {"name":"Saudi Arabia","let2":"SA","let3":"SAU"},
    {"name":"Senegal","let2":"SN","let3":"SEN"},
    {"name":"Serbia","let2":"RS","let3":"SRB"},
    {"name":"Seychelles","let2":"SC","let3":"SYC"},
    {"name":"Sierra Leone","let2":"SL","let3":"SLE"},
    {"name":"Singapore","let2":"SG","let3":"SGP"},
    {"name":"Slovakia","let2":"SK","let3":"SVK"},
    {"name":"Slovenia","let2":"SI","let3":"SVN"},
    {"name":"Solomon Islands","let2":"SB","let3":"SLB"},
    {"name":"Somalia","let2":"SO","let3":"SOM"},
    {"name":"South Africa","let2":"ZA","let3":"ZAF"},
    {"name":"Spain","let2":"ES","let3":"ESP"},
    {"name":"Sri Lanka","let2":"LK","let3":"LKA"},
    {"name":"Sudan","let2":"SD","let3":"SDN"},
    {"name":"Suriname","let2":"SR","let3":"SUR"},
    {"name":"Swaziland","let2":"SZ","let3":"SWZ"},
    {"name":"Sweden","let2":"SE","let3":"SWE"},
    {"name":"Switzerland","let2":"CH","let3":"CHE"},
    {"name":"Syrian Arab Republic","let2":"SY","let3":"SYR"},
    {"name":"Tajikistan","let2":"TJ","let3":"TJK"},
    {"name":"Tanzania","let2":"TZ","let3":"TZA"},
    {"name":"Thailand","let2":"TH","let3":"THA"},
    {"name":"Timor-Leste","let2":"TL","let3":"TLS"},
    {"name":"Togo","let2":"TG","let3":"TGO"},
    {"name":"Tonga","let2":"TO","let3":"TON"},
    {"name":"Trinidad and Tobago","let2":"TT","let3":"TTO"},
    {"name":"Tunisia","let2":"TN","let3":"TUN"},
    {"name":"Turkey","let2":"TR","let3":"TUR"},
    {"name":"Turkmenistan","let2":"TM","let3":"TKM"},
    {"name":"Tuvalu","let2":"TV","let3":"TUV"},
    {"name":"Uganda","let2":"UG","let3":"UGA"},
    {"name":"Ukraine","let2":"UA","let3":"UKR"},
    {"name":"United Arab Emirates","let2":"AE","let3":"ARE"},
    {"name":"United Kingdom","let2":"GB","let3":"GBR"},
    {"name":"United States of America","let2":"US","let3":"USA"},
    {"name":"Uruguay","let2":"UY","let3":"URY"},
    {"name":"Uzbekistan","let2":"UZ","let3":"UZB"},
    {"name":"Vanuatu","let2":"VU","let3":"VUT"},
    {"name":"Venezuela","let2":"VE","let3":"VEN"},
    {"name":"Viet Nam","let2":"VN","let3":"VNM"},
    {"name":"Virgin Islands, US","let2":"VI","let3":"VIR"},
    {"name":"Yemen","let2":"YE","let3":"YEM"},
    {"name":"Zambia","let2":"ZM","let3":"ZMB"},
    {"name":"Zimbabwe","let2":"ZW","let3":"ZWE"}
]
regtocode = [
  {
    "Country": "Russia",
    "Code": 0
  },
  {
    "Country": "Ukraine",
    "Code": 1
  },
  {
    "Country": "Kazakhstan",
    "Code": 2
  },
  {
    "Country": "China",
    "Code": 3
  },
  {
    "Country": "Philippines",
    "Code": 4
  },
  {
    "Country": "Myanmar",
    "Code": 5
  },
  {
    "Country": "Indonesia",
    "Code": 6
  },
  {
    "Country": "Malaysia",
    "Code": 7
  },
  {
    "Country": "Kenya",
    "Code": 8
  },
  {
    "Country": "Tanzania",
    "Code": 9
  },
  {
    "Country": "Vietnam",
    "Code": 10
  },
  {
    "Country": "Kyrgyzstan",
    "Code": 11
  },
  {
    "Country": "United States",
    "Code": 12
  },
  {
    "Country": "Israel",
    "Code": 13
  },
  {
    "Country": "HongKong",
    "Code": 14
  },
  {
    "Country": "Poland",
    "Code": 15
  },
  {
    "Country": "United Kingdom",
    "Code": 16
  },
  {
    "Country": "Madagascar",
    "Code": 17
  },
  {
    "Country": "DCongo",
    "Code": 18
  },
  {
    "Country": "Nigeria",
    "Code": 19
  },
  {
    "Country": "Macao",
    "Code": 20
  },
  {
    "Country": "Egypt",
    "Code": 21
  },
  {
    "Country": "India",
    "Code": 22
  },
  {
    "Country": "Ireland",
    "Code": 23
  },
  {
    "Country": "Cambodia",
    "Code": 24
  },
  {
    "Country": "Laos",
    "Code": 25
  },
  {
    "Country": "Haiti",
    "Code": 26
  },
  {
    "Country": "Ivory",
    "Code": 27
  },
  {
    "Country": "Gambia",
    "Code": 28
  },
  {
    "Country": "Serbia",
    "Code": 29
  },
  {
    "Country": "Yemen",
    "Code": 30
  },
  {
    "Country": "South africa",
    "Code": 31
  },
  {
    "Country": "Romania",
    "Code": 32
  },
  {
    "Country": "Colombia",
    "Code": 33
  },
  {
    "Country": "Estonia",
    "Code": 34
  },
  {
    "Country": "Canada",
    "Code": 36
  },
  {
    "Country": "Morocco",
    "Code": 37
  },
  {
    "Country": "Ghana",
    "Code": 38
  },
  {
    "Country": "Argentina",
    "Code": 39
  },
  {
    "Country": "Uzbekistan",
    "Code": 40
  },
  {
    "Country": "Cameroon",
    "Code": 41
  },
  {
    "Country": "Chad",
    "Code": 42
  },
  {
    "Country": "Germany",
    "Code": 43
  },
  {
    "Country": "Lithuania",
    "Code": 44
  },
  {
    "Country": "Croatia",
    "Code": 45
  },
  {
    "Country": "Sweden",
    "Code": 46
  },
  {
    "Country": "Iraq",
    "Code": 47
  },
  {
    "Country": "Netherlands",
    "Code": 48
  },
  {
    "Country": "Latvia",
    "Code": 49
  },
  {
    "Country": "Austria",
    "Code": 50
  },
  {
    "Country": "Belarus",
    "Code": 51
  },
  {
    "Country": "Thailand",
    "Code": 52
  },
  {
    "Country": "Saudiarabia",
    "Code": 53
  },
  {
    "Country": "Mexico",
    "Code": 54
  },
  {
    "Country": "Taiwan",
    "Code": 55
  },
  {
    "Country": "Spain",
    "Code": 56
  },
  {
    "Country": "Algeria",
    "Code": 58
  },
  {
    "Country": "Slovenia",
    "Code": 59
  },
  {
    "Country": "Bangladesh",
    "Code": 60
  },
  {
    "Country": "Senegal",
    "Code": 61
  },
  {
    "Country": "Turkey",
    "Code": 62
  },
  {
    "Country": "Czech",
    "Code": 63
  },
  {
    "Country": "Srilanka",
    "Code": 64
  },
  {
    "Country": "Peru",
    "Code": 65
  },
  {
    "Country": "Pakistan",
    "Code": 66
  },
  {
    "Country": "Newzealand",
    "Code": 67
  },
  {
    "Country": "Guinea",
    "Code": 68
  },
  {
    "Country": "Mali",
    "Code": 69
  },
  {
    "Country": "Venezuela",
    "Code": 70
  },
  {
    "Country": "Ethiopia",
    "Code": 71
  },
  {
    "Country": "Mongolia",
    "Code": 72
  },
  {
    "Country": "Brazil",
    "Code": 73
  },
  {
    "Country": "Afghanistan",
    "Code": 74
  },
  {
    "Country": "Uganda",
    "Code": 75
  },
  {
    "Country": "Angola",
    "Code": 76
  },
  {
    "Country": "Cyprus",
    "Code": 77
  },
  {
    "Country": "France",
    "Code": 78
  },
  {
    "Country": "Papua",
    "Code": 79
  },
  {
    "Country": "Mozambique",
    "Code": 80
  },
  {
    "Country": "Nepal",
    "Code": 81
  },
  {
    "Country": "Belgium",
    "Code": 82
  },
  {
    "Country": "Bulgaria",
    "Code": 83
  },
  {
    "Country": "Hungary",
    "Code": 84
  },
  {
    "Country": "Moldova",
    "Code": 85
  },
  {
    "Country": "Italy",
    "Code": 86
  },
  {
    "Country": "Paraguay",
    "Code": 87
  },
  {
    "Country": "Honduras",
    "Code": 88
  },
  {
    "Country": "Tunisia",
    "Code": 89
  },
  {
    "Country": "Nicaragua",
    "Code": 90
  },
  {
    "Country": "Timorleste",
    "Code": 91
  },
  {
    "Country": "Bolivia",
    "Code": 92
  },
  {
    "Country": "Costarica",
    "Code": 93
  },
  {
    "Country": "Guatemala",
    "Code": 94
  },
  {
    "Country": "Uae",
    "Code": 95
  },
  {
    "Country": "Zimbabwe",
    "Code": 96
  },
  {
    "Country": "Puertorico",
    "Code": 97
  },
  {
    "Country": "Togo",
    "Code": 99
  },
  {
    "Country": "Kuwait",
    "Code": 100
  },
  {
    "Country": "Salvador",
    "Code": 101
  },
  {
    "Country": "Libyan",
    "Code": 102
  },
  {
    "Country": "Jamaica",
    "Code": 103
  },
  {
    "Country": "Trinidad",
    "Code": 104
  },
  {
    "Country": "Ecuador",
    "Code": 105
  },
  {
    "Country": "Swaziland",
    "Code": 106
  },
  {
    "Country": "Oman",
    "Code": 107
  },
  {
    "Country": "Bosnia",
    "Code": 108
  },
  {
    "Country": "Dominican",
    "Code": 109
  },
  {
    "Country": "Qatar",
    "Code": 111
  },
  {
    "Country": "Panama",
    "Code": 112
  },
  {
    "Country": "Mauritania",
    "Code": 114
  },
  {
    "Country": "Sierraleone",
    "Code": 115
  },
  {
    "Country": "Jordan",
    "Code": 116
  },
  {
    "Country": "Portugal",
    "Code": 117
  },
  {
    "Country": "Barbados",
    "Code": 118
  },
  {
    "Country": "Burundi",
    "Code": 119
  },
  {
    "Country": "Benin",
    "Code": 120
  },
  {
    "Country": "Brunei",
    "Code": 121
  },
  {
    "Country": "Bahamas",
    "Code": 122
  },
  {
    "Country": "Botswana",
    "Code": 123
  },
  {
    "Country": "Belize",
    "Code": 124
  },
  {
    "Country": "Caf",
    "Code": 125
  },
  {
    "Country": "Dominica",
    "Code": 126
  },
  {
    "Country": "Grenada",
    "Code": 127
  },
  {
    "Country": "Georgia",
    "Code": 128
  },
  {
    "Country": "Greece",
    "Code": 129
  },
  {
    "Country": "Guineabissau",
    "Code": 130
  },
  {
    "Country": "Guyana",
    "Code": 131
  },
  {
    "Country": "Iceland",
    "Code": 132
  },
  {
    "Country": "Comoros",
    "Code": 133
  },
  {
    "Country": "Saintkitts",
    "Code": 134
  },
  {
    "Country": "Liberia",
    "Code": 135
  },
  {
    "Country": "Lesotho",
    "Code": 136
  },
  {
    "Country": "Malawi",
    "Code": 137
  },
  {
    "Country": "Namibia",
    "Code": 138
  },
  {
    "Country": "Niger",
    "Code": 139
  },
  {
    "Country": "Rwanda",
    "Code": 140
  },
  {
    "Country": "Slovakia",
    "Code": 141
  },
  {
    "Country": "Suriname",
    "Code": 142
  },
  {
    "Country": "Tajikistan",
    "Code": 143
  },
  {
    "Country": "Monaco",
    "Code": 144
  },
  {
    "Country": "Bahrain",
    "Code": 145
  },
  {
    "Country": "Reunion",
    "Code": 146
  },
  {
    "Country": "Zambia",
    "Code": 147
  },
  {
    "Country": "Armenia",
    "Code": 148
  },
  {
    "Country": "Somalia",
    "Code": 149
  },
  {
    "Country": "Congo",
    "Code": 150
  },
  {
    "Country": "Chile",
    "Code": 151
  },
  {
    "Country": "Burkinafaso",
    "Code": 152
  },
  {
    "Country": "Lebanon",
    "Code": 153
  },
  {
    "Country": "Gabon",
    "Code": 154
  },
  {
    "Country": "Albania",
    "Code": 155
  },
  {
    "Country": "Uruguay",
    "Code": 156
  },
  {
    "Country": "Mauritius",
    "Code": 157
  },
  {
    "Country": "Bhutan",
    "Code": 158
  },
  {
    "Country": "Maldives",
    "Code": 159
  },
  {
    "Country": "Guadeloupe",
    "Code": 160
  },
  {
    "Country": "Turkmenistan",
    "Code": 161
  },
  {
    "Country": "Frenchguiana",
    "Code": 162
  },
  {
    "Country": "Finland",
    "Code": 163
  },
  {
    "Country": "Saintlucia",
    "Code": 164
  },
  {
    "Country": "Luxembourg",
    "Code": 165
  },
  {
    "Country": "Saint vincent grenadines",
    "Code": 166
  },
  {
    "Country": "Equatorial guinea",
    "Code": 167
  },
  {
    "Country": "Djibouti",
    "Code": 168
  },
  {
    "Country": "Antigua barbuda",
    "Code": 169
  },
  {
    "Country": "Cayman islands",
    "Code": 170
  },
  {
    "Country": "Montenegro",
    "Code": 171
  },
  {
    "Country": "Denmark",
    "Code": 172
  },
  {
    "Country": "Switzerland",
    "Code": 173
  },
  {
    "Country": "Norway",
    "Code": 174
  },
  {
    "Country": "Australia",
    "Code": 175
  },
  {
    "Country": "Eritrea",
    "Code": 176
  },
  {
    "Country": "South sudan",
    "Code": 177
  },
  {
    "Country": "Saotomeandprincipe",
    "Code": 178
  },
  {
    "Country": "Aruba",
    "Code": 179
  },
  {
    "Country": "Montserrat",
    "Code": 180
  },
  {
    "Country": "Anguilla",
    "Code": 181
  },
  {
    "Country": "North macedonia",
    "Code": 183
  },
  {
    "Country": "Seychelles",
    "Code": 184
  },
  {
    "Country": "New caledonia",
    "Code": 185
  },
  {
    "Country": "Capeverde",
    "Code": 186
  },
  {
    "Country": "Fiji",
    "Code": 189
  },
  {
    "Country": "Singapor",
    "Code": 196
  }
]

def log(message, color, task):
    now = datetime.now()
    now = now.strftime("  [%b %d @ %H:%M:%S.%f")[:-3]+("] ")
    print(color + f"{now}TASK {str(task)}: {message}" + Fore.WHITE)
  
def getinfo(row,column):
    with open(r'Settings\Personal Settings.csv', 'r') as file:
        rows = file.readlines() #returns a list of strings
    value = rows[row].split(",")[column].replace("\n", "")
    return value
  
def getphone(country,smsKEY,service):
    for i in range(len(pre2code)):
        if pre2code[i]["iso"] == country:
            countryname = pre2code[i]["country"]
            prefix = pre2code[i]["code"]
            break
    def countrytocode(country):
        for i in range(len(regtocode)):
            if regtocode[i]["Country"] == country:
                code = regtocode[i]["Code"]
                break
        return code
    try:
        smsActivateCode = countrytocode(countryname)
    except:
        print("INCORRECT SMS COUNTRY")
    response = requests.get(f"https://sms-activate.org/stubs/handler_api.php?api_key={smsKEY}&action=getNumber&service={service}&ref=1996036&country={smsActivateCode}")
    if 'ACCESS_NUMBER' in response.text:
        sms_number = (str(response.text).split(':')[2][len(prefix):])
        sms_id = str((response.text).split(':')[1])
        return sms_number, sms_id
    elif 'NO_BALANCE' in response.text:
                print(Fore.RED + 'FAILED, Please add a balance to SMS-Activate!' + Fore.WHITE)
    elif 'NO_NUMBERS' in response.text:
        print(Fore.RED + 'FAILED, There are no numbers for the country you requested, pleaseselect another region!' + Fore.WHITE)
    elif 'STATUS_CANCEL' in response.text:
        print(Fore.RED + 'FAILED, Error getting code, restarting!' + Fore.WHITE)
        #restart from here(call function again from 0)
    else:
        print('failed',response.text)

def getselectvalue(country):
    for i in range(len(pre2code)):
        if pre2code[i]["iso"] == country:
            countryname = pre2code[i]["country"]
            prefix = pre2code[i]["code"]
            break
    return prefix + "_" + country

def getCode(timeout_tries, sms_activate, sms_id):
    for _ in range(int(timeout_tries)):
        response = requests.get(f"https://api.sms-activate.org/stubs/handler_api.php?api_key={sms_activate}&action=getStatus&id={sms_id}")
        if 'STATUS_WAIT_CODE' in response.text:
            time.sleep(5)
            gotcode = False
        elif 'STATUS_OK' in response.text:
            get_code = response.text
            received_code = get_code.split(':')[1]
            gotcode = True
            break

        elif 'STATUS_CANCEL' in response.text:
            print('failed','Error getting code, closing!')
            gotcode = False
            break
          
        elif 'BAD_STATUS' in response.text:
            print('failed','Error getting code (BAD_STATUS), closing!')
            gotcode = False
            break
        else:
            print(response.text)
            gotcode = False
            break
    if gotcode == True:
        return received_code
    else:
        return gotcode

def prefix2code(prefix):
    for i in range(len(pre2code)):
        if pre2code[i]["code"] == prefix:
            region = pre2code[i]["iso"]
            return region
    


def short2country(short):
    for i in range(len(pre2code)):
        if pre2code[i]["iso"] == short:
            country = pre2code[i]["country"]
            return country

def two2three(short):
    for i in range(len(twoandthreelet)):
        if twoandthreelet[i]["let2"] == short:
            country = twoandthreelet[i]["let3"]
            return country


def region2country(region):
  for i in range(len(pre2code)):
      if pre2code[i]["iso"] == region:
          country = pre2code[i]["country"]
          return country




