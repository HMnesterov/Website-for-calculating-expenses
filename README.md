## Website-for-calculating-expenses on Django



## If you want to change  settings, you should edit the env file



Launch
------

```
git clone https://github.com/BenitoSwaggolini/Website-for-calculating-expenses.git
python -m venv venv
.\venv\Scripts\activate
cd Website-for-calculating-expenses
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



Docker
------

```
git clone https://github.com/BenitoSwaggolini/Website-for-calculating-expenses.git
docker-compose up -d
```




Opportunities:
------


* `auth/(login or register or logout)` - User authorization/reg/logout
* `add_category/` - add new category
* `add_item/` - add a new product(after category)
* `filter/<int:days>` - get info about expenses for this time
* `see_difference/` - check difference between two dates expenses
* `` - beautiful main page with charts


