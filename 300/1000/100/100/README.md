# 100 - Install using NPM

Make sure that you have [Node.js](https://nodejs.org/en/) and [Tailwind CSS](https://tailwindcss.com/) installed.

> Install Tailwind CSS as follows:
> $ cd flask_app
> $ npm install -D tailwindcss
> $ npx tailwindcss init
>
> MORE
>
>

1. Install Flowbite as a dependency using NPM by running the following command:

```
$ cd flask_app
$ npm install flowbite --save-dev
```

2. Require Flowbite as a plugin inside the ```tailwind.config.js``` file:

```
module.exports = {

    plugins: [
        require('flowbite/plugin')
    ]

}
```

3. Make sure that you add the template path to the ```tailwind.config.js``` file:

```
module.exports = {

    content: [
        "./node_modules/flowbite/**/*.js"
    ]

}
```

4. Include the main JavaScript file to make interactive elements work:

```
<script src="../path/to/flowbite/dist/flowbite.js"></script>
```