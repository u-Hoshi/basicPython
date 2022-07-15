const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  publicPath: 'http://0.0.0.0:8080/',
  outputDir: './dist/',
  transpileDependencies: ['vuetify'],

  chainWebpack: config => {
    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{ filename: './webpack-stats.json' }]);
    config.output.filename('bundle.js');
    config.optimization.splitChunks(false);
    config.resolve.alias.set('__STATIC__', 'static');
    // config.devServerを記述するとフロントが起動しなくなる
    // config.devServer
    //   .hotOnly(true)
    //   .watchOptions({ poll: 1000 })
    //   .https(false)
    //   .disableHostCheck(true)
    //   .headers({ 'Access-Control-Allow-Origin': ['*'] });
  },
};
