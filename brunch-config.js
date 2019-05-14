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
  plugins: {
    npm: ["babel-brunch"]
  }
};
