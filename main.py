import requests
from bs4 import BeautifulSoup
import csv
import os
import time

class Scraper():
    
    def configure(self,url, wait_time, start_page, end_page, records_per_page):
        self.url = url
        self.wait_time= wait_time
        self.start_page = start_page
        self.end_page = end_page
        self.records_per_page = records_per_page

    def start_requests(self,output_file):
        for page_no in range(self.start_page, self.end_page):
            page_number_formatting= "c0:KV|2;[];CT|2;{};CR|18;{\"ctrlWidth\":2700};GB|20;12|PAGERONCLICK3|PN"+ str(page_no) +";"

            headers = {
                "accept": "text/html, */*; q=0.01",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                    "origin": "https://gats.pjm-eis.com",
                "priority": "u=1, i",
                "referer": "https://gats.pjm-eis.com/gats2/PublicReports/RenewableGeneratorsRegisteredinGATS",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
            }

            cookies = {
                "ASP.NET_SessionId": "244g4ctn0fprk4c3nzox3ewe",
                "SessionStart": "7/28/2025 9:27:08 AM",
                "LastController": "RenewableGeneratorsRegisteredInGATS/GridViewPartial",
                "LastControllerTime": "7/28/2025 9:50:29 AM"
            }
            data = {
                "DXCallbackName": "GridView",
                "__DXCallbackArgument": page_number_formatting,
                # "GridView":"{&quot;resizingState&quot;:&quot;{\&quot;ctrlWidth\&quot;:2700}&quot;,&quot;keys&quot;:[],&quot;callbackState&quot;:&quot;LZORV9h4JSP1YlaDTVcDKqTrRmL0u3UIKEYOlg2SFu/rTNzA9riHpJdjf4O7W3klkA7wTH+8zQxiN/HsRRqEfAM4w/sCo9rPAHBtJ5V6fmCxj0EJ8Am3GM8dz0RXWVD3qUhevSvCfgI7xuVxzNFCL3UIpMRatuv7Nt8VRTMqADSGWJnXVVw8ibtwQrdq7TGInTum+jJ5I/D//3h8soEn0ilC1/hSqeR/5M2wAyRV5aXndYCfpgVKU+UNDBkY2PrUcHiokbmp4L26KckSzRZu2QWAcY4cX1upTyVuKc4aHzdvzwm0Gr9NnL4nnoqZec3g6geRlLrio+f7XDXAbGX5IHQLA3Uv6DIQmJwnJJL2aZd0+RazkTAIsXIZcs9LVKXgUVBgAj3wYSvSz9nVg4+EXQWOkEYUhWkoeWblebji2N8obKngsbrOuvh7dOMEya6E0qRNEa1vT79p3Nw6vk5PJwZ4hgRydjvcdOokMU/U1D7gYYbaDgO9rdMvSxK2Bb5IjF42AF0h160uNhVbIS8e/xox3CougVzTcdTjWz8WHiozP1oi+z9R1fzF4jdRAZkC5W17DfT99W3oUhsqwyy9mbp35ArWeaxa2MMG1CPcbav/FUzD4cdnoG6xgGicema48OPoMWdJYZGZRnr/Dz3cFPFPRcFixshxTqz6mDDfeM7NZ+ma72BgfXSDlC+R5IsY79o3hKJrf9RngxVAYfz0WHaQduQfqy85Pv1ooEcxK/P0P1kpBbS3XqRI9DnhMKtMvmzlgvijuSHE9NgxMei0g0Z0a/5wy19TVUSNfqhF8VK8XFFBAhVoAnh8mQDZ19zqgFvspLjHS30+2clNhxq67/i57R4Gc/bybxyCuHzbCmsmYPp0ITY+ZkNCpnx2r/ytFqZSJHzinD6nQAPSI1vk/0lG2zsqXEF2v0xDMJ1y1X0i6TSnibCIi5+8zOByu2foxDYaDOi70cQKhABtEGJisdIftP5V4Ag7oN6dUhpuEpirTJpWCA7Rpbzp+IuPClGqj2Ivqfz/P/8cgpeArf9s2o3B/u4QFhwnxXJDQudQijB6x4IjeLiS01LLVG/H2poC56zGRyDQzSkP8UJEfqgLGWA42FFmXGWdGLq0u8NyWz1Wy1L/nmhHgcse/6Szjwfq1JMwF/Ik3r8KjxCK/nmrWpYkk87DgNZOQt8gL3GX/mOEnCs0OBcfdPeGdPZ8uVIWNLSgXcxPiI+bMg26kYJQrNCD5qWANFAYtZk/XMXgEOXLiIiU2k98UJOq+08C8qt6+xX0SbypC0ORZTvRh2o78/jTa3KId10tAwg5xxol/jRD86lsEtjotkFfu0fYHnHkp6QxAg==&quot;,&quot;groupLevelState&quot;:{},&quot;selection&quot;:&quot;&quot;,&quot;toolbar&quot;:&quot;{}&quot;,&quot;contextMenu&quot;:null}",
                 "GridView":"{&quot;resizingState&quot;:&quot;{\&quot;ctrlWidth\&quot;:2700}&quot;,&quot;keys&quot;:[],&quot;callbackState&quot;:&quot;qtTjLmNXuodHzJsc+vnRnbrdTax/gPi0mbkK2BYFXkDpptlzEtSt2zxpogsKKwJdT+dghKs0oBKLLpWM3eCMbm+Y6KJmgB+EO2zBU13U4Wr5AOtFozHmlzSptr+s4hi4M0puwyhWZG+TR/7r6TuZ29jXKDXyS+BptLVESwKTxOap+B6mkSMQxXDuK+Dredh6W7uX2m/ppMXQH8eBRjmXPvIOtknhYBZRbAff4vJ5+boKUfQKMTpHXB63Obe6p2Vk3NJJNMAILrd49LVU+ki8vk4wBfgZKmQoaN9gsxbZq9aiRzkq6O/THEZApcOY3DaEn5WHJiK7ZLXsEnY04LTJui3P+7H68HUUnxCkrobqtOlHsHSvXWkfifWCXW4lG5GosyjR2kIzl5DD/LxunRG+9JoABGNcuxS9TR39597T3r3h3IK6NOX9ct/Zrx8OD2W3YO/yLJCUezdnk7rs3v9zi9obG8lzaY7ZXsUNLfn/uKHNCgXWtatsuTR0LrHkj/QVjVgiWjq00E7ormll1fL+bESSXwdW3D4Dy2/I7HrFo5goibF2pM/tTtD4hbpkRkvHRvMucyKZMGqYmi1QawRHVMzlD3IyvjKxBFh75FmD0lIapYsHHpYr9evxLkpbCEagEmqGUf3YpifjqwHaYGj1HSb+z5Clmc9JnPrU+Ce/6+r3oe9YMVrWHiv4K0J/lwx7nuUOBoCLRjo2YYA/xwy9yRcgtw7HEeJonZ/3+uMFFVaNVZWFBs9YYPxym5D1O6TWn+G+LXb5JUEBNvt3uPEf7e6S3infn+Cgr4LqLwk4JKz5Efvcat66N0ZkECSTeGUvzRZlk8rr/I1sIqI9P4vpJPE6e5Aw+2JZ/XS5BlWxv6RL3fJYXJFsKwv5oykFOR/74gS5vT0RWJcm6BT8WK/05EEAknotVE43gQWu/dCis0uZoo8yma1jmyaYP0UGt35b8hqEJpls5PcTW0th7DgdTVVeuWXC//D6giat37A0GuZdGsQO7TBvYLVDQ4qbkg9lwQtuKdX96jtBMAcTOjiFpV5Kvmn4FASqje3bu+GyCo+RXXwttY8aS+jDQluPkPIChKG5HS/tMrAQ2uFUmzE3lHqZB6hT6NZIq65FQ7m3MtUMHQMFBpMaRVPIuVL2T7w1a6mGpCIHvfoG6v2DC8qpqkrhLcg468KenroDPCvV+afdwInigyE21Vz5zT7DugONGkYznRi/vrZcXZRRvqNjcVi4m6vRFfJydm3+HZGneEseKuLM0x8fTRZX1CtZqzTRkV2DT5GmZfB0pJX6+Q85LSdYT2ZQQtZJ4KW3zjH8PnsB7taC&quot;,&quot;groupLevelState&quot;:{},&quot;selection&quot;:&quot;&quot;,&quot;toolbar&quot;:&quot;{}&quot;,&quot;contextMenu&quot;:null}",
   
                "GridView$custwindowState":"{&quot;windowsState&quot;:&quot;0:0:-1:0:0:0:-10000:-10000:1:0:0:0&quot;}",
                "GridView$DXHFP$TPCFCm1$O": "OK",
            "GridView$DXHFP$TPCFCm1$C": "Cancel",
            "GridView$DXFREditorcol0": None,
            "GridView$DXFREditorcol1": None,
            "GridView$DXFREditorcol2": None,
            "GridView$DXFREditorcol3": None,
            "GridView$DXFREditorcol4": None,
            "GridView$DXFREditorcol5": None,
            "GridView$DXFREditorcol6": None,
            "GridView$DXFREditorcol7": None,
            "GridView$DXFREditorcol8": None,
            "GridView$DXFREditorcol9": None,
            "GridView$DXFREditorcol10": None,
            "GridView$DXFREditorcol11": None,
            "GridView$DXFREditorcol12": None,
            "GridView$DXFREditorcol13": None,
            "GridView$DXFREditorcol14": None,
            "GridView$DXFREditorcol15": None,
            "GridView$DXFREditorcol16": None,
            "GridView$DXFREditorcol17": None,
            "GridView$DXFREditorcol18": None,
            "GridView$DXFREditorcol19": None,
            "GridView$DXFREditorcol20": None,
            "GridView$DXFREditorcol21": None,
            "GridView$DXFREditorcol22": None,
            "GridView$DXFREditorcol23": None,
            "GridView$DXFREditorcol24": None,
            "GridView$DXFREditorcol25": None,
            "GridView$DXFREditorcol26": None,
            "DXMVCEditorsValues":'{"GridView_DXFREditorcol0":null,"GridView_DXFREditorcol1":null,"GridView_DXFREditorcol2":null,"GridView_DXFREditorcol3":null,"GridView_DXFREditorcol4":null,"GridView_DXFREditorcol5":null,"GridView_DXFREditorcol6":null,"GridView_DXFREditorcol7":null,"GridView_DXFREditorcol8":null,"GridView_DXFREditorcol9":null,"GridView_DXFREditorcol10":null,"GridView_DXFREditorcol11":null,"GridView_DXFREditorcol12":null,"GridView_DXFREditorcol13":null,"GridView_DXFREditorcol14":null,"GridView_DXFREditorcol15":null,"GridView_DXFREditorcol16":null,"GridView_DXFREditorcol17":null,"GridView_DXFREditorcol18":null,"GridView_DXFREditorcol19":null,"GridView_DXFREditorcol20":null,"GridView_DXFREditorcol21":null,"GridView_DXFREditorcol22":null,"GridView_DXFREditorcol23":null,"GridView_DXFREditorcol24":null,"GridView_DXFREditorcol25":null,"GridView_DXFREditorcol26":null}'
            }


            response = requests.post(self.url, headers=headers, cookies=cookies, data=data)
            with open("smaple2.txt", "w", encoding='utf-8') as w:
                w.writelines(response.text)
            if response.status_code == 200:
                self.parse_data(response.content, page_no, self.records_per_page, output_file)
            time.sleep(self.wait_time)

        
    def parse_data(self,html_content, page_no, total_records_per_page, output_file):
        
        def get_serial_range(page_no, records_per_page=50):
            start_serial = page_no * records_per_page + 1
            end_serial = (page_no + 1) * records_per_page
            return start_serial, end_serial

        soup = BeautifulSoup(html_content, "html.parser")
        headers = []
        for i in range(0, 27): 
            header_td = soup.find("td", id=f"GridView_tcheader{i}")
            headers.append(header_td.get_text(strip=True) if header_td else f"Column{i}")

        with open(output_file, "a", newline='', encoding='utf-8') as file:
            
            writer = csv.writer(file)
            if not os.path.exists(output_file):
                writer.writerow(headers)


        start_serial, end_serial = get_serial_range(page_no, total_records_per_page)
        print(start_serial, end_serial )
        for i in range(start_serial, end_serial):
            target_row = soup.find("tr", id=f"GridView_DXDataRow{i}")

            if target_row:
                td_values = [td.get_text(strip=True) for td in target_row.find_all("td")]

                with open(output_file, "a", newline='', encoding='utf-8') as file:
                    
                    writer = csv.writer(file)
 
                    writer.writerow(td_values)

                print(f"Data extracted and saved to {output_file}")
            else:
                print("Target row not found")

                    
                    
if __name__ == "__main__":
    s = Scraper()
    s.configure("https://gats.pjm-eis.com/GATS2/PublicReports/RenewableGeneratorsRegisteredInGATS/GridViewPartial", 5, 1,2, 200)
    s.start_requests("out2.csv")