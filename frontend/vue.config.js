const { defineConfig } = require('@vue/cli-service')
module.exports = {
  // You might have other configurations here, like publicPath: '/'
  publicPath: '/', // Example if you already have this

  // Add or modify the pages configuration:
  pages: {
    index: {
      // entry for the page
      entry: 'src/main.js', // Should match your entry point
      // the source template
      template: 'public/index.html', // Should match your HTML template
      // output as dist/index.html
      filename: 'index.html',
      // THIS IS THE KEY: Set the browser tab title here
      title: 'RecApp' // <--- CHANGE THIS TO YOUR DESIRED APP NAME
    }
    // You could define other pages here if you had a multi-page app
  }
};
