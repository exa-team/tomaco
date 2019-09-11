module.exports = {
  files: {
    javascripts: {
      joinTo: "main.js"
    },
    stylesheets: {
      joinTo: "main.css"
    }
  },
  paths: {
    public: "tomaco/static/build",
    watched: ["tomaco/static/src"]
  },
  npm: {
    compilers: ["babel-brunch"]
  },
  plugins: {
    copycat: {
      images: ["tomaco/static/src/images"],
      manifest: ["tomaco/static/src/manifest.json"]
    },
    cleancss: {
      keepSpecialComments: 0,
      removeEmpty: true
    },
    terser: {
      mangle: false,
      compress: {
        global_defs: {
          "@console.log": "alert"
        }
      },
      output: {
        beautify: false,
        preamble: "/* minified */"
      }
    }
  }
};
