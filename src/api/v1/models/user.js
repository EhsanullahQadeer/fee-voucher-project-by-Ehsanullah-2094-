import mongoose, { Schema } from "mongoose";

const userSchema = new Schema({
  username: { type: String, unique: true, sparse: true },
  password: { type: String, required: true },
  creationDate: { type: Date, default: Date.now },
});

export default mongoose.model("user", userSchema);