import requests
from seleniumwire import webdriver
import time
from selenium.webdriver.common.by import By
from colorama import init, Fore, Back, Style
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import pickle
from selenium.webdriver.chrome.options import Options
from discord import SyncWebhook, file, colour, Embed, embeds
import json
import os
from convertcookies import seltoreqcookie
from validate import validate
from webhooks import icloudpersonal

def clear():
    os.system('cls')

init(convert=True)


def icloud():
    #launch chrome
    def session():
        options = Options()
        options.headless = False
        options.add_argument('log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        print("Opening browser to log in")
        browser.get("https://www.icloud.com/")
        enter = input("Press enter when you have logged in and the page has loaded")
        cookies = browser.get_cookies()
        cookies2 = seltoreqcookie(cookies)
        print("session saved succesfully")
        return cookies2

    def genmail(cookies):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'text/plain',
            # 'Cookie': 'X_APPLE_WEB_KB-TY8LWQ0YFC6FSBUCAH3_BUWD33G="v=1:t=FA==BST_IAAAAAAABLwIAAAAAGObWFQRDmdzLmljbG91ZC5hdXRovQAA6p0WcICbjI7ZamXucoR3sYHPf-tX5qbVP5k0o_gVwknhWx7mUYagAA7JDS5vdzieRrkmpoOWwDxJBwNwZgrx2_49DjvojqUAw2UDT1B8KzdFzCCBCfZ2STc0_t2A-tCZLqCx54-AscJdl2GIy_LbCHEnlA~~"; X-APPLE-WEBAUTH-HSA-TRUST="dc6304d5964bdb7d583f095ce5c60dbcb77948a6230b29eab483f29978c426ef_HSARMTKNSRVXWFlazqmlJsf+HyS295T8fhb6VgU3oxcZNAGISHEVTySXSBYJM077eQ3WZpacnFtA6fQBw4xteWnkSRjnIv20PREI92wGJKo/EtX/joQfTjzxD1YYSXvxdxOTYilujvkecC0Gq4OQya6pbXLSsNMomM3wM2zIvsl3FB0OJ10VcS29qfjiLQ==SRVX:b49d329bfc34b45781ec06e2d49d018bf31340a8312e9fb6237345e1a42d0959_HSARMTKNSRVXWFlagS7JcwaJwXJ6buQSAUMH2YeqHwwhOch/UjFdqFLLiW3jdawtfAlm5Ps0mLwlg/U0OS4xgMRO6gIfWeNmwtNpInP4FlH6n6rtbr1Z9BIvHPwAf7qVaPbWnmG5jU2w/VIFhXmg6qTqAsKFKnu7mGUKLNHo0LnLbn0Gc6ruVv0W+738cNZJ9fHjTjGJw1vPAWP56XCMo3jimRiDQN2ElkHO1y6A4A==SRVX"; X-APPLE-WEBAUTH-PCS-Documents="TGlzdEFwcGw6MTpBcHBsOjE6Aar11pnWzNVxBLQRuZpB7obqEq8uPLe9a/qsBQreIKfi708QyOk6l718IEmTlv2Q/OpxyWpfw6D1fK9WOAeDqTm4675Mms117Gl2iK4aex1hgdGC1LtI836t5hOQanxFc+sAf28hgdeIt73ByEWuA42w3wcEV0QdlljUCWpDuOZxHM4sMGSlHg=="; X-APPLE-WEBAUTH-PCS-Photos="TGlzdEFwcGw6MTpBcHBsOjE6AZ3qAxx6oFLfx7K8+nM8LNqaTmGjRqNMQQd71Kie8nNSAV5eLEvjx4bvFa1jWkqA+L85r9OlDr1iBB2GSsI76cQSeilmc/mWaaRPMU5k5oHkmvbL3tF43Eu8PmcwTakDBZjmifUbFGbcEnIu/rpCFwK34JoIS0tkR4o4ryS5+13Q9W1p4+8iZg=="; X-APPLE-WEBAUTH-PCS-Cloudkit="TGlzdEFwcGw6MTpBcHBsOjE6ATOag6c4wt0d1zXR4MAWoNPTQRSxZM7y95hXZ30gv6zzza7j8rlGWsKjfCG4oR+8Z2jNIpA9yR0Ijerk90GkRA4asm+YZzCETwbMzG73bOJq2tLUpqoBvIrO4MKLruxMwR76v9L3IW6CMZx+5GARN3Qn3JETfgH9k6eh9L3DK7PGl7cCBkWoxQ=="; X-APPLE-WEBAUTH-PCS-Safari="TGlzdEFwcGw6MTpBcHBsOjE6AaK+XdI7q5XmnkYNy+Qrc8Vj4Ct0G6/j24IBngufjDGfWZ5KYRyftSppVMlxSEPkDwlpFFSar0IWj4yrXjlyA2ycSEzUwz7AE31LvjU8c7Lw4hUUItrwBiutwUi9s5lU/s/qWyhbjuxqimE7GPfRp6AVvwr+OUywtG1VAjznPSCz88qI9UjcIw=="; X-APPLE-WEBAUTH-PCS-Mail="TGlzdEFwcGw6MTpBcHBsOjE6ASqpntvPzaBlmsrwS2vf2qHuYpxeL6Co9NnCNbBdl6HW+AvbyUlUPCY5KvJY6+3Z7uCYImB/dSbfRWSEnppUkqz3Q2aIPKFxddAcOk2Oe4EIfc16qPhDlh9u9zjWbzdygkHjyM0rS9rGf64HWUmUC3yylhZ7bVZqvATZWxEgpc74wNm8l1zF6g=="; X-APPLE-WEBAUTH-PCS-Notes="TGlzdEFwcGw6MTpBcHBsOjE6AQMCVHSmfZY4YdCcZFDzfQ3y3BE9CaIlOE41K4roqZqsNkyP+5Um8TwqQEhEuc8F14EciBZKTciJC9TOYE0ZJdQudw70sUB9hq1oeDkX719qmp8CEYZnnGOgw4Q4l3f9Upq7EClCN8vq3W3IdCzqWtK1trLAkPBRd+ASY4rn4/KLJ/8HiaK45w=="; X-APPLE-WEBAUTH-PCS-News="TGlzdEFwcGw6MTpBcHBsOjE6ATFVfTsjwKa6yD58MmX8IP/XprCOAk8Q8tbgdp6KxEPjKtmG8RZMkuHleDtgrbSqLJluuyDitQrd1J3glCw5mhd+kZOrni0ipwFmgXCX8LrTiMJgIKul+vRcEbYHx5MEnushXIS8Qmj2OFjC4uI86EorNrYSxDgXmI9jHVJ2Kf4SnLvE2yW73g=="; X-APPLE-WEBAUTH-PCS-Sharing="TGlzdEFwcGw6MTpBcHBsOjE6ATenXHzLsb+eckCx8WmWFzwqi8tAUVxqGZp0Wi4HeTCt1JdOmzNY/aceOih6x59o4k4bJEXIhzrPp7ibYALybiXKBqSP1d80axihH/hio8MhRXeVq4qvm5CyByHnj1mKHXugZdicruzMi7njcamRN2FEyj5S0SRt2z6REaevycibhWKT/GPzKQ=="; X-APPLE-UNIQUE-CLIENT-ID="Fg=="; X-APPLE-WEBAUTH-LOGIN="v=1:t=Fg==BST_IAAAAAAABLwIAAAAAGOcQeYRDmdzLmljbG91ZC5hdXRovQCicixqybI4DtOtdloGvqRC2MJC923zApS7MlxVgFp7Vhg4KXK-nMIdjnSkmezQrJqCijU9gvlzhceazmAGR-feTK6wvyDXh4O-XCjttcSY-nCH1NIMElvpDg6jpWQmvrJJhajyIV99wUMI3IeAGLAEOQuaZA~~"; X-APPLE-WEBAUTH-VALIDATE="v=1:t=Fg==BST_IAAAAAAABLwIAAAAAGOcQeYRDmdzLmljbG91ZC5hdXRovQCicixqybI4DtOtdloGvqRC2MJC923zApS7MlxVgFp7Vhg4KXK-nMIdjnSkmezQrJqCijU9gvlzhceazmAGR-feTK6wvyDXh4O-XCjttcSY-oJPgDoaWJq9ZlZSE02mKh76YkM8A6kKjkwVBOElsTAde-PJqg~~"; X-APPLE-WEBAUTH-USER="v=1:s=0:d=25044865433"; X-APPLE-DS-WEB-SESSION-TOKEN="AQFmwX7oZ7Aidn6FClZRXIh2QiL+y6qc9VNBAdALmX6bkCARMI2Mw0+HDyFqFSRqGKDSkiFKjix802A2X3oYiRjW/PjlgO8hcfZ1zmpIN59YEhWiygUCsAeFDQVbnZKXI60CDm8Nkg8OOMTcRtDSpQe6btHBGA6oXXVJx5+GSwWOiZo9a+XsLJ/xpXPMPd4c3EQrEoeoHxGBv/M6tgCo9VwRwm3ZLi0PJA/KKPmgvHRNZeS3M/KHkazDb8eu/VfBznaURmYct8r7bsBoxtoqesHKsjD0ypEzalg4EFbBJV33sUMY1KsnBPR6hXQWUte6vNijA4bGvLOH7x6yiN+mrGqJb/8rr80BFAK78WK3PoWdenVoFAPYpVL5vlo+XdwvPaj2/YqU29mMLKkhAU0s/IcYvmGfAtR2+BcbF4EWZiktSloI1agkO9k2xhCyHnnTBsyJl55ntZLuS02KABYkcyKqcNhsU9hNjZFrlMreqMffmD8/Ejd+OMeg4y+17RL56XT3PPuVrJVUI7v8eMXFJpqRzo31jij9mJImD9Ljs5lkflOL6ACTCTdJq3UmfNg/GfDkHrJwcSuWtPobfa9/YhSwUohRENGPxNQOlTK0EtY2FlKa+34cOxVxaVtagUvuM+mEiKFs6Cdv8wmNSdtF3Jl0pqDd3N8sgMqjkV2cLEibdX9ZpaDDEPcD7B2MOlm+A4ARH/dnx/Gp+36JD/M1XFCRrCkedfum3cDBiHC50gKO4snuiReZLTyCABCb9FVHS0o="; X-APPLE-WEB-ID=A3D87AF667FA7ADB23B67C84E9159274749A394D; X-APPLE-WEBAUTH-TOKEN="v=2:t=Fg==BST_IAAAAAAABLwIAAAAAGOcQfMRDmdzLmljbG91ZC5hdXRovQCVQJb8HxR4bwkcUnsb893XTPj2SbYCAH9SIt_NCh47wDGBLVtbVC8MJ-B-Ner4dB7Ycadr_KprmsqSBbsSCnaX6D1nEXqfS6O-BtJvprDNzKYo6YRxHnkDyaKUnkF0Rp5TYAEmjK2BTeOrDGUYVP-OLPjKWw~~"',
            'Origin': 'https://www.icloud.com',
            'Referer': 'https://www.icloud.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'clientBuildNumber': '2304Project37',
            'clientMasteringNumber': '2304B26',
            'clientId': '7086153e-3718-49a5-89b5-438d426df2d0',
            'dsid': "25045865433",
        }

        data = '{"langCode":"en-us"}'

        response = requests.post(
            'https://p53-maildomainws.icloud.com/v1/hme/generate',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).json()

        try:
            print(Fore.RED + "Error: " + response["error"]["errorMessage"] + Fore.WHITE)
            return False
        except:
            mail = response["result"]["hme"]
            print(mail)

        #segunda request
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'text/plain',
            # 'Cookie': 'X_APPLE_WEB_KB-TY8LWQ0YFC6FSBUCAH3_BUWD33G="v=1:t=FA==BST_IAAAAAAABLwIAAAAAGObWFQRDmdzLmljbG91ZC5hdXRovQAA6p0WcICbjI7ZamXucoR3sYHPf-tX5qbVP5k0o_gVwknhWx7mUYagAA7JDS5vdzieRrkmpoOWwDxJBwNwZgrx2_49DjvojqUAw2UDT1B8KzdFzCCBCfZ2STc0_t2A-tCZLqCx54-AscJdl2GIy_LbCHEnlA~~"; X-APPLE-WEBAUTH-HSA-TRUST="dc6304d5964bdb7d583f095ce5c60dbcb77948a6230b29eab483f29978c426ef_HSARMTKNSRVXWFlazqmlJsf+HyS295T8fhb6VgU3oxcZNAGISHEVTySXSBYJM077eQ3WZpacnFtA6fQBw4xteWnkSRjnIv20PREI92wGJKo/EtX/joQfTjzxD1YYSXvxdxOTYilujvkecC0Gq4OQya6pbXLSsNMomM3wM2zIvsl3FB0OJ10VcS29qfjiLQ==SRVX:b49d329bfc34b45781ec06e2d49d018bf31340a8312e9fb6237345e1a42d0959_HSARMTKNSRVXWFlagS7JcwaJwXJ6buQSAUMH2YeqHwwhOch/UjFdqFLLiW3jdawtfAlm5Ps0mLwlg/U0OS4xgMRO6gIfWeNmwtNpInP4FlH6n6rtbr1Z9BIvHPwAf7qVaPbWnmG5jU2w/VIFhXmg6qTqAsKFKnu7mGUKLNHo0LnLbn0Gc6ruVv0W+738cNZJ9fHjTjGJw1vPAWP56XCMo3jimRiDQN2ElkHO1y6A4A==SRVX"; X-APPLE-WEBAUTH-PCS-Documents="TGlzdEFwcGw6MTpBcHBsOjE6Aar11pnWzNVxBLQRuZpB7obqEq8uPLe9a/qsBQreIKfi708QyOk6l718IEmTlv2Q/OpxyWpfw6D1fK9WOAeDqTm4675Mms117Gl2iK4aex1hgdGC1LtI836t5hOQanxFc+sAf28hgdeIt73ByEWuA42w3wcEV0QdlljUCWpDuOZxHM4sMGSlHg=="; X-APPLE-WEBAUTH-PCS-Photos="TGlzdEFwcGw6MTpBcHBsOjE6AZ3qAxx6oFLfx7K8+nM8LNqaTmGjRqNMQQd71Kie8nNSAV5eLEvjx4bvFa1jWkqA+L85r9OlDr1iBB2GSsI76cQSeilmc/mWaaRPMU5k5oHkmvbL3tF43Eu8PmcwTakDBZjmifUbFGbcEnIu/rpCFwK34JoIS0tkR4o4ryS5+13Q9W1p4+8iZg=="; X-APPLE-WEBAUTH-PCS-Cloudkit="TGlzdEFwcGw6MTpBcHBsOjE6ATOag6c4wt0d1zXR4MAWoNPTQRSxZM7y95hXZ30gv6zzza7j8rlGWsKjfCG4oR+8Z2jNIpA9yR0Ijerk90GkRA4asm+YZzCETwbMzG73bOJq2tLUpqoBvIrO4MKLruxMwR76v9L3IW6CMZx+5GARN3Qn3JETfgH9k6eh9L3DK7PGl7cCBkWoxQ=="; X-APPLE-WEBAUTH-PCS-Safari="TGlzdEFwcGw6MTpBcHBsOjE6AaK+XdI7q5XmnkYNy+Qrc8Vj4Ct0G6/j24IBngufjDGfWZ5KYRyftSppVMlxSEPkDwlpFFSar0IWj4yrXjlyA2ycSEzUwz7AE31LvjU8c7Lw4hUUItrwBiutwUi9s5lU/s/qWyhbjuxqimE7GPfRp6AVvwr+OUywtG1VAjznPSCz88qI9UjcIw=="; X-APPLE-WEBAUTH-PCS-Mail="TGlzdEFwcGw6MTpBcHBsOjE6ASqpntvPzaBlmsrwS2vf2qHuYpxeL6Co9NnCNbBdl6HW+AvbyUlUPCY5KvJY6+3Z7uCYImB/dSbfRWSEnppUkqz3Q2aIPKFxddAcOk2Oe4EIfc16qPhDlh9u9zjWbzdygkHjyM0rS9rGf64HWUmUC3yylhZ7bVZqvATZWxEgpc74wNm8l1zF6g=="; X-APPLE-WEBAUTH-PCS-Notes="TGlzdEFwcGw6MTpBcHBsOjE6AQMCVHSmfZY4YdCcZFDzfQ3y3BE9CaIlOE41K4roqZqsNkyP+5Um8TwqQEhEuc8F14EciBZKTciJC9TOYE0ZJdQudw70sUB9hq1oeDkX719qmp8CEYZnnGOgw4Q4l3f9Upq7EClCN8vq3W3IdCzqWtK1trLAkPBRd+ASY4rn4/KLJ/8HiaK45w=="; X-APPLE-WEBAUTH-PCS-News="TGlzdEFwcGw6MTpBcHBsOjE6ATFVfTsjwKa6yD58MmX8IP/XprCOAk8Q8tbgdp6KxEPjKtmG8RZMkuHleDtgrbSqLJluuyDitQrd1J3glCw5mhd+kZOrni0ipwFmgXCX8LrTiMJgIKul+vRcEbYHx5MEnushXIS8Qmj2OFjC4uI86EorNrYSxDgXmI9jHVJ2Kf4SnLvE2yW73g=="; X-APPLE-WEBAUTH-PCS-Sharing="TGlzdEFwcGw6MTpBcHBsOjE6ATenXHzLsb+eckCx8WmWFzwqi8tAUVxqGZp0Wi4HeTCt1JdOmzNY/aceOih6x59o4k4bJEXIhzrPp7ibYALybiXKBqSP1d80axihH/hio8MhRXeVq4qvm5CyByHnj1mKHXugZdicruzMi7njcamRN2FEyj5S0SRt2z6REaevycibhWKT/GPzKQ=="; X-APPLE-UNIQUE-CLIENT-ID="Fg=="; X-APPLE-WEBAUTH-LOGIN="v=1:t=Fg==BST_IAAAAAAABLwIAAAAAGOcQeYRDmdzLmljbG91ZC5hdXRovQCicixqybI4DtOtdloGvqRC2MJC923zApS7MlxVgFp7Vhg4KXK-nMIdjnSkmezQrJqCijU9gvlzhceazmAGR-feTK6wvyDXh4O-XCjttcSY-nCH1NIMElvpDg6jpWQmvrJJhajyIV99wUMI3IeAGLAEOQuaZA~~"; X-APPLE-WEBAUTH-VALIDATE="v=1:t=Fg==BST_IAAAAAAABLwIAAAAAGOcQeYRDmdzLmljbG91ZC5hdXRovQCicixqybI4DtOtdloGvqRC2MJC923zApS7MlxVgFp7Vhg4KXK-nMIdjnSkmezQrJqCijU9gvlzhceazmAGR-feTK6wvyDXh4O-XCjttcSY-oJPgDoaWJq9ZlZSE02mKh76YkM8A6kKjkwVBOElsTAde-PJqg~~"; X-APPLE-WEBAUTH-USER="v=1:s=0:d=25044865433"; X-APPLE-DS-WEB-SESSION-TOKEN="AQFmwX7oZ7Aidn6FClZRXIh2QiL+y6qc9VNBAdALmX6bkCARMI2Mw0+HDyFqFSRqGKDSkiFKjix802A2X3oYiRjW/PjlgO8hcfZ1zmpIN59YEhWiygUCsAeFDQVbnZKXI60CDm8Nkg8OOMTcRtDSpQe6btHBGA6oXXVJx5+GSwWOiZo9a+XsLJ/xpXPMPd4c3EQrEoeoHxGBv/M6tgCo9VwRwm3ZLi0PJA/KKPmgvHRNZeS3M/KHkazDb8eu/VfBznaURmYct8r7bsBoxtoqesHKsjD0ypEzalg4EFbBJV33sUMY1KsnBPR6hXQWUte6vNijA4bGvLOH7x6yiN+mrGqJb/8rr80BFAK78WK3PoWdenVoFAPYpVL5vlo+XdwvPaj2/YqU29mMLKkhAU0s/IcYvmGfAtR2+BcbF4EWZiktSloI1agkO9k2xhCyHnnTBsyJl55ntZLuS02KABYkcyKqcNhsU9hNjZFrlMreqMffmD8/Ejd+OMeg4y+17RL56XT3PPuVrJVUI7v8eMXFJpqRzo31jij9mJImD9Ljs5lkflOL6ACTCTdJq3UmfNg/GfDkHrJwcSuWtPobfa9/YhSwUohRENGPxNQOlTK0EtY2FlKa+34cOxVxaVtagUvuM+mEiKFs6Cdv8wmNSdtF3Jl0pqDd3N8sgMqjkV2cLEibdX9ZpaDDEPcD7B2MOlm+A4ARH/dnx/Gp+36JD/M1XFCRrCkedfum3cDBiHC50gKO4snuiReZLTyCABCb9FVHS0o="; X-APPLE-WEB-ID=A3D87AF667FA7ADB23B67C84E9159274749A394D; X-APPLE-WEBAUTH-TOKEN="v=2:t=Fg==BST_IAAAAAAABLwIAAAAAGOcRD0RDmdzLmljbG91ZC5hdXRovQDTAqxgnYPNjGmkehdgclRtxgF-85qie0NJtmHikoVZkxsrI8yLzSKR338HcjRfZ3ZAOTpxxsnzXMd71Z86XXWmJUHJBeigGl4rMKjvX1gD1dR7v8gXh5G3jv_1dRqyiDYrBR-pQiMGQhvLGGCl6xQ9ie3euQ~~"',
            'Origin': 'https://www.icloud.com',
            'Referer': 'https://www.icloud.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'clientBuildNumber': '2304Project37',
            'clientMasteringNumber': '2304B26',
            'clientId': '7086153e-3718-49a5-89b5-438d426df2d0',
            'dsid': "25045865433",
        }

        data = '{"hme":"'+ mail + '","label":"TREX","note":"Email generated by TREX toolbox"}'

        response = requests.post(
            'https://p53-maildomainws.icloud.com/v1/hme/reserve',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).json()

        if bool(response["success"]) == True:
            print(Fore.GREEN + "iCloud mail generated succesfully")
            print(Fore.CYAN + "Adding to CSV")
            print(Fore.MAGENTA + "iCloud mail saved succesfully")
            f = open(r'Accounts\Account Generators\iCloud\GeneratediCloud.csv','a')
            f.write("\n" + mail)
            f.close()
            print(Fore.WHITE)
            icloudpersonal(mail)
        else:
            print(Fore.RED + "Unknown Error!")

    print("Welcome to the iCloud Module")
    spaces = ""
    print()
    print(spaces + "1. iCloud Mail Generator")
    print(spaces + "2. iCloud Mail Exporter(coming soon)")
    print()             
    module = input("select an option(1-2)")
    if module == "1":
        if validate() == True:
            clear()
            num = int(input("How many mails do you want to generate:"))
            cookies = session()
            for i in range(num):
                if genmail(cookies) == False:
                    break
                else:
                    time.sleep(185)
