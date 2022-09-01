import ddddocr
import requests

from common.log import MyLog

logger = MyLog.get_log().logger
class GlobalCookies:
    global cookies

    def get_image_code(self):

        url = "http://192.168.9.221:8086/getCaptcha"
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        response= requests.get(url, headers).content

        #存入返回的图片
        with open('./test.jpg', 'wb') as fp:
            fp.write(response)

        #识别图片中的验证码
        ocr = ddddocr.DdddOcr()
        with open('./test.jpg', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        return res

        """text = pytesseract.image_to_string(Image.open('./test.jpg'))
                print(text)
                return text"""

    def save_cookies(self):
        """登录123接口"""
        captcha = self.get_image_code()#获取验证码
        url = "http://192.168.9.221:8086/login"
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        data = {"username":"chengy3","password":"1","captcha":captcha}
        print(data)
        response = requests.post(url,data,headers,allow_redirects=False)
        # 将获取的cookie转化为字典
        cookies = requests.utils.dict_from_cookiejar(response.cookies)
        print(cookies)
        return cookies


"""if __name__ == '__main__':
    globalCookies = GlobalCookies()
    globalCookies.save_cookies()"""
