# Databáze příkladů z matematiky

## Spusteni backendu

>cd website
>
>py manage.py runserver

## Spusteni frontendu

>cd frontend
>
>npm run dev

## Přihlašovací údaje

>name: admin
>
>password: admin

## Podporované funkce

| Název             | Zápis         | | LaTex     | | Python           | Mathquill|
| -----------       | -----------   |-| -------   |-| -------          | -------- |
| absolutní hodnota | $\|\|$        |O| \left\right|0| abs(e)          | \|       |
| zlomky            | $\frac{e}{e}$ |O| frac{e}{e}|χ| e/e              | /        |
| scitani           | $e+e$         |O| e+e       |χ| e+e              | +        |
| odcitani          | $e-e$         |O| e-e       |χ| e-e              | -        |
| nasobeni          | $e\cdot e$    |O| e\cdot e  |χ| e*e              | *        |
| deleni            | $e\div e$     |χ| e\div e   |χ| e/e              | \div     |
| faktorial         | $e!$          |χ| e!        |χ| math.factorial(e)| !        |
| kulaté závorky    | $()$          |χ| ()        |χ| ()               | (        |
| hranaté závorky   | $$            |χ| []        |χ| ()               | [        |
| složené závorky   | $\{\}$        |χ| \{\}      |χ| ()               | {        |
| odmocniny         | $$            |χ| \sqrt     |χ| math.sqrt()      | \sqrt    |
| mocniny           | $2^{3}$       |χ| ^{}       |χ| math.pow()       | ^        |
| konstanta pí      | $\pi$         |χ| \pi       |χ| math.pi          | \pi      |
| konstanta e       | $e$           |χ| e         |χ| math.e           | nepodpo  |
| logaritmy         | $$            |χ|           |χ| math.log         | \log,\ln |
| sinus             | $\sin$        |χ| \sin      |χ| math.sin()       | \sin     |
| cosinus           | $\cos$        |χ| \cos      |χ| math.cos()       | \cos     |
| tangens           | $\tan$        |χ| \tan      |χ| math.tan()       | \tan     |


## Technologie

<img src="./img/django.png" alt="django"></img>
<img src="./img/chart.jpg" alt="chart.js" style="max-height:132px;"></img>
<img src="./img/mathquill.jpg" alt="mathquill" style="max-height:132px;"></img>
<img src="./img/math_jax.svg" alt="math_jax" style="max-height:120px;"></img>

### Mathjax
https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference

https://pic.plover.com/MISC/symbols.pdf