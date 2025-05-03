# Diplom_2

### Структура проекта

Метод test_create_order_with_authorization_and_valid_ingredients проверяет, что успешный запрос создание заказа возвращает код ответа 200 и success: True.

Метод test_create_order_without_authorization проверяет, что успешный запрос создание заказа без авторизации возвращает код ответа 200 и success: True.

Метод test_create_order_without_ingredients проверяет, что запрос создание заказа без ингредиентов возвращает код ответа 400 и message: Ingredient ids must be provided.

Метод test_create_order_with_invalid_ingredients проверяет, что запрос создание заказа с неверным хэшем ингредиентов возвращает код ответа 400 и message: One or more ids provided are incorrect.

Метод test_create_unique_user проверяет, что успешный запрос создание пользователя возвращает код ответа 200 и success: True.

Метод test_create_existing_user проверяет, что попытка создания уже зарегистрированного пользователя возвращает код ответа 403 и message: User already exists.

Метод test_create_user_with_missing_fields_email проверяет, что попытка создания пользователя без email, password или name возвращает код ответа 403 и message: Email, password and name are required fields.

Метод test_get_orders_with_authorization проверяет, что успешный запрос получения заказов возвращает код ответа 200 и orders: [].

Метод test_get_orders_without_authorization проверяет, что запрос получения заказов без авторизации возвращает код ответа 401 и message: You should be authorised.

Метод test_login_with_valid_credentials проверяет, что успешный запрос авторизации пользователя возвращает код ответа 200 и success: True.

Метод test_login_with_invalid_credentials проверяет, что запрос авторизации пользователя без email или password возвращает код ответа 403 и message: email or password are incorrect.

Метод test_update_user_with_authorization проверяет, что успешный запрос обновления данных пользователя возвращает код ответа 200 и обновлённые данные.

Метод test_update_user_without_authorization проверяет, что запрос обновления данных пользователя без авторизации возвращает код ответа 401 и message: You should be authorised.

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

> `$ pytest ./tests/ --alluredir=allure_results`
