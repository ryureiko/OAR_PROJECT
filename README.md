# О ПРОЕКТЕ

Дашборд представляет собой интерактивную визуализацию данных о численности экономически активного населения, уровне безработицы и занятости по регионам России за период 2001-2019 гг.

*Он состоит из 4 страниц:*
>1. Численность экономически активного населения по годам 
>2. Распределение безработных и занятых по возрастным группам по регионам РФ
>3. Численность безработных и занятых по возрастным группам по регионам РФ
>4. Карта уровня безработицы и занятости по регионам России

С помощью Dash и Plotly, пользователи могут исследовать данные, представленные в виде линейной диаграммы, круговых и столбчатых диаграмм, а также фоновой картограммы. Проект позволяет анализировать численность занятых и безработных по различным возрастным группам, что способствует более глубокому пониманию демографических и экономических тенденций в стране.

## Описание датасета

Набор данных предоставляет информацию о численности экономически активного населения, безработных, уровне безработицы и сопоставляет эти показатели между различными возрастными группами по субъектам РФ.

Набор данных включает в себя следующие показатели:

1. Численность экономически активного населения - всего
2. Численность населения занятого в экономике
3. Численность безработных
4. Уровень экономической активности
5. Уровень занятости
6. Уровень безработицы
7. Распределение безработных по возрастным группам по регионам РФ
8. Численность безработных по возрастным группам по регионам РФ
9. Распределение занятых в экономике по возрастным группам по регионам РФ
10. Численность занятых в экономике по возрастным группам по регионам РФ

Данные представлены за период 2001-2019 гг. (с заданной частотой наблюдения по показателям).

Источники данных: Федеральная служба государственной статистики

#### Ссылка на источник: <https://data.rcsi.science/data-catalog/datasets/156/#>

### Понятия, используемые в источнике:

* *Экономически активное население* – лица в возрасте, установленном для измерения экономической активности населения, которые в рассматриваемый период считаются занятыми или безработными (в возрасте 15-72 года).
* *Уровень экономической активности населения* – удельный вес численности экономически активного населения в общей численности населения, рассчитанный в процентах.
* *Уровень занятости* – удельный вес численности занятого населения в общей численности населения, рассчитанный в процентах.
* *Уровень безработицы* – удельный вес численности безработных в численности экономически активного населения, рассчитанный в процентах.

## Установка и запуск

**1. Клонирование репозитория**

```
git clone https://github.com/ryureiko/OAR_PROJECT.git
cd OAR_PROJECT
```

**2. Создание виртуального окружения и установка зависимостей**

```
python -m venv venv
source venv\Scripts\activate
pip install dash pandas
pip install dash-bootstrap-components
```

**3. Запуск приложения**

```python app.py```

**4. Открытие приложения**

Откройте браузер и перейдите по адресу http://127.0.0.1:8050, чтобы увидеть приложение в действии.
 
