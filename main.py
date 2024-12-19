import flet as ft
import requests
import json
import random

words = ['спасибо', "отправлено", "теперь я знаю", "ооо, я это прочту!", "надеюсь ты не писал туда плохие слова", "ваше мнение очень важно для нас"]

def post_webhookah(text):
    url ="https://discord.com/api/webhooks/1319254035202838529/M1Se4W5aEESgQY9ULg0FiPtxcO_vzSvaMr5OHyRutJOAtdvJyEHVGa1vFzMih3L8D6qt"
    ## Text only:
    data = {
        "content" : text
        }

    result = requests.post(url, json=data)
    return result


def example():
    def button_clicked(e):
        posted = post_webhookah(tb4.value)
        if posted.status_code == 204:
            t.value = random.choice(words)
        else:
            t.vavlue = f"{posted}"
        t.update()

    t = ft.Text()
    tb4 = ft.TextField(label="пиши!", hint_text="Анонимно отправить какащке")
    b = ft.ElevatedButton(text="Отправить", on_click=button_clicked)

    return ft.Column(controls=[tb4, b, t])

def main(pagfe: ft.Page):
    pagfe.add(example())

ft.app(main)
