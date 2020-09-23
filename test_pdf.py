import requests


class TestPdf:
    def test_pdf_down(self):
        url = "https://pdf.ceshiren.com/lg3/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95%E5%AE%9E%E6%88%981/assets/30D7A139-5813-489B-AF20-836D3063E9CF/assets/30D7A139-5813-489B-AF20-836D3063E9CF.pdf"
        url = "https://hellorfimg.zcool.cn/preview260/1142161535.jpg"
        r = requests.get(url=url, stream=True)
        with open("python_logo.jpg", 'wb') as f:
            f.write(r.content)
        print(r.text)