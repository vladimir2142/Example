<h1>Пример использования технолонгий</h1>
<h3>В данной программе написаны мини примеры по каждой технологии, с которой я работал</h3><br>
<h2>Содержание </h2>

<ol>
<li><a href='#start'>Старт работы</a></li>
<li><a href='#fast_api_get'>FastAPI get request</a></li>
<li><a href='#fast_api_post'>FastAPI post request</a></li>
<li><a href='#sqlalchemy'>SQLAlchemy</a></li>
</ol>

<h2 id="start">Старт работы</h2>
<p>Для установки библиотек используйте команду:</p>
<pre>pip install -r requirements.txt</pre>
<h2 id ="fast_api_get" >Get request</h2>
<p>Для того чтобы протестировать работу get запроса:</p>
<ol>
<li>Запустите программу</li>
<li>В браузере или программе "Postman" отправте запрос на адресс "localhost:2142/test/{*}"</li>
</ol>
<p>{*}-произвольная надпись</p>
</br>
<p>Пример ответа:</p>
<pre>
{
    "name": "Vladimir",
    "request_time": "2022-01-31T22:58:48.090493"
}
</pre>
</br>
<h2 id ="fast_api_post" >Post request</h2>
<p>Для того чтобы протестировать работу post запроса:</p>
<ol>
<li>Запустите программу</li>
<li>B программе "Postman" отправте post запрос на адресс "localhost:2142/post/"</li>
<li>Для правильной работы в body запроса, нужно отправить:</li>
<h3>Формат:</h3>
<pre>{
    name: str
    info: dict
}</pre>
<h3>Пример:</h3>
<pre>{
    "name": "vova",
    "info":{
        "age":21,
            "gender":"male"
    }
}</pre>
</ol>
<h3>Пример ответа:</h3>
<pre>
{
    "name": "vova",
    "info": {
        "age": 21,
        "gender": "male"
    }
}</pre>
</br>
<h2 id="#sqlalchemy">SQLAlchemy</h2>

