const path = require('path');
const htmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {

    entry: './src/index.js',
    output: {
        path: path.join(__dirname, '/dist'),
        filename: 'index.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use:{
                    loader: 'babel-loader'
                }
            }
        ]
    },
    plugins: [
        new htmlWebpackPlugin({
            template: './src/index.html'
        })
    ],
    devServer: {
        compress: true,
        port: 3000
    }

}