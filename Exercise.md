# Тестовое задание

Реализовать одностраничное приложение (SPA) для просмотра информации сервиса с возможностью авторизации.

## Требования

Приложение должно состоять из следующих страниц:

1. `/` - главная страница.
2. `/login` - страница авторизации.
3. `/browse` - страница для просмотра информации сервиса.

В приложении реализовать навигацию:

1. На главную (`/`).
2. Просмотр (`/browse`).

В приложении реализовать вывод кнопки для прохождения авторизации (Войти / Выйти).

**Для запросов информации (страница просмотра) и авторизации реализовать асинхронный функциюнал с запросами к "фейковому" серверу (реализовывать полноценную серверную часть не нужно, достаточно функций-хэлперов для возвращения данных с задержкой).**

Информацию об авторизации пользователя можно сохранять в ``localStorage``.

## Требования к страницам

**Главная**

Главная страница является публичной, доступной как авторизованным, так и неавторизованным пользователям. На ней располагается навигация и любая другая информация которую посчитаете нужной.

**Страница авторизации**

Страница авторизации доступна только если пользователь не авторизован. Если авторизованный пользователь попытается перейти по адресу `/login`, то происходит редирект на главную.

При успешной авторизации происходит редирект на главную.

**Страница для просмотра информации сервиса**

Является приватной. Если пользователь попытается на нее перейти, произвести редирект на страницу авторизации.

На данной странице реализовать вывод приведенной ниже информации в виде (данные получаются с "фейкового" сервера):

1. В левой части ввывести древовидную структуру, содержащую только родительские элементы с возможностью выбора.
2. В правой части вывести список дочерних элементов выбранного родителя. Реализовать поиск и сортировку по имени.

```js
const data = [
  {
    key: '_',
    name: 'root',
    children: [
      {
        key: '0',
        name: 'quidem molestiae enim',
        children: [
          {
            key: '0-1',
            name: 'sunt qui excepturi placeat culpa',
            children: [
              {
                key: '0-1-0',
                name: 'omnis laborum odio',
              },
              {
                key: '0-1-1',
                name: 'non esse culpa molestiae omnis sed optio',
              },
              {
                key: '0-1-2',
                name: 'molestiae voluptate non',
              },
              {
                key: '0-1-3',
                name: 'eaque aut omnis a',
              },
              {
                key: '0-1-4',
                name: 'tenetur explicabo ea',
              },
              {
                key: '0-1-5',
                name: 'temporibus molestiae aut',
              }
            ],
          },
          {
            key: '0-2',
            name: 'natus impedit quibusdam illo est',
            children: [],
          },
        ],
      },
      {
        key: '1',
        name: 'quibusdam autem aliquid et et quia',
        children: [],
      },
      {
        key: '2',
        name: 'qui fuga est a eum',
        children: [
          {
            key: '2-0',
            name: 'saepe unde necessitatibus rem',
            children: [
              {
                key: '2-0-0',
                name: 'est placeat dicta ut nisi rerum iste',
                children: [
                  {
                    key: '2-0-0-0',
                    name: 'ea voluptates maiores eos accusantium officiis tempore mollitia consequatur',
                  },
                  {
                    key: '2-0-0-1',
                    name: 'tenetur explicabo ea',
                  }
                ],
              },
            ],
          },
          {
            key: '2-1',
            name: 'distinctio laborum qui',
          },
          {
            key: '2-2',
            name: 'quam nostrum impedit mollitia quod et dolor',
          },
          {
            key: '2-3',
            name: 'consequatur autem doloribus natus consectetur',
          },
        ],
      },
      {
        key: '3',
        name: 'ab rerum non rerum consequatur ut ea unde',
        children: [],
      },
      {
        key: '4',
        name: 'ducimus molestias eos animi atque nihil',
        children: [],
      },
      {
        key: '5',
        name: 'ut pariatur rerum ipsum natus repellendus praesentium',
        children: [],
      }
    ],
  },
];
```
