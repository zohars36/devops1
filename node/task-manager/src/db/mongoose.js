const mongoose = require("mongoose");

mongoose.connect(process.env.MONGODB_URL);

// mongoose.connect(process.env.MONGODB_URL, {
//   useNewUrlParser: true,
//   useCreateIndex: true,
//   useFindAndModify: false,
// });
