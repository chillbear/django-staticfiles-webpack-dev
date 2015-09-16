# django-staticfiles-webpack-dev

Simple StaticFilesStorage that can be used together with the assets-webpack-plugin to include hashed files. Meant to be used in development, with [schocco/django-staticfiles-webpack](https://github.com/schocco/django-staticfiles-webpack) used in production.

## Why

When the [assets-webpack-plugin](https://github.com/sporto/assets-webpack-plugin) is added to the webpack configuration, then a json file is created which maps entry points
to generated file names.
This json file is read by the custom django staticfiles storage class to resolve the url for the entry point.

In production, you can use [hashed filenames for cache-busting purposes](https://github.com/schocco/django-staticfiles-webpack). In development, where this is intended to be used, you can serve up urls that point directly to your webpack-dev-server (and all the features, like hot reloading, that come with serving from there).


## Webpack Configuration

Install the assets plugin with `npm install --save-dev assets-webpack-plugin`
and include it in the plugins section of `webpack.conf.js`:

```javascript
AssetsPlugin = require('assets-webpack-plugin');
var entry = ['.src/app/App.js']
  
module.exports = {

  output = {
       path: path.join(__dirname, 'static/build'),
       publicPath: isProduction ? 'build/' : 'http://localhost:8080/',
       filename: isProduction ? "scripts/[name]-[chunkhash].js" : 'scripts/[name].js'
    };
plugins: [
    new AssetsPlugin() // writes webpack-assets.json file that can be read in by custom django storage class
],
    module
:
{
    loaders: [
        {test: /\.js?$/, exclude: /node_modules/, loader: 'babel-loader'},
        //your other loaders ...
    ]
}
```

When a build is completed, a `webpack-assets.json` file in development should be in the directory with content like this:

```javascript
{"main":{"js":"http://localhost:8080/main.js"}}
```

Note that the entry point has been called 'main' as there was no name specified.
When multiple entry points are defined in a dict, then each key is reflected in the assets.json.
See the webpack [docs](https://webpack.github.io/docs/multiple-entry-points.html).


## Django Configuration

Install package with `pip install django-staticfiles-webpack` in your projects venv.

### STATICFILES_STORAGE
Name of the storage class: `webpack.storage.WebpackDevServerStorage`

### WEBPACK_ASSETS_FILE
A path pointing to the generated webpack-assets.json file. E.g. `"path-to-your/webpack-assets.json"`


## Need something more sophisticated?
Maybe https://github.com/owais/django-webpack-loader suits your needs.
