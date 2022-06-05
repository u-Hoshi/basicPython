const BundleTracker = require('webpack-bundle-tracker');

const baseConfig = {
  // ...
  plugins: [
    // ⇓ 追加 ⇓
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json',
    }),
  ],
};

const devConfig = merge(baseConfig, {
  // ...
  devServer: {
    port: 3000,
    hot: true,
    // ⇓ 追加 ⇓
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
    watchOptions: {
      ignored: /node_modules/,
    },
  },
});
