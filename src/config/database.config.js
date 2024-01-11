import mongoose from "mongoose";
export const connect = () => {
  mongoose
    .connect(process.env.MONGO_URI)
    .then(() => console.info("Connected to MongoDB"))
    .catch((err) => console.error(err.message));
  return mongoose.connection;
};

export const connection = mongoose.connection;
