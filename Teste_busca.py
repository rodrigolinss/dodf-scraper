import requests
from bs4 import BeautifulSoup

url = "https://www.dodf.df.gov.br/dodf/jornal/diario"
res = requests.get(url)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    link_element = soup.find("div", class_="jornais-das-internas")
    if link_element:
        pdf_link_tag = link_element.find("a", href=True)
        if pdf_link_tag and "INTEGRA.pdf" in pdf_link_tag.text:
            pdf_url = "https://www.dodf.df.gov.br" + pdf_link_tag["href"]
            print("Link do PDF encontrado:", pdf_url)
        else:
            print("PDF não encontrado.")
    else:
        print("Div não encontrada.")
else:
    print("Erro ao acessar a página:", res.status_code)
