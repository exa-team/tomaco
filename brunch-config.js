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
    public: "tomaco/static",
    watched: ["frontend"]
  },
  npm: {
    compilers: ["babel-brunch"]
  },
  plugins: {
    copycat: {
      images: ["frontend/images"],
      public: ["frontend/public"]
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
